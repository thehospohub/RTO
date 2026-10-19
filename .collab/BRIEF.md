# Project brief — The Hospo Hub RTO

## Goal
"Develop The Hospo Hub RTO application and resources using existing ChatGPT and Claude
subscriptions and shared Google Drive. Target lodgement: 1 April 2027. Delivery begins
only following applicable approvals." (START HERE baseline, Draft v0.1)

## Constraints / stack / conventions
- Proposed Brisbane-based Pty Ltd (not yet incorporated); Queensland context.
- Documents live in Google Drive; this repo holds bridge records.
- Start with existing subscriptions. No API or n8n setup. No new paid system assumed.
- Status vocabulary from START HERE: QUEUED; DRAFTING; READY FOR CLAUDE REVIEW;
  READY FOR CHATGPT REVISION; NEEDS DIRECTOR DECISION; NEEDS SPECIALIST REVIEW;
  APPROVED BY DIRECTORS. Never use APPROVED to describe AI agreement.
- At most two AI review rounds per work package before escalating to the directors.
- No automated test gate; director approval is the release gate.

## How we work (set by the user)
- The user directs the project; Claude Code and OpenAI Codex both work on it.
- Every piece of work is cross-checked by the other agent before it ships.
- Nothing merges to `main` without the user's OK (unless the user says "merge when done").
- Do not assume. Ask the user when a decision is genuinely theirs.

## Decisions log
(Only the USER's decisions, dated. Never record an agent's suggestion as a decision.)
- 2026-10-10 — DEC-01 (directors, recorded in START HERE): "The directors confirm no
  changes to the agreed SIT20322 qualification, its twelve selected units/core and
  electives, or the agreed standalone offerings. DEC-01 scope retention is confirmed.
  Do not substitute electives or add café/espresso/table-service units. RMLV remains a
  separate approval workstream; this decision does not establish any approval. ...
  Other plan, budget and operating approvals remain pending."
- 2026-10-18 — Bridge set up between Claude Code and Codex for this project.
- 2026-10-18 — Working model (owner): "Codex and Claude are to work together, challenging
  and quality controlling eachother, with the owner as the director of the project. Each
  prompt is to be consulted with both parties (Claude code and Codex), before a final
  solution is presented to the owner for approval after workup is complete."
- 2026-10-18 — Roles (owner): "Whatever is in the Drive plan is what the client wants, so go
  ahead." ChatGPT stays project manager and primary drafter per Delivery Plan v0.2;
  Claude and Codex together form the review side.
- 2026-10-19 — Owner approved the PLAN-01 joint AI review round 1 (J01–J17) ("Approve."). This
  approves the review for handover to ChatGPT; it is not approval of PLAN-01 itself.
- 2026-10-19 — DEC-02 (budget): "Provided budget has been given as a guide. We are aware that the
  provided budget is extremely tight. The provided budget is more for illustrative purposes. The
  point to get across is that the budget has to remain extremely lean throughout the duration of
  this project."
- 2026-10-19 — DEC-03 (entity/accountant): "Companies will be set up in due course. Accountant will
  also be engaged in due course. Companies and accountant do not prevent us from commencing. No
  lodgement will be made without the aforementioned two in place."
- 2026-10-19 — DEC-04 (capacity): "Sharne and Amelia both 4 hours per week for review, strategising,
  and sign off purposes."
- 2026-10-19 — DEC-05 (operating assumptions): "Domestic only. Assumption is that the intended scope
  of registration is going to attract a younger cohort most likely entering the workforce for the
  first time (16-22). Elective units have been selected so students can complete practicals in their
  own environment (I.e. at home, workplace, etc.). Should they require facility, they will be able to
  attend in house training at our office."
- 2026-10-19 — DEC-06 (Ammonite): "Ammonite will be a go (65% sure)"
- 2026-10-19 — DEC-07 (state pathways): "QLD as that is the location we are based - if we can not get
  approvals we will loop back around once registration is obtained"
- 2026-10-19 — DEC-08: owner asked for further clarification before deciding (pending).
  (Numbering note, Claude: DEC-02..08 above follow the joint review's numbering. In Drive REG-01 v0.1,
  DEC-02 budget, DEC-03 entity/accountant, DEC-04 owner split/cadence and DEC-06 Ammonite match, but
  REG-01 DEC-05 means "Plan v0.3 release". The owner's DEC-05 (operating assumptions) and DEC-07 (Qld
  first) need new REG-01 IDs from ChatGPT.)
