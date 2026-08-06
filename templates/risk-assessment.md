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

**Category:** [Coding / Code analysis / Synthetic data generation / Product feature / User-facing support / Live service operations / User research / Design / Content / Business analysis / General productivity]

**Autonomy level:** [Suggests / Drafts for review / Acts with approval / Acts autonomously]
_What is the AI permitted to do, not what you intend to let it do. See [Step 1](../assess/1-scope.md#assess-the-level-of-autonomy)._

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

See [Step 2 of the framework](../assess/3-identify-risks.md) for guidance on identifying and rating each risk, and the [risk catalogue](../reference/risk-catalogue.md) for detail on each category. If the autonomy level above is "acts with approval" or "acts autonomously", apply the autonomy adjustment in Step 2 before recording these ratings.

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

**Is this tool on the project's tool register?** [Yes / No]

_If no, a profile must be completed and the tool added to the register before proceeding. See [tool profile template](tool-evaluation.md)._

**Is it excluded?** [Yes / No] — _if yes, stop._

**Highest classification cleared:** [From the profile] — _is the data in this assessment at or below it? If not, escalate to the SRO._

**The facts that matter for this use.** Pull these from the tool's profile. They are not a permission to proceed — they are what the risk ratings below are based on.

| | From the profile | Why it matters here |
| ---- | ---- | ---- |
| **What the tool is** (design — feeds inherent risk) | [e.g. cloud-hosted, third party receives the data; holds standing repository access; can execute commands] | |
| **What the supplier promises** (terms — count as mitigations) | [e.g. no training on inputs; UK residency; 30-day retention; IP indemnified] | |

_If anything in the profile does not fit what you are doing, that is not a blocker in itself — it is an input to the risk ratings below, and may call for extra mitigations in Step 4._

---

## How are the risks being mitigated?

### Mitigations

Based on the inherent risk level, describe the mitigations that will be applied. See [Step 4 of the framework](../assess/4-safeguards.md) for required mitigations at each risk level.

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

_An autonomy level of "acts autonomously" requires SRO approval regardless of the risk level._

| Role | Name | Decision | Date |
| ---- | ---- | ---- | ---- |
| Assessed by | | | |
| Approved by | | | |

---

## Review and learnings

_Update this section once the work is complete (see [Step 5](../assess/5-record-and-work.md))._

**Issues encountered:**

[Description, or "None"]

**What worked well:**

[Description]

**What would you do differently:**

[Description]

**Were the risk level and mitigations appropriate in practice?**

[Description]

**Review date:** [Date for next review, if applicable]
