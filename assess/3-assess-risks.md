# Step 3: Assess the Risks

Not every risk matters equally for every use. Identify the risks that apply to yours, then take each one through the same short procedure: **describe** it, **rate** it, **adjust for autonomy**, **mitigate** it, and **re-rate** what is left.

Risk levels are shown throughout as 🟢 low, 🟠 medium, 🔴 high, and ⛔ do not proceed.

Finish one risk before starting the next, and record all of it together. Keeping a rating, its mitigations, and what remains in one place is what makes the assessment readable by whoever has to approve it, and it shows whether a mitigation has actually changed anything.

## What one assessed risk looks like

Before the procedure, here is what it produces. A developer wants to use a cloud-hosted coding assistant to generate unit tests for a case management service holding OFFICIAL-SENSITIVE data. Taken through the six stages below, the first of the eight risks comes out like this:

> **Data leakage**
>
> The assistant is cloud-hosted, so code leaves our estate to a third party. The tests reference data structures that mirror the real case data model, including field names for personal information. No real records are sent, but the structures reveal how sensitive cases are handled.
>
> | Likelihood | Impact | Inherent risk |
> | ---- | ---- | ---- |
> | Possible | Medium | 🟠 **Medium** |
>
> **Mitigations:**
>
> - Enterprise terms: no training on inputs, EU processing *(likelihood)*
> - Secrets scan before any file is shared *(likelihood)*
> - Review generated tests for sensitive business logic in test names and assertions. This goes beyond the ordinary review our *drafts for review* autonomy level already assumes *(likelihood)*
> - No real data values in test fixtures *(impact)*
>
> What these mitigations cut is how likely exposure is, not how bad it would be. The data model structures still reach the provider; what changes is that they are not retained or trained on, and the extra review keeps identifiable patterns out of what is sent. If they were exposed the consequence would be the same as before, so the impact rating does not move.
>
> | Likelihood | Impact | Residual risk |
> | ---- | ---- | ---- |
> | Unlikely | Medium | 🟢 **Low** |

This shows one assessed risk: the reasoning, a rating, what was done about it, and what is left. The rest of this step is the procedure that produces it, repeated for each of the eight risks. Six of the eight in this example came out low and needed a line each.

## Find the risks for your use

Find your use type (from [Step 1](1-scope.md)) in the heatmap below. The shaded cells are the risks that typically matter most for that use, so start there. Do not ignore the lighter cells entirely, but spend your effort where the risk usually concentrates.

**⬤ Typically high · ● Worth assessing · ○ Usually low**

| Use type | Data leakage | Accuracy | Accountability | Bias & fairness | IP & licensing | Over-reliance | Supply chain | Prompt injection |
| ---- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **Software development** | ● | ● | ○ | ○ | ● | ○ | ● | ● |
| **Code analysis** | ⬤ | ● | ○ | ○ | ○ | ● | ○ | ● |
| **Synthetic data generation** | ⬤ | ⬤ | ○ | ⬤ | ○ | ● | ○ | ○ |
| **Product feature** | ⬤ | ⬤ | ⬤ | ⬤ | ○ | ○ | ● | ⬤ |
| **User-facing support** | ⬤ | ● | ● | ● | ○ | ● | ● | ● |
| **Live service operations** | ⬤ | ⬤ | ● | ○ | ○ | ● | ⬤ | ⬤ |
| **User research** | ⬤ | ● | ○ | ⬤ | ○ | ● | ○ | ● |
| **Design** | ● | ● | ○ | ⬤ | ● | ● | ○ | ○ |
| **Content** | ● | ⬤ | ● | ⬤ | ● | ● | ○ | ○ |
| **Business analysis** | ● | ⬤ | ⬤ | ○ | ○ | ● | ○ | ● |
| **General productivity** | ● | ● | ○ | ○ | ○ | ● | ● | ● |

The heatmap shows *typical* starting points, not fixed ratings. Your situation may raise or lower any cell. The ratings you make below are what count.

Still assess all eight, including the ones that look quiet. A shaded cell tells you where to spend your effort, not which risks you are allowed to skip.

## Work through each risk

Take the eight risks in turn. For each one, work through these six stages.

### 1. Describe the risk in your own terms

Write a sentence or two on how this risk shows up in *this* use. Not the general definition, but the specific thing that could go wrong given your scope, your data, and your tool. "Agents paste customer emails containing addresses and case references into the assistant" is assessable. "Data could leak" is not.

[Reference: Risk Catalogue](../reference/risk-catalogue.md) gives, for each risk, how it typically manifests in your use type and the questions to ask yourself. Start there and make it specific.

If the risk genuinely does not apply, record **N/A** with one line saying why, and move on. Do not leave it blank.

### 2. Rate the likelihood and the impact

Rate both **before any mitigations**:

- **Likelihood**: unlikely, possible, or likely
- **Impact**: low, medium, or high

**Rate the design, not the promises.** A model running in your own tenancy has lower inherent data leakage than a cloud service: the data never leaves. That is the tool's **design**, and it changes the size of the risk, so it belongs here. "We don't train on your inputs", UK residency and indemnification are **promises**. They shrink a risk that already exists, so they belong at stage 5. The facts in the tool's profile ([Step 2](2-check-tool.md)) are already split along this line.

This is the distinction that keeps inherent and residual as two different numbers. Get it wrong and you will use the same fact twice: once to hold the inherent rating down, and again to justify the drop.

### 3. Adjust for autonomy

The heatmap assumes a person reviews the AI's output before it has any effect. The more the AI is allowed to do on its own, the less that assumption holds, and some risks stop being theoretical because a mistake now reaches a real system rather than a reviewer.

Take the autonomy level you recorded in [Step 1](1-scope.md#assess-the-level-of-autonomy) and apply the adjustment to the ratings you just made:

| Autonomy level | Adjustment |
| ---- | ---- |
| **Suggests** | No adjustment, because the heatmap already assumes this |
| **Drafts for review** | No adjustment, provided review is genuine and unhurried. If the artefact is large enough that review will be shallow in practice, raise **accuracy** by one likelihood step |
| **Acts with approval** | Raise **accuracy**, **accountability**, **supply chain**, and **prompt injection** by one likelihood step. A human clicking "approve" on something they did not fully read is not a mitigation |
| **Acts autonomously** | Rate **accuracy**, **accountability**, **supply chain**, and **prompt injection** as at least **High impact**, and raise **bias** by one impact step. Requires SRO approval regardless of the overall level (see [Step 4](4-record-and-work.md)) |

Note the adjustment where you apply it, so the rating shows its working. The reasoning behind these particular adjustments is at the [end of this step](#why-autonomy-moves-these-risks).

### 4. Calculate the inherent rating

Combine the likelihood and impact you have landed on:

| | **Low impact** | **Medium impact** | **High impact** |
| ---- | ---- | ---- | ---- |
| **Unlikely** | 🟢 Low | 🟢 Low | 🟠 Medium |
| **Possible** | 🟢 Low | 🟠 Medium | 🔴 High |
| **Likely** | 🟠 Medium | 🔴 High | ⛔ Do not proceed |

That is the **inherent** risk for this category, the risk before you do anything about it. Record it with the likelihood and impact that produced it, so someone reading it later can see how you got there.

### 5. Choose mitigations that address this risk

If the inherent rating is **Low**, record that no mitigation is needed and go to the next risk. For **Medium** or **High**, choose mitigations that address *this specific* risk. The [risk catalogue](../reference/risk-catalogue.md) lists key mitigations under each of the eight. Start there, then adapt to your situation.

Some things to consider:

- **Target the actual risk.** "We will review the output" is not a mitigation for data leakage; the data has already gone. Be honest when a mitigation you like does not address the risk that is driving the rating.
- **Say whether it cuts likelihood or impact.** Anonymising data before submitting it reduces the *likelihood* of a PII breach. A kill switch reduces the *impact* of one. You need to know which, because that is what you re-rate next.
- **Only count what is additional.** If a mitigation is already baked into your autonomy level or your tool's design, the inherent rating has counted it once. Human review is the common case: a use scoped at *suggests* or *drafts for review* already assumes review, so what counts here is review that goes further: a second reviewer, a domain expert rather than the author, or checking against source material rather than reading through.
- **Some risks resist mitigation.** Prompt injection cannot be eliminated, and bias in historical data cannot be tested away. Where that is true, control the *consequences* instead, and say so plainly rather than claiming a reduction you have not achieved.

### 6. Re-rate for the residual risk

Rate likelihood and impact again **with those mitigations in place**, and read the matrix a second time. That is the **residual** risk. Ask:

- Does the mitigation reduce the **likelihood** of this risk materialising?
- Does it reduce the **impact** if it does materialise?
- Is what remains at an acceptable level?

Three things to watch as you write it down:

- **Never justify the inherent and the residual rating with the same fact.** If the sentence you are writing here also appears in stage 2, you have counted it twice and the drop is not real. Writing the two a few lines apart is what makes this visible.
- **If a risk has not moved**, either the mitigation does not address it or it is not additional. Both are worth knowing: an unmoved rating is more useful than an inflated one.
- **If a risk remains at "Do not proceed"**, the mitigations are insufficient. Find stronger ones, change your approach, or do not proceed.

Then move to the next risk.

---

Whatever the ratings come out at, these always apply: use only a tool from the register within its cleared classification ([Step 2](2-check-tool.md)), follow the relevant per-use [checklist](../reference/checklists.md), and record the assessment ([Step 4](4-record-and-work.md)).

## Add the mitigations that scale with autonomy

These attach to the whole use rather than to any single risk, so apply them once, on top of the per-risk mitigations above. If you recorded an autonomy level of *acts with approval* or *acts autonomously* in [Step 1](1-scope.md#assess-the-level-of-autonomy):

- **Least privilege.** The AI's access should be the minimum the task needs. Review what it was actually granted, not what was intended. Inherited service accounts and broad API tokens are the common failure.
- **A hard stop on irreversible actions.** Deleting data, changing access control, spending money, and communicating with the public should require a human decision, enforced in code rather than by instructing the AI to ask first.
- **A complete action log.** Every action the AI takes, and the identity it acted under, must be recorded somewhere a person can reconstruct afterwards. If you cannot answer "what did it do?" after the fact, you cannot investigate an incident.
- **A named accountable owner** for the AI's actions, meaning a specific person, not a team.
- **A kill switch** that someone on shift can operate without a deployment.

## Roll up to your overall levels

Once every risk has been through the procedure, take the highest rating in each column:

- Your **overall inherent risk** is the highest inherent rating across all eight. A use that is low for data leakage but high for accuracy is a high-risk use.
- Your **overall residual risk** is the highest residual rating across all eight.

Record both, and which risks drive each. The overall **inherent** level determines the approval you need in [Step 4](4-record-and-work.md). Residual risk confirms your mitigations are sufficient; it does not reduce what has to be signed off.

## Why autonomy moves these risks

Not needed to complete the assessment, but worth knowing if you are wondering where stage 3 comes from.

**Accuracy** because autonomy does not change how often the model is wrong, which is a property of the model, but it changes whether anyone catches it. **Accountability** because there is no longer a person who chose each action, only one who configured a system. **Supply chain** because an AI permitted to act is an actor inside your systems with whatever access you granted it. **Prompt injection** because injection stops being an information-disclosure problem and becomes a remote-action problem. An attacker who can get text in front of the AI can make it do things, and the NCSC's position that injection "may never be totally mitigated" means you cannot rely on the model refusing.

**Bias moves on impact rather than likelihood**, and the reason is worth knowing: human review is a weak mitigation for bias in the first place. Bias is systematic, so each individual output looks perfectly reasonable and the pattern only appears in aggregate; the reviewer often shares it; and reviewers check whether an output is *correct*, not whether it is *fair across groups*. Removing a mitigation that was barely working does not raise the likelihood much. What autonomy changes is the consequence. A reviewer is also a rate limiter, so at scale the skew now reaches every case. An autonomous system is reliably biased in the same direction every time, where humans are inconsistently biased, and consistency is what shows up in a legal challenge. And under UK GDPR Article 22, a solely automated decision with legal or similarly significant effects is a different proposition from a human decision that AI informed.

---

[Next: Step 4, Approve, Record and Do the Work >](4-record-and-work.md)
