# Reference: Alignment with UK Government Guidance

This framework is designed to be consistent with current UK Government guidance on AI. It does not replace that guidance but provides a practical mechanism for delivery teams to apply it in their day-to-day work.

## Key publications this framework aligns with

- **[AI Playbook for the UK Government](https://assets.publishing.service.gov.uk/media/67aca2f7e400ae62338324bd/AI_Playbook_for_the_UK_Government__12_02_.pdf)** (February 2025) — the primary government guidance on AI use, setting out 10 principles for responsible AI including knowing AI's limitations, using AI lawfully and ethically, and maintaining meaningful human control. This framework operationalises those principles into a practical assessment process. Its accompanying [AI Knowledge Hub guidance on security](https://ai.gov.uk/knowledge-hub/how-to/security/) sets the rule that public or unassured generative AI must not process OFFICIAL information carrying additional markings such as ‑SENSITIVE or ‑PERSONAL.

- **Data and AI Ethics Framework** (updated December 2025) — provides ethical principles covering privacy, fairness, accountability, and transparency, along with a self-assessment tool. The risk categories in [Step 3: Assess the Risks](../assess/3-assess-risks.md) map directly to these principles.

- **[Algorithmic Transparency Recording Standard (ATRS)](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub)** — mandatory for central government departments since 2024. If you are building a product feature or using AI in user-facing support in a way that involves algorithmic decision-making affecting how requests are handled, you may need to complete an ATRS record. This is addressed in [Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md) and the relevant [checklists](checklists.md).

- **Code of Practice for the Cyber Security of AI** (January 2025) — establishes baseline security requirements for AI systems across five lifecycle phases. The facts recorded in a [tool profile](../assess/2-check-tool.md) and the security considerations in the [risk catalogue](risk-catalogue.md) reflect these requirements.

- **NCSC guidance on prompt injection** (December 2025) — the National Cyber Security Centre's position that prompt injection "may never be totally mitigated" and that LLMs should be treated as "inherently confusable deputies." This informs the prompt injection risk category and the emphasis on deterministic safeguards and least privilege throughout the checklists.

- **[Government Security Classifications Policy](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1166145/Government_Security_Classifications_Policy_June_2023.pdf)** (June 2023; [quick read](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1166147/Government_Security_Classifications_Policy_Quick_Read.pdf)) — the classification framework (OFFICIAL, SECRET, TOP SECRET, with ‑SENSITIVE as a handling caveat on OFFICIAL) is one of the key inputs to the data assessment in [Step 1: Scope Your Use](../assess/1-scope.md). Its requirement that SECRET and above be handled on dedicated accredited systems is the basis for the [hard stop at those tiers](../assess/1-scope.md#if-your-data-is-secret-or-above).

- **ICO AI and Data Protection Risk Toolkit** — the Information Commissioner's Office's practical toolkit for assessing AI systems against UK GDPR requirements, covering accountability, transparency, lawfulness, accuracy, fairness, security, individual rights, and automated decision-making. The risk assessment and the DPIA requirements align with this toolkit.

- **ICO Toolkit for Data Analytics** — the ICO's introductory assessment for organisations considering data analytics, covering lawfulness, accountability, data protection principles, and data subject rights. Useful for teams new to AI-assisted data processing.

- **Understanding AI Ethics and Safety** (Office for AI / GDS / Alan Turing Institute) — establishes the SUM values framework (respect dignity, connect sincerely, care for wellbeing, protect social values) and the FAST Track principles (Fairness, Accountability, Sustainability, Transparency) for public sector AI. The ethical considerations throughout this framework reflect these principles.

- **UNESCO Recommendation on the Ethics of AI** (2021) — adopted by all 193 UNESCO member states, establishing principles including proportionality, safety, privacy, accountability, transparency, and human oversight. Provides the broader ethical context for responsible AI use.

- **AI Action Plan for Justice** (2025) — for teams working on justice sector projects, this sets out the Ministry of Justice's approach to AI adoption, including the role of the Justice AI Unit, the SAFE-D ethical principles (Sustainability, Accountability, Fairness, Explainability, Data Responsibility), and approved tools. Justice sector teams should follow this plan alongside this framework.

## Mapping to the AI Playbook's 10 principles

| AI Playbook principle | Where addressed in this framework |
| ---- | ---- |
| 1. Know AI's limitations | [Step 3](../assess/3-assess-risks.md) (Accuracy and hallucination), [checklists](checklists.md) (all require human review) |
| 2. Use AI lawfully and ethically | [Step 1](../assess/1-scope.md) (data and consent assessment), [Step 3](../assess/3-assess-risks.md) (bias and fairness, IP), [risk assessment template](../templates/risk-assessment.md) |
| 3. Ensure meaningful human control | [Step 3](../assess/3-assess-risks.md) (per-risk mitigations, plus those that scale with autonomy), [Step 4](../assess/4-record-and-work.md) (approvals), [checklists](checklists.md) (human review in all) |
| 4. Be transparent about AI use | [Step 4](../assess/4-record-and-work.md) (record and share), [checklists](checklists.md) (ATRS, methodology documentation) |
| 5. Use the right tool for the job | [Step 1](../assess/1-scope.md) (define the use), [Step 2](../assess/2-check-tool.md) (tool profiles) |
| 6. Work collaboratively | [Step 4](../assess/4-record-and-work.md) (share and document learnings, periodic review) |
| 7. Manage AI throughout its lifecycle | [checklists](checklists.md) (ongoing monitoring), [Step 4](../assess/4-record-and-work.md) (periodic review) |
| 8. Secure AI systems | [Step 3](../assess/3-assess-risks.md) (supply chain and security, prompt injection), [Step 2](../assess/2-check-tool.md) (security certifications), [checklists](checklists.md) (all include prompt injection considerations). Aligned with the NCSC's guidance that prompt injection is a design-time concern requiring deterministic safeguards and least privilege. |
| 9. Use AI proportionately | [Step 3](../assess/3-assess-risks.md) (risk rating and proportionate mitigations), [Step 4](../assess/4-record-and-work.md) (approval scaled to the level) |
| 10. Learn, iterate, and improve | [Step 4](../assess/4-record-and-work.md) (share and document learnings, periodic review) |

## Mapping to other referenced frameworks

| Framework | Key principles | Where addressed in this framework |
| ---- | ---- | ---- |
| **ICO AI and Data Protection Risk Toolkit** | Accountability, transparency, lawfulness, accuracy, fairness, security, individual rights, Article 22 compliance | [Step 1](../assess/1-scope.md) (data assessment, GDPR), [Step 3](../assess/3-assess-risks.md) (all risk categories), [Step 4](../assess/4-record-and-work.md) (DPIA), [risk assessment template](../templates/risk-assessment.md) |
| **ICO Data Analytics Toolkit** | Lawfulness, accountability, data protection principles, data subject rights | [Step 1](../assess/1-scope.md) (data classification, consent), [Step 2](../assess/2-check-tool.md) (tool profiles) |
| **UNESCO Recommendation on the Ethics of AI** | Proportionality, safety, privacy, governance, accountability, transparency, human oversight, sustainability, awareness, fairness | Proportionality: [Step 3](../assess/3-assess-risks.md). Human oversight: [checklists](checklists.md). Fairness: [Step 3](../assess/3-assess-risks.md) (bias). Transparency: [Step 4](../assess/4-record-and-work.md). Awareness: ground rules in the [overview](../readme.md). |
| **Understanding AI Ethics and Safety (SUM/FAST)** | Fairness, Accountability, Sustainability, Transparency | Fairness: [Step 3](../assess/3-assess-risks.md) (bias and fairness). Accountability: [Step 3](../assess/3-assess-risks.md) (accountability gaps), [Step 4](../assess/4-record-and-work.md). Sustainability: [checklists](checklists.md) (ongoing monitoring). Transparency: [Step 4](../assess/4-record-and-work.md) (ATRS). |
| **AI Action Plan for Justice (SAFE-D)** | Sustainability, Accountability, Fairness, Explainability, Data Responsibility | Sustainability: [checklists](checklists.md) (ongoing monitoring), [Step 4](../assess/4-record-and-work.md) (periodic review). Accountability: [Step 3](../assess/3-assess-risks.md), [Step 4](../assess/4-record-and-work.md). Fairness: [Step 3](../assess/3-assess-risks.md) (bias). Explainability: [checklists](checklists.md) (ATRS, model card). Data Responsibility: [Step 1](../assess/1-scope.md), [Step 2](../assess/2-check-tool.md). |
