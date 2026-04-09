# AI Risk Assessment Framework — Agent Instructions

This repository contains a practical risk-based framework for assessing AI use on government IT projects. It is a documentation project, not a software project — the primary content is markdown files.

## Repository structure

- `readme.md` — Main framework overview with the 8-step process and table of contents
- `step-1-define.md` through `step-8-share.md` — The eight assessment steps
- `appendix-a-tool-evaluation.md` through `appendix-e-worked-examples.md` — Supporting appendices
- `getting-started.md` — Practical guide for applying the framework to a project
- `templates/introduction.md` — Template for teams to adopt into their own documentation
- `scripts/` — Utility scripts (e.g. combining sections into a single document)

## Writing style

- Write in plain, direct English suitable for a UK government audience
- Use markdown formatting consistently with the existing files (ATX headings, pipe tables, bold for emphasis)
- Keep guidance practical and actionable — this is a working document, not an academic paper
- Use "you" and "your" to address the reader directly
- When referencing other steps or appendices, use relative markdown links (e.g. `[Step 3](step-3-assess-risks.md)`)

## Key concepts

- **Inherent risk** — risk level before mitigations are applied
- **Residual risk** — risk level after mitigations are applied
- **Risk assessments are the record** — there is no separate usage log; each assessed use case has its own risk assessment document
- **"Stricter wins"** — where a client or department has its own AI policy, the more restrictive position takes precedence
- Six categories of AI use: coding, code analysis, product features, support, research & design, general productivity
- Eight risk categories: data leakage, accuracy/hallucination, accountability, bias/fairness, IP/licensing, over-reliance, supply chain/security, prompt injection

## When editing

- Do not add content that duplicates what is already covered in another step or appendix — link to it instead
- Keep the framework aligned with UK government guidance (AI Playbook, ATRS, NCSC, ICO)
- Worked examples in Appendix E should be realistic and cover different risk levels and use categories
