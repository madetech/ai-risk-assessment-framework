# Risk Assessment: [Title]

> Copy this template to create a new risk assessment. Give it a descriptive title, e.g. "Using Copilot for unit test generation on payments service". See the [Getting Started guide](../getting-started.md) for how to set up your documentation space.

| | |
| ---- | ---- |
| **Date** | [Date] |
| **Author** | [Name] |
| **Status** | [Draft / Proposed / Approved / Rejected] |

---

## How is AI being used?

**What activity will AI assist with?**
_Be specific. "Using AI for coding" is too broad. "Using an AI coding assistant to generate unit tests for the payments service" is better._

[Description]

**Category:** [Coding / Code analysis / Product feature / Support / Research & design / General productivity]

**What will you do with the AI's output?**
_Will it go directly into production? Inform a decision? Be reviewed and edited first?_

[Description]

**Who is affected?**
_Just your team? End users? Members of the public whose data is being processed?_

[Description]

---

## What data is being shared?

**What data will be sent to or shared with the AI tool?**

[Description — e.g. source code, user research transcripts, support tickets, meeting recordings]

**Data classification:** [OFFICIAL / OFFICIAL-SENSITIVE / Other]

**Does the data contain personal information (PII)?** [Yes / No]

_If yes, describe what personal data is involved and the lawful basis for processing it:_

[Description]

**Does the data contain secrets, credentials, or API keys?** [Yes / No]

**Are there consent or contractual constraints on how this data can be processed?** [Yes / No]

_If yes, describe the constraints:_

[Description]

**Is the data commercially sensitive?** [Yes / No]

_If yes, describe:_

[Description]

---

## What are the risks?

For each risk category, rate the **likelihood** (how likely is this to happen?) and **impact** (how serious would it be if it did?) to determine the inherent risk level — the risk before any mitigations are applied.

Use: **Low**, **Medium**, **High**, or **N/A** (if genuinely not applicable to this use case — justify briefly).

See [Step 3 of the framework](../step-3-assess-risks.md) for detailed guidance on each risk category.

| Risk category | Likelihood | Impact | Inherent risk | Notes |
| ---- | ---- | ---- | ---- | ---- |
| Data leakage | | | | |
| Accuracy and hallucination | | | | |
| Accountability gaps | | | | |
| Bias and fairness | | | | |
| IP and licensing | | | | |
| Over-reliance and skill erosion | | | | |
| Supply chain and security | | | | |
| Prompt injection | | | | |

**Overall inherent risk level:** [Highest individual inherent risk rating]

---

## Which tool is being used?

**Tool name:** [e.g. GitHub Copilot Business, Claude API via AWS Bedrock]

**Is this tool on the project's approved tools list?** [Yes / No]

_If no, a tool evaluation must be completed before proceeding. See [tool evaluation template](tool-evaluation.md)._

**Does the tool meet baseline criteria for:**

| Criterion | Met? | Notes |
| ---- | ---- | ---- |
| Data residency requirements | | |
| Data retention and deletion policy | | |
| Inputs not used for model training | | |
| Security certifications | | |
| Acceptable IP/licensing terms | | |

---

## How are the risks being mitigated?

### Mitigations

Based on the inherent risk level, describe the mitigations that will be applied. See [Step 5 of the framework](../step-5-mitigate.md) for required mitigations at each risk level.

| Risk category | Mitigation | Detail |
| ---- | ---- | ---- |
| Data leakage | | |
| Accuracy and hallucination | | |
| Accountability gaps | | |
| Bias and fairness | | |
| IP and licensing | | |
| Over-reliance and skill erosion | | |
| Supply chain and security | | |
| Prompt injection | | |

### Residual risk

Re-rate each risk category with the mitigations in place.

| Risk category | Inherent risk | Residual risk |
| ---- | ---- | ---- |
| Data leakage | | |
| Accuracy and hallucination | | |
| Accountability gaps | | |
| Bias and fairness | | |
| IP and licensing | | |
| Over-reliance and skill erosion | | |
| Supply chain and security | | |
| Prompt injection | | |

**Overall residual risk level:** [Highest individual residual risk rating]

**Is the residual risk acceptable?** [Yes / No]

_If no, identify additional mitigations and reassess, or do not proceed._

---

## Approval

**Approval required:** [None (low) / Tech/Delivery Lead (medium) / SRO (high)]

| Role | Name | Decision | Date |
| ---- | ---- | ---- | ---- |
| Assessed by | | | |
| Approved by | | | |

---

## Review and learnings

_Update this section once the work is complete (see [Step 8](../step-8-share.md))._

**Issues encountered:**

[Description, or "None"]

**What worked well:**

[Description]

**What would you do differently:**

[Description]

**Were the risk level and mitigations appropriate in practice?**

[Description]

**Review date:** [Date for next review, if applicable]
