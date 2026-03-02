# Step 2: Understand What You Are Sharing

Now that you have defined what you want to do, assess what you will actually be sharing with the AI tool. This is often the single most important factor in determining what level of safeguards are needed.

Most AI uses on delivery projects involve sharing **code**, **data**, or **both**. These have different risk profiles, different legal frameworks, and different mitigations — so it is worth assessing them separately.

## Understand the code

If your AI use involves sharing source code with the tool — whether snippets during coding assistance or entire repositories during code analysis — consider the following.

> **Secrets must NEVER be shared with any AI tool.** API keys, credentials, tokens, database connection strings, and service endpoints must be removed before any code is shared. Run a secrets scanning tool before sharing code with any AI service. If you find secrets in the code, remove them and re-evaluate what you should share.

**Does the code contain embedded secrets?**
API keys, credentials, database connection strings, service endpoints, and tokens are commonly found in codebases, particularly legacy ones. These are high-impact if leaked. If the answer is yes, remove them before proceeding.

**Does the code reveal security-sensitive architecture?**
Even without secrets, source code reveals how systems are designed — authentication mechanisms, access control logic, data validation approaches, and infrastructure configuration. This information could be valuable to an attacker.

**Does the code contain proprietary business logic?**
Rules engines, pricing algorithms, eligibility calculations, and case handling logic may be commercially sensitive or operationally sensitive even if the code itself is classified as OFFICIAL.

**How much code will be shared?**
There is a significant difference between sharing a function or file (AI-assisted coding) and sharing an entire codebase (AI-assisted code analysis). The more code shared, the greater the exposure and the harder it is to manually review what the AI tool receives.

| Use type | What code is typically shared | Key concerns | Action required |
| ---- | ---- | ---- | ---- |
| **AI-assisted coding** | Code snippets, individual files, function signatures, error messages. The AI tool may also see surrounding context in the editor. | Embedded secrets in the working file or adjacent files; proprietary business logic in the immediate context | Check the contents of your code before sharing. Remove any secrets, credentials, or sensitive configuration. Ensure the AI tool is on the approved list. |
| **AI-assisted code analysis** | Potentially the entire codebase — source code, configuration, infrastructure-as-code, build scripts, dependency manifests, database schemas | Volume is much larger. May include embedded secrets throughout, security-sensitive architecture details, and sensitive business logic across the full system. Manual review of every input is impractical. | Run a secrets scanning tool across the entire codebase before sharing. Evaluate whether the AI tool has been approved for this classification level. For OFFICIAL-SENSITIVE codebases, obtain SRO approval before proceeding. |

## Understand the data

If your AI use involves sharing data — whether user data, research data, or operational data — consider the following:

**What is the data classification?**
Government information is classified under the Government Security Classifications Policy. The classification of the data you are sharing with an AI tool is one of the key factors in determining what safeguards are needed:

| Classification | Description | AI implications |
| ---- | ---- | ---- |
| **OFFICIAL** | The majority of government information. Routine business operations and services. | AI tools that meet the criteria in [Step 4](step-4-check-tool.md) are generally appropriate, subject to the risk assessment in [Step 3](step-3-assess-risks.md). |
| **OFFICIAL-SENSITIVE** | OFFICIAL information that requires additional handling controls. Includes personal data, commercial data, and operationally sensitive information. | Only AI tools that have been formally assessed and approved for use with OFFICIAL-SENSITIVE data should be used. Do not make this assessment yourself — if the tool has not been approved for this classification level, escalate to the SRO before proceeding. Client approval is likely needed. |
| **SECRET / TOP SECRET** | Information where compromise would cause serious or exceptionally grave damage. | Do not use external AI services. Any AI use must be within accredited secure environments. This is outside the scope of most delivery projects and requires specialist security guidance. |

Classification is important, but it is not the only factor. Data classified as OFFICIAL can still carry significant risks if it contains PII, is subject to consent constraints, or is commercially sensitive. The questions below help you assess these additional dimensions.

**Does the data contain personally identifiable information (PII)?**
If yes, UK GDPR obligations apply. You may need to conduct a Data Protection Impact Assessment (DPIA). Consider whether the data can be fully anonymised before being processed by AI. **Important:** pseudonymised data is still personal data under UK GDPR — only fully anonymised data (where individuals cannot be identified by any means) falls outside GDPR scope. If you are unsure whether data is truly anonymised, treat it as personal data. Before sharing any personal data with an AI tool, confirm with your Data Protection Officer or data protection team that the proposed use has been approved.

**Is the data subject to specific consent constraints?**
Research participant data may have been collected under consent agreements that do not cover AI processing. Check the consent forms and ethics approvals. If consent does not cover AI processing, you cannot use AI tools on that data without obtaining additional consent.

**Are there contractual restrictions on data processing?**
Client contracts may specify where data can be processed, by whom, and using what tools. Check the contract and any data handling agreements before using AI tools on client data.

**Is the data commercially sensitive?**
Business strategy, commercial terms, financial data, and operational information may be valuable to competitors or damaging if leaked. Even if not formally classified above OFFICIAL, commercial sensitivity is a real risk factor.

| Use type | What data is typically shared | Key concerns | Action required |
| ---- | ---- | ---- | ---- |
| **AI-powered product features** | User PII, case records, health or financial data — processed by the AI feature at runtime, on an ongoing basis | Data handling must be robust at scale and over time. Subject to GDPR, accessibility, and equality obligations. Users may share sensitive information unprompted. Ethical concerns include the potential for discriminatory outcomes and the impact of errors on vulnerable individuals. | Complete a DPIA before processing personal data. Ensure the AI provider's data handling meets GDPR requirements. Consider the equality impact — could this feature disadvantage any group? Obtain SRO and client approval. |
| **AI-assisted support** | Support tickets, error logs, screenshots, system configuration details, user contact information — often containing an unpredictable mix of sensitive content | Ticket content is inherently unpredictable: users routinely paste credentials, PII, system architecture details, and vulnerability information into support requests. Attachments and screenshots may contain visible sensitive data that is hard to automatically scan or redact. Ethical concerns include the risk of biased prioritisation and the consequences of incorrect triage on individuals. | Implement automatic PII detection and credential scanning before data reaches the AI tool. Define exclusion rules for sensitive ticket types. Complete a DPIA given the high likelihood of personal data. |
| **AI-assisted research & design** | Interview transcripts, survey responses, user behaviour data, demographic information | Research participant data is often highly personal. Consent constraints are common. Even anonymised data may be re-identifiable in context. Ethical concerns include the risk of misrepresenting participant views and using data beyond the scope of consent. | Check that participant consent covers AI processing. Remove or anonymise PII before sharing with the AI tool. If consent does not cover AI processing, do not proceed without additional consent. |
| **AI-assisted general productivity** | Meeting transcripts, email content, documents, calendar data, contact lists | Meetings and emails frequently contain sensitive discussions, PII, commercial information, and operational details. AI tools used for productivity often request broad permissions (access to calendar, contacts, files) that may expose more data than intended. | Review what permissions the AI tool requires and whether they are proportionate. Do not transcribe or summarise meetings containing sensitive discussions without assessing the data involved. Check whether the tool is approved for the classification level of the data it will access. |

## When both code and data are involved

Many AI uses involve both code and data, and it is important to assess each:

- **AI-assisted coding** primarily involves code, but test fixtures and seed data may contain data patterns that mirror real records. Configuration files may contain connection strings or service credentials.
- **AI-assisted code analysis** primarily involves code, but the codebase may contain embedded data — sample records in test files, real values in configuration, data migration scripts with actual content.
- **AI-powered product features** primarily involve data at runtime, but the code and prompts that define the AI feature's behaviour are also shared with the AI provider.
- **AI-assisted support** primarily involves data (ticket content, user details, operational information), but tickets frequently contain code snippets, error logs, configuration details, and system architecture information.
- **AI-assisted research & design** primarily involves data, but design artefacts may reference system behaviour or architecture.
- **AI-assisted general productivity** primarily involves data (documents, emails, meeting content), but the AI tool may require permissions that expose additional data beyond what you intend to share (calendar entries, contact lists, file directories).

If both code and data are involved, assess each independently and apply the more restrictive set of safeguards.

**Record your assessment.** Note the data classification, what code and data will be shared, whether PII is involved, any consent or contractual constraints, and the volume of material that will be shared with the AI tool. You will use this in [Step 3](step-3-assess-risks.md).

---

[Next: Step 3 — Assess the Risks >](step-3-assess-risks.md)
