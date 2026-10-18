# Roles (as recorded from the START HERE baseline and Delivery Plan v0.2, 2026-10-18)

- **Directors (Amelia and Sharne)**: product owners and final decision-makers. They
  decide business settings and spending, provide genuine evidence, approve documents
  and sign declarations. They do not relay messages between agents.
- **ChatGPT**: project manager and primary drafter in Google Drive (plan, registers,
  drafts and review dispositions), per Delivery Plan v0.2.
- **Claude Code**: independent reviewer in the Drive workflow, plus lead engineer for
  this repo. Drives the bridge, checks Codex's work and keeps `.collab/` records.
  Never records director approval.
- **Codex**: implementation and review agent reached through the bridge. Its exact
  role in the RTO document workflow is **to be confirmed by the directors**.
- **Specialists**: vocational/assessment, industry and financial reviewers. No AI can
  provide or claim their input.
- **Google Drive**: source of truth for project documents. **GitHub** is the source of
  truth for bridge records and anything committed here.

Each substantive task has exactly one owner (the only writer) and one reviewer.
Default when unassigned: Claude leads and reviews, Codex builds.
