# P06 Assessment System — Director review pack

Status: **ready for director review. Not approved.** Drafted by Claude (policies) and Codex (templates). Each was
cross-checked by the other, then reviewed independently by the ChatGPT reviewer (an OpenAI GPT model, a different one
from Codex). All three reviewers have cleared it: no open AI findings. This is not compliance confirmation or specialist
review.

## What's in it
| ID | Document | Written by |
|---|---|---|
| P06-POL-01 | Assessment Policy and Procedure | Claude |
| P06-POL-02 | Pre-use Assessment Tool Review and Assessment Validation Policy and Procedure | Claude |
| P06-T01 | Pre-use assessment tool review checklist and sign-off | Codex |
| P06-T02 | Validation plan and 5-year schedule | Codex |
| P06-T03 | Risk-based component selection and sample-size worksheet | Codex |
| P06-T04 | Validation team capability, credential and independence check | Codex |
| P06-T05 | Assessment validation record | Codex |
| P06-T06 | Validation and review outcomes and action register | Codex |
| P06-T07 | Reasonable adjustment request and record | Codex |
| P06-T08 | Student authenticity declaration and assessor identity checks | Codex |

## Decisions the directors need to make
1. **Feedback timeframe:** how many business days after submission students get their result (POL-01 4.3). Commonly 10.
2. **Free reattempts:** how many reattempts a student gets at no extra cost before further training is arranged (POL-01 4.7). Commonly 2.

## Left open on purpose (filled in later; no decision needed now)
- Office simulated environment address; LMS/SMS details (Ammonite, subject to agreement).
- Records retention periods: the AI team will verify ASQA's current requirements when drafting P02.
- What a non-credentialled person may contribute to assessment: to be verified against the Credential Policy before release.
- Any cost for an external validator: needs director approval when it arises (lean budget).

---

# P06 — Assessment System (assessment, pre-use tool review, validation)

Status: DRAFT for AI review. Not director-approved. Not for use.
Organisation: The Hospo Hub (proposed Brisbane Pty Ltd, **not yet incorporated**; RTO number: none — not registered).
Basis: Standards for RTOs 2025 — Outcome Standards 1.3, 1.4, 1.5, 1.6, 1.7 (text: .collab/sources/captured-2026-10-19/Outcome-Standards-2025-QA1-excerpt.md),
Compliance Requirements and Credential Policy (validation credentials). Scope (DEC-01): SIT20322 + 12 units; standalone SITHFAB021, SITHGAM022, SITXFSA005; SITSS00069.

## Conventions (all P06 documents)
- Header block: Document ID, title, version (v0.1), status "DRAFT — not approved", owner role, approved by (blank),
  approval date (blank), next review (blank), Standards references.
- Roles, not names: **CEO**; **Training and Assessment Manager (TAM)** — role holder to be confirmed;
  **Trainer/Assessor**; **Validator**; **Student Services Officer**. Never name staff or imply anyone is appointed.
- Placeholders in square brackets, e.g. [Ammonite LMS/SMS — subject to agreement], [office simulated environment address].
- Practical setting rule (owner 14 Nov): online/virtual where the unit allows; otherwise the office simulated environment.
- Australian English, plain language, Markdown. Forms use tables with blank fields.
- **LMS/SMS compatibility (owner, 14 Nov 2026):** all training and assessment is delivered and recorded online through
  an LMS/SMS (most likely Ammonite; format capabilities not yet confirmed). So every learning and assessment document
  must be platform-agnostic and import-ready:
  - modular structure (unit > topic > activity), each item with a stable unique ID (e.g. SITXFSA005-T2-Q04);
  - questions in structured tables (ID, type, stem, options, correct answer/benchmark, mapping refs, marks/decision rule);
  - observation checklists and forms built so they can become digital forms completed in the LMS
    (one row per observable item, Satisfactory / Not Yet Satisfactory, comments, date, assessor sign-off);
  - practical evidence captured digitally (video, photos, live video observation, third-party report uploads);
  - no layout that only works on paper (no free-floating text boxes, no merged-cell tricks); accessible (WCAG 2.2 AA).
  Exact import formats will be fixed once Ammonite's capabilities are confirmed (SYS-01).

## Document list and writers (one writer per file)
| ID | File | Title | Writer |
|---|---|---|---|
| P06-POL-01 | P06-POL-01-assessment-policy-procedure.md | Assessment Policy and Procedure (principles of assessment, rules of evidence, conduct, decisions, reasonable adjustment, reassessment, authenticity/integrity, records, appeals link, RPL/credit transfer interface) | Claude |
| P06-POL-02 | P06-POL-02-pre-use-review-and-validation-policy-procedure.md | Pre-use Assessment Tool Review and Assessment Validation Policy and Procedure | Claude |
| P06-T01 | P06-T01-pre-use-tool-review-checklist.md | Pre-use assessment tool review checklist and sign-off (Std 1.3) | Codex |
| P06-T02 | P06-T02-validation-plan-and-schedule.md | Validation plan and 5-year schedule (every product at least once in 5 years; risk triggers) | Codex |
| P06-T03 | P06-T03-validation-risk-and-sampling-worksheet.md | Risk-based component selection and sample-size worksheet (Std 1.5(c)) | Codex |
| P06-T04 | P06-T04-validator-capability-and-independence-check.md | Validation team capability, credential and independence check (Std 1.5(e),(f); Credential Policy) | Codex |
| P06-T05 | P06-T05-validation-record.md | Assessment validation record (per sampled judgement and tool) | Codex |
| P06-T06 | P06-T06-validation-outcomes-action-register.md | Validation and review outcomes and corrective action register | Codex |
| P06-T07 | P06-T07-reasonable-adjustment-record.md | Reasonable adjustment request and record | Codex |
| P06-T08 | P06-T08-authenticity-declaration-and-checks.md | Student authenticity declaration and assessor authenticity/identity checks (incl. online) | Codex |

---

# Assessment Policy and Procedure

| Field | Detail |
|---|---|
| Document ID | P06-POL-01 |
| Version | v0.1 |
| Status | DRAFT — not approved. Not for use. |
| Owner (role) | Training and Assessment Manager (TAM) |
| Approved by | |
| Approval date | |
| Next review | |
| Standards references | Outcome Standards 1.3, 1.4, 1.6, 1.7 (Standards for RTOs 2025); Credential Policy (assessor credentials) |
| Related documents | P06-POL-02 Pre-use Assessment Tool Review and Assessment Validation; P06-T01 to P06-T08; P12 Complaints and Appeals [to be drafted]; P13 RPL and Credit Transfer [to be drafted]; P10 Student Support and Accessibility [to be drafted]; P11 Under-18 Safeguarding [to be drafted]; P04 Workforce [to be drafted]; TAS-01, TAS-02 |

Organisation: The Hospo Hub (proposed company, not yet incorporated; not a registered training organisation). In this document "the RTO" means The Hospo Hub once registered.

## 1. Purpose

This policy sets out how the RTO plans, conducts, decides and records assessment, so that every assessment decision:
- is consistent with the requirements of the training product (unit of competency, skill set or qualification);
- follows the principles of assessment and the rules of evidence; and
- gives each student a fair and accurate judgement of competency.

## 2. Scope

All assessment for every training product on the RTO's scope of registration. The proposed scope, subject to registration, is:
- SIT20322 Certificate II in Hospitality, with core units BSBTWK201, SITHIND006, SITHIND007, SITXCCS011, SITXCOM007 and SITXWHS005, and electives SITXFSA005, SITHFAB021, SITHGAM022, SITXFSA006, BSBTEC201 and SITXCOM006;
- standalone SITHFAB021, SITHGAM022 and SITXFSA005;
- SITSS00069 Food Safety Supervision Skill Set.

It applies to:
- all trainers and assessors, the TAM, the CEO and any validators;
- assessment conducted online, in a student's workplace, or in the RTO's simulated environment;
- assessment through recognition of prior learning (RPL);
- the assessment-related parts of credit transfer.

Before this policy is used, the scope list is reconciled to the RTO's actual registered scope on training.gov.au (as in P06-T02).

## 3. Policy

3.1 **Consistent with the training product (Std 1.3(a)).** Every assessment tool must address all of the unit's elements and performance criteria, foundation skills, performance evidence, knowledge evidence and assessment conditions. This includes the required number of occasions or service periods, the specified environment, equipment and participants, and any assessor requirements. Mapping alone does not show this. The tool must collect the evidence.

3.2 **Tools reviewed before use (Std 1.3(b),(c)).** No assessment tool is used with students until it has passed a pre-use review under P06-POL-02, recorded on P06-T01. Any changes the review requires are made first.

3.3 **Principles of assessment (Std 1.4(a)).** Every assessment must be:
- **Fair:** it accommodates the student's needs, including reasonable adjustments where appropriate, and allows reassessment where necessary (sections 4.6 and 4.7).
- **Flexible:** it suits the context, the training product and the student. It assesses the skills and knowledge relevant to the training product, however or wherever the student gained them, including through RPL.
- **Valid:** it includes practical application components that let the student show the skills and knowledge in a practical setting. Knowledge questions or quizzes alone never establish practical competence.
- **Reliable:** assessors interpret evidence consistently, and outcomes are comparable whichever assessor conducts the assessment. Marking guides, model answers, benchmarks and observation checklists with clear decision rules support this.

3.4 **Rules of evidence (Std 1.4(b)).** Assessors make each judgement on evidence that is:
- **Valid:** adequate to assure the assessor that the student has the skills and knowledge in the training product.
- **Sufficient:** of enough quality, quantity and relevance for an informed judgement, including the required repetitions.
- **Authentic:** the student's own original work (section 4.8; P06-T08).
- **Current:** it shows the student's current skills and knowledge (this matters especially for RPL).

3.5 **Who may assess.** Only a person who meets the Credential Policy and the RTO's workforce requirements (P04) may make an assessment judgement. That person must also have the vocational competency and current industry skills for the unit, and meet any assessor requirement in the unit's Assessment Requirements.

For example, the current Assessment Requirements for SITHFAB021, SITHGAM022 and SITHIND007 require assessors to have worked in industry for at least three years applying the skills and knowledge of the unit. A person who doesn't hold an accepted credential may contribute only as the Credential Policy permits [to verify against the Credential Policy before release]. The final judgement then rests with a credentialled assessor.

3.6 **Online delivery through the LMS/SMS.** All training and assessment is delivered and recorded online through the RTO's learning and student management system [most likely Ammonite — subject to agreement] (directors' instruction, 14 November 2026). Assessment tasks, observation checklists, evidence uploads, decisions and feedback are completed and stored in that system, including for any practical task observed in the office simulated environment.

3.6A **Where practical assessment happens.** Practical tasks are conducted online or virtually wherever the unit's assessment conditions allow it (directors' instruction, 14 November 2026). Where a unit's conditions can't be met online, practical assessment takes place in the RTO's office simulated environment [address to be confirmed]. It must contain the environment, equipment and participants the unit specifies. A student's own workplace may be used only where it is shown to meet the unit's conditions and the RTO has the access it needs to observe or verify the evidence.

Each unit's assessor guide states the setting for each task.

Simulation cannot replace a mandatory real-workplace requirement in a unit. If a proposed setting can't meet the unit's conditions, the tool is not released and the assessment does not go ahead until the TAM has resolved it.

3.7 **Under-18 students.** Assessment arrangements for students under 18 follow P11 Under-18 Safeguarding [to be drafted]. This includes guardian information where required, supervision online and in the simulated environment, and lawful access to licensed or gaming settings. For example, minors may not play gaming machines, so SITHGAM022 practical tasks use a lawful simulation.

3.8 **Students know what to expect.** Before an assessment, each student is told in writing:
- what will be assessed;
- how and where it will be assessed;
- the conditions and resources;
- how and when the result is given;
- how to ask for a reasonable adjustment;
- the reassessment and appeal arrangements.

## 4. Procedure

### 4.1 Planning assessment

| Step | Action | Responsible | Record |
|---|---|---|---|
| 1 | Confirm the current release of the unit and its Assessment Requirements on training.gov.au, and record the retrieval date. | TAM | Unit source record in the resource package |
| 2 | Design or obtain assessment tools: tasks, instructions, marking guide with model answers or benchmarks, observation checklists, assessor guide, and mapping. | TAM / tool developer | Resource package |
| 3 | Pre-use review under P06-POL-02. Make any required changes before release. | TAM / reviewer | P06-T01; P06-T06 |
| 4 | Load the approved version into the learning management system [Ammonite LMS/SMS — subject to agreement] under version control. | TAM | Document register (P02) |
| 5 | Make the assessment information in 3.8 available to students. | Trainer/Assessor | Student assessment guide |

### 4.2 Conducting assessment

| Step | Action | Responsible | Record |
|---|---|---|---|
| 1 | Confirm the student's identity, especially for online assessment (P06-T08). | Trainer/Assessor | Identity check |
| 2 | Confirm any approved reasonable adjustment is in place (4.6). | Trainer/Assessor | P06-T07 |
| 3 | Conduct the assessment under the conditions in the assessor guide: online, the student's workplace, or the office simulated environment. | Trainer/Assessor | Observation checklist; submission |
| 4 | Collect evidence of every required repetition and occasion. Record observations when they happen. | Trainer/Assessor | Observation checklist |
| 5 | Collect the student's authenticity declaration (P06-T08). | Trainer/Assessor | P06-T08 |

### 4.3 Making and recording the decision

| Step | Action | Responsible | Record |
|---|---|---|---|
| 1 | Judge each task against the marking guide or checklist decision rules: Satisfactory or Not Yet Satisfactory. | Assessor | Marked task |
| 2 | Make the unit decision: Competent only when every task is Satisfactory and all evidence meets the rules of evidence. Otherwise Not Yet Competent. | Assessor | Unit outcome record |
| 3 | Give the student written feedback within [x] business days [timeframe to be set by directors]. Explain any gaps and the reassessment arrangements. | Assessor | Feedback record |
| 4 | Record the outcome in the student management system [Ammonite — subject to agreement]. | Assessor / Student Services Officer | SMS record |
| 5 | Keep the student's completed assessment evidence for the required period. | Student Services Officer | Records system (P02) |

The required retention period follows ASQA's current requirements [to verify: ASQA's direction on retaining completed student assessment items, and the period applying under the 2025 Standards and Compliance Requirements].

### 4.4 Recognition of prior learning (Std 1.6)

| Step | Action | Responsible | Record |
|---|---|---|---|
| 1 | Tell every student about RPL at or before enrolment, with the policy. | Student Services Officer | Enrolment record |
| 2 | Assess RPL through this assessment system, using RPL tools that have passed pre-use review. The tools gather evidence of prior skills, learning and experience against the full unit requirements, including currency. | Assessor | RPL kit; P06-T01 |
| 3 | Make and document the decision fairly, transparently and consistently, in a way that keeps the training product's integrity. Where evidence is incomplete, gather more evidence (for example a practical demonstration) rather than refuse. | Assessor | RPL decision record |

Full RPL procedure: P13 [to be drafted].

### 4.5 Credit transfer (Std 1.7)

At or before enrolment, the Student Services Officer offers every student the opportunity to seek credit transfer, provides the policy and application instructions, and records that this was done (Std 1.7(a)).

Credit transfer is granted on evidence of prior completion of an equivalent training product, shown by AQF certification documentation or an authenticated VET transcript, unless licensing or regulatory requirements of the training product prevent it. The decision is documented and made fairly, transparently and consistently.

Equivalence and verification steps are in P13 [to be drafted]. Credit transfer is not an assessment of competency.

### 4.6 Reasonable adjustment (Std 1.4(a)(i))

| Step | Action | Responsible | Record |
|---|---|---|---|
| 1 | A student, or a guardian for a student under 18 where appropriate, may ask for an adjustment at enrolment or at any time. Trainers also identify needs. | Student / Trainer | P06-T07 |
| 2 | Agree an adjustment that removes a barrier without changing the competency standard or the evidence the unit requires. Examples: extra time, oral questioning in place of written answers, assistive technology, a format change. | Trainer/Assessor with TAM | P06-T07 |
| 3 | Where an adjustment would change what the unit requires, it can't be approved. Explore other support instead (P10). | TAM | P06-T07 |
| 4 | Record the adjustment and apply it consistently. | Assessor | P06-T07 |

This is consistent with the Disability Standards for Education 2005 [applicability to be confirmed in P10].

### 4.7 Reassessment

- A student whose task is Not Yet Satisfactory receives feedback and at least [two] further attempts at no extra cost [number and fees to be set by directors and stated in P09 Fees].
- Each reattempt targets the gaps identified.
- If the student is still Not Yet Competent after the allowed reattempts, the TAM and the student agree further training and another assessment plan.

### 4.8 Authenticity and academic integrity

- Students sign the authenticity declaration on each submission (P06-T08).
- For online assessment, assessors use the identity and authenticity checks in P06-T08. These can include live video verification, questioning about the submitted work, and checks for copied or AI-generated text.
- Where the assessor isn't satisfied the work is authentic, the assessor gathers further evidence, such as a supervised re-performance or verbal questioning, before deciding.
- Suspected misconduct is handled under [student conduct procedure — to be drafted]. Procedural fairness applies, and the student may appeal.

### 4.9 Appeals

A student may appeal an assessment decision under P12 Complaints and Appeals [to be drafted]. The appeal is reviewed by a credentialled assessor who didn't make the original decision.

## 5. Records

| Record | Kept by | Where |
|---|---|---|
| Marked assessment tasks, observation checklists and evidence | Student Services Officer | Student management system / records system [Ammonite — subject to agreement] |
| Unit outcome and feedback | Assessor | Student management system |
| Pre-use review records (P06-T01) and outcome register (P06-T06) | TAM | Quality records |
| Reasonable adjustment records (P06-T07) | TAM | Student file (confidential) |
| Authenticity declarations and checks (P06-T08) | Assessor | Student file |
| RPL and credit transfer decisions | Assessor / Student Services Officer | Student file |

Retention periods: as set in P02 Document and Record Control [to be drafted], and in line with ASQA's current requirements [to verify].

## 6. Monitoring and improvement

- Assessment practices and judgements are validated under P06-POL-02 and P06-T02.
- Validation and pre-use review findings, student and assessor feedback, complaints and appeals all feed into P06-T06 and the continuous improvement register (P03).
- The TAM reviews this policy at least annually, and when the Standards or a training product changes.

## 7. Definitions

- **Assessment tool:** the instruments and instructions for collecting and interpreting evidence: tasks, instructions, conditions, marking guide, observation checklists, decision rules and mapping.
- **Assessment system:** the policies, procedures, tools, people and records the RTO uses to conduct and quality-assure assessment.
- **Competent / Not Yet Competent:** unit outcomes. **Satisfactory / Not Yet Satisfactory:** task outcomes.
- **Simulated environment:** a setting the RTO operates that reproduces the industry environment, equipment and participants a unit's assessment conditions specify.

## 8. Version history

| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 | 14 Nov 2026 | Claude (draft for AI review) | First draft |

---

# Pre-use Assessment Tool Review and Assessment Validation Policy and Procedure

| Field | Detail |
|---|---|
| Document ID | P06-POL-02 |
| Version | v0.1 |
| Status | DRAFT — not approved. Not for use. |
| Owner (role) | Training and Assessment Manager (TAM) |
| Approved by | |
| Approval date | |
| Next review | |
| Standards references | Outcome Standards 1.3(b)–(c) (pre-use review) and 1.5(a)–(g) (validation) (Standards for RTOs 2025); Credential Policy (validation credentials) |
| Related documents | P06-POL-01 Assessment Policy and Procedure; P06-T01 Pre-use review checklist; P06-T02 Validation plan and schedule; P06-T03 Risk and sampling worksheet; P06-T04 Validator capability and independence check; P06-T05 Validation record; P06-T06 Outcomes and action register; P03 Risk and Continuous Improvement [to be drafted]; P04 Workforce [to be drafted] |

Organisation: The Hospo Hub (proposed company, not yet incorporated; not a registered training organisation).

## 1. Purpose

The RTO quality-assures its assessment system in two separate ways. This document sets out both.

1. **Pre-use review ("pre-validation"):** every assessment tool is reviewed **before** it is used with students. The review checks that assessment can be conducted in line with the principles of assessment and rules of evidence (Std 1.3(b)). Its outcomes are used to make any necessary changes (Std 1.3(c)).
2. **Assessment validation ("post-validation"):** a regular, risk-based review **after** assessment, of assessment practices and judgements. It checks that the assessment system produces judgements consistent with the training product and the Standards (Std 1.5).

Pre-use review does not replace validation, and validation does not replace pre-use review.

## 2. Scope

Every training product on the RTO's scope of registration (see P06-POL-01 section 2), including the RPL tools for each, and every version of every assessment tool.

## 3. Pre-use assessment tool review (Std 1.3)

### 3.1 When it happens
- Before a new tool is first used.
- Before a revised tool is used. Only the changed parts and anything they affect need re-reviewing, but the reviewer records what was re-reviewed.
- When a training product is superseded or its Assessment Requirements change. The tool may not be used again until it is reviewed.

### 3.2 Who reviews
- A person or people with vocational competency in the unit and assessment expertise. Where possible, this is someone other than the tool's developer.
- If the only available reviewer developed the tool, a second reviewer is added. The TAM records why.
- Claude, Codex or any other AI review may help prepare a tool. It does not count as the pre-use review and cannot sign P06-T01.

### 3.3 What is checked (recorded on P06-T01)
- The tool is for the current release of the unit, and the Assessment Requirements were retrieved and dated.
- Every element and performance criterion, foundation skill, performance evidence item (including the required number of occasions or service periods), knowledge evidence item and assessment condition is assessed by a specific task. This must be shown in the task itself, not only in the mapping.
- The setting, equipment, resources and participants match the assessment conditions, under the practical setting rule: online where the unit allows it, otherwise the office simulated environment. Simulation cannot replace a mandatory real-workplace requirement. If the proposed setting can't meet the unit's conditions, the tool is held and the matter goes to the TAM.
- The **principles of assessment** (fair, flexible, valid, reliable) and **rules of evidence** (valid, sufficient, authentic, current) can be met. This includes clear decision rules, model answers or benchmarks, observable behaviours on checklists, and arrangements for reasonable adjustment, reassessment and authenticity.
- The instructions to students and assessors are clear and suit the cohort (domestic, mostly aged 16–22, online-first). Language, literacy and digital demands match the unit, not more.
- The required assessor qualifications and industry experience are stated, for example the three-year industry rule in SITHFAB021, SITHGAM022 and SITHIND007.
- Where students under 18 may take part, the tool complies with P11 [to be drafted].

### 3.4 Outcome
| Outcome | Meaning | Next step |
|---|---|---|
| Approved for use | No changes needed | TAM releases the tool under version control (P02) |
| Approved with minor changes | Changes that don't affect validity | Make the changes; the TAM confirms they're done; then release |
| Not approved | Changes affect validity or coverage | Revise, then a new pre-use review |

Every required change is logged on P06-T06, made, and rechecked (documented on P06-T01) before release (Std 1.3(c)). Where a change's effectiveness can only be shown after first use, a separate follow-up action stays open on P06-T06, with an owner, due date and interim controls, until it is verified.

## 4. Assessment validation (Std 1.5)

### 4.1 Frequency (Std 1.5(b))
- Every training product on scope is validated **at least once every five years**. The plan is on P06-T02.
- A product is validated **sooner** when the RTO becomes aware of any of these:
  - risks to training outcomes (for example high Not Yet Competent rates, appeals upheld, complaints, assessor changes, new delivery settings);
  - changes to the training product;
  - relevant feedback from students, trainers, assessors or industry.
- Recommended practice, not a regulatory requirement: validate each product early in its first year of delivery, once enough completed assessments exist.

### 4.2 Risk-based approach (Std 1.5(c))
For each validation, the TAM uses P06-T03 to decide, from the risks, changes and feedback above:
- which components of the assessment system are validated, for example tools, assessor judgements, RPL decisions or particular tasks; and
- how many completed assessments to sample.

The method and the reasons are recorded. The Standards don't set a sampling formula, so the RTO's documented method is used, and the sample is increased where risk is higher.

### 4.3 Who validates (Std 1.5(e),(f))
- The validation team, together, must have:
  - industry competencies, skills and knowledge relevant to the training product;
  - a practical understanding of current industry practice relevant to the training product;
  - one of the validation credentials in the Credential Policy.
- This is checked and recorded on P06-T04 before validation starts.
- **The outcome of a validation is not decided solely by a person who designed or delivered the training or assessment being validated** (Std 1.5(f)). So at least one person who did not design or deliver the training or assessment being validated must take a substantive part in deciding the outcome. That person may be an external validator, but being external is not enough on its own: they must not have designed or delivered it, and they must genuinely take part in the decision. Their contribution and the decision method are recorded on P06-T05.
- The extra requirement for an independent validator after the first cohort (Std 1.5(d)) applies to qualifications and skill sets from the Training and Education (TAE) Training Package that let people make assessment judgements. It does **not** apply to the RTO's current scope. It would apply if TAE products were added later.
- Engaging external validators, and any cost, needs director approval (lean budget principle).

### 4.4 How validation is done
| Step | Action | Responsible | Record |
|---|---|---|---|
| 1 | Confirm the product is due (schedule or risk trigger) and set the scope and sample. | TAM | P06-T02, P06-T03 |
| 2 | Form the validation team and check capability, credentials and independence. | TAM | P06-T04 |
| 3 | Select the sample of completed assessments, including Competent and Not Yet Competent decisions, different assessors and different settings (online, workplace, simulated). | TAM | P06-T03 |
| 4 | Review each sampled judgement and the tool. Check the evidence meets the rules of evidence, the decision follows the decision rules, and the tool still matches the current unit. | Validation team | P06-T05 |
| 5 | Agree findings and recommendations. Record any team disagreement. The outcome must meet 4.3. | Validation team | P06-T05 |
| 6 | Log each recommendation as an action with an owner and due date. | TAM | P06-T06 |
| 7 | Put changes in place: revise tools (with a new pre-use review), assessor guidance, moderation or professional development. Where judgements were unsound, decide what happens for affected students, such as reassessment. | TAM | P06-T06; P02 version record |
| 8 | Report the results to the CEO and record them in continuous improvement (P03). | TAM | P03 register |

### 4.5 Using the outcomes (Std 1.5(g))
- Validation outcomes drive changes to the assessment system, including tools, procedures, assessor practice and professional development.
- Each action on P06-T06 is closed only with evidence it was done.
- Patterns across validations are reviewed at least once a year in the continuous improvement review (P03).

## 5. Records
| Record | Template | Kept by |
|---|---|---|
| Pre-use review and sign-off | P06-T01 | TAM |
| Validation plan and schedule | P06-T02 | TAM |
| Risk and sampling decisions | P06-T03 | TAM |
| Validator capability and independence check | P06-T04 | TAM |
| Validation record | P06-T05 | TAM |
| Outcomes and action register | P06-T06 | TAM |

Validation records are kept for at least the period set in P02 [to be drafted; to verify against ASQA's current requirements].

## 6. Responsibilities
- **CEO:** makes sure resources exist for pre-use review and validation, approves the validation plan, and receives the results.
- **TAM:** maintains the plan, organises reviews and validations, keeps records and makes sure actions are closed.
- **Trainers/Assessors:** take part as requested and act on the outcomes. They don't validate their own judgements alone.
- **Validators:** review independently and record findings honestly.

## 7. Version history
| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 | 14 Nov 2026 | Claude (draft for AI review) | First draft |

---

# P06-T01 — Pre-use assessment tool review checklist and sign-off


| Document control | Value |
| --- | --- |
| Document ID | P06-T01 |
| Title | Pre-use assessment tool review checklist and sign-off |
| Version | v0.1 |
| Status | DRAFT — not approved |
| Owner role | Training and Assessment Manager (TAM) — role holder to be confirmed |
| Approved by | [ ] |
| Approval date | [ ] |
| Next review | [ ] |
| Standards references | Std 1.3(a)–(c); 1.4(a)–(b) |


## Source and use limits

Outcome Standards 2025, Quality Area 1, [official instrument as made](https://www.legislation.gov.au/F2025L00354/asmade/2025-03-14/text/original/epub/OEBPS/document_1/document_1.html), retrieved 14 November 2026 in the supplied project capture. Check the current compilation before publication. Clause references identify the evidence purpose; the Standards do not prescribe these form fields.

The Hospo Hub is not registered; proposed entity not yet incorporated. This blank draft records no completed activity or approval. Roles do not imply appointments.

## Completion instructions

TAM coordinates review under P06-POL-02 before first use and after tool changes. Review the complete student and assessor packs, mapping and evidence instruments. This is pre-use review, not validation of completed assessment judgements. Repeat rows for every requirement; record Yes / No / N/A with reasons and evidence locations. Hold release while material gaps remain.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Review ID/date; reviewer role; product code/title/release; unit codes/releases | [ ] | 1.3(a)–(b) |
| Tool IDs/versions; student pack, assessor guide, mapping and source requirements locations; intended first use | [ ] | 1.3(a)–(b) |
| Cohort, delivery mode, assessment context and site readiness evidence | [ ] | 1.3(a); 1.4(a) |


| Check | Result / evidence location / reason | Gap / action ID |
| --- | --- | --- |
| All elements, performance criteria, foundation skills, performance evidence, knowledge evidence and assessment conditions mapped and assessed — 1.3(a) | [ ] | [ ] |
| Practical tasks, required frequency, resources, people and assessor requirements match the unit — 1.3(a); 1.4(a)(iii) | [ ] | [ ] |
| Online/virtual only where allowed; otherwise [office simulated environment address], subject to verified unit conditions; mandatory real workplace requirements cannot be replaced by simulation — 1.3(a) | [ ] | [ ] |
| Clear instructions, support, reasonable adjustment and reassessment arrangements — 1.4(a)(i) | [ ] | [ ] |
| Context, learner needs and recognition of prior skills accommodated without reducing requirements — 1.4(a)(ii) | [ ] | [ ] |
| Benchmarks, observation criteria and decision rules support consistent individual judgements — 1.4(a)(iv) | [ ] | [ ] |
| Evidence is relevant and adequate, with sufficient quality, quantity and coverage — 1.4(b)(i)–(ii) | [ ] | [ ] |
| Identity/authenticity checks and currency requirements are workable, including online — 1.4(b)(iii)–(iv) | [ ] | [ ] |
| Assessor requirements in the unit's Assessment Requirements stated and workable (e.g. at least 3 years' industry experience applying the unit's skills for SITHFAB021, SITHGAM022, SITHIND007) — 1.3(a) | [ ] | [ ] |
| Under-18 students: tasks, settings and supervision comply with P11 [to be drafted] (e.g. lawful simulation for SITHGAM022; minors may not play gaming machines) — 1.4(a)(i) | [ ] | [ ] |
| Built for online delivery through the LMS/SMS [Ammonite — subject to agreement]: item IDs, structured question tables, digital observation checklists, evidence upload and electronic sign-off; works on a phone and meets WCAG 2.2 AA — 1.3(a); 1.4(a)(i) | [ ] | [ ] |
| Review findings incorporated; revised versions checked and superseded tools withdrawn — 1.3(c) | [ ] | [ ] |


| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Linked T06 action IDs; revised tool versions; recheck evidence and date | [ ] | 1.3(c) |
| Release recommendation: ready / hold; reasons; authorised release role/date and exact version (leave blank until actual decision) | [ ] | 1.3(b)–(c) |


## LMS/SMS implementation

This form is designed to be built as a digital form in the LMS/SMS [most likely Ammonite — subject to agreement and confirmed capability]. Each row becomes a form field; signatures become electronic sign-off recording the user ID, role and timestamp; attachments are uploaded and linked; completed records are stored in the SMS under P02 [to be drafted]. Until the platform is confirmed, the Markdown version is the master.

## Sign-off and records

Sign-off records responsibility for the completed activity; it does not approve this draft template or establish registration.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Reviewer — name, role, signature and date | [ ] | Std 1.3(a)–(c); 1.4(a)–(b) |
| TAM — review decision, unresolved matters, signature and date | [ ] | Std 1.3(a)–(c); 1.4(a)–(b) |
| Record ID, secure storage location, access roles and linked records | [ ] | Std 1.3(a)–(c); 1.4(a)–(b) |
| Retention rule / authority, disposal review date and responsible role | [ ] | Std 1.3(a)–(c); 1.4(a)–(b) |


Keep the completed form, attachments and version history together in [controlled records repository — to be confirmed]. Restrict personal information to authorised roles; link sensitive evidence securely rather than copying it unnecessarily. Apply the confirmed records policy and applicable retention requirements; do not destroy records before these are established.

---

# P06-T02 — Validation plan and 5-year schedule


| Document control | Value |
| --- | --- |
| Document ID | P06-T02 |
| Title | Validation plan and 5-year schedule |
| Version | v0.1 |
| Status | DRAFT — not approved |
| Owner role | Training and Assessment Manager (TAM) — role holder to be confirmed |
| Approved by | [ ] |
| Approval date | [ ] |
| Next review | [ ] |
| Standards references | Std 1.5(a)–(g) |


## Source and use limits

Outcome Standards 2025, Quality Area 1, [official instrument as made](https://www.legislation.gov.au/F2025L00354/asmade/2025-03-14/text/original/epub/OEBPS/document_1/document_1.html), retrieved 14 November 2026 in the supplied project capture. Check the current compilation before publication. Clause references identify the evidence purpose; the Standards do not prescribe these form fields.

The Hospo Hub is not registered; proposed entity not yet incorporated. This blank draft records no completed activity or approval. Roles do not imply appointments.

## Completion instructions

Use P06-POL-02. On registration, reconcile this plan to the actual scope register; add every authorised product without assuming proposed offerings are registered. Validate every product at least once every five years and earlier when risks to training outcomes, product changes or relevant student, trainer, assessor or industry feedback arise. Five years is an outer limit, not a reason to defer a risk response. Leave all dates blank until evidence and responsibility are confirmed. Pre-use reviews do not count as validation of completed judgements.

SITSS00069 Food Safety Supervision Skill Set (SITXFSA005 + SITXFSA006) is one of the directors' agreed offerings in BASE-01 v0.2 (10 October 2026). Like every row, it is proposed until it is on the actual registered scope.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Plan ID/version; planning period; actual scope register source and reconciliation date | [ ] | 1.5(b) |
| Initial registration/scope addition dates and basis for first validation deadlines; previous validation evidence | [ ] | 1.5(b) |


| Product / scope status | Last validation / evidence | Five-year deadline / basis | Planned validation date / lead role | T03 components and sample / T04 team | Completion T05 / T06 / next due |
| --- | --- | --- | --- | --- | --- |
| SIT20322 — proposed; verify registered scope | [ ] | [ ] | [ ] | [ ] | [ ] |
| SITHFAB021 — proposed standalone; verify registered scope | [ ] | [ ] | [ ] | [ ] | [ ] |
| SITHGAM022 — proposed standalone; verify registered scope | [ ] | [ ] | [ ] | [ ] | [ ] |
| SITXFSA005 — proposed standalone; verify registered scope | [ ] | [ ] | [ ] | [ ] | [ ] |
| SITSS00069 — proposed skill set; verify registered scope | [ ] | [ ] | [ ] | [ ] | [ ] |
| [Additional actual scope product, if authorised] | [ ] | [ ] | [ ] | [ ] | [ ] |


For SIT20322, use T03 to address risk across BSBTWK201, SITHIND006, SITHIND007, SITXCCS011, SITXCOM007, SITXWHS005, SITXFSA005, SITHFAB021, SITHGAM022, SITXFSA006, BSBTEC201 and SITXCOM006. Shared unit evidence must identify qualification and standalone contexts; do not assume one review automatically covers both.

| Trigger / evidence purpose | Evidence / date identified | Risk response / revised date / accountable role | T03 / T06 links |
| --- | --- | --- | --- |
| Risks to training outcomes — 1.5(b)–(c) | [ ] | [ ] | [ ] |
| Training product change — 1.5(b)–(c) | [ ] | [ ] | [ ] |
| Student/trainer/assessor/industry feedback — 1.5(b)–(c) | [ ] | [ ] | [ ] |
| Scheduled scope/deadline monitoring; delay or no completed judgements available — 1.5(b) | [ ] | [ ] | [ ] |


| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Monitoring frequency, responsible role and next review date; overdue escalation and interim controls | [ ] | 1.5(b)–(c) |
| If no completed assessments: earliest available cohort, interim pre-use controls and validation arrangement; do not record validation as complete | [ ] | 1.5(a)–(b) |
| Team capability/independence T04; planned outcomes follow-up T06 | [ ] | 1.5(e)–(g) |


## LMS/SMS implementation

This form is designed to be built as a digital form in the LMS/SMS [most likely Ammonite — subject to agreement and confirmed capability]. Each row becomes a form field; signatures become electronic sign-off recording the user ID, role and timestamp; attachments are uploaded and linked; completed records are stored in the SMS under P02 [to be drafted]. Until the platform is confirmed, the Markdown version is the master.

## Sign-off and records

Sign-off records responsibility for the completed activity; it does not approve this draft template or establish registration.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Plan preparer — name, role, signature and date | [ ] | Std 1.5(a)–(g) |
| TAM — review decision, unresolved matters, signature and date | [ ] | Std 1.5(a)–(g) |
| Record ID, secure storage location, access roles and linked records | [ ] | Std 1.5(a)–(g) |
| Retention rule / authority, disposal review date and responsible role | [ ] | Std 1.5(a)–(g) |


Keep the completed form, attachments and version history together in [controlled records repository — to be confirmed]. Restrict personal information to authorised roles; link sensitive evidence securely rather than copying it unnecessarily. Apply the confirmed records policy and applicable retention requirements; do not destroy records before these are established.

---

# P06-T03 — Risk-based component selection and sample-size worksheet


| Document control | Value |
| --- | --- |
| Document ID | P06-T03 |
| Title | Risk-based component selection and sample-size worksheet |
| Version | v0.1 |
| Status | DRAFT — not approved |
| Owner role | Training and Assessment Manager (TAM) — role holder to be confirmed |
| Approved by | [ ] |
| Approval date | [ ] |
| Next review | [ ] |
| Standards references | Std 1.5(a)–(c), (g) |


## Source and use limits

Outcome Standards 2025, Quality Area 1, [official instrument as made](https://www.legislation.gov.au/F2025L00354/asmade/2025-03-14/text/original/epub/OEBPS/document_1/document_1.html), retrieved 14 November 2026 in the supplied project capture. Check the current compilation before publication. Clause references identify the evidence purpose; the Standards do not prescribe these form fields.

The Hospo Hub is not registered; proposed entity not yet incorporated. This blank draft records no completed activity or approval. Roles do not imply appointments.

## Completion instructions

Under P06-POL-02, define the product and assessment population before selecting records. Select both assessment-system components and completed judgements using documented risk evidence. There is no regulator-mandated sample formula in Std 1.5(c). The method below is a proposed local method, to be justified for each activity; no percentage guarantees compliance. Keep original selections and explain exclusions, substitutions and expansion.

1. Inventory all components and completed assessments in the period, including RPL and reassessments where used.
2. Identify risk strata: units/tasks, assessors, tool versions, sites/modes, cohorts, outcomes, adjustments, authenticity issues and complaints. Rate risk with stated criteria and evidence, not assumptions about age or disability.
3. Select targeted records for known risks, then use a reproducible random or systematic selection within remaining relevant strata. Document why coverage and number are sufficient for the validation purpose.
4. Review linked tools and full evidence behind each selected judgement. Expand into affected strata when evidence is missing or inconsistent judgements or systemic defects are found. Record the stopping rationale and limitations; escalate material risk through T06.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Activity/product/release; T02 link; period; population definition and exclusions | [ ] | 1.5(b)–(c) |
| Population inventory location; total records and distinct students; units, versions, assessors and modes represented | [ ] | 1.5(c) |
| Risk criteria, rating method, training outcome risks, product changes and feedback evidence | [ ] | 1.5(c) |


| Component / stratum | Population count / evidence | Risk / reason | Selected count / record IDs / selection method | Coverage rationale / exclusions |
| --- | --- | --- | --- | --- |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |


### Worked blank example — complete with real data

For [unit/task] delivered via [mode], the inventory contains [N] completed judgement records. Feedback [reference] identifies [risk]. Select [n targeted] records linked to that risk and [n further] records from [remaining strata] using [random seed and ordered list / systematic interval and start]. Deduplicate to [n unique]. This covers [assessors, versions, outcomes and contexts] because [evidence-based rationale]. It excludes [items] because [reason]; the resulting limitation is [ ]. Expand by [method] if [finding threshold]. Stop when [documented coverage and consistency criteria] are met. These symbols are blank variables, not prescribed numbers.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Selected tools, mappings, assessment practices and decision records; evidence access arrangements | [ ] | 1.5(a), (c) |
| Initial and final sample counts; additions/substitutions and reasons; reproducibility record | [ ] | 1.5(c) |
| Expansion findings; stopping rationale; residual uncertainty and follow-up actions T06 | [ ] | 1.5(c), (g) |


## LMS/SMS implementation

This form is designed to be built as a digital form in the LMS/SMS [most likely Ammonite — subject to agreement and confirmed capability]. Each row becomes a form field; signatures become electronic sign-off recording the user ID, role and timestamp; attachments are uploaded and linked; completed records are stored in the SMS under P02 [to be drafted]. Until the platform is confirmed, the Markdown version is the master.

## Sign-off and records

Sign-off records responsibility for the completed activity; it does not approve this draft template or establish registration.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Sampling lead Validator — name, role, signature and date | [ ] | Std 1.5(a)–(c), (g) |
| TAM — review decision, unresolved matters, signature and date | [ ] | Std 1.5(a)–(c), (g) |
| Record ID, secure storage location, access roles and linked records | [ ] | Std 1.5(a)–(c), (g) |
| Retention rule / authority, disposal review date and responsible role | [ ] | Std 1.5(a)–(c), (g) |


Keep the completed form, attachments and version history together in [controlled records repository — to be confirmed]. Restrict personal information to authorised roles; link sensitive evidence securely rather than copying it unnecessarily. Apply the confirmed records policy and applicable retention requirements; do not destroy records before these are established.

---

# P06-T04 — Validation team capability, credential and independence check


| Document control | Value |
| --- | --- |
| Document ID | P06-T04 |
| Title | Validation team capability, credential and independence check |
| Version | v0.1 |
| Status | DRAFT — not approved |
| Owner role | Training and Assessment Manager (TAM) — role holder to be confirmed |
| Approved by | [ ] |
| Approval date | [ ] |
| Next review | [ ] |
| Standards references | Std 1.5(d)–(f); Credential Policy 3A |


## Source and use limits

Outcome Standards 2025, Quality Area 1, [official instrument as made](https://www.legislation.gov.au/F2025L00354/asmade/2025-03-14/text/original/epub/OEBPS/document_1/document_1.html), retrieved 14 November 2026 in the supplied project capture. Check the current compilation before publication. Clause references identify the evidence purpose; the Standards do not prescribe these form fields.

The Hospo Hub is not registered; proposed entity not yet incorporated. This blank draft records no completed activity or approval. Roles do not imply appointments.

## Completion instructions

Complete before validation under P06-POL-02. Verify evidence, not just declarations. The team must collectively cover relevant industry competencies, skills and knowledge, practical understanding of current industry practice, and a specified validation credential. At least one actual participant must hold an accepted credential. If evidence or coverage is missing, hold validation and arrange suitable participation; a planned appointment is not evidence.

### Official credential reference

[Credential Policy, section 3A, page 9 and glossary page 10](https://content.training.gov.au/sites/default/files/2025-03/Credential%20Policy.pdf), retrieved 14 November 2026 by web search and PDF readback. A later version, [Credential Policy 10 December 2025](https://content.training.gov.au/sites/default/files/2025-12/Credential%20Policy%2010%20December%202025.pdf), is reported to contain formatting corrections only; confirm against it before use. Accepted pathways are summarised below (codes identify exact credentials):

- Certificate IV in Training and Assessment: TAE40122 (or successor), TAE40116, or TAE40110.
- Secondary teaching qualification together with TAESS00024 (or successor).
- Assessor Skill Set: TAESS00019 (or successor), TAESS00011, or TAESS00001.
- Diploma or higher qualification in adult education or vocational education and training.

For the last pathway, verify AQF level 5 or above and transcript content covering adult training/assessment and VET competency-based practice; a title alone is insufficient. For teaching, verify a higher education credential meeting academic requirements for secondary teacher registration in at least one Australian jurisdiction. Verify any claimed successor against the current policy/register.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Activity/product/release; T02/T03 links; check date | [ ] | 1.5(e) |
| Current Credential Policy version/source/check date and changes since this draft | [ ] | 1.5(e)(iii) |


| Participant / role / participation planned | Relevant industry capability evidence and coverage — 1.5(e)(i) | Current practical industry understanding evidence/date — 1.5(e)(ii) | Credential code/title/issuer; verified evidence/location/date/verifier — 1.5(e)(iii) | Designed/delivered this training/assessment? Conflicts and controls — 1.5(f) |
| --- | --- | --- | --- | --- |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |


| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Collective coverage map: requirements to participants/evidence; gaps and resolution | [ ] | 1.5(e)(i)–(iii) |
| Who did not design or deliver the training/assessment; their substantive role in considering evidence and determining outcomes | [ ] | 1.5(f) |
| Decision method; safeguards against sole determination by designer/deliverer; disagreement/escalation process | [ ] | 1.5(f) |
| Team ready / hold; reasons and unresolved gaps; recheck arrangements | [ ] | 1.5(e)–(f) |


Std 1.5(d), the additional first-cohort and external-independence rule for specified TAE qualifications/skill sets, is not applicable to the protected SIT/BSB hospitality scope: it contains no TAE training product enabling assessment judgements. SITSS00069 (an agreed offering in BASE-01 v0.2) is not a TAE skill set either. This does not remove 1.5(f). Reassess applicability on any future authorised scope change. A single validator who designed or delivered the training/assessment cannot solely determine its validation outcome.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Scope checked; 1.5(d) applicability confirmed with reason; scope-change referral if needed | [ ] | 1.5(d) |
| Each participant declaration: evidence accurate, conflicts disclosed; signature/date (repeat per participant) | [ ] | 1.5(e)–(f) |


## LMS/SMS implementation

This form is designed to be built as a digital form in the LMS/SMS [most likely Ammonite — subject to agreement and confirmed capability]. Each row becomes a form field; signatures become electronic sign-off recording the user ID, role and timestamp; attachments are uploaded and linked; completed records are stored in the SMS under P02 [to be drafted]. Until the platform is confirmed, the Markdown version is the master.

## Sign-off and records

Sign-off records responsibility for the completed activity; it does not approve this draft template or establish registration.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Capability-check verifier — name, role, signature and date | [ ] | Std 1.5(d)–(f); Credential Policy 3A |
| TAM — review decision, unresolved matters, signature and date | [ ] | Std 1.5(d)–(f); Credential Policy 3A |
| Record ID, secure storage location, access roles and linked records | [ ] | Std 1.5(d)–(f); Credential Policy 3A |
| Retention rule / authority, disposal review date and responsible role | [ ] | Std 1.5(d)–(f); Credential Policy 3A |


Keep the completed form, attachments and version history together in [controlled records repository — to be confirmed]. Restrict personal information to authorised roles; link sensitive evidence securely rather than copying it unnecessarily. Apply the confirmed records policy and applicable retention requirements; do not destroy records before these are established.

---

# P06-T05 — Assessment validation record


| Document control | Value |
| --- | --- |
| Document ID | P06-T05 |
| Title | Assessment validation record |
| Version | v0.1 |
| Status | DRAFT — not approved |
| Owner role | Training and Assessment Manager (TAM) — role holder to be confirmed |
| Approved by | [ ] |
| Approval date | [ ] |
| Next review | [ ] |
| Standards references | Std 1.5(a), (c), (e)–(g); 1.3(a); 1.4(a)–(b) |


## Source and use limits

Outcome Standards 2025, Quality Area 1, [official instrument as made](https://www.legislation.gov.au/F2025L00354/asmade/2025-03-14/text/original/epub/OEBPS/document_1/document_1.html), retrieved 14 November 2026 in the supplied project capture. Check the current compilation before publication. Clause references identify the evidence purpose; the Standards do not prescribe these form fields.

The Hospo Hub is not registered; proposed entity not yet incorporated. This blank draft records no completed activity or approval. Roles do not imply appointments.

## Completion instructions

Use P06-POL-02 after assessment. Attach T03 selection and T04 verified team records. Repeat the judgement block for each selected decision and the tool block for each relevant version. Inspect actual evidence and assessor reasoning; agreement with a result without examining evidence is insufficient. Validation does not itself replace an individual student decision: refer any affected decision for controlled reassessment/review under P06-POL-01.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Activity ID/date; product/unit/releases; period/context; T02/T03/T04 references | [ ] | 1.5(a), (c), (e)–(f) |
| Actual participants, roles, attendance and contribution; any changes from checked team and re-verification | [ ] | 1.5(e)–(f) |


### Per sampled judgement — duplicate this block

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Pseudonymous student/record ID; unit/task; assessor; date; mode/site; tool version; original result and reasons | [ ] | 1.5(a), (c) |
| Full evidence locations; original submission/observations/benchmarks/feedback; missing evidence | [ ] | 1.5(a); 1.4(b) |
| Requirement-by-requirement comparison, including practical evidence and assessment conditions | [ ] | 1.3(a); 1.4(a)(iii), (b)(i)–(ii) |
| Fairness, flexibility and reliability findings, including adjustments and reassessment if relevant | [ ] | 1.4(a)(i)–(iv) |
| Validity, sufficiency, authenticity and currency findings with evidence references for each | [ ] | 1.4(b)(i)–(iv) |
| Validator conclusion: supported / not supported / cannot determine; evidence and differences from original reasoning | [ ] | 1.5(a) |
| Student impact/risk; further sample or decision review referral; T06 action IDs | [ ] | 1.5(c), (g) |


### Per tool / practice — duplicate this block

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Tool/version/practice; requirements tested; evidence of how assessment was conducted | [ ] | 1.5(a) |
| Findings against training product, principles and rules of evidence; systemic versus isolated issues | [ ] | 1.5(a); 1.4(a)–(b) |
| Recommendations, affected cohorts/versions/decisions, interim controls and T06 references | [ ] | 1.5(g) |
| Overall outcome and limitations; sample expansion T03; disagreements and resolution/escalation | [ ] | 1.5(a), (c), (g) |
| How actual outcome was determined; contribution of participant who did not design/deliver; confirmation no sole determination by designer/deliverer | [ ] | 1.5(f) |


## LMS/SMS implementation

This form is designed to be built as a digital form in the LMS/SMS [most likely Ammonite — subject to agreement and confirmed capability]. Each row becomes a form field; signatures become electronic sign-off recording the user ID, role and timestamp; attachments are uploaded and linked; completed records are stored in the SMS under P02 [to be drafted]. Until the platform is confirmed, the Markdown version is the master.

## Sign-off and records

Sign-off records responsibility for the completed activity; it does not approve this draft template or establish registration.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Participating Validators — each signs with date and any dissent — name, role, signature and date | [ ] | Std 1.5(a), (c), (e)–(g); 1.3(a); 1.4(a)–(b) |
| TAM — review decision, unresolved matters, signature and date | [ ] | Std 1.5(a), (c), (e)–(g); 1.3(a); 1.4(a)–(b) |
| Record ID, secure storage location, access roles and linked records | [ ] | Std 1.5(a), (c), (e)–(g); 1.3(a); 1.4(a)–(b) |
| Retention rule / authority, disposal review date and responsible role | [ ] | Std 1.5(a), (c), (e)–(g); 1.3(a); 1.4(a)–(b) |


Keep the completed form, attachments and version history together in [controlled records repository — to be confirmed]. Restrict personal information to authorised roles; link sensitive evidence securely rather than copying it unnecessarily. Apply the confirmed records policy and applicable retention requirements; do not destroy records before these are established.

---

# P06-T06 — Validation and review outcomes and corrective action register


| Document control | Value |
| --- | --- |
| Document ID | P06-T06 |
| Title | Validation and review outcomes and corrective action register |
| Version | v0.1 |
| Status | DRAFT — not approved |
| Owner role | Training and Assessment Manager (TAM) — role holder to be confirmed |
| Approved by | [ ] |
| Approval date | [ ] |
| Next review | [ ] |
| Standards references | Std 1.3(c); 1.5(g) |


## Source and use limits

Outcome Standards 2025, Quality Area 1, [official instrument as made](https://www.legislation.gov.au/F2025L00354/asmade/2025-03-14/text/original/epub/OEBPS/document_1/document_1.html), retrieved 14 November 2026 in the supplied project capture. Check the current compilation before publication. Clause references identify the evidence purpose; the Standards do not prescribe these form fields.

The Hospo Hub is not registered; proposed entity not yet incorporated. This blank draft records no completed activity or approval. Roles do not imply appointments.

## Completion instructions

TAM maintains this register under P06-POL-02 for both pre-use review and validation. Use one row per finding/action, linking T01 or T05. Assign a role and obtain actual acceptance; do not imply anyone is appointed. Close only after objective evidence of implementation and effectiveness is checked. For pre-use review actions, release needs the correction made and a documented pre-release recheck (T01); effectiveness after first use is tracked as a separate follow-up action, kept open with an owner, due date and interim controls until verified. A revised document alone may not show the issue is resolved in practice. Escalate unresolved material risks and overdue actions under the policy.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Register ID/version; responsible role; review date and linked products | [ ] | 1.3(c); 1.5(g) |


| Action ID / source / clause | Finding / evidence / affected tools, students and decisions | Risk / priority / rationale / interim control | Required change / accountable role / acceptance date / due date | Status / escalation date and recipient role |
| --- | --- | --- | --- | --- |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |


| Action ID | Implementation evidence / date / exact revised version | Pre-use recheck T01 / affected decision review under P06-POL-01 | Effectiveness test, evidence / date / verifier role | Residual risk / closed or reopened / next check |
| --- | --- | --- | --- | --- |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] |


| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Communication/training to assessors and relevant students; obsolete version withdrawal; dates/evidence | [ ] | 1.3(c); 1.5(g) |
| Trends, repeat findings, schedule/sample changes T02/T03 and escalation decisions | [ ] | 1.5(g) |
| Closure authorisation: action IDs, reasons, verifier signature/date; open items and next review | [ ] | 1.3(c); 1.5(g) |


## LMS/SMS implementation

This form is designed to be built as a digital form in the LMS/SMS [most likely Ammonite — subject to agreement and confirmed capability]. Each row becomes a form field; signatures become electronic sign-off recording the user ID, role and timestamp; attachments are uploaded and linked; completed records are stored in the SMS under P02 [to be drafted]. Until the platform is confirmed, the Markdown version is the master.

## Sign-off and records

Sign-off records responsibility for the completed activity; it does not approve this draft template or establish registration.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Register custodian — name, role, signature and date | [ ] | Std 1.3(c); 1.5(g) |
| TAM — review decision, unresolved matters, signature and date | [ ] | Std 1.3(c); 1.5(g) |
| Record ID, secure storage location, access roles and linked records | [ ] | Std 1.3(c); 1.5(g) |
| Retention rule / authority, disposal review date and responsible role | [ ] | Std 1.3(c); 1.5(g) |


Keep the completed form, attachments and version history together in [controlled records repository — to be confirmed]. Restrict personal information to authorised roles; link sensitive evidence securely rather than copying it unnecessarily. Apply the confirmed records policy and applicable retention requirements; do not destroy records before these are established.

---

# P06-T07 — Reasonable adjustment request and record


| Document control | Value |
| --- | --- |
| Document ID | P06-T07 |
| Title | Reasonable adjustment request and record |
| Version | v0.1 |
| Status | DRAFT — not approved |
| Owner role | Training and Assessment Manager (TAM) — role holder to be confirmed |
| Approved by | [ ] |
| Approval date | [ ] |
| Next review | [ ] |
| Standards references | Std 1.4(a)(i)–(iv), (b); 1.3(a) |


## Source and use limits

Outcome Standards 2025, Quality Area 1, [official instrument as made](https://www.legislation.gov.au/F2025L00354/asmade/2025-03-14/text/original/epub/OEBPS/document_1/document_1.html), retrieved 14 November 2026 in the supplied project capture. Check the current compilation before publication. Clause references identify the evidence purpose; the Standards do not prescribe these form fields.

The Hospo Hub is not registered; proposed entity not yet incorporated. This blank draft records no completed activity or approval. Roles do not imply appointments.

## Completion instructions

Student Services Officer receives requests under P06-POL-01; Trainer/Assessor assesses implications against the unit. Explain options accessibly to a domestic, online-first cohort aged approximately 16–22. Seek only information needed for support; diagnosis is not a default requirement. Record discussion, student preferences and permission for any relevant disclosure. An adjustment changes access or method while preserving competency and evidence requirements. Do not use this form to waive practical tasks, licensing conditions or assessment conditions.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Record ID/date; student ID; product/unit/release; assessment/task/version and proposed date | [ ] | 1.4(a)(i); 1.3(a) |
| Student-described barrier, preferred contact method and requested support; minimal supporting evidence reference | [ ] | 1.4(a)(i) |
| Consultation with student; accessible explanation of options and student preference; disclosure permissions | [ ] | 1.4(a)(i)–(ii) |
| Under-18 status where relevant; whether guardian/support-person involvement is appropriate; student views, authority/consent basis and information-sharing limits, or N/A with reason | [ ] | 1.4(a)(i) |
| Proposed adjustment: time, format, assistive technology, breaks or other method; implementation arrangements and role | [ ] | 1.4(a)(i)–(ii) |
| Each affected requirement mapped to unchanged competency/evidence standard; practical and licensing/assessment conditions checked | [ ] | 1.3(a); 1.4(a)(iii), (b)(i)–(ii) |
| Online access/connectivity/accessibility; identity and authenticity controls T08; alternative arrangements if needed | [ ] | 1.4(a)(i)–(ii), (b)(iii) |
| Setting: online/virtual only if permitted; otherwise [office simulated environment address] after suitability checks; refer mandatory workplace conditions for resolution | [ ] | 1.3(a); 1.4(a)(iii) |
| Decision: agreed / alternative offered / declined / deferred; reasons, limits, unresolved matters and decision-maker role | [ ] | 1.4(a)(i)–(iv) |
| Student notified date/method; reassessment and appeals pathway explained via P06-POL-01 | [ ] | 1.4(a)(i) |
| Student acknowledgement of discussion (not waiver of rights); signature/date or accessible acknowledgement record | [ ] | 1.4(a)(i) |
| Implementation record; actual supports used; student feedback and review date | [ ] | 1.4(a)(i)–(ii) |
| Assessor evaluation: evidence quality, authenticity, currency and comparable decision standards preserved; further action | [ ] | 1.4(a)(iv), (b) |


Guardian involvement is considered case by case; this template creates no blanket guardian-signature rule. Refer uncertain consent, privacy or safeguarding questions to TAM under applicable confirmed policies before disclosure. A support person must not complete the assessment for the student.

## LMS/SMS implementation

This form is designed to be built as a digital form in the LMS/SMS [most likely Ammonite — subject to agreement and confirmed capability]. Each row becomes a form field; signatures become electronic sign-off recording the user ID, role and timestamp; attachments are uploaded and linked; completed records are stored in the SMS under P02 [to be drafted]. Until the platform is confirmed, the Markdown version is the master.

## Sign-off and records

Sign-off records responsibility for the completed activity; it does not approve this draft template or establish registration.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Trainer/Assessor — name, role, signature and date | [ ] | Std 1.4(a)(i)–(iv), (b); 1.3(a) |
| TAM — review decision, unresolved matters, signature and date | [ ] | Std 1.4(a)(i)–(iv), (b); 1.3(a) |
| Record ID, secure storage location, access roles and linked records | [ ] | Std 1.4(a)(i)–(iv), (b); 1.3(a) |
| Retention rule / authority, disposal review date and responsible role | [ ] | Std 1.4(a)(i)–(iv), (b); 1.3(a) |


Keep the completed form, attachments and version history together in [controlled records repository — to be confirmed]. Restrict personal information to authorised roles; link sensitive evidence securely rather than copying it unnecessarily. Apply the confirmed records policy and applicable retention requirements; do not destroy records before these are established.

---

# P06-T08 — Student authenticity declaration and assessor authenticity/identity checks


| Document control | Value |
| --- | --- |
| Document ID | P06-T08 |
| Title | Student authenticity declaration and assessor authenticity/identity checks |
| Version | v0.1 |
| Status | DRAFT — not approved |
| Owner role | Training and Assessment Manager (TAM) — role holder to be confirmed |
| Approved by | [ ] |
| Approval date | [ ] |
| Next review | [ ] |
| Standards references | Std 1.4(b)(iii); supporting 1.4(a)(i)–(ii), (b)(i)–(iv) |


## Source and use limits

Outcome Standards 2025, Quality Area 1, [official instrument as made](https://www.legislation.gov.au/F2025L00354/asmade/2025-03-14/text/original/epub/OEBPS/document_1/document_1.html), retrieved 14 November 2026 in the supplied project capture. Check the current compilation before publication. Clause references identify the evidence purpose; the Standards do not prescribe these form fields.

The Hospo Hub is not registered; proposed entity not yet incorporated. This blank draft records no completed activity or approval. Roles do not imply appointments.

## Completion instructions

Use P06-POL-01 for each submission or clearly defined group of tasks. Explain the declaration in accessible language. A declaration or LMS login alone does not establish authenticity. Trainer/Assessor records proportionate identity and authorship checks, especially online. Offer an accessible alternative if the student lacks suitable technology or documents. Treat suspected misconduct as a concern to investigate fairly, not a finding based solely on software or appearance.

### Student declaration

I confirm that the work identified below is my own, except for sources and help I have disclosed. I have described any collaboration, assistive tools or AI use and how it follows the assessment instructions. I have not submitted someone else's work as mine or allowed another person to act as me. I understand the assessor may ask me to explain or demonstrate my work and that I can ask for support or clarification.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Student ID; product/unit; task IDs and versions; submission date/version covered | [ ] | 1.4(b)(iii) |
| Sources, collaboration, AI/assistive tools and other help used, or none; relevant permission/instruction reference | [ ] | 1.4(b)(iii) |
| Student signature/date or traceable electronic acknowledgement; accessible declaration explanation if needed | [ ] | 1.4(a)(i), (b)(iii) |


### Assessor checks

Use an approved identity-checking process appropriate to the task: for example a live comparison to verified enrolment identity plus task-specific questioning, or supervised observation and an oral explanation of selected evidence. These are options requiring contextual justification, not mandatory legal methods. Do not collect full identity document copies or recordings by default; record the verification result and secure reference instead. Explain any necessary recording and its access/retention arrangements first.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Assessor role; check date; student/assessment record reference; verified enrolment identity reference | [ ] | 1.4(b)(iii) |
| Identity method and result; online live check or accessible alternative; discrepancies and resolution, without unnecessary identity-document details | [ ] | 1.4(a)(i)–(ii), (b)(iii) |
| Authorship checks: task-specific questions and responses, live demonstration or other corroboration; evidence locations and result | [ ] | 1.4(b)(i)–(iii) |
| If video/third-party evidence used: student identity, date/context, continuity/coverage and corroboration of personal performance | [ ] | 1.4(b)(i)–(iv) |
| Permitted support/adjustment T07; boundary between help and student performance; guardian/support-person involvement where relevant and privacy/consent basis | [ ] | 1.4(a)(i), (b)(iii) |
| Under-18 considerations: explanation understood, appropriate support/contact arrangement and safe/private online participation; no blanket guardian signature rule | [ ] | 1.4(a)(i)–(ii) |
| Concerns and objective evidence; student invited to respond; response, further checks and interim status under P06-POL-01 | [ ] | 1.4(a)(i), (b)(iii) |
| Conclusion: assured / further evidence needed / referred; reasons and evidence; reassessment/appeal information communicated | [ ] | 1.4(a)(i), (b)(iii) |
| Individual competency decision reference, if subsequently made; authenticity alone does not establish validity, sufficiency or currency | [ ] | 1.4(b)(i)–(iv) |


Do not treat AI-detector scores, matching text or a signed declaration as conclusive proof of authorship or misconduct. Where identity or authorship is unresolved, obtain further evidence or refer under the policy before making a competency judgement.

## LMS/SMS implementation

This form is designed to be built as a digital form in the LMS/SMS [most likely Ammonite — subject to agreement and confirmed capability]. Each row becomes a form field; signatures become electronic sign-off recording the user ID, role and timestamp; attachments are uploaded and linked; completed records are stored in the SMS under P02 [to be drafted]. Until the platform is confirmed, the Markdown version is the master.

## Sign-off and records

Sign-off records responsibility for the completed activity; it does not approve this draft template or establish registration.

| Field / instruction | Entry | Evidence purpose |
| --- | --- | --- |
| Trainer/Assessor — name, role, signature and date | [ ] | Std 1.4(b)(iii); supporting 1.4(a)(i)–(ii), (b)(i)–(iv) |
| TAM — review decision, unresolved matters, signature and date | [ ] | Std 1.4(b)(iii); supporting 1.4(a)(i)–(ii), (b)(i)–(iv) |
| Record ID, secure storage location, access roles and linked records | [ ] | Std 1.4(b)(iii); supporting 1.4(a)(i)–(ii), (b)(i)–(iv) |
| Retention rule / authority, disposal review date and responsible role | [ ] | Std 1.4(b)(iii); supporting 1.4(a)(i)–(ii), (b)(i)–(iv) |


Keep the completed form, attachments and version history together in [controlled records repository — to be confirmed]. Restrict personal information to authorised roles; link sensitive evidence securely rather than copying it unnecessarily. Apply the confirmed records policy and applicable retention requirements; do not destroy records before these are established.

---

