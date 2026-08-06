# Reference: Use-Type Profiles

This reference gives the detail behind the eleven use types. Use it alongside [Step 1: Scope Your Use](../assess/1-scope.md) to categorise your use precisely, and alongside [Step 3: Identify the Risks](../assess/3-identify-risks.md) to understand the typical risk fingerprint of your use type.

The use types describe **tasks people do while delivering a government service**, not the services themselves. The one exception is AI-powered product features, which covers AI you build *into* the service — it is included because it carries the highest governance requirements and teams need to recognise when they have crossed into it.

Most AI use on delivery projects falls into one of eleven categories. Some uses span more than one — if so, assess against each relevant category and apply the more restrictive set of safeguards. As [Step 1](../assess/1-scope.md#categorise-your-use) sets out, these are a thinking aid rather than an exhaustive taxonomy: they exist to get you to the right risks quickly, so pick the closest fit rather than arguing the boundary.

## Types of AI

Before categorising your use, it helps to understand the types of AI involved. Different types have different risk profiles:

- **Generative AI (GenAI)** — models that generate new content such as text, images, or code. This includes most of the AI tools used in delivery work today (ChatGPT, Claude, Gemini, GitHub Copilot, Microsoft 365 Copilot). The key risks are hallucination (plausible but wrong outputs), data leakage (what you share becomes an input to a third-party service), and prompt injection.

- **Large Language Models (LLMs)** — a subset of generative AI focused on text. Most coding assistants, chatbots, and summarisation tools are LLM-based. LLMs have specific risks around prompt injection (because they cannot distinguish instructions from data) and hallucination (because they generate statistically plausible text, not verified facts).

- **Machine Learning (ML)** — the broader category that includes classification, prediction, anomaly detection, and pattern recognition. ML models may not be generative — they may classify inputs or predict outcomes. The risk profile is different: bias and fairness are typically higher concerns, while prompt injection is less relevant (though data poisoning applies).

- **Natural Language Processing (NLP)** — text analysis, transcription, translation, and sentiment analysis. These capabilities are increasingly LLM-based, but can also use traditional ML. The risks depend on the underlying technology and what data is being processed.

Many tools combine multiple types. A support ticket triage system might use an LLM for summarisation and a traditional ML model for classification. Assess the risks of each component.

---

## AI-assisted coding

Using AI tools to help write, complete, review, test, or debug code. This includes code generation from prompts, inline code completion, AI-assisted code review, test generation, and using AI to help debug issues.

The key characteristic is that **AI is generating or modifying code** that may end up in the product.

**Common tools:** GitHub Copilot, Cursor, Claude Code, Amazon CodeWhisperer.

**What is typically shared:** Code snippets, individual files, function signatures, error messages. The AI tool may also see surrounding context in the editor.

**Key concerns:** Embedded secrets in the working file or adjacent files; proprietary business logic in the immediate context.

**Also covers testing work:** generating test cases from acceptance criteria, exploratory test charters, and accessibility audit assistance. Test coverage is evidence against the Service Standard, so AI-written tests carry a specific failure mode — tests that pass without meaningfully testing anything. Review AI-generated tests for what they actually assert, not just that they are green. If you are generating *test data* rather than test code, that is a separate use type — see AI-assisted synthetic data generation below.

**Action required:** Check the contents of your code before sharing. Remove any secrets, credentials, or sensitive configuration. Ensure the AI tool is on the register and cleared for the classification of the code.

**Typical risk fingerprint:** Data leakage and IP/licensing are worth assessing; accuracy, supply chain, and prompt injection depend on how AI-generated code enters the product. Accountability, bias, and over-reliance are usually lower (but watch skill erosion in junior developers).

---

## AI-assisted code analysis

Using AI to analyse existing codebases — identifying patterns, mapping dependencies, assessing architecture, finding technical debt, detecting security issues, or building understanding of legacy systems.

The key characteristic is that **large volumes of existing code are being sent to the AI tool**, and the output is analytical (findings, assessments, recommendations) rather than code destined for production. This is distinct from AI-assisted coding because the risk profile differs: the primary concerns are the sensitivity of the code being shared and the reliability of the analysis, rather than the quality of generated code.

**Common tools:** Claude, ChatGPT Enterprise, Gemini, SonarQube AI.

**What is typically shared:** Potentially the entire codebase — source code, configuration, infrastructure-as-code, build scripts, dependency manifests, database schemas.

**Key concerns:** Volume is much larger. May include embedded secrets throughout, security-sensitive architecture details, and sensitive business logic across the full system. Manual review of every input is impractical.

**Legacy system comprehension** is the most common government application — using AI to understand and document mainframe, COBOL, or long-unmaintained systems ahead of migration. It is genuinely useful, but AI is weakest exactly where legacy systems are hardest: undocumented business rules, edge cases, and behaviour that only makes sense in historical policy context. Treat AI-derived descriptions of legacy business logic as hypotheses to verify against the running system, never as specification.

**Security work** also sits here — AI-assisted threat modelling, vulnerability triage, and secure code review. Note that threat models and unremediated vulnerability findings are among the most sensitive artefacts a delivery team holds; assess sharing them with the same care as OFFICIAL-SENSITIVE data.

**Action required:** Run a secrets scanning tool across the entire codebase before sharing. Evaluate whether the AI tool has been approved for this classification level. For OFFICIAL-SENSITIVE codebases, obtain SRO approval before proceeding.

**Typical risk fingerprint:** Data leakage is high (whole-codebase volume). Accuracy, over-reliance, and prompt injection are worth assessing. Others are usually lower.

---

## AI-assisted synthetic data generation

Using AI to generate artificial datasets that stand in for real data — test data for development and QA environments, demonstration data, data for load and performance testing, or training data for a model.

The key characteristic is that **real data is used to produce artificial data that is then treated as safe**. That assumption is the risk. Synthetic data is often generated *from* production data, and the resulting dataset can carry real records through — either memorised verbatim by the model or reconstructable by combining fields. A dataset that everyone believes is synthetic will be handled with far less care than the data it was derived from, so a leak here bypasses every control you have placed on the real thing.

The second failure mode is fidelity. Synthetic data that does not reflect the real distribution gives false confidence: the service passes its tests and then fails in production on the cases the generator never produced — unusual names, non-Latin characters, missing fields, very long values, edge-case dates. Under-representation is not random. Generators trained on majority-case data under-produce exactly the minority cases where government services most often fail their users, so a fidelity problem becomes an equality problem.

**Common tools:** Claude, ChatGPT Enterprise, Gretel, Tonic.ai, Synthesized, Mostly AI, and bespoke scripts calling a model API.

**What is typically shared:** Real production or pre-production data used as the seed or reference; database schemas; data dictionaries; sample records. In some approaches, nothing real is shared and the generator works from the schema alone — a materially lower-risk approach where it is viable.

**Key concerns:** Re-identification of individuals from supposedly synthetic records. Real records reproduced verbatim in the output. Downstream handling of the dataset as non-personal data when it may still be personal data under UK GDPR. Distribution skew that under-represents minority cases and produces misleading test or model results.

**Action required:** Prefer schema-only generation where it meets the need. Where real data seeds the generation, treat the output as personal data until you have tested otherwise — run re-identification and duplicate-record checks against the source. Document what the dataset does and does not represent, and record the classification you have assigned it and why. If the synthetic data will train or evaluate a model, assess its distribution against the real population.

**Typical risk fingerprint:** Data leakage and accuracy are typically high, and bias is high because distribution skew propagates into everything tested or trained on the dataset. Over-reliance is worth assessing. Accountability, IP, supply chain, and prompt injection are usually lower.

---

## AI-powered product features

Building AI capabilities into the product or service being delivered — chatbots, content summarisation, document classification, triage systems, recommendation engines, or automated decision support.

The key characteristic is that **AI will directly interact with or affect end users** of the service. This carries the highest governance requirements because of the potential impact on members of the public.

**Common tools:** Claude API, Azure OpenAI Service, AWS Bedrock, Google Vertex AI.

**What is typically shared:** User PII, case records, health or financial data — processed by the AI feature at runtime, on an ongoing basis. The code and prompts that define the feature's behaviour are also shared with the AI provider.

**Key concerns:** Data handling must be robust at scale and over time. Subject to GDPR, accessibility, and equality obligations. Users may share sensitive information unprompted. Ethical concerns include the potential for discriminatory outcomes and the impact of errors on vulnerable individuals.

**This is not only about generative AI.** Classification, prediction, and scoring models — fraud detection, demand forecasting, caseworker prioritisation — sit here too, and they are where much of government's AI risk actually lives. For these, bias and fairness dominate rather than hallucination, and additional duties apply: UK GDPR Article 22 restricts solely automated decisions with legal or similarly significant effects, affected people need a route to explanation and challenge, and an ATRS record is likely to be mandatory.

**Action required:** Complete a DPIA before processing personal data. Ensure the AI provider's data handling meets GDPR requirements. Consider the equality impact — could this feature disadvantage any group? Obtain SRO and client approval.

**Typical risk fingerprint:** The highest-governance use type. Data leakage, accuracy, accountability, bias, and prompt injection are all typically high; supply chain is worth assessing.

---

## AI-assisted user-facing support

Using AI to help manage support and service desk operations — auto-categorising and routing tickets, suggesting or drafting responses for agents, providing first-line chatbot support, summarising ticket history, generating knowledge base articles, or predicting escalations and SLA risks.

The key characteristic is that **AI is processing operational support data to help teams respond to and resolve requests from people**. This is distinct from AI-powered product features: support AI is an internal/operational tool that assists the team, whereas product features are delivered directly to end users. It is also distinct from live service operations: this use type is about handling requests from *people*, whereas live service operations is about diagnosing and fixing *systems*. The risks here are the unpredictable sensitivity of ticket content (users routinely paste credentials, PII, and system details), the consequences of incorrect triage or advice, and the potential for automation to act without adequate human oversight.

**Common tools:** Microsoft Copilot for Service, Zendesk AI, ServiceNow AI.

**What is typically shared:** Support tickets, error logs, screenshots, system configuration details, user contact information — often containing an unpredictable mix of sensitive content.

**Key concerns:** Ticket content is inherently unpredictable: users routinely paste credentials, PII, system architecture details, and vulnerability information into support requests. Attachments and screenshots may contain visible sensitive data that is hard to automatically scan or redact. Ethical concerns include the risk of biased prioritisation and the consequences of incorrect triage on individuals.

**Action required:** Implement automatic PII detection and credential scanning before data reaches the AI tool. Define exclusion rules for sensitive ticket types. Complete a DPIA given the high likelihood of personal data.

**Typical risk fingerprint:** Data leakage is high. Accuracy, accountability, bias, over-reliance, supply chain, and prompt injection are all worth assessing — this is a broad-front use type.

---

## AI-assisted live service operations

Using AI in the running of a live service — triaging alerts, investigating incidents, correlating and summarising logs, proposing root causes, generating or reviewing infrastructure-as-code, drafting runbooks, and suggesting or applying remediations.

The key characteristic is that **AI is working against production systems**, often at speed and under pressure. This is distinct from user-facing support, which handles requests from people; here the subject is the infrastructure itself. It is distinct from coding because the output takes effect in a live environment: an AI-suggested Terraform change is a production change, and it should pass through the same change control as any other.

**Common tools:** Datadog and Dynatrace AI features, incident.io, PagerDuty AI, Rootly, GitHub Copilot and Claude Code for infrastructure-as-code, and general-purpose assistants used ad hoc during incidents.

**What is typically shared:** Production logs, traces and metrics, stack traces, alert payloads, infrastructure and network configuration, deployment manifests, incident timelines, and — during a live incident — whatever a responder pastes into a chat window at 3am.

**Key concerns:** Production logs are among the most credential-rich data a team touches: access tokens, session identifiers, connection strings, and user PII all routinely appear in them, and nobody has reviewed them before they are pasted into an AI tool. Log content is also partly attacker-controlled — anyone who can cause your service to log a string they chose has a prompt injection route into your operations assistant. Incident pressure erodes the review step that other use types rely on. And where the AI can act rather than advise, the blast radius is production.

**Action required:** Decide in advance — not during an incident — what may be shared with an AI tool and what must not, and make the decision easy to follow under pressure. Scrub or restrict credential-bearing log fields before they reach the tool. Route AI-proposed infrastructure changes through normal change control and peer review. Where the AI can execute actions, apply least privilege, require approval for anything destructive or irreversible, and ensure every action is logged to the incident record. Maintain and periodically practise operating without the tool.

**Typical risk fingerprint:** Data leakage, accuracy, supply chain, and prompt injection are typically high. Accountability and over-reliance are worth assessing — and both rise sharply if the AI can act rather than advise, so pay close attention to the [autonomy level](../assess/1-scope.md#assess-the-level-of-autonomy) you recorded in Step 1. Bias and IP are usually lower.

---

## AI-assisted user research

Using AI to support research with users — transcribing and summarising interviews, identifying themes across sessions, analysing survey free text, synthesising findings, and building personas or journey maps from research data.

The key characteristic is that **AI is processing what real people told you, in order to represent them to the team**. Two things follow from that. The data is often highly personal and was collected under a specific consent, so the handling constraints are unusually tight. And the output stands in for people who are not in the room — if the synthesis quietly drops the participants who were hardest to understand, nobody notices, and the service gets designed for everyone else.

**Common tools:** Claude, ChatGPT Enterprise, Otter.ai, Dovetail, Marvin.

**What is typically shared:** Interview transcripts and recordings, survey responses, diary study entries, usability session notes, user behaviour data, demographic information.

**Key concerns:** Participant data is often highly personal — health, finances, immigration status, experiences of harm. Consent constraints are common and frequently predate AI. Even anonymised transcripts may be re-identifiable from the detail of what someone described. Ethical concerns include misrepresenting participant views and using data beyond the scope of consent.

**The representativeness problem** is the signature risk. AI synthesis gravitates to the clearly-expressed majority view. Participants who spoke through an interpreter, took longer to make a point, used non-standard English, or described something the model has little training data for are the ones most likely to be smoothed out of a themes list — and in government research they are frequently the users the service most needs to work for. Check the synthesis against the sessions that were hardest to summarise, not the ones that were easiest.

**Action required:** Check that participant consent covers AI processing before you upload anything. If it does not, you cannot proceed without obtaining it — this is a hard constraint, not a risk to be mitigated. Remove or anonymise PII where the tool's handling does not meet the sensitivity of the data. Validate themes against source transcripts, paying particular attention to under-represented participants.

**Typical risk fingerprint:** Data leakage is high (personal participant data under consent) and bias is high (representativeness of synthesis). Accuracy, over-reliance, and prompt injection are worth assessing. Accountability, IP, and supply chain are usually lower.

---

## AI-assisted design

Using AI in the design of the service — exploring interaction and service design options, generating and iterating prototypes, producing diagrams and journey maps, and assessing designs against accessibility standards.

The key characteristic is that **AI is shaping how the service works and how people move through it**. AI's role here is usually divergent — producing options to react to rather than answers to adopt — and everything downstream passes through research and testing, which is the main thing keeping the risk contained. The exposure is in what AI quietly normalises along the way: patterns that exclude people, and generated visual material of uncertain provenance.

**Common tools:** Figma AI, Miro AI, Claude, ChatGPT Enterprise, image generation tools.

**What is typically shared:** Design briefs, wireframes and prototypes, journey maps, existing service patterns, and summarised research findings.

**Key concerns:** AI produces accessibility antipatterns confidently — colour as the only carrier of meaning, insufficient contrast, vague link text, unlabelled imagery, and form patterns that break with assistive technology. It will then assess a design for accessibility with equal confidence and be wrong, which is more dangerous than not assessing at all. AI design suggestions also reflect commercial web conventions rather than the GOV.UK Design System, and the differences are deliberate.

**Provenance matters here in a way it does not for most use types.** AI-generated images and illustration published under a government brand carry licensing uncertainty and reputational exposure if a resemblance to training material is later spotted. Establish whether AI-generated visual material is acceptable in public-facing output before you produce it, not after.

**Action required:** Treat AI accessibility assessment as a prompt to test, never a substitute for testing with assistive technology and disabled users. Check suggestions against the GOV.UK Design System rather than accepting generic web patterns. Confirm the position on AI-generated imagery before producing it. Keep AI in the divergent part of design and rely on research and testing to converge.

**Typical risk fingerprint:** Bias is high — accessibility decisions made at design time are the hardest to undo later. Data leakage, accuracy, IP/licensing, and over-reliance are worth assessing. Accountability, supply chain, and prompt injection are usually lower.

---

## AI-assisted content

Using AI to draft, edit, translate, or restructure the words in and around the service — service content and guidance, page copy, form labels and hint text, error messages, letters, emails and notifications, and published communications.

The key characteristic is that **AI is producing text that reaches the public in the department's name**. This is the use type where AI is most capable, most used, and where the gap between *fluent* and *correct* is widest — output that reads well is the least likely to be checked.

**Common tools:** Claude, ChatGPT Enterprise, Microsoft 365 Copilot, translation services, CMS content assistants.

**What is typically shared:** Existing service content, style and tone guidance, content requirements, policy and legislative source material, and — for letters and notifications — templates that may include personal data examples.

**Key concerns:** Reading age and register drift. GOV.UK targets a reading age of nine; AI writes fluent, confident prose well above that, in a register that drifts corporate. It reproduces the conventions of its training data, not government content conventions, and will reach for "please note", "utilise", and constructions the style guide prohibits. Left unchecked, this excludes exactly the users who most need the content to work.

**Accuracy has direct consequences here.** A wrong eligibility statement on a guidance page is read and acted on by thousands of people, and for many users the guidance *is* the service. Any content asserting a rule, entitlement, deadline, or statutory duty must be traced back to the authoritative source — a model's recollection of policy is not a source.

**Tone with people in difficulty.** Content about bereavement, debt, immigration status, or a refused application needs a register AI does not reliably produce; it tends towards brightness and reassurance where plainness and directness are needed. Test this content with users, not just with colleagues.

**Translation carries statutory weight.** Where Welsh Language Standards or equivalent duties apply, an AI translation is not a compliance artefact until a qualified human translator has confirmed it. Meaning shifts invisible to a monolingual reviewer are precisely the errors those duties exist to prevent.

**Action required:** Check AI-drafted content against the GOV.UK style guide and the service's reading age target. Trace every factual claim about rules, entitlements, and deadlines to the authoritative source. Have a content designer review it as content, not merely proofread it. Obtain qualified human verification for any translation carrying a statutory duty. Confirm the position on AI-generated copy in published material.

**Typical risk fingerprint:** Accuracy and bias are typically high — wrong content and inaccessible content both land directly on users. Data leakage, accountability, IP/licensing, and over-reliance are worth assessing. Supply chain and prompt injection are usually lower.

---

## AI-assisted business analysis

Using AI to work out and write down **what the team is doing and why** — turning stakeholder notes into user stories and acceptance criteria, mapping as-is and to-be processes, analysing dependencies and options, and drafting the artefacts that record and justify decisions: architecture options papers, ADRs, business cases, spend control submissions, service assessment evidence, and DPIA drafts.

The key characteristic is that **the output is treated by others as settled reasoning**. A requirement is built from. A business case is approved against. A service assessment submission is evidence that a team thought something through. In each case the reader is not checking the reasoning — they are relying on it having happened. That is what makes this different from general productivity, where a wrong output inconveniences a colleague, and different from research and design, where the output is visibly a draft to be tested.

The name follows the delivery discipline, but the category is a little broader than business analysis strictly is: architecture decision records and assurance submissions sit here too, because they share the same risk shape. Note also that this is analysis of *the work*, not of code — AI-assisted code analysis is a separate use type with an almost opposite fingerprint.

**Common tools:** Claude, ChatGPT Enterprise, Microsoft 365 Copilot, Miro AI, Jira and Azure DevOps AI features.

**What is typically shared:** Stakeholder workshop notes, policy and legislative source material, existing service documentation, architecture diagrams, commercial and financial information, draft governance submissions.

**Key concerns:** Hallucinated detail here has a long fuse. An invented eligibility rule or misremembered statutory duty that enters a user story looks like a requirement by the time it reaches a developer, gets built, gets tested against itself, and ships — with every downstream step treating it as already verified. Nothing in the delivery process is designed to catch a requirement that was wrong from the start.

**The accountability failure is the more serious one.** Governance bodies read an options paper or a DPIA as evidence that a named person reasoned through a problem. An artefact that reads well because a model wrote it, and that nobody has genuinely thought about, defeats the purpose of the governance step while passing it. Use AI to structure and express your reasoning, not to supply it. The test is simple: can the named author defend every claim in the document without referring back to the tool?

**Action required:** Trace any AI-stated rule, entitlement, or statutory duty back to the authoritative source before it enters the backlog or a decision document, and mark it unverified until you have. For assurance artefacts, confirm the accountable person has reviewed the reasoning rather than the wording. Be transparent with governance bodies about AI involvement where it is material.

**Typical risk fingerprint:** Accuracy and accountability are typically high. Data leakage, over-reliance, and prompt injection are worth assessing. Bias, IP, and supply chain are usually lower.

---

## AI-assisted general productivity

Using AI for routine work tasks that do not shape a decision — drafting or summarising emails and meeting notes, transcribing meetings and calls, translating internal documents, generating images for presentations, extracting data from documents, or formatting and restructuring content.

The key characteristic is that **AI is assisting with everyday work tasks** that are not code, research, design, content, or product development, and whose output is not itself an input to a significant decision.

**This category is narrower than it looks, and the boundary matters.** It is tempting to file anything text-shaped here, but the low-risk feel of "productivity" is only earned when the output is genuinely routine. If the output will be read as evidence that someone reasoned something through — a business case, an options paper, service assessment evidence, a set of requirements — it belongs under business analysis, and carries an accountability risk that this category does not account for. If in doubt, ask what happens if the output is subtly wrong and nobody notices: if the answer is "a colleague is mildly inconvenienced", it is productivity; if it is "a governance decision is made on a false basis", it is not.

Even genuinely routine use is not risk-free. Meeting transcriptions may contain sensitive discussions, PII, or commercially confidential information. Email drafts may inadvertently include information that should not be shared. AI tools used for these tasks often require additional permissions — such as access to calendars, meetings, or contact lists — that must be identified, controlled, and monitored.

**Common tools:** Microsoft 365 Copilot, ChatGPT Enterprise, Claude, Google Gemini for Workspace.

**What is typically shared:** Meeting transcripts, email content, documents, calendar data, contact lists.

**Key concerns:** Meetings and emails frequently contain sensitive discussions, PII, commercial information, and operational details. AI tools used for productivity often request broad permissions (access to calendar, contacts, files) that may expose more data than intended.

**Action required:** Review what permissions the AI tool requires and whether they are proportionate. Do not transcribe or summarise meetings containing sensitive discussions without assessing the data involved. Check whether the tool is cleared for the classification level of the data it will access. Confirm the task genuinely belongs in this category rather than business analysis or content.

**Typical risk fingerprint:** Data leakage is worth assessing (and can be high given broad permissions). Accuracy, over-reliance, supply chain, and prompt injection are worth assessing.
