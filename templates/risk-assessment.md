# Risk Assessment: [Title]

> Copy this template to create a new risk assessment. Give it a descriptive title, e.g. "Using Copilot for unit test generation on payments service". See the [Getting Started guide](../getting-started.md) for how to set up your documentation space.

| | |
| ---- | ---- |
| **Date** | [Date] |
| **Author** | [Name] |
| **Status** | [Draft / Proposed / Approved / Rejected] |

---

## How is AI being used?

| Question | Answer |
| ---- | ---- |
| **What activity will AI assist with?** | [Be specific. "Using AI for coding" is too broad; "using an AI coding assistant to generate unit tests for the payments service" is assessable] |
| **Which category is it?** | [Software development / Code analysis / Synthetic data generation / Product feature / User-facing support / Live service operations / User research / Design / Content / Business analysis / General productivity] |
| **What is the AI permitted to do?** | [Suggests / Drafts for review / Acts with approval / Acts autonomously. What it is _permitted_ to do, not what you intend to let it do. See [Step 1](../assess/1-scope.md#assess-the-level-of-autonomy)] |
| **What will you do with the output?** | [Straight into production? Reviewed and edited first? Informs a decision?] |
| **Who is affected?** | [Just your team? End users of the service? Members of the public whose data is processed?] |

---

## What data is being shared?

| Question | Answer |
| ---- | ---- |
| **What data will be sent to or shared with the AI tool?** | [e.g. source code, user research transcripts, support tickets, meeting recordings] |
| **What is the data classification?** | [OFFICIAL / OFFICIAL with a ‑SENSITIVE marking / Other. See [Step 1](../assess/1-scope.md#if-you-are-sharing-data)] |
| **Does it contain personal data (PII)?** | [Yes / No. If yes, what personal data is involved and the lawful basis for processing it] |
| **Does it contain secrets, credentials, or API keys?** | [Yes / No. If yes, they must be removed before anything is shared] |
| **Are there consent or contractual constraints on processing it?** | [Yes / No. If yes, what they are] |
| **Is the data commercially sensitive?** | [Yes / No. If yes, in what way] |

---

## Which tool is being used?

| Question | Answer |
| ---- | ---- |
| **Which tool will you use?** | [Name the specific tier, e.g. GitHub Copilot Business, Claude API via AWS Bedrock. Enterprise and consumer versions are different tools] |
| **Is it on the project's tool register?** | [Yes / No. If no, it must be profiled and added before use. See the [tool profile template](tool-evaluation.md)] |
| **Is it excluded?** | [Yes / No. If yes, stop] |
| **What is the highest classification it is cleared for?** | [From the profile. Is the data above at or below it? If not, escalate to the SRO] |
| **What the tool is**, the design facts your inherent ratings rest on | [From the profile, e.g. cloud-hosted, so a third party receives the data; holds standing repository access; can execute commands] |
| **What the supplier promises**, which count as mitigations, not as lower inherent risk | [From the profile, e.g. no training on inputs; UK residency; 30-day retention; IP indemnified] |

---

## Risk summary

| | |
| ---- | ---- |
| **Overall inherent risk** | [🟢 Low / 🟠 Medium / 🔴 High. The highest inherent rating below] |
| **Driven by** | [Which risks] |
| **Overall residual risk** | [🟢 Low / 🟠 Medium / 🔴 High. The highest residual rating below] |
| **Driven by** | [Which risks] |
| **Approval required** | [None (low) / SRO (medium and high)] |

| Risk | Inherent | Residual |
| ---- | ---- | ---- |
| Data leakage | | |
| Accuracy and hallucination | | |
| Accountability gaps | | |
| Bias and fairness | | |
| IP and licensing | | |
| Over-reliance and skill erosion | | |
| Supply chain and security | | |
| Prompt injection | | |

_This table is a summary. The per-risk sections below contain the detail._

---

## The risks in detail

Work through all eight risks below. Each one takes the same shape:

> **[Risk name]**
>
> [How this risk shows up in _this_ use: the specific thing that could go wrong given your scope, your data and your tool.]
>
> | Likelihood | Impact | Inherent risk |
> | ---- | ---- | ---- |
> | [Unlikely / Possible / Likely] | [Low / Medium / High] | [🟢 **Low** / 🟠 **Medium** / 🔴 **High**] |
>
> **Mitigations:**
>
> - [What you will do about this risk] _(likelihood)_
> - [What you will do about this risk] _(impact)_
>
> [What is left once those are in place, and why.]
>
> | Likelihood | Impact | Residual risk |
> | ---- | ---- | ---- |
> | [Unlikely / Possible / Likely] | [Low / Medium / High] | [🟢 **Low** / 🟠 **Medium** / 🔴 **High**] |

Step 3 shows [one risk filled in](../assess/3-assess-risks.md#what-one-assessed-risk-looks-like); the [worked examples](../reference/worked-examples.md) show six complete assessments. Four things to hold to:

- Rate the **inherent** risk on your scope and the tool's **design**, not on supplier promises, and not on mitigations you plan to apply. Use the matrix in [Step 3](../assess/3-assess-risks.md#4-calculate-the-inherent-rating).
- If the autonomy level above is _acts with approval_ or _acts autonomously_, apply the [autonomy adjustment](../assess/3-assess-risks.md#3-adjust-for-autonomy) before you calculate the inherent rating.
- Only count mitigations that are **additional** to what the inherent rating already assumed. Where the inherent rating is low, write "None needed" and move on. A low risk needs a line, not a page.
- Do not re-use a fact you already counted in the inherent rating. If the same sentence justifies both ratings, the drop is not real.

Where a risk genuinely does not apply, write **N/A** and one line saying why. Do not leave it blank.

The [risk catalogue](../reference/risk-catalogue.md) has, for each risk, how it typically shows up in your use type, the questions to ask yourself, and the key mitigations.

### Data leakage

[Complete using the shape above.]

### Accuracy and hallucination

[Complete using the shape above.]

### Accountability gaps

[Complete using the shape above.]

### Bias and fairness

[Complete using the shape above.]

### IP and licensing

[Complete using the shape above.]

### Over-reliance and skill erosion

[Complete using the shape above.]

### Supply chain and security

[Complete using the shape above.]

### Prompt injection

[Complete using the shape above.]

### Mitigations for AI that acts rather than advises

_Complete this section if the autonomy level is "acts with approval" or "acts autonomously". These scale with autonomy rather than with any single risk rating. See [Step 3](../assess/3-assess-risks.md#add-the-mitigations-that-scale-with-autonomy)._

| Mitigation | How it is implemented |
| ---- | ---- |
| **Least privilege** | |
| **Hard stop on irreversible actions** | |
| **Complete action log** | |
| **Named accountable owner** | |
| **Kill switch** | |

---

## Is the residual risk acceptable?

**[Yes / No]**

_If no, identify additional mitigations and reassess, or do not proceed. If any risk remains at "Do not proceed", the mitigations are insufficient._

---

## Approval

_Set by the overall **inherent** level, recorded in the risk summary above. See [Step 4](../assess/4-record-and-work.md#get-the-approval-the-risk-level-requires). An autonomy level of "acts autonomously" requires SRO approval regardless of the risk level._

| Role | Name | Decision | Date |
| ---- | ---- | ---- | ---- |
| Assessed by | | | |
| Approved by | | | |

**Review date:** [Date for next review, if applicable]
