# Roles (as recorded from the START HERE baseline and Delivery Plan v0.2, 2026-10-18)

- **Directors (Amelia and Sharne)**: product owners and final decision-makers. They
  decide business settings and spending, provide genuine evidence, approve documents
  and sign declarations. They do not relay messages between agents.
- **ChatGPT**: project manager and primary drafter in Google Drive (plan, registers,
  drafts and review dispositions), per Delivery Plan v0.2.
- **Claude Code**: independent reviewer in the Drive workflow, plus lead engineer for
  this repo. Drives the bridge, checks Codex's work and keeps `.collab/` records.
  Never records director approval.
- **Codex**: equal working partner to Claude Code (owner decision, 2026-10-18). Claude
  and Codex consult on every owner prompt, challenge and quality-check each other's
  work, and only then present one final solution to the owner for approval. Codex
  reaches the work only through this repo and the bridge; it has no Google Drive access.
  In the Drive workflow, Claude + Codex together fill the plan's "Claude: independent
  reviewer" role; ChatGPT remains drafter and project manager (owner, 2026-10-18).
- **Specialists**: vocational/assessment, industry and financial reviewers. No AI can
  provide or claim their input.
- **Google Drive**: source of truth for project documents. **GitHub** is the source of
  truth for bridge records and anything committed here.

Each substantive task has exactly one owner (the only writer) and one reviewer.
Default when unassigned: Claude leads and reviews, Codex builds.

## Current working model (owner, 14 Nov 2026; replaces the ChatGPT-drafter arrangement)
- **Claude + Codex create** the documents. For each document one is the writer and the other the cross-checker;
  files are split so they never edit the same file at once.
- **ChatGPT reviewer**: an independent third review of every document by a different OpenAI GPT model
  (gpt-6.1-terra; Codex itself runs gpt-6.1-sol), run by Claude through the Codex CLI on the ChatGPT subscription
  (`bridge.py send --as reviewer --name chatgpt-reviewer --model gpt-6.1-terra`). It reviews blind to the other
  reviews. It is not the ChatGPT app and has no memory of ChatGPT conversations.
- **Directors (Amelia, Sharne)**: carry nothing between tools. Claude sends review and approval requests in chat
  on behalf of all three reviewers (Codex cannot contact the directors). Optional: a director may ask the ChatGPT app
  to check a final document in Drive, using a one-line prompt Claude supplies.
- **Publishing**: only director-approved final versions are published to the matching Google Drive folder.
- The ChatGPT app (formerly drafter and project manager) is no longer in the drafting loop.

