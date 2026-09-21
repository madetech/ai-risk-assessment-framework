# Worked Examples

Six end-to-end assessments, covering different use types, risk levels, and autonomy levels. Each follows the four steps in order and records its risks in the shape the [risk assessment template](../templates/risk-assessment.md) sets out. They are illustrative. Your ratings should reflect your own situation, not be copied from here.

Risk levels are shown as 🟢 low, 🟠 medium, 🔴 high. Risks that came out low and needed nothing are recorded in a single line, as the template intends: a low risk needs a line, not a page.

| # | Use | Category | Autonomy | Inherent → residual |
| ---- | ---- | ---- | ---- | ---- |
| [1](#example-1-coding-assistant-on-an-official-sensitive-project) | Unit test generation | Software development | Drafts for review | 🟠 Medium → 🟢 Low |
| [2](#example-2-ai-triage-chatbot-for-a-public-facing-service) | Public triage chatbot | Product feature | Acts autonomously | 🔴 High → 🟠 Medium |
| [3](#example-3-code-analysis-across-a-legacy-codebase) | Legacy codebase analysis | Code analysis | Suggests | 🔴 High → 🟠 Medium |
| [4](#example-4-service-desk-ticket-triage-and-response) | Service desk triage | User-facing support | Acts autonomously | 🔴 High → 🟠 Medium |
| [5](#example-5-a-non-generative-model-prioritising-housing-inspections) | Inspection prioritisation model | Product feature (non-generative ML) | Drafts for review | 🔴 High → 🟠 Medium |
| [6](#example-6-an-agent-triaging-and-remediating-production-alerts) | Automated alert remediation | Live service operations | Acts autonomously | 🔴 High → 🟠 Medium |

---

## Example 1: Coding assistant on an OFFICIAL-SENSITIVE project

**Scope ([Step 1](../assess/1-scope.md)):** A developer wants to use a cloud-hosted AI coding assistant to help write unit tests for a case management service. The service handles OFFICIAL-SENSITIVE data including personal details of individuals in the justice system.

- **Category:** Software development
- **Autonomy:** Drafts for review. The assistant generates whole test files that the developer reviews and edits before committing. Agent mode, which can edit files across the repository unprompted, is disabled in the team's shared configuration.

*What is shared:* The code itself is classified as OFFICIAL-SENSITIVE because it contains business logic that reveals how sensitive cases are handled. The test code will reference data structures that mirror the real data model, including field names for personal information. No real PII will be in the code, but the data structures are revealing.

**Check the tool ([Step 2](../assess/2-check-tool.md)):** The coding assistant (enterprise plan) is on the register, not excluded, and cleared up to OFFICIAL-SENSITIVE, which covers this code. From its profile: **what it is**: cloud-hosted, so code leaves the estate to a third party; sees the open file and surrounding editor context; has an agent mode capable of editing files across the repository, though the team's shared configuration disables it. **What the supplier promises**: no training on inputs, EU processing, SOC 2, audit logging, IP indemnification.

**Assess the risks ([Step 3](../assess/3-assess-risks.md)):**

| | |
| ---- | ---- |
| **Overall inherent risk** | 🟠 Medium |
| **Driven by** | Data leakage |
| **Overall residual risk** | 🟢 Low |
| **Approval required** | SRO |

| Risk | Inherent | Residual |
| ---- | ---- | ---- |
| Data leakage | 🟠 Medium | 🟢 Low |
| Accuracy and hallucination | 🟢 Low | 🟢 Low |
| Accountability gaps | 🟢 Low | 🟢 Low |
| Bias and fairness | 🟢 Low | 🟢 Low |
| IP and licensing | 🟢 Low | 🟢 Low |
| Over-reliance and skill erosion | 🟢 Low | 🟢 Low |
| Supply chain and security | 🟢 Low | 🟢 Low |
| Prompt injection | 🟢 Low | 🟢 Low |

*Autonomy adjustment:* none. At *drafts for review*, with test files small enough to review properly, the heatmap's assumptions hold.

### Data leakage

The assistant is cloud-hosted, so code leaves our estate to a third party. The test code references data structures that mirror the real case data model, including field names for personal information. No real records are sent, but the structures reveal how sensitive cases are handled.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Enterprise terms: no training on inputs, EU processing *(likelihood)*
- Review all generated tests for sensitive business logic in test names and assertions. This goes beyond the ordinary review our *drafts for review* level already assumes *(likelihood)*
- A second developer reviews a sample of AI-assisted test code *(likelihood)*
- No real data values in test fixtures *(impact)*

What these cut is how likely exposure is, not how bad it would be. The data model structures still reach the provider; what changes is that they are not retained or trained on, and the extra review keeps identifiable patterns out of what is sent. If they were exposed the consequence would be the same, so the impact rating does not move.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Accuracy and hallucination

Incorrect unit tests are caught by code review and test execution, and the consequence of a wrong test is limited. The team is alert to the specific failure mode of tests that pass without asserting anything meaningful.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Low | 🟢 **Low** |

*Mitigations*: generated tests are checked to confirm they assert meaningful behaviour rather than merely passing. This guards a known failure mode rather than reducing a rating that was already low.

**Residual: 🟢 Low**, unchanged

### Risks assessed as low

- **Accountability gaps**: 🟢 Low (unlikely × low). The developer is clearly accountable for the tests they commit, and standard code review applies. Residual unchanged.
- **Bias and fairness**: 🟢 Low (unlikely × low). Not materially applicable to unit test generation. Residual unchanged.
- **IP and licensing**: 🟢 Low (unlikely × low). Test code carries no unusual licensing requirements, and the provider indemnifies outputs. Residual unchanged.
- **Over-reliance and skill erosion**: 🟢 Low (unlikely × low). The developer is experienced and using AI to accelerate test writing, not to learn testing fundamentals. Residual unchanged.
- **Supply chain and security**: 🟢 Low (unlikely × low). Unit tests do not typically introduce new dependencies. Residual unchanged.
- **Prompt injection**: 🟢 Low (unlikely × low). The codebase is internal and trusted; the developer is working on their own code, not processing untrusted external content. AI rule files in the repository were audited. Residual unchanged.

**Approve, record, do the work, and share ([Step 4](../assess/4-record-and-work.md)):**

*Record:* The completed assessment is saved in the project's documentation space. It is the record; there is no separate usage log. It captures the inherent risk (🟠 medium), the mitigations, the residual risk (🟢 low), and SRO approval.

*Checklist:* Followed the [Software development checklist](checklists.md#checklist-software-development). Key items: no secrets in context (confirmed), agent mode disabled so the recorded autonomy level is accurate (confirmed), review all generated code (standard practice), a second review for sensitive areas (a second developer reviewing a sample).

*Learnings:* No significant issues. Tests were of good quality and saved substantial time. One instance where AI-generated test data was unrealistically similar to real case data, caught in review and replaced with clearly synthetic values. Two generated tests asserted only that a method returned without throwing; both were rewritten. Both were shared at the team retrospective.

---

## Example 2: AI triage chatbot for a public-facing service

**Scope ([Step 1](../assess/1-scope.md)):** The team is building an AI-powered chatbot that will help members of the public find the right service for their enquiry. The chatbot asks clarifying questions and directs users to the appropriate team or self-service option. It does not make decisions about eligibility or access. It is a triage tool.

- **Category:** Product feature
- **Autonomy:** Acts autonomously. The chatbot's replies reach a member of the public with no human reviewing each message. Its scope is narrow: it can reply and route, and cannot change records or make eligibility decisions, but nobody approves what it says before it is said, so it is assessed at the highest level. This triggers SRO approval regardless of the risk rating.

*What is shared:* At runtime, the chatbot processes user messages which may contain PII (names, case references, personal circumstances). The configuration data includes service descriptions and routing rules, which are OFFICIAL. User conversations are logged for quality monitoring.

**Check the tool ([Step 2](../assess/2-check-tool.md)):** This is a new tool, so it needs a profile before use. The team completes one with the [tool profile template](../templates/tool-evaluation.md). Not excluded. **What it is**: a hosted API; user messages leave the estate at runtime, continuously; it produces text that reaches the public directly and holds no access to case records. **What the supplier promises**: UK data residency, GDPR-compliant DPA, no training on inputs, ISO 27001, SOC 2, 99.9% SLA, audit logging via the API. The SRO clears it up to OFFICIAL, which covers the data involved.

**Assess the risks ([Step 3](../assess/3-assess-risks.md)):**

| | |
| ---- | ---- |
| **Overall inherent risk** | 🔴 High |
| **Driven by** | Data leakage, accuracy, accountability, bias, supply chain, prompt injection |
| **Overall residual risk** | 🟠 Medium |
| **Driven by** | Data leakage, accuracy, bias, prompt injection |
| **Approval required** | SRO, and required regardless by the autonomy level |

| Risk | Inherent | Residual |
| ---- | ---- | ---- |
| Data leakage | 🔴 High | 🟠 Medium |
| Accuracy and hallucination | 🔴 High | 🟠 Medium |
| Accountability gaps | 🔴 High | 🟢 Low |
| Bias and fairness | 🔴 High | 🟠 Medium |
| IP and licensing | 🟢 Low | 🟢 Low |
| Over-reliance and skill erosion | 🟢 Low | 🟢 Low |
| Supply chain and security | 🔴 High | 🟢 Low |
| Prompt injection | 🔴 High | 🟠 Medium |

*Autonomy adjustment:* at *acts autonomously*, accuracy, accountability, supply chain and prompt injection are rated at least high impact, and bias is raised by one impact step.

### Data leakage

Members of the public will share personal and sensitive information in their messages (names, case references, circumstances), and there is no gate in front of it. Everything they type is processed by a third-party API at runtime, continuously.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- DPIA completed for user data processing *(likelihood)*
- Supplier terms: UK data residency, GDPR-compliant DPA, no training on inputs *(likelihood)*
- Trust boundaries enforce that the chatbot cannot reach data beyond public service information, so a leak cannot extend to case records *(impact)*

User PII will still be processed at runtime by a third party. That cannot be designed away while the service exists, so the exposure is reduced rather than removed.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | High | 🟠 **Medium** |

### Accuracy and hallucination

If the chatbot directs someone to the wrong service, they may not get help in time. Nobody checks a reply before it is sent, so a wrong answer reaches the public directly.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Likely | Medium | 🔴 **High** |

**Mitigations:**

- Every triage path offers a "speak to a person" option *(impact)*
- If the chatbot cannot triage with confidence, it routes to a human operator *(impact)*
- Weekly accuracy audit of a sample of conversations *(likelihood)*
- Model card documenting capabilities, limitations, and intended use *(likelihood)*

Fallback routing and the route to a person limit what a wrong answer costs, and the weekly audit catches systematic drift. Incorrect triage will still occur.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Accountability gaps

Raised to high impact by the autonomy adjustment: no person approves each reply, so accountability rests entirely on the design and on whoever configured it. Users need to know they are dealing with AI and have a route to a person.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- ATRS record drafted: the chatbot is an algorithmic tool used in public service delivery *(impact)*
- A named product owner accountable for its behaviour *(impact)*
- Every conversation logged *(impact)*
- A visible route to a human on every path *(impact)*

The record, the named owner, the logs and the human route together establish who is answerable and how a user challenges an outcome.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Bias and fairness

The chatbot may struggle with users who have limited English, use assistive technology, or describe their situation in non-standard ways, disproportionately affecting people already least well served. Raised by one impact step by the autonomy adjustment, because at scale the same skew reaches every case.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- Equality Impact Assessment completed, identifying risks for users with limited English and users of assistive technology *(likelihood)*
- Testing with users from diverse backgrounds, including assistive technology users *(likelihood)*
- Ongoing monitoring for disparities across user groups *(likelihood)*
- The "speak to a person" route means a user the chatbot handles badly is not stuck *(impact)*

Bias cannot be tested away, so what the EIA and monitoring buy is detection rather than prevention. The residual rating reflects a risk being managed, not solved.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Supply chain and security

Raised to high impact by the autonomy adjustment. The AI service is a runtime dependency that speaks to the public unsupervised. A provider-side model change alters what the public is told, with no code change on the team's part.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- 99.9% SLA, with fallback to human operators when the service is unavailable *(impact)*
- A kill switch that reverts the entry point to the existing contact page without a deployment *(impact)*
- Monitoring for anomalous outputs, so a behaviour change is noticed rather than discovered by users *(likelihood)*

Because the chatbot can be switched off in favour of an existing channel within minutes, a disruption or behaviour change is an inconvenience rather than a service failure.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Prompt injection

The chatbot is public-facing, so anyone can craft input for it. Users may attempt to extract the system prompt, bypass triage logic, or make it produce inappropriate content. Indirect injection is possible too, if it retrieves from a knowledge base that could be compromised.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- Adversarial testing (red teaming) before launch *(likelihood)*
- AI output sanitised before rendering, to prevent XSS *(impact)*
- No secrets in the system prompt *(impact)*
- Trust boundaries enforce that the chatbot cannot access data beyond public service information, and it has no actions available beyond replying and routing *(impact)*
- Monitoring for anomalous outputs *(likelihood)*

Injection cannot be prevented in a public-facing system, so the work here is on consequences: the worst a successful injection achieves is an inappropriate reply from a system that cannot reach any record or take any action.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Risks assessed as low

- **IP and licensing**: 🟢 Low (unlikely × low). Triage replies are short, factual routing statements; provenance is not a live concern. Residual unchanged.
- **Over-reliance and skill erosion**: 🟢 Low (unlikely × low). The chatbot supplements rather than replaces existing service channels, which remain staffed. Residual unchanged.

**Approve, record, do the work, and share ([Step 4](../assess/4-record-and-work.md)):**

*Record:* The assessment is saved as the project's record for this use, capturing inherent risk (🔴 high), the mitigations, residual risk (🟠 medium), and SRO and client approval. The autonomy mitigations are recorded alongside: least privilege (read-only access to public service information, no access to case records); no irreversible actions available to it; every conversation logged; a named product owner; a kill switch operable without a deployment.

*Checklist:* Followed the [Product feature checklist](checklists.md#checklist-product-feature). All items addressed including DPIA, ATRS, monitoring metrics, human oversight model, diverse testing, accessibility testing, and adversarial testing.

*Learnings:* Ongoing monitoring in place, with monitoring data reviewed and shared monthly. First review date set for four weeks after launch. Incident response process documented and communicated to the team.

---

## Example 3: Code analysis across a legacy codebase

**Scope ([Step 1](../assess/1-scope.md)):** The team is conducting a technical discovery of a legacy case management system. They want to use an AI tool to analyse the codebase (approximately 500,000 lines of Java) to map dependencies between modules, identify areas of high complexity and technical debt, and flag potential security vulnerabilities. The findings will inform a modernisation strategy.

- **Category:** Code analysis
- **Autonomy:** Suggests. The tool produces findings; engineers decide what to do with them. It has no write access to the repository.

*What is shared:* The codebase is classified as OFFICIAL-SENSITIVE. It contains business logic for case management in the justice system, including rules about case handling, sentencing calculations, and data access controls. There are configuration files that may contain database connection strings and service endpoints. The codebase also contains comments that reference specific operational procedures.

**Check the tool ([Step 2](../assess/2-check-tool.md)):** The cloud-hosted tool is not yet on the register. The team's existing coding assistant is on it, but cleared only up to OFFICIAL (below this codebase), so it is out on classification alone. The team profiles the options using the [tool profile template](../templates/tool-evaluation.md). A cloud-hosted AI tool with enterprise terms (no training on inputs, UK data residency, SOC 2) is available but requires sending the full codebase to an external service. An alternative is to use a locally-hosted open-source model, which keeps the code on-premises but may produce lower-quality analysis. The team decides to:

1. First run a secrets scanning tool across the codebase to identify and remove embedded credentials
2. Use the cloud-hosted tool with enterprise terms for the bulk analysis, having removed secrets
3. Submit the profile to the SRO for a classification decision, and seek explicit client approval given the OFFICIAL-SENSITIVE data

The SRO clears the tool up to OFFICIAL-SENSITIVE. The profile records what matters for the risk work that follows: **what it is**: the whole codebase leaves the estate to a third party in bulk, and the tool has no write access to the repository. **What the supplier promises**: enterprise terms with no training on inputs, UK residency, SOC 2. The secrets scan is not part of the profile: it is a mitigation this team is choosing to apply, and belongs in their mitigations.

**Assess the risks ([Step 3](../assess/3-assess-risks.md)):**

| | |
| ---- | ---- |
| **Overall inherent risk** | 🔴 High |
| **Driven by** | Data leakage |
| **Overall residual risk** | 🟠 Medium |
| **Driven by** | Data leakage |
| **Approval required** | SRO |

| Risk | Inherent | Residual |
| ---- | ---- | ---- |
| Data leakage | 🔴 High | 🟠 Medium |
| Accuracy and hallucination | 🟠 Medium | 🟢 Low |
| Accountability gaps | 🟢 Low | 🟢 Low |
| Bias and fairness | 🟢 Low | 🟢 Low |
| IP and licensing | 🟢 Low | 🟢 Low |
| Over-reliance and skill erosion | 🟠 Medium | 🟢 Low |
| Supply chain and security | 🟢 Low | 🟢 Low |
| Prompt injection | 🟠 Medium | 🟢 Low |

*Autonomy adjustment:* none. At *suggests*, with no write access, the heatmap's assumptions hold.

### Data leakage

The entire codebase (500,000 lines) is sent to a third-party service in bulk. It contains sensitive business logic, security-sensitive implementation details, and probably embedded credentials nobody has catalogued. The volume means reviewing every input by hand is impractical.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- Secrets scan completed and all embedded credentials removed or redacted before analysis *(impact)*
- Enterprise terms: no training on inputs, UK residency *(likelihood)*
- The tool's outbound network access restricted *(likelihood)*
- Client briefed on the approach and the data handling guarantees, with approval obtained in writing *(likelihood)*

Removing the credentials takes the worst outcome off the table: 14 were found. But the codebase itself, with its business logic and architecture, still goes to the provider in full. That is inherent to the task, so the impact of exposure has not changed.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | High | 🟠 **Medium** |

### Accuracy and hallucination

Incorrect analysis could lead to wrong modernisation decisions: underestimating complexity, missing critical dependencies. AI is weakest precisely where legacy systems are hardest: undocumented business rules that only make sense in historical policy context.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Minimum 20% sample of findings manually verified by experienced engineers *(likelihood)*
- Findings cross-referenced with traditional SAST tools for anything security-related *(likelihood)*
- AI-derived descriptions of business logic treated as hypotheses to verify against the running system, never as specification *(impact)*
- Limitations of the analysis documented in the findings report *(impact)*

Sampling and SAST cross-referencing give an independent check, and treating descriptions as hypotheses means a wrong one is caught before it reaches a decision rather than after.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Over-reliance and skill erosion

The team might accept the AI's architectural assessment without verifying it, particularly for the parts of the codebase they know least well, which are exactly the parts where they can least judge whether it is right.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Manual validation of a sample is mandatory, not optional *(likelihood)*
- A domain expert (the original system architect, available part-time) reviews the high-level architectural findings *(likelihood)*

Requiring engineers to verify a fixed proportion themselves keeps them engaged with the codebase rather than with the report about it.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Prompt injection

The legacy codebase could contain comments or string literals that inadvertently or deliberately mislead the analysis tool, for instance by causing it to downgrade a security finding. Given the size of the codebase, reviewing all comments for adversarial content is impractical.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Cross-referencing with SAST tools provides an independent check that does not read comments *(likelihood)*
- Manual validation of a sample will catch systematic distortion *(likelihood)*
- Restricted outbound network access limits what a successful injection could achieve *(impact)*

An independent, non-AI check on the security findings is what makes this manageable: a manipulated AI finding does not survive comparison with a static analyser.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Risks assessed as low

- **Accountability gaps**: 🟢 Low (unlikely × low). The analysis is clearly labelled as an AI-assisted input, and the team making modernisation decisions is accountable for validating the findings. Residual unchanged.
- **Bias and fairness**: 🟢 Low (unlikely × low). Not materially applicable to dependency and complexity analysis. Residual unchanged.
- **IP and licensing**: 🟢 Low (unlikely × low). The codebase is owned by the client and the analysis outputs are advisory. Residual unchanged.
- **Supply chain and security**: 🟢 Low (unlikely × low). The tool is used for analysis only, generates no production code, and has no write access to the repository. Residual unchanged.

**Approve, record, do the work, and share ([Step 4](../assess/4-record-and-work.md)):**

*Record:* The assessment is saved as the record for this use, capturing inherent risk (🔴 high), the mitigations, residual risk (🟠 medium), and SRO and client approval.

*Checklist:* Followed the [Code analysis checklist](checklists.md#checklist-code-analysis).

- Secrets scan completed before sharing code (confirmed: 14 embedded credentials found and removed)
- Tool data handling confirmed appropriate for OFFICIAL-SENSITIVE with the mitigations applied
- Findings treated as hypotheses: the team manually verified a sample of dependency mappings and found the AI was approximately 85% accurate, with the main issues being outdated or incomplete dependency detection in older modules
- Limitations documented: the AI struggled with the system's custom build configuration and missed some transitive dependencies through proprietary frameworks
- Domain expert (the original system architect, available part-time) reviewed the high-level architectural findings

*Learnings:* The AI was most useful for identifying patterns of code duplication and mapping module boundaries, but less reliable for understanding the intent behind complex business rules. It confidently described a sentencing calculation in terms that turned out to describe a superseded policy. The secrets scan before analysis was essential: 14 credentials would have been exposed. The team recommends this approach for future legacy analysis with the same mitigations.

---

## Example 4: Service desk ticket triage and response

**Scope ([Step 1](../assess/1-scope.md)):** The team wants to use AI to help the service desk manage incoming support tickets for an internal case management system used by approximately 2,000 staff. The AI will auto-categorise and route tickets, suggest responses for agents to review and send, and surface relevant knowledge base articles.

- **Category:** User-facing support
- **Autonomy:** Mixed, so assessed at the higher level: **acts autonomously**. The response path only drafts for review: no reply is sent without an agent approving it. But categorisation and routing happen with no human approving each decision, and a miscategorised ticket changes how urgently a real problem is handled. This triggers SRO approval regardless of the risk rating.

*What is shared:* Support tickets are classified as OFFICIAL but frequently contain OFFICIAL-SENSITIVE material in practice: users paste error messages containing database details, attach screenshots showing case data, and include personal information about themselves and the people they work with. Tickets sometimes contain reports of security vulnerabilities or system misconfigurations. The ticketing system contains approximately 50,000 historical tickets that would be used to fine-tune the categorisation model.

**Check the tool ([Step 2](../assess/2-check-tool.md)):** The team profiles the selected AI service with the [tool profile template](../templates/tool-evaluation.md). Not excluded, and cleared up to OFFICIAL. **What it is**: integrates with the ticketing system via API and holds standing read access to it; ticket content leaves the estate; it can write back to a ticket, so it is capable of acting, not only suggesting. **What the supplier promises**: enterprise tier with no training on inputs, UK residency, SOC 2 and ISO 27001, audit logging, GDPR-compliant DPA.

**Assess the risks ([Step 3](../assess/3-assess-risks.md)):**

| | |
| ---- | ---- |
| **Overall inherent risk** | 🔴 High |
| **Driven by** | Data leakage, accountability, supply chain, prompt injection |
| **Overall residual risk** | 🟠 Medium |
| **Driven by** | Data leakage, supply chain |
| **Approval required** | SRO, and required regardless by the autonomy level |

| Risk | Inherent | Residual |
| ---- | ---- | ---- |
| Data leakage | 🔴 High | 🟠 Medium |
| Accuracy and hallucination | 🟠 Medium | 🟢 Low |
| Accountability gaps | 🔴 High | 🟢 Low |
| Bias and fairness | 🟠 Medium | 🟢 Low |
| IP and licensing | 🟢 Low | 🟢 Low |
| Over-reliance and skill erosion | 🟠 Medium | 🟢 Low |
| Supply chain and security | 🔴 High | 🟠 Medium |
| Prompt injection | 🔴 High | 🟢 Low |

*Autonomy adjustment:* at *acts autonomously*, accuracy, accountability, supply chain and prompt injection are rated at least high impact.

### Data leakage

Ticket content is inherently unpredictable. Users routinely paste credentials, attach screenshots containing PII and system details, and describe security issues in plain text. On top of that, 50,000 historical tickets would be used for fine-tuning, and reviewing them by hand is impractical.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- Automatic PII detection and credential scanning on ticket content before it is sent *(likelihood)*
- Exclusion rules enforced in code: security incidents, data breach reports and safeguarding concerns are routed straight to a human with no AI processing *(likelihood)*
- Enterprise tier: no training on inputs, UK residency *(likelihood)*

Scanning and exclusions keep the highest-risk material away from the service, but ticket content is unpredictable and some sensitive data will reach the AI before a scanner catches it. What is exposed when that happens is unchanged.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | High | 🟠 **Medium** |

### Accountability gaps

Raised to high impact by the autonomy adjustment. Nobody approves each categorisation, so if the AI routes a critical security incident as routine, there is no person in the chain who made that call, only the configuration.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- A named service desk manager accountable for the categorisation path *(impact)*
- Every categorisation written to the ticket's audit trail *(impact)*
- A documented chain: the AI categorises within bounds, an agent reviews responses, management audits fortnightly *(impact)*

Each categorisation is now attributable and reconstructable after the fact, and there is a named person answerable for the behaviour of the path as a whole.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Supply chain and security

Raised to high impact by the autonomy adjustment. The AI holds standing access to the ticketing system and acts on it unsupervised; a provider-side change to categorisation behaviour would alter how the service desk operates with no change on the team's part.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- Bounded permissions: the AI can set a category and a queue and nothing else: it cannot close, merge, or delete a ticket, or drop priority below the floor set by the exclusion rules *(impact)*
- Categorisation can be switched off from the admin console without a deployment *(impact)*
- Fallback procedures documented for operating the service desk without AI tools *(impact)*

A behaviour change at the provider cannot exceed setting a category and a queue, and the team can turn it off in minutes. The dependency itself remains, and that is what keeps this at medium.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Prompt injection

Raised to high impact by the autonomy adjustment. The user base is known and authenticated rather than public, which keeps the likelihood down, but a crafted ticket that manipulates categorisation now changes routing directly rather than proposing it to someone.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- Exclusion rules enforced in code, not by the AI, so a manipulated categorisation cannot reach the ticket types that matter most *(impact)*
- Confidence thresholds: categorisation at 70%+, responses at 85%+; below threshold a ticket is flagged for manual handling, and crafted input tends to score oddly *(likelihood)*
- IT security reviewed the injection risk and approved with the exclusion rules in place *(likelihood)*

The deterministic exclusion rules are what make this work: they are enforced outside the AI, so no amount of manipulation reaches a security incident or a safeguarding report.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Accuracy and hallucination

Incorrect categorisation delays resolution of critical issues, and wrong troubleshooting advice makes problems worse. Human agents review all responses before sending, which limits the impact on that path but not on categorisation.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Confidence thresholds send low-confidence categorisations to manual handling *(likelihood)*
- All AI-suggested responses require agent approval before sending: this is the *drafts for review* path, and the approval is genuine rather than nominal *(impact)*
- Fortnightly accuracy audit of a sample of categorisations and suggested responses *(likelihood)*

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Bias and fairness

The system serves staff with varying technical literacy and English proficiency, and categorisation quality may vary across them. Historical ticket data may also embed existing prioritisation biases that fine-tuning would reproduce.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Bias testing completed during setup, across user groups *(likelihood)*
- Fortnightly audits include monitoring for disparities between groups *(likelihood)*
- Thresholds adjusted following initial findings *(likelihood)*

Testing found that tersely written tickets received lower confidence scores, which correlated with staff who write in a second language. The threshold was adjusted; the monitoring continues because this is the kind of skew that returns.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Over-reliance and skill erosion

Support agents may stop building deep system knowledge if they lean on AI-suggested resolutions, and the desk's ability to function during an outage of the tool becomes a real question.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Fallback procedures documented and tested *(impact)*
- Agents required to review and edit AI suggestions rather than accept them *(likelihood)*
- Regular training sessions scheduled *(likelihood)*

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Risks assessed as low

- **IP and licensing**: 🟢 Low (unlikely × low). Internal support operations; no published or externally licensed material is produced. Residual unchanged.

**Approve, record, do the work, and share ([Step 4](../assess/4-record-and-work.md)):**

*Record:* The assessment is saved as the record for this use, capturing inherent risk (🔴 high), the mitigations, residual risk (🟠 medium), and SRO and IT security approval. The autonomy mitigations on the categorisation path are recorded alongside: bounded permissions, every categorisation in the audit trail, a named accountable manager, and an off switch that needs no deployment.

*Checklist:* Followed the [User-facing support checklist](checklists.md#checklist-user-facing-support). Key items: PII scanning in place (confirmed), exclusion rules for sensitive ticket types (confirmed), human review of all responses (confirmed), confidence thresholds defined (confirmed), bias testing across user groups (completed: identified that tickets written in terse style received lower confidence scores, threshold adjusted).

*Learnings:* After the first month, categorisation accuracy was 82% and response suggestions were accepted (with minor edits) 68% of the time. Three issues identified: (1) the AI occasionally surfaced knowledge base articles for a deprecated version of the system, addressed by updating the knowledge base; (2) one ticket containing test credentials reached the AI before the PII scanner caught it, so the scanner rules were updated; (3) the fortnightly audit found agents were approving suggested responses in a median of four seconds, which is not review, so the team added a minimum-display-time and a spot-check on approved responses, and noted this as autonomy creep on the response path. Monthly review cadence established, with monitoring data shared at the team's service review.

---

## Example 5: A non-generative model prioritising housing inspections

*This example covers a use type that is easy to overlook: a conventional machine learning model, not a large language model. Prompt injection barely applies; bias dominates; and the statutory obligations are different.*

**Scope ([Step 1](../assess/1-scope.md)):** A local authority housing service is adding a prioritisation model to its disrepair reporting system. The model scores incoming reports for likely severity (damp and mould, structural defects, hazards to health), and orders the inspection queue. A scheduling officer reviews the ranked queue each morning and books visits.

- **Category:** Product feature. It is not generative: it is a gradient-boosted classifier trained on historical inspection outcomes.
- **Autonomy:** Drafts for review. The model produces a ranked queue; a scheduling officer reviews it and can reorder before visits are booked.

*What is shared:* The model is trained on six years of historical inspection records: address, property type, tenure, the text of the original report, repair history, and the inspector's recorded outcome. This is personal data: addresses identify households even with names removed. Both training and inference run inside the authority's own cloud tenancy. **No third-party AI service receives any data at any point.**

**Check the tool ([Step 2](../assess/2-check-tool.md)):** There is no third-party service here, so most of the facts a [profile](../assess/2-check-tool.md) records (residency, retention, training on inputs, provider certifications) simply have no supplier to be true of. The team still writes a profile, because the facts that *do* apply are the ones the risk work needs. **What it is**: trained and hosted entirely inside the authority's own tenancy; no data leaves; it scores and ranks but cannot act on the queue. **In place of supplier promises**: a model card covering intended use, training data, performance by subgroup and known limitations; the hosting platform assured under existing arrangements; ML libraries under the standard dependency policy. Cleared up to OFFICIAL by the SRO.

**Assess the risks ([Step 3](../assess/3-assess-risks.md)):**

| | |
| ---- | ---- |
| **Overall inherent risk** | 🔴 High |
| **Driven by** | Bias, accuracy, accountability |
| **Overall residual risk** | 🟠 Medium |
| **Driven by** | Bias, accuracy |
| **Approval required** | SRO |

| Risk | Inherent | Residual |
| ---- | ---- | ---- |
| Data leakage | 🟢 Low | 🟢 Low |
| Accuracy and hallucination | 🔴 High | 🟠 Medium |
| Accountability gaps | 🔴 High | 🟢 Low |
| Bias and fairness | 🔴 High | 🟠 Medium |
| IP and licensing | 🟢 Low | 🟢 Low |
| Over-reliance and skill erosion | 🟠 Medium | 🟢 Low |
| Supply chain and security | 🟢 Low | 🟢 Low |
| Prompt injection | N/A | N/A |

*Autonomy adjustment:* none. At *drafts for review*, the scheduling officer genuinely reviews and reorders the queue.

### Bias and fairness

The defining risk of this use. Six years of inspection records reflect who historically reported problems and who historically got a visit. Areas and groups that were under-served in the past generated fewer records, so the model learns to keep deprioritising them, a feedback loop that tightens with every retraining cycle. Tenure and property type correlate with ethnicity and disability across the borough, so the model can produce indirectly discriminatory outcomes without ever seeing a protected characteristic as a feature.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- Equality Impact Assessment completed; performance tested across tenure, property type, ward, and the protected characteristics the authority holds *(likelihood)*
- **A random sample to break the feedback loop:** 10% of weekly inspections are drawn at random regardless of score, and their outcomes feed into evaluation. This is the only way to learn about the cases the model would have kept deprioritising *(likelihood)*
- **A floor rule enforced in code, not by the model:** any report mentioning damp, mould, or a child under two is inspected within the statutory timeframe regardless of score *(impact)*
- Drift monitoring, six-monthly revalidation, and a fixed review date *(likelihood)*

Bias embedded in six years of historical data cannot be removed by testing alone. The random sample is what makes it *detectable*, and the floor rule caps what an undetected skew can cost a household. The residual rating reflects a risk being managed, not solved.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Accuracy and hallucination

A wrongly deprioritised damp and mould report can leave a household in a hazardous home for weeks. The consequences fall on residents rather than on the service, and the people most affected are least able to escalate.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- The floor rule removes the worst outcome: a hazardous report cannot sit unvisited whatever the model scores it *(impact)*
- Random sampling detects systematic under-scoring *(likelihood)*
- Scheduling officers are trained to override and required to record a reason *(likelihood)*

The floor rule takes the catastrophic case off the table. Ranking errors within the safe band will still happen, and they still delay people.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Accountability gaps

Residents whose reports are deprioritised need to know a model was involved and have a route to challenge it. This is an algorithmic tool affecting public service delivery, so an ATRS record is required. The scheduling officer has to be a genuine decision-maker rather than a rubber stamp, or the accountability is nominal.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- ATRS record completed and published *(impact)*
- A named accountable officer for the model's use *(impact)*
- Override reasons recorded, which also produces the data for detecting rubber-stamping *(likelihood)*
- An explanation of the ranking available to residents on request, with a documented complaints route *(impact)*

A resident can now find out that a model was involved, get an explanation, and challenge the outcome, and the authority can show who is answerable.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Over-reliance and skill erosion

Scheduling officers under time pressure will accept the ranking. Their own judgement about which reports sound urgent will decay, and with it the ability to notice when the model is wrong.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Officers trained to override, and required to record a reason when they do *(likelihood)*
- Override rates reviewed: a rate near zero is itself the warning sign *(likelihood)*

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Risks assessed as low, or not applicable

- **Data leakage**: 🟢 Low (unlikely × medium). No external AI service is involved, so the framework's most common leakage route does not exist here. Training data is personal data but stays inside the existing system boundary under existing access controls. The residual concern is that models can memorise training records and leak them through outputs. A ranked score reveals very little. Residual unchanged.
- **IP and licensing**: 🟢 Low (unlikely × low). Model, training data, and outputs are all owned by the authority. Residual unchanged.
- **Supply chain and security**: 🟢 Low (unlikely × medium). No runtime dependency on an external AI service; the ML libraries are ordinary software dependencies under existing patching and vulnerability controls. Residual unchanged.
- **Prompt injection**: **N/A.** The model does not follow instructions and there is no prompt to inject. The analogous risk is **data poisoning**: someone able to influence recorded inspection outcomes over time could shift the model's behaviour. Assessed as 🟢 low: outcome records are written only by inspectors, under individual accounts, with an audit trail.

**Approve, record, do the work, and share ([Step 4](../assess/4-record-and-work.md)):**

*Record:* The assessment is saved as the record for this use, alongside the DPIA, EIA, model card, and ATRS record.

*Checklist:* Followed the [Product feature checklist](checklists.md#checklist-product-feature), noting which items did not apply and what replaced them. Adversarial and prompt injection testing were recorded as not applicable, substituted by a data poisoning review of who can write inspection outcomes. Bias testing, accessibility of the explanation route, monitoring metrics, human oversight model, and the ATRS record were all completed.

*Learnings:* After three months, the random-sample inspections found the model was systematically under-scoring reports from one ward with a high proportion of tenants who do not speak English as a first language. Their reports were shorter and used less of the vocabulary the model had learned to associate with severity, so the model read brevity as low urgency. The model was retrained with report length removed as a feature and the text handling revised. **This would not have been detected without the random sample**. Every other monitoring measure looked healthy, because the model was accurate on the cases it chose to send inspectors to. The team has recommended the random-sample mitigation to other services in the authority using scoring models.

---

## Example 6: An agent triaging and remediating production alerts

*This example covers the autonomy dimension doing real work: the same tool at "acts with approval" and at "acts autonomously" produces materially different assessments.*

**Scope ([Step 1](../assess/1-scope.md)):** The team runs a public-facing application service and wants to use an AI agent, integrated with their observability platform, to triage out-of-hours alerts. In phase one, the agent investigates and proposes a remediation, and the on-call responder approves each action. In phase two, planned for the following quarter, the agent would apply a fixed set of pre-approved remediations (restarting a stuck queue worker, scaling a service up) without waking anyone.

- **Category:** Live service operations
- **Autonomy:** Assessed at **acts autonomously**. Phase one is "acts with approval", but the team assesses at the higher level for two reasons: they intend to move to phase two within the quarter, and the per-action approval is a configuration flag that anyone with admin access can turn off. Assess what the tool is permitted to do, not what you intend to let it do. This triggers SRO approval regardless of the risk rating.

*What is shared:* Production logs, traces, metrics, alert payloads, deployment manifests, and infrastructure state. The service handles OFFICIAL data including personal details of applicants, and its logs were never written on the assumption that a third party would read them.

**Check the tool ([Step 2](../assess/2-check-tool.md)):** The vendor's agent product is not excluded, and the SRO clears it up to OFFICIAL. **What it is**: integrates with the observability platform and holds standing read access to the full production telemetry stream; can execute actions against production, not merely propose them. **What the supplier promises**: UK and EU data residency, no training on customer inputs, SOC 2 and ISO 27001, an audit API. Two facts carry unusual weight here because the tool can act. On **change and notice**, the vendor confirms 30 days' contractual notice of model changes, without which the team would have an agent in production whose behaviour could shift silently. On **control over what it can do**, the vendor confirms customer-defined action allowlists, and the team goes further by enforcing the limit in their own IAM rather than the agent's configuration, so a change at the vendor's end cannot widen it.

Note what the profile does and does not settle. It records that the agent is *capable* of acting autonomously against production: a fact, and the reason this assessment is a serious one. It does not say the team may let it. That is their autonomy decision in Step 1, and what bounds it are the mitigations below.

**Assess the risks ([Step 3](../assess/3-assess-risks.md)):**

| | |
| ---- | ---- |
| **Overall inherent risk** | 🔴 High |
| **Driven by** | Data leakage, accuracy, accountability, supply chain, prompt injection |
| **Overall residual risk** | 🟠 Medium |
| **Driven by** | Data leakage, accuracy, over-reliance, supply chain, prompt injection |
| **Approval required** | SRO, and required regardless by the autonomy level |

| Risk | Inherent | Residual |
| ---- | ---- | ---- |
| Data leakage | 🔴 High | 🟠 Medium |
| Accuracy and hallucination | 🔴 High | 🟠 Medium |
| Accountability gaps | 🔴 High | 🟢 Low |
| Bias and fairness | 🟢 Low | 🟢 Low |
| IP and licensing | 🟢 Low | 🟢 Low |
| Over-reliance and skill erosion | 🟠 Medium | 🟠 Medium |
| Supply chain and security | 🔴 High | 🟠 Medium |
| Prompt injection | 🔴 High | 🟠 Medium |

*Autonomy adjustment:* at *acts autonomously*, accuracy, accountability, supply chain and prompt injection are rated at least high impact.

### Data leakage

Logs contain session tokens, authorisation headers, connection strings, and applicant PII in error payloads. Unlike a one-off share, the agent has standing read access to the whole telemetry stream, continuously, with nobody reviewing what it sees.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- **Credential scrubbing in the log pipeline** before logs reach the agent, verified by a test that plants a known token upstream and asserts it is redacted downstream *(likelihood)*
- Vendor terms: UK and EU residency, no training on customer inputs *(likelihood)*

Scrubbing is verified and tested, but log content is unpredictable and new code paths log new things. The exposure is ongoing rather than one-off, which is what keeps this at medium.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Accuracy and hallucination

A confidently wrong root cause at 3am leads to a wrong remediation. Restarting the wrong component during a partial outage can turn degradation into a full outage, and incident pressure is precisely when plausible-sounding output gets least scrutiny.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- **No irreversible actions in the allowlist.** No data deletion, no access-control change, no deployment, no scale-to-zero. Every permitted action is reversible within minutes *(impact)*
- **Rate limit.** No more than three automated remediations per hour, after which the agent stops and pages a human: this stops a misdiagnosis becoming a loop *(impact)*
- **Phase two gated** on eight weeks of phase one operation with no incorrect proposed action *(likelihood)*

The allowlist bounds what a wrong diagnosis can do to four reversible actions, and the rate limit stops a wrong one repeating. Wrong diagnoses will still happen.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Accountability gaps

Raised to high impact by the autonomy adjustment. In phase two nobody chooses each action; the decision was made months earlier by whoever configured the allowlist. Without deliberate design, the incident record will show a system that recovered without showing what recovered it.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- **Full action logging.** Every action is written to the incident record with the service account identity, the triggering alert, and the agent's stated reasoning *(impact)*
- **Named accountable owner:** the service's lead SRE *(impact)*

The incident record now shows what the agent did, under what identity, on what evidence, and a named person owns the behaviour of the system as a whole.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Unlikely | Medium | 🟢 **Low** |

### Supply chain and security

Raised to high impact by the autonomy adjustment. The agent holds credentials in production. A vendor compromise, or a model update that changes its behaviour, is a production incident that the team did not cause and cannot see coming.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- **Least privilege enforced outside the agent.** The allowlist lives in the team's own IAM policy, not the agent's configuration: the service account is permitted exactly four operations, and anything else fails at the infrastructure layer regardless of what the agent decides. A mitigation the AI can be talked out of is not a mitigation *(impact)*
- **Kill switch.** Any on-call engineer can disable the service account from the runbook without a deployment. Tested monthly *(impact)*
- 30 days' contractual notice of model changes, giving time to re-test *(likelihood)*

Because permissions are enforced in the team's IAM rather than the vendor's configuration, a compromised or altered agent still cannot exceed four reversible actions. The dependency itself remains.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Prompt injection

Raised to high impact by the autonomy adjustment, and the vector here is unusually accessible: the service logs user-supplied form fields, so anyone who can submit the public form can place text in front of the agent without authenticating or touching any system. Combined with the ability to act, this is remote action in production triggered by an anonymous member of the public.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | High | 🔴 **High** |

**Mitigations:**

- The IAM-enforced allowlist applies here too: a successful injection can at worst trigger one of four safe, reversible, rate-limited, logged actions *(impact)*
- **Injection testing.** Adversarial strings submitted through the public form and traced through the log pipeline to confirm they cannot trigger an action *(likelihood)*

Injection cannot be eliminated, so the likelihood does not move: the whole of the work here is on consequences. That is a bounded outcome rather than a prevented one, and the team says so rather than claiming a reduction it has not achieved.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Likely | Low | 🟠 **Medium** |

### Over-reliance and skill erosion

Out-of-hours incidents are where diagnostic skill is built. If the agent handles the routine ones, new joiners may never work an unassisted incident, and the team's ability to cope when the agent is wrong (or down) decays quietly.

| Likelihood | Impact | Inherent risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

**Mitigations:**

- Engineers rotated through unassisted incident practice *(likelihood)*

Partly mitigated, but the underlying tension is real: the agent is most useful on exactly the incidents that build skill. **The rating does not move**, and the team has chosen to accept it with monitoring rather than claim a reduction.

| Likelihood | Impact | Residual risk |
| ---- | ---- | ---- |
| Possible | Medium | 🟠 **Medium** |

### Risks assessed as low

- **Bias and fairness**: 🟢 Low (unlikely × low). Alert triage does not treat groups of people differently; the alerts concern infrastructure, not individuals. Residual unchanged.
- **IP and licensing**: 🟢 Low (unlikely × low). Generated runbook and configuration content is small in volume and internal. Residual unchanged.

**Approve, record, do the work, and share ([Step 4](../assess/4-record-and-work.md)):**

*Record:* The assessment is saved as the record for this use, capturing the autonomy level and the reasoning for assessing at the higher level, inherent risk (🔴 high), the mitigations including the autonomy set, residual risk (🟠 medium), and SRO approval with a review date at the phase two gate.

*Checklist:* Followed the [Live service operations checklist](checklists.md#checklist-live-service-operations). What may and may not be shared was agreed and written into the runbook before go-live rather than during an incident. Credential-bearing log fields identified and restricted. Kill switch tested. Autonomy level confirmed against the tool's actual configuration.

*Learnings:* Over eight weeks of phase one the agent proposed the correct remediation for 31 of 38 alerts. Of the seven wrong proposals, two would have made the incident worse, both during partial outages where the agent read a downstream symptom as the cause. Phase two was **delayed rather than approved**, and the allowlist narrowed to exclude restarts while a multi-component incident is declared. Separately, the injection test found the log scrubber missed tokens arriving in a third-party webhook payload, which had not been in scope when the scrubbing rules were written. Both findings were shared at the department's SRE community of practice.
