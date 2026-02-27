# Step 2: Understand What You Are Sharing

Now that you have defined what you want to do, assess what you will actually be sharing with the AI tool. This is often the single most important factor in determining what level of safeguards are needed.

Most AI uses on delivery projects involve sharing **code**, **data**, or **both**. These have different risk profiles, different legal frameworks, and different mitigations — so it is worth assessing them separately.

## Understand the code

If your AI use involves sharing source code with the tool — whether snippets during coding assistance or entire repositories during code analysis — consider the following:

**Does the code contain embedded secrets?**
API keys, credentials, database connection strings, service endpoints, and tokens are commonly found in codebases, particularly legacy ones. These are high-impact if leaked. Run a secrets scanning tool before sharing code with any AI service.

**Does the code reveal security-sensitive architecture?**
Even without secrets, source code reveals how systems are designed — authentication mechanisms, access control logic, data validation approaches, and infrastructure configuration. This information could be valuable to an attacker.

**Does the code contain proprietary business logic?**
Rules engines, pricing algorithms, eligibility calculations, and case handling logic may be commercially sensitive or operationally sensitive even if the code itself is classified as OFFICIAL.

**How much code will be shared?**
There is a significant difference between sharing a function or file (AI-assisted coding) and sharing an entire codebase (AI-assisted code analysis). The more code shared, the greater the exposure and the harder it is to manually review what the AI tool receives.

| Use type | What code is typically shared | Key concerns |
| ---- | ---- | ---- |
| **AI-assisted coding** | Code snippets, individual files, function signatures, error messages. The AI tool may also see surrounding context in the editor. | Embedded secrets in the working file or adjacent files; proprietary business logic in the immediate context |
| **AI-assisted code analysis** | Potentially the entire codebase — source code, configuration, infrastructure-as-code, build scripts, dependency manifests, database schemas | Volume is much larger. May include embedded secrets throughout, security-sensitive architecture details, and sensitive business logic across the full system. Manual review of every input is impractical. |

## Understand the data

If your AI use involves sharing data — whether user data, research data, or operational data — consider the following:

**What is the data classification?**
Government information is classified under the Government Security Classifications Policy. The classification of the data you are sharing with an AI tool is one of the key factors in determining what safeguards are needed:

| Classification | Description | AI implications |
| ---- | ---- | ---- |
| **OFFICIAL** | The majority of government information. Routine business operations and services. | AI tools that meet the criteria in [Step 4](step-4-check-tool.md) are generally appropriate, subject to the risk assessment in [Step 3](step-3-assess-risks.md). |
| **OFFICIAL-SENSITIVE** | OFFICIAL information that requires additional handling controls. Includes personal data, commercial data, and operationally sensitive information. | Cloud-hosted AI tools may be appropriate if they have strong data handling guarantees (no training on inputs, appropriate data residency, contractual protections). Requires careful assessment. Client approval likely needed. |
| **SECRET / TOP SECRET** | Information where compromise would cause serious or exceptionally grave damage. | Do not use external AI services. Any AI use must be within accredited secure environments. This is outside the scope of most delivery projects and requires specialist security guidance. |

Classification is important, but it is not the only factor. Data classified as OFFICIAL can still carry significant risks if it contains PII, is subject to consent constraints, or is commercially sensitive. The questions below help you assess these additional dimensions.

**Does the data contain personally identifiable information (PII)?**
If yes, GDPR obligations apply. You may need to conduct a Data Protection Impact Assessment (DPIA). Consider whether the data can be anonymised or pseudonymised before being processed by AI. Remember that even apparently anonymised data may be re-identifiable when combined with other information.

**Is the data subject to specific consent constraints?**
Research participant data may have been collected under consent agreements that do not cover AI processing. Check the consent forms and ethics approvals. If consent does not cover AI processing, you cannot use AI tools on that data without obtaining additional consent.

**Are there contractual restrictions on data processing?**
Client contracts may specify where data can be processed, by whom, and using what tools. Check the contract and any data handling agreements before using AI tools on client data.

**Is the data commercially sensitive?**
Business strategy, commercial terms, financial data, and operational information may be valuable to competitors or damaging if leaked. Even if not formally classified above OFFICIAL, commercial sensitivity is a real risk factor.

| Use type | What data is typically shared | Key concerns |
| ---- | ---- | ---- |
| **AI-powered product features** | User PII, case records, health or financial data — processed by the AI feature at runtime, on an ongoing basis | Data handling must be robust at scale and over time. Subject to GDPR, accessibility, and equality obligations. Users may share sensitive information unprompted. |
| **AI-assisted support** | Support tickets, error logs, screenshots, system configuration details, user contact information — often containing an unpredictable mix of sensitive content | Ticket content is inherently unpredictable: users routinely paste credentials, PII, system architecture details, and vulnerability information into support requests. Attachments and screenshots may contain visible sensitive data that is hard to automatically scan or redact. |
| **AI-assisted research & design** | Interview transcripts, survey responses, user behaviour data, demographic information | Research participant data is often highly personal. Consent constraints are common. Even anonymised data may be re-identifiable in context. |

## When both code and data are involved

Many AI uses involve both code and data, and it is important to assess each:

- **AI-assisted coding** primarily involves code, but test fixtures and seed data may contain data patterns that mirror real records. Configuration files may contain connection strings or service credentials.
- **AI-assisted code analysis** primarily involves code, but the codebase may contain embedded data — sample records in test files, real values in configuration, data migration scripts with actual content.
- **AI-powered product features** primarily involve data at runtime, but the code and prompts that define the AI feature's behaviour are also shared with the AI provider.
- **AI-assisted support** primarily involves data (ticket content, user details, operational information), but tickets frequently contain code snippets, error logs, configuration details, and system architecture information.
- **AI-assisted research & design** primarily involves data, but design artefacts may reference system behaviour or architecture.

If both code and data are involved, assess each independently and apply the more restrictive set of safeguards.

**Record your assessment.** Note the data classification, what code and data will be shared, whether PII is involved, any consent or contractual constraints, and the volume of material that will be shared with the AI tool. You will use this in [Step 3](step-3-assess-risks.md).

---

[Next: Step 3 — Assess the Risks >](step-3-assess-risks.md)
