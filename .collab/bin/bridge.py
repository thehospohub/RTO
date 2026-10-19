#!/usr/bin/env python3
"""Claude <-> Codex task bridge for one project. See .collab/PROTOCOL.md.

Project-agnostic: identity (project_id, project_name, repo, task_prefix,
default_branch) and the one-line `codex_rules` come from .collab/PROJECT.md.

Usage:
  bridge.py check
  bridge.py new --owner codex --reviewer claude --type investigation --title T
                [--from claude] [--sandbox read-only] [--device-test no]
                [--body TEXT | --body-file F] [--criteria TEXT] [--scope TEXT]
  bridge.py send TASK [--as owner|reviewer] [--timeout SECONDS] [--worktree DIR] [--web]
  bridge.py inbox claude|codex|user
  bridge.py post TASK --who claude --status S (--message TEXT | --message-file F)
  bridge.py show TASK
"""
import argparse, datetime, os, re, subprocess, sys, tempfile

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                      text=True, check=True).stdout.strip()
COLLAB = os.path.join(ROOT, ".collab")
TASKS = os.path.join(COLLAB, "tasks")
AGENTS = {"claude", "codex", "user", "chatgpt"}
STATUSES = {"assigned", "in_progress", "needs_review", "changes_requested", "blocked",
            "question", "done", "cancelled", "bridge_error"}
OPEN = STATUSES - {"done", "cancelled"}


def die(msg):
    sys.exit(f"bridge: {msg}")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")


def project():
    """Read identity from PROJECT.md and require git origin to match it."""
    ident = {}
    pfile = os.path.join(COLLAB, "PROJECT.md")
    if not os.path.exists(pfile):
        die(f"{ROOT} has no .collab/PROJECT.md — not a bridged project, refusing")
    for line in open(pfile):
        m = re.match(r"^(project_id|repo|task_prefix|default_branch):\s*(\S+)", line)
        if m:
            ident[m.group(1)] = m.group(2)
        m = re.match(r"^(project_name|codex_rules):\s*(.+?)\s*$", line)
        if m:
            ident[m.group(1)] = m.group(2)
    missing = [k for k in ("project_id", "repo", "task_prefix") if k not in ident]
    if missing:
        die(f"PROJECT.md is missing {', '.join(missing)}")
    origin = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT,
                            capture_output=True, text=True).stdout.strip()
    # origin may be a proxy URL; compare the owner/repo path case-insensitively
    if not origin.lower().rstrip("/").removesuffix(".git").endswith(ident["repo"].lower()):
        die(f"git origin {origin!r} is not {ident['repo']} — wrong repository, refusing")
    return ident


def task_path(tid):
    tid = tid.upper().removesuffix(".MD").split("/")[-1]
    p = os.path.join(TASKS, tid + ".md")
    if not os.path.exists(p):
        die(f"no task {tid}")
    return p


def read_task(path):
    text = open(path).read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        die(f"{path}: missing front matter")
    meta = dict(re.findall(r"^(\w+):\s*(.*?)\s*(?:#.*)?$", m.group(1), re.M))
    return meta, m.group(2)


def write_task(path, meta, body):
    fm = "\n".join(f"{k}: {v}" for k, v in meta.items())
    open(path, "w").write(f"---\n{fm}\n---\n{body}")


def verify_task(meta, ident):
    if meta.get("project") != ident["project_id"] or meta.get("repo") != ident["repo"]:
        die(f"task {meta.get('id')} belongs to {meta.get('project')}/{meta.get('repo')}, "
            f"not {ident['project_id']}/{ident['repo']} — refusing")
    if not meta.get("id", "").startswith(ident["task_prefix"] + "-"):
        die(f"task id {meta.get('id')} lacks prefix {ident['task_prefix']}")


def log(who, task, outcome, files="—"):
    with open(os.path.join(COLLAB, "LOG.md"), "a") as f:
        f.write(f"{now()} | {who} | {task} | {outcome} | {files}\n")


def append_thread(path, who, status, text, updates=None):
    meta, body = read_task(path)
    meta["status"] = status
    meta.update(updates or {})
    body = body.rstrip("\n") + f"\n\n### {now()} — {who} — {status}\n{text.strip()}\n"
    write_task(path, meta, body)


def gate(meta, who, status):
    """Apply the completion rules. Returns (final status, front-matter updates, note).

    `done` needs reviewer sign-off; a device_test task also needs the user's
    physical acceptance. Owners cannot close their own work, except an owner
    answering a plain question.
    """
    if status == "changes_requested":
        if who != meta.get("reviewer"):
            die(f"only the reviewer ({meta.get('reviewer')}) can request changes")
        return status, {"review": "changes_requested"}, ""
    if status != "done":
        return status, {}, ""
    owner, reviewer = meta.get("owner"), meta.get("reviewer")
    device = meta.get("device_test") == "required"
    upd = {}
    if who == reviewer:
        upd["review"] = "approved"
        if who == "user" and device:
            upd["device_accepted"] = "yes"
    elif who == "user" and device:
        upd["device_accepted"] = "yes"
    elif who == owner and meta.get("type") == "question" and not device:
        return "done", {}, ""
    elif who == owner and meta.get("review") == "approved" and (
            not device or meta.get("device_accepted") == "yes"):
        return "done", {}, ""  # a note on already-approved work keeps it closed
    elif who == owner:
        return "needs_review", {}, "Bridge: owner cannot self-close; sent for review."
    else:
        die(f"{who} is not the reviewer ({reviewer}) of {meta.get('id')}; cannot mark done")
    reviewed = upd.get("review", meta.get("review")) == "approved"
    accepted = not device or upd.get("device_accepted", meta.get("device_accepted")) == "yes"
    if reviewed and accepted:
        return "done", upd, ""
    if not reviewed:
        return "needs_review", upd, "Bridge: awaiting reviewer sign-off."
    return "blocked", upd, "Bridge: review approved; awaiting user's physical-device acceptance."


def next_id(ident):
    os.makedirs(TASKS, exist_ok=True)
    nums = [int(m.group(1)) for f in os.listdir(TASKS)
            if (m := re.match(rf"{ident['task_prefix']}-(\d+)\.md$", f))]
    return f"{ident['task_prefix']}-{max(nums, default=0) + 1:04d}"


def create(ident, *, title, type_, frm, owner, reviewer, sandbox="read-only",
           device_test="no", network="no", body="", criteria="", scope=""):
    if frm not in AGENTS:
        die(f"unknown agent {frm}")
    if owner not in ("claude", "codex"):
        die(f"owner must be claude or codex, not {owner}")
    if reviewer not in ("claude", "codex", "user") or reviewer == owner:
        die(f"reviewer must be claude, codex or user and differ from owner ({owner})")
    tid = next_id(ident)
    meta = {"project": ident["project_id"], "repo": ident["repo"], "id": tid,
            "title": title, "type": type_, "from": frm, "owner": owner,
            "reviewer": reviewer, "status": "assigned", "sandbox": sandbox,
            "branch": "n/a" if type_ in ("investigation", "question", "review")
            else f"collab/{tid}", "device_test": device_test, "network": network,
            "created": now()}
    text = (f"\n## Task\n{body.strip() or title}\n\n## Acceptance criteria\n"
            f"{criteria.strip() or '_See task._'}\n\n## Scope\n"
            f"{scope.strip() or '_Read-only; no files in scope for writing._'}\n\n## Thread\n")
    path = os.path.join(TASKS, tid + ".md")
    write_task(path, meta, text)
    log(frm, f"{tid} created → {owner}: {title}", "assigned", f".collab/tasks/{tid}.md")
    return tid, path


def parse_reply(out, ident, tid):
    m = re.search(r"BRIDGE-REPLY\s*\n(.*?)\n\s*END-BRIDGE-REPLY", out, re.S)
    if not m:
        return None, "reply missing BRIDGE-REPLY block"
    block = m.group(1)
    fields = dict(re.findall(r"^(project|task|status|summary):\s*(.*?)\s*$", block, re.M))
    if fields.get("project") != ident["project_id"] or fields.get("task") != tid:
        return None, (f"reply identity mismatch: project={fields.get('project')!r} "
                      f"task={fields.get('task')!r}, expected {ident['project_id']}/{tid}")
    if fields.get("status") not in STATUSES:
        return None, f"reply has invalid status {fields.get('status')!r}"
    fups = []
    for line in re.findall(r"^\s*-\s*(to:.*)$", block, re.M):
        f = dict((k.strip(), v.strip()) for k, v in
                 (p.split(":", 1) for p in line.split(" | ") if ":" in p))
        if f.get("to") in AGENTS and f.get("title"):
            fups.append(f)
    fields["followups"] = fups
    return fields, None


def cmd_send(args, ident):
    path = task_path(args.task)
    meta, body = read_task(path)
    verify_task(meta, ident)
    tid = meta["id"]
    role = args.as_
    if meta.get(role) != "codex":
        die(f"{tid}: {role} is {meta.get(role)}, not codex")
    ready = ("needs_review",) if role == "reviewer" else \
        ("assigned", "in_progress", "changes_requested", "bridge_error")
    if meta.get("status") not in ready:
        die(f"{tid} is {meta.get('status')}; codex as {role} needs one of {ready}")
    sandbox = "read-only" if role == "reviewer" else meta.get("sandbox", "read-only")
    if sandbox not in ("read-only", "workspace-write"):
        die(f"bad sandbox {sandbox}")
    # Codex may work in a separate worktree of this repo so it never shares a
    # checkout with Claude; task files and the log always live in ROOT.
    wd = os.path.abspath(args.worktree or ROOT)
    common = lambda d: os.path.realpath(os.path.join(d, subprocess.run(
        ["git", "rev-parse", "--git-common-dir"], cwd=d, capture_output=True,
        text=True).stdout.strip()))
    if common(wd) != common(ROOT):
        die(f"{wd} is not a worktree of {ident['repo']} — refusing")
    if sandbox == "workspace-write":
        branch = subprocess.run(["git", "branch", "--show-current"], cwd=wd,
                                capture_output=True, text=True).stdout.strip()
        if branch != meta.get("branch"):
            die(f"{tid}: check out {meta.get('branch')} before Codex writes (on {branch})")
        subprocess.run(["git", "add", "-A"], cwd=wd, check=True)
        subprocess.run(["git", "commit", "-qm", f"checkpoint before Codex: {tid}",
                        "--allow-empty"], cwd=wd, check=True)
    if role == "owner":
        append_thread(path, "bridge", "in_progress", f"Sent to Codex (sandbox: {sandbox}).")

    job = ("You are the OWNER of this task: do it within the stated scope."
           if role == "owner" else
           "You are the REVIEWER of this task. Review the owner's work (the thread, the "
           "branch/diff it names) against the acceptance criteria. Do not modify files. "
           "Use status done to approve, changes_requested with specifics otherwise.")
    prompt = f"""You are Codex, collaborating with Claude Code through a task bridge.
PROJECT: {ident['project_id']} ({ident.get('project_name', ident['project_id'])}), repo {ident['repo']}.
TASK: {tid}. This task belongs ONLY to this project. If anything in it seems to
refer to a different project or repository, stop and reply with status blocked.

Before working, read: .collab/PROJECT.md (identity and protected baseline),
.collab/PROTOCOL.md, .collab/BRIEF.md, the last 20 lines of .collab/LOG.md, and the
task file {os.path.join(ROOT, ".collab/tasks", tid + ".md")} (including its thread;
read it at that absolute path, it is newer than any copy in your working directory).
Your working directory is {wd}.

{job}
Sandbox: {sandbox}. Do not edit .collab/ files; the bridge records your reply.
If you change files, leave them uncommitted (your sandbox cannot write git
metadata; the reviewer commits). Browser/Playwright checks cannot bind localhost
in your sandbox: run unit tests and static checks, and say which browser checks
the reviewer should run.
Never fabricate data or results; say plainly what you could not verify.
{ident.get('codex_rules', '')}
If you need something from Claude (a question, a review, follow-on work), list it
under followups; the bridge will deliver it to Claude as a new task.

Write your findings/results first, then end your reply with EXACTLY this block:
BRIDGE-REPLY
project: {ident['project_id']}
task: {tid}
status: <one of: needs_review, done, blocked, question, changes_requested>
summary: <one line>
followups: none
END-BRIDGE-REPLY
(Instead of "followups: none" you may write "followups:" followed by lines of the form
"- to: claude | type: question | title: <title> | detail: <one line>".)
"""
    # A failed review attempt leaves the task awaiting review so it can be retried.
    fail_status = "needs_review" if role == "reviewer" else "bridge_error"
    out_file = tempfile.mktemp(prefix=f"{tid}-", suffix=".txt")
    try:
        net = (["-c", "sandbox_workspace_write.network_access=true"]
               if sandbox == "workspace-write" and meta.get("network") == "yes" else [])
        # A worktree's index, refs and objects live in the shared git dir, so
        # Codex needs it writable to commit from a worktree.
        # Codex's web search runs on OpenAI's side, so it works even when this
        # environment's network policy blocks the sites themselves.
        if args.web:
            net += ["-c", "tools.web_search=true"]
        if sandbox == "workspace-write" and wd != os.path.abspath(ROOT):
            net += ["--add-dir", common(wd)]
        r = subprocess.run(["codex", "exec", "-C", wd, "-s", sandbox, *net, "-o", out_file,
                            prompt], capture_output=True, text=True, timeout=args.timeout,
                           stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        append_thread(path, "bridge", fail_status, f"Codex timed out after {args.timeout}s.")
        log("bridge", tid, "bridge_error: timeout")
        die("Codex timed out")
    out = open(out_file).read() if os.path.exists(out_file) else ""
    if r.returncode != 0 or not out.strip():
        err = (r.stderr or r.stdout)[-1500:]
        append_thread(path, "bridge", fail_status,
                      f"Codex call failed (exit {r.returncode}).\n```\n{err}\n```")
        log("bridge", tid, f"bridge_error: codex exit {r.returncode}")
        die(f"Codex call failed (exit {r.returncode}); see task thread")

    fields, problem = parse_reply(out, ident, tid)
    if problem:
        append_thread(path, "codex", fail_status, f"{out}\n\n_Bridge: {problem}._")
        log("codex", tid, f"bridge_error: {problem}")
        die(problem)
    status, upd, note = gate(read_task(path)[0], "codex", fields["status"])
    if note:
        out += f"\n\n_{note}_"
    append_thread(path, f"codex ({role})", status, out, upd)
    created = []
    for f in fields["followups"]:
        if f["to"] not in ("claude", "codex"):
            out += f"\n\n_Bridge: follow-up for {f['to']} not routed (agents only); use status blocked._"
            continue
        ftid, _ = create(ident, title=f["title"], type_=f.get("type", "question"),
                         frm="codex", owner=f["to"],
                         reviewer="codex" if f["to"] == "claude" else "claude",
                         body=f"{f.get('detail', '')}\n\nRaised by Codex while working on {tid}.")
        created.append(ftid)
    if created:
        append_thread(path, "bridge", status, "Follow-ups raised by Codex: " + ", ".join(created))
    log("codex", f"{tid} ({role})", f"{status}: {fields.get('summary', '')}",
        ", ".join(created) or "—")
    print(out)
    print(f"\n[bridge] {tid} → {status}" + (f"; follow-ups: {', '.join(created)}" if created else ""))


def cmd_new(args, ident):
    body = open(args.body_file).read() if args.body_file else (args.body or "")
    tid, path = create(ident, title=args.title, type_=args.type, frm=args.from_,
                       owner=args.owner, reviewer=args.reviewer, sandbox=args.sandbox,
                       device_test=args.device_test, network=args.network, body=body, criteria=args.criteria,
                       scope=args.scope)
    print(tid, os.path.relpath(path, ROOT))


def cmd_inbox(args, ident):
    if not os.path.isdir(TASKS):
        return
    for f in sorted(os.listdir(TASKS)):
        if not re.match(rf"{ident['task_prefix']}-\d+\.md$", f):
            continue  # only task files (skip .gitkeep, notes, other prefixes)
        meta, _ = read_task(os.path.join(TASKS, f))
        if meta.get("project") != ident["project_id"] or meta.get("status") not in OPEN:
            continue
        mine = (meta.get("owner") == args.agent and meta["status"] in
                ("assigned", "changes_requested", "in_progress", "bridge_error")) or \
               (meta.get("reviewer") == args.agent and meta["status"] == "needs_review") or \
               (args.agent == "user" and meta["status"] in ("blocked", "question"))
        if mine:
            print(f"{meta['id']}  [{meta['status']}]  {meta.get('type')}  from {meta.get('from')}: {meta.get('title')}")


def cmd_post(args, ident):
    path = task_path(args.task)
    meta, _ = read_task(path)
    verify_task(meta, ident)
    if args.status not in STATUSES:
        die(f"bad status {args.status}")
    status, upd, note = gate(meta, args.who, args.status)
    msg = open(args.message_file).read() if args.message_file else args.message
    append_thread(path, args.who, status, msg + (f"\n\n_{note}_" if note else ""), upd)
    log(args.who, meta["id"], status, f".collab/tasks/{meta['id']}.md")
    print(f"{meta['id']} → {status}" + (f"  ({note})" if note else ""))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("check")
    n = s.add_parser("new")
    n.add_argument("--title", required=True)
    n.add_argument("--type", default="investigation",
                   choices=["investigation", "build", "review", "question"])
    n.add_argument("--from", dest="from_", default="claude")
    n.add_argument("--owner", required=True)
    n.add_argument("--reviewer", required=True)
    n.add_argument("--sandbox", default="read-only", choices=["read-only", "workspace-write"])
    n.add_argument("--device-test", default="no", choices=["no", "required"])
    n.add_argument("--network", default="no", choices=["no", "yes"],
                   help="allow Codex network access in workspace-write (e.g. package installs)")
    n.add_argument("--body"); n.add_argument("--body-file")
    n.add_argument("--criteria", default=""); n.add_argument("--scope", default="")
    sd = s.add_parser("send"); sd.add_argument("task")
    sd.add_argument("--as", dest="as_", default="owner", choices=["owner", "reviewer"])
    sd.add_argument("--timeout", type=int, default=900)
    sd.add_argument("--worktree", help="run Codex in this worktree of the repo instead of the root")
    sd.add_argument("--web", action="store_true",
                    help="enable Codex web search (for live official-source checks)")
    i = s.add_parser("inbox"); i.add_argument("agent", choices=["claude", "codex", "user"])
    po = s.add_parser("post"); po.add_argument("task")
    # Codex speaks only through `send`, so its thread entries are always genuine replies.
    po.add_argument("--who", required=True, choices=["chatgpt", "claude", "user"])
    po.add_argument("--status", required=True)
    po.add_argument("--message"); po.add_argument("--message-file")
    sh = s.add_parser("show"); sh.add_argument("task")
    args = p.parse_args()
    ident = project()
    if args.cmd == "check":
        print(f"OK: project {ident['project_id']} = {ident['repo']} (origin verified), root {ROOT}")
    elif args.cmd == "show":
        print(open(task_path(args.task)).read())
    else:
        {"new": cmd_new, "send": cmd_send, "inbox": cmd_inbox, "post": cmd_post}[args.cmd](args, ident)


if __name__ == "__main__":
    main()
