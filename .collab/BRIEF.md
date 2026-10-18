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
