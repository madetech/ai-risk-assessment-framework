# AI Use on This Project

## Purpose

This document sets out how this project approaches the use of AI tools. It provides a clear statement of our position, the people responsible for AI governance, and where to find the detailed framework we follow.

We use the [Practical Risk-Based Approach to the Use of AI in Projects](https://github.com/madetech/ai-risk-assessment) framework to assess and manage AI use. This document summarises our local application of that framework.

## Our approach

We recognise that AI tools can significantly improve the quality and efficiency of delivery work when used responsibly. Our approach is:

- **Risk-based** — we assess each AI use case individually rather than applying blanket rules. Higher-risk uses require more rigorous assessment and approval.
- **Proportionate** — safeguards are matched to the level of risk. Low-risk uses follow standard practices; higher-risk uses require formal documentation and senior approval.
- **Transparent** — all AI use is recorded, and assessments are available for review. Each assessed use case has its own risk assessment document; that assessment is the record, and we review our assessments regularly.
- **"Stricter wins" by default** — where this framework and our client or department policy differ, the more restrictive position on any given point applies automatically. A less restrictive approach is only permitted with a specific, documented exemption approved by the SRO.

## Responsible people

| Role | Name | Responsibilities |
| ---- | ---- | ---- |
| **Senior Responsible Owner (SRO)** | [Name] | Overall accountability for AI use on the project. Approves high-risk use cases and new tools. |
| **Delivery Lead** | [Name] | Day-to-day oversight of AI use. Approves medium-risk use cases. Reviews the project's risk assessments periodically. |
| **Technical Lead** | [Name] | Assesses technical risks, tool suitability, and security implications. Reviews mitigations for coding and product feature use cases. |
| **Data Protection Lead** | [Name] | Advises on data classification, PII handling, and DPIA requirements. Reviews use cases involving personal data. |

## Tool register

The following AI tools have been assessed. Each has a **profile** recording what it does and what its supplier promises. A profile is not permission to use the tool for a given task — that is decided by the risk assessment for each specific use.

| Tool (and tier) | Highest classification cleared | What it is, in short | Full profile | Last reviewed |
| ---- | ---- | ---- | ---- | ---- |
| [e.g. GitHub Copilot Business] | [e.g. OFFICIAL] | [e.g. Cloud-hosted, EU processing, no training on inputs, can run an agent mode that edits files and opens PRs] | [Link] | [Date] |
| | | | | |
| | | | | |

**Do not use a tool that is not on this register.** If you want to use a new one, speak to the Technical Lead and complete a profile using the [tool profile template](https://github.com/madetech/ai-risk-assessment/blob/main/templates/tool-evaluation.md).

If your data is above a tool's cleared classification, escalate to the SRO before using it.

**Do not use free or consumer versions of AI tools** (e.g. free ChatGPT, consumer Claude) for any work-related information.

## How to assess a new AI use case

Before using AI for a new activity, follow the five-step assessment process:

1. **Scope your use** — define the activity, categorise it, record how much the AI is allowed to do on its own, and assess what code and data you will share
2. **Identify the risks** — find the risks that matter for your use, rate each, adjust for autonomy, and take the highest as your inherent risk level
3. **Check the tool** — confirm it is approved for your classification and use
4. **Safeguards and approvals** — apply mitigations proportionate to the inherent risk, reassess the residual risk, and get the required sign-off
5. **Record and do the work** — save the assessment, follow the relevant checklist, and share what you learned

For full details, see the [framework documentation](https://github.com/madetech/ai-risk-assessment).

## Training and awareness

Before using AI tools on this project, all team members should:

- Read this document
- Be familiar with the assessment framework (at minimum, the overview and the checklist for their use type)
- Understand the data classification levels relevant to their work
- Know which tools are approved and where to find this list

## Review

This document should be reviewed when:

- The tool register changes
- Responsible people change
- The project's risk profile changes significantly
- At least every six months

| Date | Reviewed by | Changes |
| ---- | ---- | ---- |
| [Date] | [Name] | Initial version |
| | | |
