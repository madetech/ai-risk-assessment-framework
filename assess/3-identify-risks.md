# Step 3: Identify the Risks

Not every risk matters equally for every use. The goal of this step is to quickly find the risks that are **relevant to your use**, then rate those by likelihood and impact to arrive at an inherent risk level — the risk before any mitigations are applied.

Work in four stages: **identify your risks** using the heatmap, **rate** each of them, **adjust for autonomy**, and **take the highest rating** as your overall inherent risk.

## 1. Identify your risks

Find your use type (from [Step 1](1-scope.md)) in the heatmap below. The shaded cells are the risks that typically matter most for that use — start there. Do not ignore the lighter cells entirely, but spend your effort where the risk usually concentrates.

**⬤ Typically high · ● Worth assessing · ○ Usually low**

| Use type | Data leakage | Accuracy | Accountability | Bias & fairness | IP & licensing | Over-reliance | Supply chain | Prompt injection |
| ---- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **Coding** | ● | ● | ○ | ○ | ● | ○ | ● | ● |
| **Code analysis** | ⬤ | ● | ○ | ○ | ○ | ● | ○ | ● |
| **Synthetic data** | ⬤ | ⬤ | ○ | ⬤ | ○ | ● | ○ | ○ |
| **Product feature** | ⬤ | ⬤ | ⬤ | ⬤ | ○ | ○ | ● | ⬤ |
| **User-facing support** | ⬤ | ● | ● | ● | ○ | ● | ● | ● |
| **Live service operations** | ⬤ | ⬤ | ● | ○ | ○ | ● | ⬤ | ⬤ |
| **User research** | ⬤ | ● | ○ | ⬤ | ○ | ● | ○ | ● |
| **Design** | ● | ● | ○ | ⬤ | ● | ● | ○ | ○ |
| **Content** | ● | ⬤ | ● | ⬤ | ● | ● | ○ | ○ |
| **Business analysis** | ● | ⬤ | ⬤ | ○ | ○ | ● | ○ | ● |
| **Productivity** | ● | ● | ○ | ○ | ○ | ● | ● | ● |

The heatmap shows *typical* starting points, not fixed ratings. Your specific situation may raise or lower any cell — the ratings in the next move are what count.

## 2. Rate each risk

For each risk that is live for your use, read the one-paragraph definition below, ask yourself the questions, and rate the **likelihood** (how likely is this to happen?) and **impact** (how serious if it did?) **before any mitigations**. For the full detail on how each risk shows up per use type, and the controls that reduce it, see [Reference: Risk Catalogue](../reference/risk-catalogue.md).

### Rate the design, not the promises

A model running in your own tenancy has lower inherent data leakage than a cloud service — the data never leaves. That is the tool's **design**, and it changes the size of the risk.

"We don't train on your inputs", UK residency, indemnification — are **promises**. They shrink a risk that already exists, so they belong in [Step 4](4-safeguards.md).

### Data leakage
Sensitive data sent to a third-party AI service is exposed, retained, used for training, or otherwise leaves your control — via prompts, context windows, uploaded files, or metadata.
- What will actually be sent? Have you checked for embedded secrets or PII?
- Does the provider retain or train on your inputs? Where is data processed geographically?
- What would the impact be if this data were exposed?

### Accuracy and hallucination
AI produces output that is plausible and confident but factually incorrect, logically flawed, or subtly misleading. This is inherent to current AI, not an occasional bug.
- What is the consequence if the output is wrong — minor inconvenience, or harm to individuals?
- Will a qualified human review the output before it is acted on?
- Can the output be validated against a source of truth, and how easily would errors be detected?

### Accountability gaps
When AI contributes to an output or decision, the chain of responsibility can become unclear — a particular concern given statutory duties and public accountability in government.
- Is there a named individual accountable for the AI-assisted output?
- Will it be clear to stakeholders that AI was involved, and is there an audit trail?
- If something goes wrong, is the escalation path clear?

### Bias and fairness
AI can reflect, amplify, or introduce biases from its training data, leading to discriminatory outcomes that may breach the Equality Act 2010 and the public sector equality duty.
- Could the output treat different groups of people differently?
- Has it been tested with diverse inputs representative of the actual user population?
- Are protected characteristics (age, disability, gender, race, etc.) in play, and how would you detect bias?

### Intellectual property and licensing
The legal status of AI-generated content is uncertain. AI outputs may incorporate training-data material with unclear licensing, and copyright ownership is unresolved.
- Will AI-generated code enter a codebase with specific licensing requirements?
- Does the provider offer IP indemnification?
- Is provenance important, and could AI-generated content create legal exposure?

### Over-reliance and skill erosion
Teams become dependent on AI in ways that erode critical thinking, core competencies, and the ability to work without it. Research links higher AI reliance to reduced critical thinking.
- Could the team still do this work effectively without the AI tool?
- Are junior team members developing foundational skills alongside AI use?
- Is AI augmenting human capability, or replacing it? Would anyone notice if the output were subtly wrong?

### Supply chain and security
AI tools and their outputs can introduce vulnerabilities, malicious dependencies, or compromised packages; the AI service itself becomes part of your supply chain.
- Will AI-generated code get the same security review as human-written code?
- Are AI-suggested dependencies verified against vulnerability databases?
- Is the AI tool itself a risk (access to code/data, exfiltration potential)? What if the service changes behaviour or goes down?

### Prompt injection
Adversarial content — in code, documents, tickets, or user inputs — can manipulate the AI into ignoring instructions, revealing information, or taking unintended actions. Ranked #1 on the OWASP Top 10 for LLM Applications (2025); the NCSC warns it "may never be totally mitigated."
- What untrusted content will the AI process? Could any of it be crafted to manipulate the AI?
- If injection succeeds, what is the worst that could happen — can the AI access data, take actions, or bypass human review?
- Are there deterministic safeguards (enforced in code, not by the AI), and has the system been tested adversarially?

## 3. Adjust for autonomy

The heatmap assumes a person reviews the AI's output before it has any effect. The more the AI is allowed to do on its own, the less that assumption holds, and some risks stop being theoretical because a mistake now reaches a real system rather than a reviewer.

Take the autonomy level you recorded in [Step 1](1-scope.md#assess-the-level-of-autonomy) and apply the adjustment:

| Autonomy level | Adjustment |
| ---- | ---- |
| **Suggests** | No adjustment — the heatmap already assumes this |
| **Drafts for review** | No adjustment, provided review is genuine and unhurried. If the artefact is large enough that review will be shallow in practice, raise **accuracy** by one likelihood step |
| **Acts with approval** | Raise **accuracy**, **accountability**, **supply chain**, and **prompt injection** by one likelihood step. A human clicking "approve" on something they did not fully read is not a control |
| **Acts autonomously** | Rate **accuracy**, **accountability**, **supply chain**, and **prompt injection** as at least **High impact**, and raise **bias** by one impact step. Requires SRO approval regardless of the overall level (see [Step 4](4-safeguards.md)) |

Why these. **Accuracy** because autonomy does not change how often the model is wrong — that is a property of the model — but it changes whether anyone catches it. **Accountability** because there is no longer a person who chose each action, only one who configured a system. **Supply chain** because an AI permitted to act is an actor inside your systems with whatever access you granted it. **Prompt injection** because injection stops being an information-disclosure problem and becomes a remote-action problem — an attacker who can get text in front of the AI can make it do things, and the NCSC's position that injection "may never be totally mitigated" means you cannot rely on the model refusing.

**Bias moves on impact rather than likelihood**, and the reason is worth knowing: human review is a weak control for bias in the first place. Bias is systematic, so each individual output looks perfectly reasonable and the pattern only appears in aggregate; the reviewer often shares it; and reviewers check whether an output is *correct*, not whether it is *fair across groups*. Removing a control that was barely working does not raise the likelihood much. What autonomy changes is the consequence. A reviewer is also a rate limiter, so at scale the skew now reaches every case. An autonomous system is reliably biased in the same direction every time, where humans are inconsistently biased — and consistency is what shows up in a legal challenge. And under UK GDPR Article 22, a solely automated decision with legal or similarly significant effects is a different proposition from a human decision that AI informed.

## 4. Determine your inherent risk level

Rate each live risk using the matrix:

| | **Low impact** | **Medium impact** | **High impact** |
| ---- | ---- | ---- | ---- |
| **Unlikely** | Low risk | Low risk | Medium risk |
| **Possible** | Low risk | Medium risk | High risk |
| **Likely** | Medium risk | High risk | Do not proceed |

Your **overall inherent risk level is the highest rating across all categories.** A use that is low risk for data leakage but high risk for accuracy is a high-risk use overall.

Record your inherent risk assessment — the overall level and the individual ratings. You will use it in [Step 4: Safeguards and Approvals](4-safeguards.md) to determine proportionate mitigations, then reassess the residual risk. A blank [risk assessment template](../templates/risk-assessment.md) is provided.

---

[Next: Step 4 — Safeguards and Approvals >](4-safeguards.md)
