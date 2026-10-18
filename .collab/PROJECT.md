# Project identity — read this first

project_id: rto
project_name: The Hospo Hub RTO
repo: thehospohub/RTO
default_branch: main
task_prefix: RTO
codex_rules: Never invent agreements, staff, consultation, competence, facilities, approvals or evidence; cite official sources with URL and retrieval date; never mark anything as director-approved.

Every task, reply and review on this bridge carries `project: rto` and
`repo: thehospohub/RTO`. The bridge script (`.collab/bin/bridge.py`) refuses to run
if the task file, this file and the git `origin` remote disagree, and rejects any Codex
reply that does not echo the same project and task id.

Not this project: Caddie / Golf Performance OS, and any other repository or Drive
folder not named here.

## What this project is
Preparing The Hospo Hub's application for initial RTO registration with ASQA
(target lodgement 1 April 2027), plus its policies, procedures, TAS documents and
twelve unit resource packages. Master documents live in the directors' shared
Google Drive project folder; the controlling document is
"START HERE — AI Handover and Project Baseline"
(https://docs.google.com/document/d/1w0BeG5stUwDWvfuR1sHzO3UimnLjHrrmHcSaDjpmj6Y).
This repo holds the bridge records and any working drafts the directors choose to keep here.

## Protected baseline (do not change without an explicit task that names it)
- Director-confirmed scope (DEC-01, 10 Oct 2026): SIT20322 Certificate II in
  Hospitality with core BSBTWK201, SITHIND006, SITHIND007, SITXCCS011, SITXCOM007,
  SITXWHS005 and electives SITXFSA005, SITHFAB021, SITHGAM022, SITXFSA006, BSBTEC201,
  SITXCOM006; standalone SITHFAB021 (RSA), SITHGAM022 (RSG), SITXFSA005. Do not
  substitute electives or add units.
- Founder facts in the START HERE baseline (entity, ownership, roles, credentials,
  Ammonite, budget) are recorded as stated; do not alter them.
- Never fabricate data, evidence or approvals. Unknown stays unknown; mark assumptions
  and missing evidence. Two AI reviews do not establish compliance.
- Director-approved content is never edited in place; changes go in as new drafts.
- Only the directors approve documents, sign declarations and lodge. Specialist review
  (vocational, industry, financial) cannot be done or claimed by an AI.
- RMLV and other Queensland approvals are separate workstreams; do not present ASQA
  registration as covering them, and do not advertise national recognition.
- No broad rewrites. Prefer the smallest change that meets the acceptance criteria.

## Key areas and commands
- Content is documents (Markdown/Google Docs), not application code.
- Tests / lint / build: none yet (to be decided if code or tooling is added).
- Release gate: no automated gate. A document is finished only when both AI reviews
  have no open material findings (status READY FOR DIRECTOR REVIEW) and the directors
  approve it.
