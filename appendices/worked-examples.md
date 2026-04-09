# Worked Examples

## Example 1: Developer using an AI coding assistant on an OFFICIAL-SENSITIVE project

**[Step 1](step-1-define.md) — Define the use:** A developer wants to use an AI coding assistant (cloud-hosted) to help write unit tests for a case management service. The service handles OFFICIAL-SENSITIVE data including personal details of individuals in the justice system.

**[Step 2](step-2-understand-data.md) — Understand the data:** The code itself is classified as OFFICIAL-SENSITIVE because it contains business logic that reveals how sensitive cases are handled. The test code will reference data structures that mirror the real data model, including field names for personal information. No real PII will be in the code, but the data structures are revealing.

**[Step 3](step-3-assess-risks.md) — Assess the inherent risks (before mitigations):**

- **Data leakage: Medium inherent risk (Possible likelihood, Medium impact).** Code snippets containing sensitive business logic and data model structures will be sent to the cloud AI service. No actual PII, but the structures are revealing.
- **Accuracy: Low inherent risk (Possible likelihood, Low impact).** Incorrect unit tests will be caught by code review and test execution. The consequence of a wrong test is limited.
- **Accountability: Low inherent risk.** The developer is clearly accountable for the tests they commit. Standard code review applies.
- **Bias: Low inherent risk.** Not directly applicable to unit test generation.
- **IP: Low inherent risk.** Test code is not typically subject to complex licensing concerns.
- **Over-reliance: Low inherent risk.** The developer is experienced and using AI to accelerate test writing, not to learn testing fundamentals.
- **Supply chain: Low inherent risk.** Unit tests don't typically introduce new dependencies.
- **Prompt injection: Low inherent risk.** The codebase is internal and trusted. The developer is working on their own code, not processing untrusted external content. AI rule files in the repository were audited.

**Overall inherent risk level: Medium** (driven by data leakage).

**[Step 4](step-4-check-tool.md) — Check the tool:** The coding assistant is on the project's approved tools list (enterprise plan). Confirmed: no training on inputs, EU data residency, SOC 2 certification, audit logging, and IP indemnification. Meets all criteria. As this is an approved tool being used within its approved scope, no additional SRO approval is needed at this step.

**[Step 5](step-5-mitigate.md) — Mitigations and residual risk:** Medium inherent risk requires enhanced controls and tech lead approval.

Mitigations applied:

- Review all AI-generated tests to ensure they don't expose sensitive business logic in test names or assertions
- Ensure no real data values appear in test fixtures
- Tech lead to review a sample of AI-assisted test code

Residual risk after mitigations:

- **Data leakage: Low residual risk.** The enterprise tool does not train on inputs and has appropriate data residency. Enhanced review ensures no sensitive patterns are exposed in test code. The data model structures are still shared with the AI provider, but the risk is reduced.
- All other categories remain low.

**Overall residual risk level: Low.** Tech lead approval obtained.

**[Step 6](step-6-record.md) — Record:** Logged in AI usage log with inherent risk (medium), mitigations (enhanced review, no real data in fixtures), residual risk (low), and tech lead approval.

**[Step 7](step-7-checklists.md) — Checklist:** Follow checklist 7a (AI-Assisted Coding). Key items: no secrets in context (confirmed), review all generated code (standard practice), enhanced review for sensitive areas (tech lead reviewing sample).

**[Step 8](step-8-share.md) — Learnings:** No issues encountered. Tests were of good quality and saved significant time. One instance where AI-generated test data was unrealistically similar to real case data — caught in review and replaced with clearly synthetic values. Usage log updated.

---

## Example 2: Team building an AI triage chatbot for a public-facing service

**[Step 1](step-1-define.md) — Define the use:** The team is building an AI-powered chatbot that will help members of the public find the right service for their enquiry. The chatbot will ask clarifying questions and direct users to the appropriate team or self-service option. It does not make decisions about eligibility or access — it is a triage tool.

**[Step 2](step-2-understand-data.md) — Understand the data:** At runtime, the chatbot will process user messages which may contain PII (names, case references, personal circumstances). The training/configuration data includes service descriptions and routing rules, which are OFFICIAL. User conversations will be logged for quality monitoring.

**[Step 3](step-3-assess-risks.md) — Assess the inherent risks (before mitigations):**

- **Data leakage: High inherent risk (Likely likelihood, High impact).** Users will inevitably share personal and sensitive information in their messages. This data will be processed by the AI service. Data handling must be robust.
- **Accuracy: High inherent risk (Likely likelihood, Medium impact).** If the chatbot directs someone to the wrong service, they may not get the help they need in time. Incorrect triage could have real consequences.
- **Accountability: Medium inherent risk (Possible likelihood, Medium impact).** There must be a clear accountability chain. If triage goes wrong, who is responsible? Users need to understand they are interacting with AI.
- **Bias: High inherent risk (Possible likelihood, High impact).** The chatbot may struggle with users who have limited English, use assistive technology, or describe their situation in non-standard ways. This could disproportionately affect already disadvantaged groups.
- **IP: Low inherent risk.** Not a significant factor for this use case.
- **Over-reliance: Low inherent risk.** The chatbot supplements, not replaces, existing service channels.
- **Supply chain: Medium inherent risk (Possible likelihood, Medium impact).** The AI service is a runtime dependency. If it goes down or changes behaviour, the public-facing service is directly affected.
- **Prompt injection: High inherent risk (Likely likelihood, Medium impact).** The chatbot is public-facing — anyone can interact with it. Users (malicious or otherwise) could attempt to extract system prompts, bypass triage logic, or cause the chatbot to produce inappropriate content. Indirect injection is also possible if the chatbot retrieves content from a knowledge base that could be compromised.

**Overall inherent risk level: High** (driven by data leakage, accuracy, bias, and prompt injection).

**[Step 4](step-4-check-tool.md) — Check the tool:** This is a new tool not previously on the approved list. The team gathered evidence using the [tool evaluation template](templates/tool-evaluation.md): UK data residency, GDPR-compliant DPA, no training on inputs, ISO 27001, SOC 2, 99.9% SLA, API access with audit logging. Meets all criteria. Submitted to SRO for approval — SRO approved the tool for use on this project.

**[Step 5](step-5-mitigate.md) — Mitigations and residual risk:** High inherent risk requires formal documentation and SRO approval.

Mitigations applied:

- DPIA completed for user data processing
- ATRS record drafted — the chatbot is an algorithmic tool used in public service delivery
- Model card documenting the system's capabilities, limitations, and intended use
- Human oversight: all triage decisions have a "speak to a person" option. Conversations flagged by sentiment analysis are reviewed by staff. Weekly accuracy audit of a sample of conversations
- Fallback: if the chatbot cannot triage with confidence, it routes to a human operator
- Equality Impact Assessment completed, identifying risks for users with limited English and users of assistive technology
- Prompt injection mitigations: adversarial testing (red teaming) conducted before launch. AI output sanitised before rendering to prevent XSS. System prompt does not contain secrets. Trust boundaries enforce that the chatbot cannot access data beyond public service information. Monitoring for anomalous outputs in place

Residual risk after mitigations:

- **Data leakage: Medium residual risk.** The AI provider has strong data handling guarantees (no training, UK residency, GDPR DPA). However, user PII will still be processed at runtime — the risk is reduced but not eliminated.
- **Accuracy: Medium residual risk.** The "speak to a person" option and fallback routing reduce impact. Weekly accuracy audits will catch systematic issues. But incorrect triage will still occasionally occur.
- **Accountability: Low residual risk.** ATRS record, model card, and clear human oversight model establish a transparent accountability chain.
- **Bias: Medium residual risk.** Equality Impact Assessment identified key risks and diverse testing was conducted. Ongoing monitoring is in place. But bias cannot be fully eliminated — it requires continuous attention.
- **Supply chain: Low residual risk.** 99.9% SLA and fallback to human operators reduce the impact of service disruption.
- **Prompt injection: Medium residual risk.** Red teaming, output sanitisation, and trust boundaries significantly reduce the attack surface. But prompt injection cannot be fully prevented in a public-facing system — it requires ongoing monitoring.

**Overall residual risk level: Medium.** The mitigations have reduced the overall risk from high to medium. The remaining risks are manageable with the ongoing monitoring and review processes in place. SRO approval obtained. Client approval obtained.

**[Step 6](step-6-record.md) — Record:** Logged in AI usage log with inherent risk (high), mitigations (DPIA, ATRS, model card, human oversight, EIA, prompt injection hardening), residual risk (medium), and SRO/client approval.

**[Step 7](step-7-checklists.md) — Checklist:** Follow checklist 7c (AI-Powered Product Features). All items addressed including DPIA, ATRS, monitoring metrics, human oversight model, diverse testing, accessibility testing, and adversarial testing.

**[Step 8](step-8-share.md) — Learnings:** Ongoing monitoring in place. First review date set for 4 weeks after launch. Incident response process documented and communicated to the team. Usage log updated.

---

## Example 3: Using AI to perform code analysis across a legacy codebase

**[Step 1](step-1-define.md) — Define the use:** The team is conducting a technical discovery of a legacy case management system. They want to use an AI tool to analyse the codebase (approximately 500,000 lines of Java) to map dependencies between modules, identify areas of high complexity and technical debt, and flag potential security vulnerabilities. The findings will inform a modernisation strategy.

**[Step 2](step-2-understand-data.md) — Understand the data:** The codebase is classified as OFFICIAL-SENSITIVE. It contains business logic for case management in the justice system, including rules about case handling, sentencing calculations, and data access controls. There are configuration files that may contain database connection strings and service endpoints. The codebase also contains comments that reference specific operational procedures.

**[Step 3](step-3-assess-risks.md) — Assess the inherent risks (before mitigations):**

- **Data leakage: High inherent risk (Likely likelihood, High impact).** The entire codebase — 500,000 lines — will be processed by the AI tool. This includes sensitive business logic, potential embedded credentials, and security-sensitive implementation details. The volume means manual review of every input is impractical.
- **Accuracy: Medium inherent risk (Possible likelihood, Medium impact).** Incorrect analysis could lead to wrong modernisation decisions (e.g. underestimating complexity, missing critical dependencies). However, the analysis will be validated by experienced engineers and is an input to decision-making, not a final decision itself.
- **Accountability: Low inherent risk.** The analysis is clearly an AI-assisted input. The team making modernisation decisions is accountable for validating the findings.
- **Bias: Low inherent risk.** Not significantly applicable to code analysis.
- **IP: Low inherent risk.** The codebase is owned by the client. Analysis outputs are advisory.
- **Over-reliance: Medium inherent risk (Possible likelihood, Medium impact).** The team might trust the AI's architectural assessment without sufficient manual verification, especially for parts of the codebase they are less familiar with.
- **Supply chain: Low inherent risk.** The AI tool is used for analysis only, not generating production code.
- **Prompt injection: Medium inherent risk (Possible likelihood, Medium impact).** The legacy codebase could contain comments or string literals that inadvertently or deliberately mislead the analysis tool. Given the size of the codebase (500,000 lines), it is impractical to review all comments for adversarial content.

**Overall inherent risk level: High** (driven by data leakage).

**[Step 4](step-4-check-tool.md) — Check the tool:** The cloud-hosted tool is not yet on the approved list. The team evaluates options using the [tool evaluation template](templates/tool-evaluation.md). A cloud-hosted AI tool with enterprise terms (no training on inputs, UK data residency, SOC 2) is available but requires sending the full codebase to an external service. An alternative is to use a locally-hosted open-source model, which keeps the code on-premises but may produce lower-quality analysis. The team decides to:

1. First run a secrets scanning tool across the codebase to identify and remove embedded credentials
2. Use the cloud-hosted tool with enterprise terms for the bulk analysis, having removed secrets
3. Submit the tool evaluation to the SRO for approval, and seek explicit client approval given the OFFICIAL-SENSITIVE classification

SRO approved the tool for this specific use case with the condition that secrets are removed first.

**[Step 5](step-5-mitigate.md) — Mitigations and residual risk:** High inherent risk requires formal documentation and SRO approval.

Mitigations applied:

- Secrets scan completed and all embedded credentials removed or redacted before analysis
- Client briefed on the approach and tool, including the data handling guarantees. Client approval obtained in writing
- Analysis findings to be validated by experienced engineers — minimum 20% sample manually verified
- Findings to be cross-referenced with traditional SAST tools for security-related analysis
- Limitations of the AI analysis to be clearly documented in the findings report
- SRO approval obtained

Residual risk after mitigations:

- **Data leakage: Medium residual risk.** Secrets removed from the codebase before sharing. Enterprise tool does not train on inputs and has UK data residency. However, the full codebase (sensitive business logic, architecture) is still shared with the provider — the risk is reduced but not eliminated.
- **Accuracy: Low residual risk.** 20% manual validation and SAST cross-referencing provide a strong check. Findings are treated as inputs to decision-making, not final decisions.
- **Over-reliance: Low residual risk.** Mandatory manual validation of a sample and domain expert review reduce the risk of uncritical acceptance.
- **Prompt injection: Low residual risk.** Cross-referencing with SAST tools provides an independent check on AI findings. Manual validation of a sample will catch systematic errors introduced by adversarial content.

**Overall residual risk level: Medium** (driven by data leakage). The mitigations have reduced the overall risk from high to medium.

**[Step 6](step-6-record.md) — Record:** Logged in AI usage log with inherent risk (high), mitigations (secrets scan, client approval, 20% manual validation, SAST cross-referencing, SRO approval), and residual risk (medium).

**[Step 7](step-7-checklists.md) — Checklist:** Follow checklist 7b (AI-Assisted Code Analysis).

- Secrets scan completed before sharing code (confirmed — 14 embedded credentials found and removed)
- Tool data handling confirmed appropriate for OFFICIAL-SENSITIVE with the mitigations applied
- Findings treated as hypotheses: the team manually verified a sample of dependency mappings and found the AI was approximately 85% accurate, with the main issues being outdated or incomplete dependency detection in older modules
- Limitations documented: the AI struggled with the system's custom build configuration and missed some transitive dependencies through proprietary frameworks
- Domain expert (original system architect, available part-time) reviewed the high-level architectural findings

**[Step 8](step-8-share.md) — Learnings:** Key learnings: the AI was most useful for identifying patterns of code duplication and mapping module boundaries, but less reliable for understanding the intent behind complex business rules. The secrets scan before analysis was essential — 14 credentials would have been exposed. The team recommends this approach for future legacy analysis with the same safeguards. Usage log updated.

---

## Example 4: Using AI to assist with service desk ticket triage and response

**[Step 1](step-1-define.md) — Define the use:** The team wants to use AI to help the service desk manage incoming support tickets for an internal case management system used by approximately 2,000 staff. The AI will auto-categorise tickets, suggest responses for agents to review and send, and surface relevant knowledge base articles. The AI will not send responses directly — all responses will be reviewed by a human agent before sending.

**[Step 2](step-2-understand-data.md) — Understand the data:** Support tickets are classified as OFFICIAL but frequently contain OFFICIAL-SENSITIVE material in practice — users paste error messages containing database details, attach screenshots showing case data, and include personal information about themselves and the people they work with. Tickets sometimes contain reports of security vulnerabilities or system misconfigurations. The ticketing system contains approximately 50,000 historical tickets that would be used to train/fine-tune the categorisation model.

**[Step 3](step-3-assess-risks.md) — Assess the inherent risks (before mitigations):**

- **Data leakage: High inherent risk (Likely likelihood, High impact).** Ticket content is inherently unpredictable. Users routinely paste credentials, share screenshots containing PII and system details, and describe security issues. The volume of historical tickets (50,000) makes manual review of training data impractical.
- **Accuracy: Medium inherent risk (Possible likelihood, Medium impact).** Incorrect categorisation could delay resolution of critical issues. Wrong troubleshooting suggestions could make problems worse. However, human agents review all responses before sending, which limits the impact.
- **Accountability: Medium inherent risk (Possible likelihood, Medium impact).** If AI miscategorises a critical security incident as routine, the delayed response has real consequences. The accountability chain between AI suggestion, agent acceptance, and management oversight needs to be clear.
- **Bias: Medium inherent risk (Possible likelihood, Medium impact).** The system is used by staff with varying levels of technical literacy and English language proficiency. AI categorisation and response quality may vary across these groups. Historical ticket data may embed existing prioritisation biases.
- **IP: Low inherent risk.** Not a significant concern for internal support operations.
- **Over-reliance: Medium inherent risk (Possible likelihood, Medium impact).** Support agents may stop developing deep system knowledge if they rely on AI-suggested resolutions. The team's ability to function during AI tool outages is a concern.
- **Supply chain: Medium inherent risk (Possible likelihood, Medium impact).** The AI tool will have access to the ticketing system, which contains sensitive operational data.
- **Prompt injection: Medium inherent risk (Possible likelihood, Medium impact).** The system processes tickets from 2,000 internal users. While the user base is known (not public-facing), a malicious insider or compromised account could craft tickets designed to manipulate AI categorisation, extract information from other tickets, or bypass exclusion rules. Exclusion rules are enforced in code rather than by the AI, which limits the blast radius.

**Overall inherent risk level: High** (driven by data leakage).

**[Step 4](step-4-check-tool.md) — Check the tool:** The team assessed the selected AI service using the [tool evaluation template](templates/tool-evaluation.md): UK data residency, no training on inputs (enterprise tier), SOC 2 and ISO 27001 certification, API access with audit logging, and a DPA that meets GDPR requirements. The tool integrates with the existing ticketing system via API. Meets all criteria. Tool evaluation submitted to SRO — approved for use on this project.

**[Step 5](step-5-mitigate.md) — Mitigations and residual risk:** High inherent risk requires formal documentation and SRO approval.

Mitigations applied:

- DPIA completed for AI processing of ticket data containing personal information.
- Automatic PII detection and credential scanning implemented on ticket content before it is sent to the AI service.
- Defined exclusion rules: tickets classified as security incidents, data breach reports, or safeguarding concerns are always routed directly to a human with no AI processing.
- Confidence thresholds set: categorisation at 70%+, response suggestions at 85%+. Below threshold, tickets are flagged for manual handling.
- All AI-suggested responses require human agent approval before sending.
- Fortnightly accuracy audit of a sample of AI categorisations and suggested responses.
- Fallback procedures documented for operating the service desk without AI tools.
- SRO approval obtained. IT security team reviewed the prompt injection risk and approved with the exclusion rules in place.

Residual risk after mitigations:

- **Data leakage: Medium residual risk.** PII detection and credential scanning significantly reduce exposure, but ticket content is inherently unpredictable — some sensitive data will inevitably reach the AI service before scanning catches it. Exclusion rules prevent the highest-risk tickets from being processed. The enterprise tier's no-training policy and UK data residency further limit the risk.
- **Accuracy: Low residual risk.** Confidence thresholds ensure low-confidence categorisations are flagged for manual handling. Human agents review all suggested responses before sending. Fortnightly audits catch systematic errors.
- **Accountability: Low residual risk.** Clear accountability chain documented: AI suggests, agent reviews, management oversees. Audit logging tracks all AI categorisations and response suggestions.
- **Bias: Low residual risk.** Bias testing completed during setup. Fortnightly audits include monitoring for disparities across user groups. Threshold adjustments made based on initial findings (terse writing style bias identified and corrected).
- **IP: Low residual risk.** Unchanged — not a significant concern.
- **Over-reliance: Low residual risk.** Fallback procedures documented and tested. Agents are required to review and edit all AI suggestions, maintaining their system knowledge. Regular training sessions scheduled.
- **Supply chain: Low residual risk.** Fallback procedures ensure the service desk can operate without the AI tool. API access with audit logging provides visibility into tool behaviour.
- **Prompt injection: Low residual risk.** Exclusion rules are enforced in code, not by the AI, limiting what a manipulated categorisation can achieve. Confidence thresholds cause unusual inputs to be flagged for manual handling. The internal-only user base (known, authenticated staff) significantly reduces the likelihood compared to a public-facing system.

**Overall residual risk level: Medium** (driven by data leakage). The mitigations have reduced the overall risk from high to medium.

**[Step 6](step-6-record.md) — Record:** Logged in AI usage log with inherent risk (high), mitigations (DPIA, PII scanning, exclusion rules, confidence thresholds, human review, fortnightly audits, fallback procedures, SRO and IT security approval), and residual risk (medium).

**[Step 7](step-7-checklists.md) — Checklist:** Follow checklist 7e (AI-Assisted Support). Key items: PII scanning in place (confirmed), exclusion rules for sensitive ticket types (confirmed), human review of all responses (confirmed), confidence thresholds defined (confirmed), bias testing across user groups (completed — identified that tickets written in terse style received lower confidence scores, threshold adjusted).

**[Step 8](step-8-share.md) — Learnings:** After the first month: categorisation accuracy was 82%, response suggestions were accepted (with minor edits) 68% of the time. Two issues identified: (1) the AI occasionally surfaced knowledge base articles for a deprecated version of the system — addressed by updating the knowledge base; (2) one ticket containing test credentials was sent to the AI before the PII scanner caught it — the scanner rules were updated. Monthly review cadence established. Usage log updated.
