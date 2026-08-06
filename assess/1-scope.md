# Step 1: Scope Your Use

Before assessing risks or choosing tools, describe precisely what you want to do and what you would share with the AI tool. Being specific here makes the rest of the assessment straightforward — a vague scope cannot be assessed.

This step has three parts: **define** the use, **assess the level of autonomy**, and **understand what you are sharing**.

## Define what you want to do

Answer these three questions:

1. **What activity will AI assist with?** Be specific. "Using AI for coding" is too broad. "Using an AI coding assistant to generate unit tests for the payments service" is better.

2. **What data will be involved?** What will you send to or share with the AI tool? Source code, user research transcripts, database schemas, support tickets, design briefs?

3. **Who is affected?** Just you and your team? End users of the service? Members of the public whose data is being processed?

## Categorise your use

The categories below describe **tasks people do while delivering a service**, not the services themselves — with one exception, AI-powered product features, which covers AI you build *into* the service.

Most AI use falls into one of eleven categories. Some uses span more than one — if so, assess against each and apply the more restrictive safeguards.

**These categories are a thinking aid, not an exhaustive taxonomy.** Their job is to get you to the right risks quickly by pointing at the closest well-understood shape of work. There is no prize for classifying correctly. If your use does not fit neatly, pick the nearest one or two, note why the fit is imperfect, and carry on — what matters is that you assess the right risks, not that you chose the right label. If you are doing something the categories genuinely do not describe, work through [Step 3](3-identify-risks.md) on its merits and [feed the gap back](5-record-and-work.md) so the framework can catch up.

| Category | The key characteristic |
| ---- | ---- |
| **AI-assisted coding** | AI generates or modifies code that may end up in the product |
| **AI-assisted code analysis** | Large volumes of existing code are sent to the AI; the output is analytical, not production code |
| **AI-assisted synthetic data generation** | AI produces artificial data that will be handled as though it were safe |
| **AI-powered product features** | AI directly interacts with or affects end users of the service |
| **AI-assisted user-facing support** | AI processes support data to help the team respond to requests from people |
| **AI-assisted live service operations** | AI works against production systems — alerts, incidents, logs, infrastructure |
| **AI-assisted user research** | AI processes what real people told you, to represent them to the team |
| **AI-assisted design** | AI shapes how the service works and how people move through it |
| **AI-assisted content** | AI produces text that reaches the public in the department's name |
| **AI-assisted business analysis** | AI produces requirements or decision artefacts that others treat as settled reasoning |
| **AI-assisted general productivity** | AI assists with routine work tasks that do not shape a decision |

For the full description of each category — the tools typically used, what is shared, and the typical risk fingerprint — see [Reference: Use-Type Profiles](../reference/use-type-profiles.md). (That reference also explains the underlying types of AI: GenAI, LLMs, ML, and NLP.)

## Assess the level of autonomy

Two teams can use the same tool on the same data in the same category and face very different risks, because of how much the AI is allowed to do on its own. Autonomy cuts across every category, so record it separately.

Pick the level that matches what the AI is actually permitted to do:

| Level | What it means | Example |
| ---- | ---- | ---- |
| **Suggests** | AI proposes; a person decides and does the work themselves | Inline code completion; a list of possible root causes |
| **Drafts for review** | AI produces a complete artefact that a person reviews and edits before it takes effect | A generated pull request; a drafted support response awaiting agent approval |
| **Acts with approval** | AI performs actions in a real system, but each action needs explicit human approval first | An agent that runs commands or edits files with per-action confirmation |
| **Acts autonomously** | AI performs actions in a real system with no human in the loop for each action | Automated ticket closure; auto-remediation of an alert |

Two things to be careful about. First, **the level is what the AI is permitted to do, not what you intend to let it do** — if the approval prompt can be turned off, or a "yes to all" option exists and gets used under pressure, assess at the higher level. Second, **autonomy tends to creep**: a tool introduced at *drafts for review* acquires an auto-apply setting, or a team that reviewed every suggestion in week one stops by week six. Note the level you assessed, and reassess if the way the tool is used changes.

You will use this in [Step 3](3-identify-risks.md), where higher autonomy raises specific risks, and in [Step 4](4-safeguards.md), where fully autonomous action requires SRO approval regardless of the overall risk level.

## Understand what you are sharing

What you share with the AI tool is often the single most important factor in determining what safeguards are needed. Most uses involve **code**, **data**, or **both** — assess each, because they have different risk profiles.

### If you are sharing code

> 🛑 **Secrets must NEVER be shared with any AI tool.** API keys, credentials, tokens, database connection strings, and service endpoints must be removed before any code is shared. Run a secrets scanning tool before sharing code with any AI service. If you find secrets, remove them and re-evaluate what you should share.

Beyond secrets, consider:

- **Does the code reveal security-sensitive architecture?** Authentication mechanisms, access control logic, data validation, and infrastructure configuration could be valuable to an attacker.
- **Does the code contain proprietary business logic?** Rules engines, pricing algorithms, and eligibility calculations may be commercially or operationally sensitive even if classified as OFFICIAL.
- **How much code will be shared?** There is a significant difference between a single function (coding assistance) and an entire codebase (code analysis). The more code, the greater the exposure and the harder it is to review what the tool receives.

### If you are sharing data

**What is the data classification?** This is a hard gate. The Government Security Classifications Policy classifies government information as follows:

| Classification | AI implications |
| ---- | ---- |
| **OFFICIAL** | AI tools that meet the [tool criteria](../reference/tool-criteria.md) are generally appropriate, subject to the risk assessment in [Step 3](3-identify-risks.md). |
| **OFFICIAL-SENSITIVE** | Only tools formally assessed and approved for OFFICIAL-SENSITIVE data may be used. Do not make this assessment yourself — if the tool has not been approved for this level, escalate to the SRO before proceeding. Client approval is likely needed. |
| **SECRET / TOP SECRET** | 🛑 Do not use external AI services. Any AI use must be within accredited secure environments. This is outside the scope of most delivery projects and requires specialist security guidance. |

Classification is not the only factor. OFFICIAL data can still carry significant risk. Also ask:

- **Does the data contain PII?** If yes, UK GDPR applies and you may need a DPIA. Consider whether data can be fully anonymised first. **Pseudonymised data is still personal data** — only fully anonymised data falls outside GDPR. If unsure, treat it as personal data, and confirm the proposed use with your Data Protection Officer before sharing.
- **Is the data subject to consent constraints?** Research participant data may have been collected under consent that does not cover AI processing. Check consent forms and ethics approvals. If consent does not cover AI, you cannot use AI on that data without obtaining it.
- **Are there contractual restrictions?** Client contracts may specify where data can be processed, by whom, and with what tools. Check before using AI on client data.
- **Is the data commercially sensitive?** Business strategy, commercial terms, and financial data may be damaging if leaked, even if not classified above OFFICIAL.

### When both code and data are involved

Many uses involve both — for example, code analysis on a codebase that contains sample records, or a product feature whose defining prompts are shared alongside user data at runtime. Assess each independently and apply the more restrictive set of safeguards. See [Reference: Use-Type Profiles](../reference/use-type-profiles.md) for how code and data typically combine in each use type.

**Record your scope.** Note what the AI will be used for, its category, its autonomy level, what code and data will be shared, the data classification, whether PII is involved, and any consent or contractual constraints. You will use all of this in [Step 2](2-check-tool.md) and [Step 3](3-identify-risks.md).

---

[Next: Step 2 — Check the Tool Is Eligible >](2-check-tool.md)
