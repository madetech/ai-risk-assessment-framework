# AI Risk Assessment Framework — Agent Instructions

This repository contains a practical risk-based framework for assessing AI use on government IT projects. It is a documentation project, not a software project — the primary content is markdown files.

The framework is organised into a **tight core** (the assessment steps) and a **reference library** (supporting detail), so the core stays approachable and detail is one link away.

- `readme.md` — Front door: purpose, the 5-step assessment overview, and ground rules
- `assess/` — The five core assessment steps:
  - `1-scope.md` — define and categorise the use, record the autonomy level, and assess what code/data is shared (merges the old define + data steps)
  - `2-check-tool.md` — the tool eligibility check against the project's tool register
  - `3-identify-risks.md` — the risk heatmap, the eight risk definitions, the autonomy adjustment, and the likelihood/impact matrix
  - `4-safeguards.md` — proportionate mitigations, residual risk, and approvals
  - `5-record-and-work.md` — record the assessment, do the work via the checklist, and share learnings
- `reference/` — Supporting detail linked from the core: `risk-catalogue.md` (the eight risks in depth by use type), `use-type-profiles.md` (the eleven use types), `checklists.md` (per-use before/during/after checklists), `tool-criteria.md`, `government-guidance.md`, `worked-examples.md`, `glossary.md`
- `templates/` — Reusable templates (introduction, risk assessment, tool evaluation)
- `getting-started.md` — Practical guide for applying the framework to a project
- `scripts/` — Utility scripts (e.g. `build-combined.py`, which stitches the sections into a single document; update its `FILE_ORDER` when adding or moving files)

## Writing style

- Write in plain, direct English suitable for a UK government audience
- Use markdown formatting consistently with the existing files (ATX headings, pipe tables, bold for emphasis)
- Keep guidance practical and actionable — this is a working document, not an academic paper
- Use "you" and "your" to address the reader directly
- When referencing other steps or reference material, use relative markdown links (e.g. `[Step 3](3-identify-risks.md)` within `assess/`, or `[risk catalogue](../reference/risk-catalogue.md)` across directories)
- Keep the core steps tight — push detailed or per-use-type material into `reference/` and link to it rather than restating it in the core

## Key concepts

- **Inherent risk** — risk level before mitigations are applied
- **Residual risk** — risk level after mitigations are applied
- **Risk assessments are the record** — there is no separate usage log; each assessed use case has its own risk assessment document
- **"Tools are eligible. Uses are approved."** — two distinct decisions. Eligibility is a property of the tool, recorded on the **tool register** with a classification ceiling, eligible use types, an autonomy ceiling, and conditions. Approval happens in Step 4, on the basis of risk. Never write "approved tool" — say the tool is eligible, or eligible for a given use. State the distinction once where it is needed; it is repeated too easily and reads as anxiety
- **Tool design shapes inherent risk; supplier promises are mitigations** — whether a third party is involved at all changes how big the risk is (Step 3), whereas promises like "no training on inputs" shrink a risk that already exists (Step 4). Keeping this line is what stops inherent and residual collapsing into each other
- **"Stricter wins"** — the more restrictive of this framework and any client/department policy applies by default; a less restrictive approach requires a specific, documented exemption approved by the SRO
- Eleven categories of AI use: coding, code analysis, synthetic data generation, product features, user-facing support, live service operations, user research, design, content, business analysis, general productivity. These describe **tasks people do while delivering a service**, not the services themselves — product features is the one exception, covering AI built into the service. Keep this order in every table that lists them.
- **Autonomy** — a dimension recorded in Step 1 that cuts across all eleven categories: suggests / drafts for review / acts with approval / acts autonomously. It is one of the limits checked against the tool register in Step 2, raises accountability, supply chain, and prompt injection in Step 3, and triggers extra controls plus SRO approval in Step 4
- Eight risk categories: data leakage, accuracy/hallucination, accountability, bias/fairness, IP/licensing, over-reliance, supply chain/security, prompt injection

## When editing

- Do not add content that duplicates what is already covered in another step or appendix — link to it instead
- Keep the framework aligned with UK government guidance (AI Playbook, ATRS, NCSC, ICO)
- Worked examples should be realistic and cover different risk levels and use categories
