# Worked Examples

Six end-to-end assessments, covering different use types, risk levels, and autonomy levels. Each follows the five steps in order. They are illustrative — your ratings should reflect your own situation, not be copied from here.

| # | Use | Category | Autonomy | Inherent → residual |
| ---- | ---- | ---- | ---- | ---- |
| [1](#example-1-coding-assistant-on-an-official-sensitive-project) | Unit test generation | Coding | Drafts for review | Medium → Low |
| [2](#example-2-ai-triage-chatbot-for-a-public-facing-service) | Public triage chatbot | Product feature | Acts autonomously | High → Medium |
| [3](#example-3-code-analysis-across-a-legacy-codebase) | Legacy codebase analysis | Code analysis | Suggests | High → Medium |
| [4](#example-4-service-desk-ticket-triage-and-response) | Service desk triage | User-facing support | Acts autonomously | High → Medium |
| [5](#example-5-a-non-generative-model-prioritising-housing-inspections) | Inspection prioritisation model | Product feature (non-generative ML) | Drafts for review | High → Medium |
| [6](#example-6-an-agent-triaging-and-remediating-production-alerts) | Automated alert remediation | Live service operations | Acts autonomously | High → Medium |

---

## Example 1: Coding assistant on an OFFICIAL-SENSITIVE project

**[Step 1](../assess/1-scope.md) — Scope:** A developer wants to use a cloud-hosted AI coding assistant to help write unit tests for a case management service. The service handles OFFICIAL-SENSITIVE data including personal details of individuals in the justice system.

- **Category:** AI-assisted coding
- **Autonomy:** Drafts for review — the assistant generates whole test files that the developer reviews and edits before committing. Agent mode, which can edit files across the repository unprompted, is disabled in the team's shared configuration.

*What is shared:* The code itself is classified as OFFICIAL-SENSITIVE because it contains business logic that reveals how sensitive cases are handled. The test code will reference data structures that mirror the real data model, including field names for personal information. No real PII will be in the code, but the data structures are revealing.

**[Step 2](../assess/2-check-tool.md) — Check the tool:** The coding assistant (enterprise plan) is on the register, not excluded, and cleared up to OFFICIAL-SENSITIVE — which covers this code. From its profile: **what it is** — cloud-hosted, so code leaves the estate to a third party; sees the open file and surrounding editor context; has an agent mode capable of editing files across the repository, though the team's shared configuration disables it. **What the supplier promises** — no training on inputs, EU processing, SOC 2, audit logging, IP indemnification.

**[Step 3](../assess/3-identify-risks.md) — Inherent risks (before mitigations):**

- **Data leakage: Medium inherent risk (Possible likelihood, Medium impact).** Code snippets containing sensitive business logic and data model structures will be sent to the cloud AI service. No actual PII, but the structures are revealing.
- **Accuracy: Low inherent risk (Possible likelihood, Low impact).** Incorrect unit tests will be caught by code review and test execution. The consequence of a wrong test is limited. The team is alert to the specific failure mode of tests that pass without asserting anything meaningful.
- **Accountability: Low inherent risk.** The developer is clearly accountable for the tests they commit. Standard code review applies.
- **Bias: Low inherent risk.** Not directly applicable to unit test generation.
- **IP: Low inherent risk.** Test code is not typically subject to complex licensing concerns.
- **Over-reliance: Low inherent risk.** The developer is experienced and using AI to accelerate test writing, not to learn testing fundamentals.
- **Supply chain: Low inherent risk.** Unit tests don't typically introduce new dependencies.
- **Prompt injection: Low inherent risk.** The codebase is internal and trusted. The developer is working on their own code, not processing untrusted external content. AI rule files in the repository were audited.

*Autonomy adjustment:* none. At *drafts for review*, with test files small enough to review properly, the heatmap's assumptions hold.

**Overall inherent risk level: Medium** (driven by data leakage).

**[Step 4](../assess/4-safeguards.md) — Safeguards and residual risk:** Medium inherent risk requires enhanced controls and tech lead approval.

Mitigations applied:

- Review all AI-generated tests to ensure they don't expose sensitive business logic in test names or assertions
- Ensure no real data values appear in test fixtures
- Tech lead to review a sample of AI-assisted test code
- Confirm generated tests assert meaningful behaviour rather than merely passing

Residual risk after mitigations:

- **Data leakage: Low residual risk.** The enterprise tool does not train on inputs and has appropriate data residency. Enhanced review ensures no sensitive patterns are exposed in test code. The data model structures are still shared with the AI provider, but the risk is reduced.
- All other categories remain low.

**Overall residual risk level: Low.** Tech lead approval obtained.

**[Step 5](../assess/5-record-and-work.md) — Record, do the work, and share:**

*Record:* The completed assessment is saved in the project's documentation space — it is the record; there is no separate usage log. It captures the inherent risk (medium), mitigations (enhanced review, no real data in fixtures), residual risk (low), and tech lead approval.

*Checklist:* Followed the [AI-Assisted Coding checklist](checklists.md#checklist-ai-assisted-coding). Key items: no secrets in context (confirmed), agent mode disabled so the recorded autonomy level is accurate (confirmed), review all generated code (standard practice), enhanced review for sensitive areas (tech lead reviewing sample).

*Learnings:* No significant issues. Tests were of good quality and saved substantial time. One instance where AI-generated test data was unrealistically similar to real case data — caught in review and replaced with clearly synthetic values. Two generated tests asserted only that a method returned without throwing; both were rewritten. Assessment updated with these learnings.

---

## Example 2: AI triage chatbot for a public-facing service

**[Step 1](../assess/1-scope.md) — Scope:** The team is building an AI-powered chatbot that will help members of the public find the right service for their enquiry. The chatbot asks clarifying questions and directs users to the appropriate team or self-service option. It does not make decisions about eligibility or access — it is a triage tool.

- **Category:** AI-powered product feature
- **Autonomy:** Acts autonomously. The chatbot's replies reach a member of the public with no human reviewing each message. Its scope is narrow — it can reply and route, and cannot change records or make eligibility decisions — but nobody approves what it says before it is said, so it is assessed at the highest level. This triggers SRO approval regardless of the risk rating.

*What is shared:* At runtime, the chatbot processes user messages which may contain PII (names, case references, personal circumstances). The configuration data includes service descriptions and routing rules, which are OFFICIAL. User conversations are logged for quality monitoring.

**[Step 2](../assess/2-check-tool.md) — Check the tool:** This is a new tool, so it needs a profile before use. The team completes one with the [tool profile template](../templates/tool-evaluation.md). Not excluded. **What it is** — a hosted API; user messages leave the estate at runtime, continuously; it produces text that reaches the public directly and holds no access to case records. **What the supplier promises** — UK data residency, GDPR-compliant DPA, no training on inputs, ISO 27001, SOC 2, 99.9% SLA, audit logging via the API. The SRO clears it up to OFFICIAL, which covers the data involved.

**[Step 3](../assess/3-identify-risks.md) — Inherent risks (before mitigations):**

- **Data leakage: High inherent risk (Likely likelihood, High impact).** Users will inevitably share personal and sensitive information in their messages. This data will be processed by the AI service. Data handling must be robust.
- **Accuracy: High inherent risk (Likely likelihood, Medium impact).** If the chatbot directs someone to the wrong service, they may not get the help they need in time. Incorrect triage could have real consequences.
- **Accountability: High inherent risk (Possible likelihood, High impact).** Raised from medium by the autonomy adjustment: no person approves each reply, so accountability rests entirely on the design and on whoever configured it. Users need to understand they are interacting with AI and have a route to a person.
- **Bias: High inherent risk (Possible likelihood, High impact).** The chatbot may struggle with users who have limited English, use assistive technology, or describe their situation in non-standard ways. This could disproportionately affect already disadvantaged groups.
- **IP: Low inherent risk.** Not a significant factor for this use case.
- **Over-reliance: Low inherent risk.** The chatbot supplements, not replaces, existing service channels.
- **Supply chain: High inherent risk (Possible likelihood, High impact).** Raised from medium by the autonomy adjustment. The AI service is a runtime dependency that speaks to the public unsupervised — a provider-side model change alters what the public is told, with no code change on the team's part.
- **Prompt injection: High inherent risk (Likely likelihood, High impact).** The chatbot is public-facing — anyone can interact with it. Users could attempt to extract system prompts, bypass triage logic, or cause the chatbot to produce inappropriate content. Indirect injection is also possible if the chatbot retrieves content from a knowledge base that could be compromised.

**Overall inherent risk level: High** (driven by data leakage, accuracy, accountability, bias, supply chain, and prompt injection).

**[Step 4](../assess/4-safeguards.md) — Safeguards and residual risk:** High inherent risk requires formal documentation and SRO approval. The "acts autonomously" level adds the autonomy controls.

Mitigations applied:

- DPIA completed for user data processing
- ATRS record drafted — the chatbot is an algorithmic tool used in public service delivery
- Model card documenting the system's capabilities, limitations, and intended use
- Human oversight: all triage paths have a "speak to a person" option. Conversations flagged by sentiment analysis are reviewed by staff. Weekly accuracy audit of a sample of conversations
- Fallback: if the chatbot cannot triage with confidence, it routes to a human operator
- Equality Impact Assessment completed, identifying risks for users with limited English and users of assistive technology
- Prompt injection mitigations: adversarial testing (red teaming) conducted before launch. AI output sanitised before rendering to prevent XSS. System prompt does not contain secrets. Trust boundaries enforce that the chatbot cannot access data beyond public service information. Monitoring for anomalous outputs in place
- Autonomy controls: least privilege (read-only access to public service information, no access to case records); no irreversible actions available to it; every conversation logged; a named product owner accountable for its behaviour; a kill switch that reverts the entry point to the existing contact page without a deployment

Residual risk after mitigations:

- **Data leakage: Medium residual risk.** The AI provider has strong data handling guarantees (no training, UK residency, GDPR DPA). However, user PII will still be processed at runtime — the risk is reduced but not eliminated.
- **Accuracy: Medium residual risk.** The "speak to a person" option and fallback routing reduce impact. Weekly accuracy audits will catch systematic issues. But incorrect triage will still occasionally occur.
- **Accountability: Low residual risk.** ATRS record, model card, named owner, conversation logging, and a visible route to a human establish a transparent accountability chain.
- **Bias: Medium residual risk.** Equality Impact Assessment identified key risks and diverse testing was conducted. Ongoing monitoring is in place. But bias cannot be fully eliminated — it requires continuous attention.
- **Supply chain: Low residual risk.** 99.9% SLA, fallback to human operators, and the kill switch limit the impact of service disruption or a behaviour change.
- **Prompt injection: Medium residual risk.** Red teaming, output sanitisation, and trust boundaries significantly reduce the attack surface, and the chatbot has no actions available beyond replying and routing. But prompt injection cannot be fully prevented in a public-facing system — it requires ongoing monitoring.

**Overall residual risk level: Medium.** The mitigations have reduced the overall risk from high to medium. The remaining risks are manageable with the ongoing monitoring and review processes in place. SRO approval obtained. Client approval obtained.

**[Step 5](../assess/5-record-and-work.md) — Record, do the work, and share:**

*Record:* The assessment is saved as the project's record for this use, capturing inherent risk (high), mitigations (DPIA, ATRS, model card, human oversight, EIA, prompt injection hardening, autonomy controls), residual risk (medium), and SRO and client approval.

*Checklist:* Followed the [AI-Powered Product Features checklist](checklists.md#checklist-ai-powered-product-features). All items addressed including DPIA, ATRS, monitoring metrics, human oversight model, diverse testing, accessibility testing, and adversarial testing.

*Learnings:* Ongoing monitoring in place, with monitoring data reviewed and shared monthly. First review date set for four weeks after launch. Incident response process documented and communicated to the team.

---

## Example 3: Code analysis across a legacy codebase

**[Step 1](../assess/1-scope.md) — Scope:** The team is conducting a technical discovery of a legacy case management system. They want to use an AI tool to analyse the codebase (approximately 500,000 lines of Java) to map dependencies between modules, identify areas of high complexity and technical debt, and flag potential security vulnerabilities. The findings will inform a modernisation strategy.

- **Category:** AI-assisted code analysis
- **Autonomy:** Suggests. The tool produces findings; engineers decide what to do with them. It has no write access to the repository.

*What is shared:* The codebase is classified as OFFICIAL-SENSITIVE. It contains business logic for case management in the justice system, including rules about case handling, sentencing calculations, and data access controls. There are configuration files that may contain database connection strings and service endpoints. The codebase also contains comments that reference specific operational procedures.

**[Step 2](../assess/2-check-tool.md) — Check the tool:** The cloud-hosted tool is not yet on the register. The team's existing coding assistant is on it, but cleared only up to OFFICIAL — below this codebase — so it is out on classification alone. The team profiles the options using the [tool profile template](../templates/tool-evaluation.md). A cloud-hosted AI tool with enterprise terms (no training on inputs, UK data residency, SOC 2) is available but requires sending the full codebase to an external service. An alternative is to use a locally-hosted open-source model, which keeps the code on-premises but may produce lower-quality analysis. The team decides to:

1. First run a secrets scanning tool across the codebase to identify and remove embedded credentials
2. Use the cloud-hosted tool with enterprise terms for the bulk analysis, having removed secrets
3. Submit the profile to the SRO for a classification decision, and seek explicit client approval given the OFFICIAL-SENSITIVE data

The SRO clears the tool up to OFFICIAL-SENSITIVE. The profile records what matters for the risk work that follows: **what it is** — the whole codebase leaves the estate to a third party in bulk, and the tool has no write access to the repository. **What the supplier promises** — enterprise terms with no training on inputs, UK residency, SOC 2. The secrets scan is not part of the profile: it is a control this team is choosing to apply, and belongs in their mitigations.

**[Step 3](../assess/3-identify-risks.md) — Inherent risks (before mitigations):**

- **Data leakage: High inherent risk (Likely likelihood, High impact).** The entire codebase — 500,000 lines — will be processed by the AI tool. This includes sensitive business logic, potential embedded credentials, and security-sensitive implementation details. The volume means manual review of every input is impractical.
- **Accuracy: Medium inherent risk (Possible likelihood, Medium impact).** Incorrect analysis could lead to wrong modernisation decisions (e.g. underestimating complexity, missing critical dependencies). However, the analysis will be validated by experienced engineers and is an input to decision-making, not a final decision itself. The team notes that AI is weakest precisely where legacy systems are hardest: undocumented business rules that only make sense in historical policy context.
- **Accountability: Low inherent risk.** The analysis is clearly an AI-assisted input. The team making modernisation decisions is accountable for validating the findings.
- **Bias: Low inherent risk.** Not significantly applicable to code analysis.
- **IP: Low inherent risk.** The codebase is owned by the client. Analysis outputs are advisory.
- **Over-reliance: Medium inherent risk (Possible likelihood, Medium impact).** The team might trust the AI's architectural assessment without sufficient manual verification, especially for parts of the codebase they are less familiar with.
- **Supply chain: Low inherent risk.** The AI tool is used for analysis only, not generating production code, and has no write access.
- **Prompt injection: Medium inherent risk (Possible likelihood, Medium impact).** The legacy codebase could contain comments or string literals that inadvertently or deliberately mislead the analysis tool. Given the size of the codebase, it is impractical to review all comments for adversarial content.

*Autonomy adjustment:* none. At *suggests*, with no write access, the heatmap's assumptions hold.

**Overall inherent risk level: High** (driven by data leakage).

**[Step 4](../assess/4-safeguards.md) — Safeguards and residual risk:** High inherent risk requires formal documentation and SRO approval.

Mitigations applied:

- Secrets scan completed and all embedded credentials removed or redacted before analysis
- Client briefed on the approach and tool, including the data handling guarantees. Client approval obtained in writing
- Analysis findings to be validated by experienced engineers — minimum 20% sample manually verified
- Findings to be cross-referenced with traditional SAST tools for security-related analysis
- AI-derived descriptions of business logic treated as hypotheses to verify against the running system, never as specification
- Limitations of the AI analysis to be clearly documented in the findings report
- Tool's outbound network access restricted
- SRO approval obtained

Residual risk after mitigations:

- **Data leakage: Medium residual risk.** Secrets removed from the codebase before sharing. Enterprise tool does not train on inputs and has UK data residency. However, the full codebase (sensitive business logic, architecture) is still shared with the provider — the risk is reduced but not eliminated.
- **Accuracy: Low residual risk.** 20% manual validation and SAST cross-referencing provide a strong check. Findings are treated as inputs to decision-making, not final decisions.
- **Over-reliance: Low residual risk.** Mandatory manual validation of a sample and domain expert review reduce the risk of uncritical acceptance.
- **Prompt injection: Low residual risk.** Cross-referencing with SAST tools provides an independent check on AI findings. Manual validation of a sample will catch systematic errors introduced by adversarial content. Restricted network access limits what a successful injection could achieve.

**Overall residual risk level: Medium** (driven by data leakage). The mitigations have reduced the overall risk from high to medium.

**[Step 5](../assess/5-record-and-work.md) — Record, do the work, and share:**

*Record:* The assessment is saved as the record for this use, capturing inherent risk (high), mitigations (secrets scan, client approval, 20% manual validation, SAST cross-referencing, restricted network access, SRO approval), and residual risk (medium).

*Checklist:* Followed the [AI-Assisted Code Analysis checklist](checklists.md#checklist-ai-assisted-code-analysis).

- Secrets scan completed before sharing code (confirmed — 14 embedded credentials found and removed)
- Tool data handling confirmed appropriate for OFFICIAL-SENSITIVE with the mitigations applied
- Findings treated as hypotheses: the team manually verified a sample of dependency mappings and found the AI was approximately 85% accurate, with the main issues being outdated or incomplete dependency detection in older modules
- Limitations documented: the AI struggled with the system's custom build configuration and missed some transitive dependencies through proprietary frameworks
- Domain expert (the original system architect, available part-time) reviewed the high-level architectural findings

*Learnings:* The AI was most useful for identifying patterns of code duplication and mapping module boundaries, but less reliable for understanding the intent behind complex business rules — it confidently described a sentencing calculation in terms that turned out to describe a superseded policy. The secrets scan before analysis was essential: 14 credentials would have been exposed. The team recommends this approach for future legacy analysis with the same safeguards.

---

## Example 4: Service desk ticket triage and response

**[Step 1](../assess/1-scope.md) — Scope:** The team wants to use AI to help the service desk manage incoming support tickets for an internal case management system used by approximately 2,000 staff. The AI will auto-categorise and route tickets, suggest responses for agents to review and send, and surface relevant knowledge base articles.

- **Category:** AI-assisted user-facing support
- **Autonomy:** Mixed, so assessed at the higher level: **acts autonomously**. The response path only drafts for review — no reply is sent without an agent approving it. But categorisation and routing happen with no human approving each decision, and a miscategorised ticket changes how urgently a real problem is handled. This triggers SRO approval regardless of the risk rating.

*What is shared:* Support tickets are classified as OFFICIAL but frequently contain OFFICIAL-SENSITIVE material in practice — users paste error messages containing database details, attach screenshots showing case data, and include personal information about themselves and the people they work with. Tickets sometimes contain reports of security vulnerabilities or system misconfigurations. The ticketing system contains approximately 50,000 historical tickets that would be used to fine-tune the categorisation model.

**[Step 2](../assess/2-check-tool.md) — Check the tool:** The team profiles the selected AI service with the [tool profile template](../templates/tool-evaluation.md). Not excluded, and cleared up to OFFICIAL. **What it is** — integrates with the ticketing system via API and holds standing read access to it; ticket content leaves the estate; it can write back to a ticket, so it is capable of acting, not only suggesting. **What the supplier promises** — enterprise tier with no training on inputs, UK residency, SOC 2 and ISO 27001, audit logging, GDPR-compliant DPA.

**[Step 3](../assess/3-identify-risks.md) — Inherent risks (before mitigations):**

- **Data leakage: High inherent risk (Likely likelihood, High impact).** Ticket content is inherently unpredictable. Users routinely paste credentials, share screenshots containing PII and system details, and describe security issues. The volume of historical tickets makes manual review of training data impractical.
- **Accuracy: Medium inherent risk (Possible likelihood, Medium impact).** Incorrect categorisation could delay resolution of critical issues. Wrong troubleshooting suggestions could make problems worse. However, human agents review all responses before sending, which limits the impact on that path.
- **Accountability: High inherent risk (Possible likelihood, High impact).** Raised from medium by the autonomy adjustment. Nobody approves each categorisation, so if the AI routes a critical security incident as routine, there is no person in the chain who made that call — only the configuration. The accountability chain between AI categorisation, agent acceptance, and management oversight needs to be explicit.
- **Bias: Medium inherent risk (Possible likelihood, Medium impact).** The system is used by staff with varying levels of technical literacy and English language proficiency. AI categorisation and response quality may vary across these groups. Historical ticket data may embed existing prioritisation biases.
- **IP: Low inherent risk.** Not a significant concern for internal support operations.
- **Over-reliance: Medium inherent risk (Possible likelihood, Medium impact).** Support agents may stop developing deep system knowledge if they rely on AI-suggested resolutions. The team's ability to function during AI tool outages is a concern.
- **Supply chain: High inherent risk (Possible likelihood, High impact).** Raised from medium by the autonomy adjustment. The AI tool has standing access to the ticketing system and acts on it unsupervised; a provider-side change to categorisation behaviour would alter how the service desk operates with no change on the team's part.
- **Prompt injection: High inherent risk (Possible likelihood, High impact).** Raised from medium by the autonomy adjustment. The user base is known and authenticated rather than public, which keeps likelihood at possible, but a crafted ticket that manipulates categorisation now changes routing directly rather than proposing it to someone.

**Overall inherent risk level: High** (driven by data leakage, accountability, supply chain, and prompt injection).

**[Step 4](../assess/4-safeguards.md) — Safeguards and residual risk:** High inherent risk requires formal documentation and SRO approval. The "acts autonomously" level adds the autonomy controls.

Mitigations applied:

- DPIA completed for AI processing of ticket data containing personal information
- Automatic PII detection and credential scanning implemented on ticket content before it is sent to the AI service
- Defined exclusion rules, enforced in code rather than by the AI: tickets classified as security incidents, data breach reports, or safeguarding concerns are always routed directly to a human with no AI processing
- Confidence thresholds set: categorisation at 70%+, response suggestions at 85%+. Below threshold, tickets are flagged for manual handling
- All AI-suggested responses require human agent approval before sending
- Autonomy controls on the categorisation path: the AI can set a category and a queue, and nothing else — it cannot close, merge, or delete a ticket, or change its priority below the floor set by the exclusion rules. Every categorisation is written to the ticket's audit trail. A named service desk manager is accountable. Categorisation can be switched off from the admin console without a deployment
- Fortnightly accuracy audit of a sample of AI categorisations and suggested responses
- Fallback procedures documented for operating the service desk without AI tools
- SRO approval obtained. IT security team reviewed the prompt injection risk and approved with the exclusion rules in place

Residual risk after mitigations:

- **Data leakage: Medium residual risk.** PII detection and credential scanning significantly reduce exposure, but ticket content is inherently unpredictable — some sensitive data will inevitably reach the AI service before scanning catches it. Exclusion rules prevent the highest-risk tickets from being processed. The enterprise tier's no-training policy and UK data residency further limit the risk.
- **Accuracy: Low residual risk.** Confidence thresholds ensure low-confidence categorisations are flagged for manual handling. Human agents review all suggested responses before sending. Fortnightly audits catch systematic errors.
- **Accountability: Low residual risk.** Named accountable manager, categorisations written to the audit trail, and a documented chain: AI categorises within bounds, agent reviews responses, management audits fortnightly.
- **Bias: Low residual risk.** Bias testing completed during setup. Fortnightly audits include monitoring for disparities across user groups. Threshold adjustments made based on initial findings.
- **IP: Low residual risk.** Unchanged — not a significant concern.
- **Over-reliance: Low residual risk.** Fallback procedures documented and tested. Agents are required to review and edit all AI suggestions, maintaining their system knowledge. Regular training sessions scheduled.
- **Supply chain: Medium residual risk.** Fallback procedures and the ability to disable categorisation without a deployment limit the impact. Bounded permissions mean a behaviour change cannot exceed setting a category and queue. But the dependency remains.
- **Prompt injection: Low residual risk.** Exclusion rules are enforced in code, not by the AI, limiting what a manipulated categorisation can achieve. Confidence thresholds cause unusual inputs to be flagged for manual handling. The internal-only user base significantly reduces the likelihood compared to a public-facing system.

**Overall residual risk level: Medium** (driven by data leakage and supply chain). The mitigations have reduced the overall risk from high to medium.

**[Step 5](../assess/5-record-and-work.md) — Record, do the work, and share:**

*Record:* The assessment is saved as the record for this use, capturing inherent risk (high), mitigations (DPIA, PII scanning, exclusion rules, confidence thresholds, human review, bounded autonomy, fortnightly audits, fallback procedures, SRO and IT security approval), and residual risk (medium).

*Checklist:* Followed the [AI-Assisted User-Facing Support checklist](checklists.md#checklist-ai-assisted-user-facing-support). Key items: PII scanning in place (confirmed), exclusion rules for sensitive ticket types (confirmed), human review of all responses (confirmed), confidence thresholds defined (confirmed), bias testing across user groups (completed — identified that tickets written in terse style received lower confidence scores, threshold adjusted).

*Learnings:* After the first month, categorisation accuracy was 82% and response suggestions were accepted (with minor edits) 68% of the time. Three issues identified: (1) the AI occasionally surfaced knowledge base articles for a deprecated version of the system — addressed by updating the knowledge base; (2) one ticket containing test credentials reached the AI before the PII scanner caught it — the scanner rules were updated; (3) the fortnightly audit found agents were approving suggested responses in a median of four seconds, which is not review — the team added a minimum-display-time and a spot-check on approved responses, and noted this as autonomy creep on the response path. Monthly review cadence established, with monitoring data shared at the team's service review.

---

## Example 5: A non-generative model prioritising housing inspections

*This example covers a use type that is easy to overlook: a conventional machine learning model, not a large language model. Prompt injection barely applies; bias dominates; and the statutory obligations are different.*

**[Step 1](../assess/1-scope.md) — Scope:** A local authority housing service is adding a prioritisation model to its disrepair reporting system. The model scores incoming reports for likely severity — damp and mould, structural defects, hazards to health — and orders the inspection queue. A scheduling officer reviews the ranked queue each morning and books visits.

- **Category:** AI-powered product feature. It is not generative: it is a gradient-boosted classifier trained on historical inspection outcomes.
- **Autonomy:** Drafts for review. The model produces a ranked queue; a scheduling officer reviews it and can reorder before visits are booked.

*What is shared:* The model is trained on six years of historical inspection records — address, property type, tenure, the text of the original report, repair history, and the inspector's recorded outcome. This is personal data: addresses identify households even with names removed. Both training and inference run inside the authority's own cloud tenancy. **No third-party AI service receives any data at any point.**

**[Step 2](../assess/2-check-tool.md) — Check the tool:** There is no third-party service here, so most of the facts a [profile](../assess/2-check-tool.md) records — residency, retention, training on inputs, provider certifications — simply have no supplier to be true of. The team still writes a profile, because the facts that *do* apply are the ones the risk work needs. **What it is** — trained and hosted entirely inside the authority's own tenancy; no data leaves; it scores and ranks but cannot act on the queue. **In place of supplier promises** — a model card covering intended use, training data, performance by subgroup and known limitations; the hosting platform assured under existing arrangements; ML libraries under the standard dependency policy. Cleared up to OFFICIAL by the SRO.

**[Step 3](../assess/3-identify-risks.md) — Inherent risks (before mitigations):**

- **Data leakage: Low inherent risk (Unlikely likelihood, Medium impact).** No external AI service is involved, so the framework's most common leakage route does not exist here. Training data is personal data, but it stays inside the existing system boundary under existing access controls. The residual concern is that models can memorise training records and leak them through their outputs — a ranked score reveals very little, so the exposure is small.
- **Accuracy: High inherent risk (Possible likelihood, High impact).** A wrongly deprioritised damp and mould report can leave a household in a hazardous home for weeks. The consequences fall on residents, not on the service, and the people most affected are least able to escalate.
- **Accountability: High inherent risk (Possible likelihood, High impact).** Residents whose reports are deprioritised need to know a model was involved and have a route to challenge. An ATRS record is required — this is an algorithmic tool affecting public service delivery. The scheduling officer must be a genuine decision-maker rather than a rubber stamp, or the accountability is nominal.
- **Bias: High inherent risk (Likely likelihood, High impact).** The defining risk of this use. Six years of inspection records reflect who historically reported problems and who historically got a visit. Areas and groups that were under-served in the past generated fewer records, so the model learns to keep deprioritising them — a feedback loop that tightens with every retraining cycle. Tenure and property type correlate with ethnicity and disability across the borough, so the model can produce indirectly discriminatory outcomes without ever seeing a protected characteristic as a feature.
- **IP: Low inherent risk.** Model, training data, and outputs are all owned by the authority.
- **Over-reliance: Medium inherent risk (Possible likelihood, Medium impact).** Scheduling officers under time pressure will accept the ranking. Their own judgement about which reports sound urgent will decay, and with it the ability to notice when the model is wrong.
- **Supply chain: Low inherent risk (Unlikely likelihood, Medium impact).** No runtime dependency on an external AI service. The ML libraries are ordinary software dependencies under the authority's existing patching and vulnerability controls.
- **Prompt injection: Not applicable.** The model does not follow instructions and there is no prompt to inject. The analogous risk is **data poisoning** — someone able to influence recorded inspection outcomes over time could shift the model's behaviour. Assessed as low: outcome records are written only by inspectors, under individual accounts, with an audit trail.

**Overall inherent risk level: High** (driven by bias, accuracy, and accountability).

**[Step 4](../assess/4-safeguards.md) — Safeguards and residual risk:** High inherent risk requires formal documentation and SRO approval.

Mitigations applied:

- DPIA completed — the model profiles households using personal data
- ATRS record completed and published
- Equality Impact Assessment completed. Model performance tested across tenure, property type, ward, and the protected characteristics the authority holds
- **A floor rule enforced in code, not by the model:** any report mentioning damp, mould, or a child under two is inspected within the statutory timeframe regardless of its score. The model can raise urgency but never lower it below this floor
- **A random sample to break the feedback loop:** 10% of weekly inspections are drawn at random regardless of score, and their outcomes feed into evaluation. This is the only way to learn about the cases the model would have kept deprioritising
- Named accountable officer for the model's use
- Scheduling officers trained to override, and required to record a reason when they do — which also produces the data for detecting rubber-stamping
- Explanation of the ranking available to residents on request, with a documented complaints route
- Drift monitoring, six-monthly revalidation, and a fixed review date

Residual risk after mitigations:

- **Accuracy: Medium residual risk.** The floor rule removes the worst outcome — a hazardous report sitting unvisited. Random sampling detects systematic under-scoring. But ranking errors within the safe band will still occur.
- **Accountability: Low residual risk.** ATRS record published, named officer, override reasons logged, and an explanation and challenge route available to residents.
- **Bias: Medium residual risk.** The EIA and subgroup testing identified the main risks, and random sampling breaks the feedback loop that would otherwise compound them. But bias embedded in six years of historical data cannot be removed by testing alone — this needs continuous monitoring, and the residual rating reflects that it is managed rather than solved.
- **Over-reliance: Low residual risk.** Override reasons are recorded and reviewed, and officers retain and exercise the decision.
- All other categories remain low.

**Overall residual risk level: Medium** (driven by bias and accuracy).

**[Step 5](../assess/5-record-and-work.md) — Record, do the work, and share:**

*Record:* The assessment is saved as the record for this use, alongside the DPIA, EIA, model card, and ATRS record.

*Checklist:* Followed the [AI-Powered Product Features checklist](checklists.md#checklist-ai-powered-product-features), noting which items did not apply and what replaced them. Adversarial and prompt injection testing were recorded as not applicable, substituted by a data poisoning review of who can write inspection outcomes. Bias testing, accessibility of the explanation route, monitoring metrics, human oversight model, and the ATRS record were all completed.

*Learnings:* After three months, the random-sample inspections found the model was systematically under-scoring reports from one ward with a high proportion of tenants who do not speak English as a first language. Their reports were shorter and used less of the vocabulary the model had learned to associate with severity, so the model read brevity as low urgency. The model was retrained with report length removed as a feature and the text handling revised. **This would not have been detected without the random sample** — every other monitoring measure looked healthy, because the model was accurate on the cases it chose to send inspectors to. The team has recommended the random-sample control to other services in the authority using scoring models.

---

## Example 6: An agent triaging and remediating production alerts

*This example covers the autonomy dimension doing real work: the same tool at "acts with approval" and at "acts autonomously" produces materially different assessments.*

**[Step 1](../assess/1-scope.md) — Scope:** The team runs a public-facing application service and wants to use an AI agent, integrated with their observability platform, to triage out-of-hours alerts. In phase one, the agent investigates and proposes a remediation, and the on-call responder approves each action. In phase two, planned for the following quarter, the agent would apply a fixed set of pre-approved remediations — restarting a stuck queue worker, scaling a service up — without waking anyone.

- **Category:** AI-assisted live service operations
- **Autonomy:** Assessed at **acts autonomously**. Phase one is "acts with approval", but the team assesses at the higher level for two reasons: they intend to move to phase two within the quarter, and the per-action approval is a configuration flag that anyone with admin access can turn off. Assess what the tool is permitted to do, not what you intend to let it do. This triggers SRO approval regardless of the risk rating.

*What is shared:* Production logs, traces, metrics, alert payloads, deployment manifests, and infrastructure state. The service handles OFFICIAL data including personal details of applicants, and its logs were never written on the assumption that a third party would read them.

**[Step 2](../assess/2-check-tool.md) — Check the tool:** The vendor's agent product is not excluded, and the SRO clears it up to OFFICIAL. **What it is** — integrates with the observability platform and holds standing read access to the full production telemetry stream; can execute actions against production, not merely propose them. **What the supplier promises** — UK and EU data residency, no training on customer inputs, SOC 2 and ISO 27001, an audit API. Two facts carry unusual weight here because the tool can act. On **change and notice**, the vendor confirms 30 days' contractual notice of model changes — without which the team would have an agent in production whose behaviour could shift silently. On **control over what it can do**, the vendor confirms customer-defined action allowlists, and the team goes further by enforcing the limit in their own IAM rather than the agent's configuration, so a change at the vendor's end cannot widen it.

Note what the profile does and does not settle. It records that the agent is *capable* of acting autonomously against production — a fact, and the reason this assessment is a serious one. It does not say the team may let it. That is their autonomy decision in Step 1, and the controls that bound it are mitigations in Step 4.

**[Step 3](../assess/3-identify-risks.md) — Inherent risks (before mitigations):**

- **Data leakage: High inherent risk (Likely likelihood, High impact).** Logs contain session tokens, authorisation headers, connection strings, and applicant PII in error payloads. Unlike a one-off share, the agent has standing read access to the whole telemetry stream, continuously, with nobody reviewing what it sees.
- **Accuracy: High inherent risk (Possible likelihood, High impact).** A confidently wrong root cause at 3am leads to a wrong remediation. Restarting the wrong component during a partial outage can turn degradation into a full outage, and incident pressure is precisely when plausible-sounding output gets least scrutiny.
- **Accountability: High inherent risk (Possible likelihood, High impact).** Raised by the autonomy adjustment to at least high impact. In phase two nobody chooses each action; the decision was made months earlier by whoever configured the allowlist. Without deliberate design, the incident record will show a system that recovered without showing what recovered it.
- **Bias: Low inherent risk.** Not materially applicable to alert triage.
- **IP: Low inherent risk.** Generated runbook and configuration content is small in volume and internal.
- **Over-reliance: Medium inherent risk (Possible likelihood, Medium impact).** Out-of-hours incidents are where diagnostic skill is built. If the agent handles the routine ones, new joiners may never work an unassisted incident, and the team's ability to cope when the agent is wrong — or down — decays quietly.
- **Supply chain: High inherent risk (Possible likelihood, High impact).** Raised by the autonomy adjustment to at least high impact. The agent holds credentials in production. A vendor compromise, or a model update that changes its behaviour, is a production incident that the team did not cause and cannot see coming.
- **Prompt injection: High inherent risk (Likely likelihood, High impact).** Raised by the autonomy adjustment, and the vector here is unusually accessible: the service logs user-supplied form fields, so anyone who can submit the public form can place text in front of the agent without authenticating or touching any system. Combined with the ability to act, this is remote action in production triggered by an anonymous member of the public.

**Overall inherent risk level: High**, and SRO approval is required by the autonomy level regardless.

**[Step 4](../assess/4-safeguards.md) — Safeguards and residual risk:** High inherent risk requires formal documentation and SRO approval, plus the autonomy controls.

Mitigations applied:

- **Least privilege enforced outside the agent.** The action allowlist lives in the team's own IAM policy, not in the agent's configuration: the agent authenticates with a service account permitted exactly four operations. Anything else fails at the infrastructure layer regardless of what the agent decides to do. A control the AI can be talked out of is not a control
- **No irreversible actions in the allowlist.** No data deletion, no access-control change, no deployment, no scale-to-zero. Every permitted action is reversible within minutes
- **Credential scrubbing in the log pipeline** before logs reach the agent, verified by a test that plants a known token upstream and asserts it is redacted downstream
- **Full action logging.** Every action is written to the incident record with the service account identity, the triggering alert, and the agent's stated reasoning
- **Kill switch.** Any on-call engineer can disable the agent's service account from the runbook without a deployment. Tested monthly
- **Rate limit.** No more than three automated remediations per hour, after which the agent stops and pages a human — this stops a misdiagnosis becoming a loop
- **Named accountable owner:** the service's lead SRE
- **Injection testing.** Adversarial strings submitted through the public form and traced through the log pipeline to confirm they cannot trigger an action
- **Phase two gated** on eight weeks of phase one operation with no incorrect proposed action
- SRO approval obtained, as required by the autonomy level

Residual risk after mitigations:

- **Data leakage: Medium residual risk.** Scrubbing is verified and tested, but log content is unpredictable and new code paths can log new things. The exposure is ongoing rather than one-off, so this stays at medium.
- **Accuracy: Medium residual risk.** The allowlist bounds what a wrong diagnosis can do to four reversible actions, and the rate limit stops loops. Wrong diagnoses will still happen.
- **Accountability: Low residual risk.** Named owner, full action logging into the incident record, and reasoning captured alongside each action.
- **Over-reliance: Medium residual risk.** Partly mitigated by rotating engineers through unassisted incident practice, but the underlying tension is real and the team has chosen to accept it with monitoring.
- **Supply chain: Medium residual risk.** Because permissions are enforced in the team's IAM rather than the vendor's configuration, a compromised or altered agent still cannot exceed four reversible actions. The 30-day model change notice gives time to re-test. The dependency itself remains.
- **Prompt injection: Medium residual risk.** A successful injection can at worst trigger one of four safe, reversible, rate-limited, logged actions. That is a bounded outcome rather than a prevented one — injection cannot be eliminated, so the control is on consequences, not likelihood.

**Overall residual risk level: Medium.**

**[Step 5](../assess/5-record-and-work.md) — Record, do the work, and share:**

*Record:* The assessment is saved as the record for this use, capturing the autonomy level and the reasoning for assessing at the higher level, inherent risk (high), the autonomy controls, residual risk (medium), and SRO approval with a review date at the phase two gate.

*Checklist:* Followed the [AI-Assisted Live Service Operations checklist](checklists.md#checklist-ai-assisted-live-service-operations). What may and may not be shared was agreed and written into the runbook before go-live rather than during an incident. Credential-bearing log fields identified and restricted. Kill switch tested. Autonomy level confirmed against the tool's actual configuration.

*Learnings:* Over eight weeks of phase one the agent proposed the correct remediation for 31 of 38 alerts. Of the seven wrong proposals, two would have made the incident worse — both during partial outages where the agent read a downstream symptom as the cause. Phase two was **delayed rather than approved**, and the allowlist narrowed to exclude restarts while a multi-component incident is declared. Separately, the injection test found the log scrubber missed tokens arriving in a third-party webhook payload, which had not been in scope when the scrubbing rules were written. Both findings were shared at the department's SRE community of practice.
