# Bridge protocol — Claude Code ⇄ Codex

## Who does what
See `ROLES.md`. In short: the user owns product decisions and any manual
acceptance; Claude and Codex are the engineering pair. Every task has exactly one
**owner** (the only writer) and one **reviewer**.

## Task files
One file per task: `.collab/tasks/PREFIX-NNNN.md` (PREFIX = `task_prefix` in
`PROJECT.md`). The bridge writes this front matter:

```
project: <project_id>                # must match PROJECT.md
repo: <owner>/<repo>                 # must match PROJECT.md and git origin
id: PREFIX-0001
title: ...
type: investigation | build | review | question
from: user | chatgpt | claude | codex
owner: claude | codex                # the only agent that may write code for it
reviewer: claude | codex | user      # never the owner
status: (see lifecycle)
sandbox: read-only | workspace-write # what Codex is allowed when it acts on this task
branch: n/a | collab/PREFIX-NNNN
device_test: no | required           # required when the user must accept it by hand
network: no | yes                    # Codex network access in workspace-write
```

Below it: `## Task`, `## Acceptance criteria`, `## Scope` (files in bounds), then
`## Thread`, an append-only list of entries headed `### <UTC time> — <who> — <status>`.

## Lifecycle
```
assigned → in_progress → needs_review → done
                 │             └──→ changes_requested → in_progress
                 ├──→ blocked   (needs something outside the agents: the user, a device, a decision)
                 └──→ question  (needs an answer from the other agent or the user)
```
- `done` needs reviewer sign-off (recorded as `review: approved`). An owner marking its
  own work `done` is turned into `needs_review`. Exception: the owner of a `question`
  task closes it by answering.
- If `device_test: required`, `done` also needs the user's acceptance
  (`device_accepted: yes`). Review first → `blocked` until the user accepts.
- Only the reviewer can set `changes_requested`.
- Codex's thread entries come only from real Codex replies (`send`); `post` speaks for
  claude, user or chatgpt (Claude records what they said).

## Branches and writing
- `.collab/` bookkeeping may go straight to `main` (no product effect).
- Product changes go on `collab/PREFIX-NNNN` branches, branched from `main`, and reach
  `main` only through a PR that the reviewer has reviewed and the user has OK'd.
- **One writer per file at a time.** Never let Claude and Codex edit the same file
  concurrently. Split work by file.
- **Codex edits; Claude commits.** Codex's sandbox usually keeps git metadata read-only,
  so Codex leaves changes uncommitted; Claude reviews the diff and commits it on the task
  branch, attributed to Codex in the message.
- Before Codex writes, the bridge makes a checkpoint commit so its diff is reviewable
  and reversible (`git reset --hard <checkpoint>` undoes it — only with the user's OK).
- Codex usually cannot run browser/localhost tests in its sandbox. It runs unit tests
  and static checks; Claude runs browser suites and the full gate.
- Optional: each agent works in its own git worktree; the main checkout stays on `main`.

## How messages move (the user never copy-pastes between agents)
Claude drives the bridge with `python3 .collab/bin/bridge.py`:

| Step | Command |
|---|---|
| Identity self-check | `bridge.py check` |
| Claude assigns Codex a task | `bridge.py new --owner codex --reviewer claude --type build --sandbox workspace-write --title "..." --body-file brief.md --criteria "..." --scope "..."` then `bridge.py send PREFIX-NNNN` |
| Codex's result comes back | `send` captures Codex's reply, checks identity, appends it to the thread, applies the status rules, logs it |
| Codex raises work for Claude | Codex lists `followups`; the bridge creates a task `from: codex, owner: claude` |
| Claude checks what is waiting | `bridge.py inbox claude` |
| Claude answers / reviews / closes | `bridge.py post PREFIX-NNNN --who claude --status <s> --message "..."` |
| Codex reviews Claude's work | `new --owner claude --reviewer codex`, do the work, `post ... --status needs_review`, then `bridge.py send PREFIX-NNNN --as reviewer` (always read-only) |

Every Codex reply must end with this block, or the bridge marks the task `bridge_error`:
```
BRIDGE-REPLY
project: <project_id>
task: PREFIX-NNNN
status: <lifecycle status>
summary: <one line>
followups: none
END-BRIDGE-REPLY
```
(or `followups:` then lines `- to: claude | type: question|review|build|investigation | title: <t> | detail: <one line>`)

Quick one-off consultations (independent opinions, short reviews) can also run as a
plain `codex exec -s read-only -o OUT "<prompt>" < /dev/null` without a task file —
but still log them in `LOG.md`.

## Requirements from the user (or another agent such as ChatGPT)
Requirements enter as a task file with `from: user` (or `from: chatgpt`), written by
Claude from what the user says, or committed directly to `.collab/tasks/` by another
agent with GitHub access. Claude picks them up with `bridge.py inbox claude`.
