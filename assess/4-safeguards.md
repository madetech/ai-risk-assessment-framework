# Step 4: Safeguards and Approvals

You now have a rating for each risk from [Step 3](3-identify-risks.md), and an overall inherent level that is the highest of them. This step works through three parts: **mitigate each risk that needs it**, **reassess** what is left, and **get the governance right** for the overall level.

The distinction matters. Controls are chosen risk by risk — a use that is high for data leakage and low for bias needs serious data controls, not serious everything. What the *overall* level determines is how much scrutiny the decision needs: who signs it off, and what has to be documented.

## Part A: Mitigate each risk

Take the risks you rated **Medium** or **High** in Step 3 and work through them one at a time. For each, choose controls that address that specific risk.

[Reference: Risk Catalogue](../reference/risk-catalogue.md) lists key controls under each of the eight risks. Start there, then adapt to your situation — a control that works for one team's data leakage problem may be irrelevant to yours.

Four things to hold to as you choose:

- **Target the actual risk.** "We will review the output" is not a mitigation for data leakage; the data has already gone. Say which risk each control addresses, and be honest when a control you like does not address the one that is driving your rating.
- **Say whether it cuts likelihood or impact.** Anonymising data before submitting it reduces the *likelihood* of a PII breach. A kill switch reduces the *impact* of one. You need to know which, because that is what you re-rate in Part B.
- **Only count what is additional.** If a control is already baked into your autonomy level or your tool's design, the inherent rating has counted it once. Claiming it again makes the residual look better than it is. Human review is the common case: a use scoped at *suggests* or *drafts for review* already assumes review, so what counts here is review that goes further — a second reviewer, a domain expert rather than the author, or checking against source material rather than reading through.
- **Some risks resist mitigation.** Prompt injection cannot be eliminated, and bias in historical data cannot be tested away. Where that is true, control the *consequences* instead, and say so plainly rather than claiming a reduction you have not achieved.

Whatever the ratings, these always apply: use only a tool from the register within its cleared classification ([Step 2](2-check-tool.md)), follow the relevant per-use [checklist](../reference/checklists.md), and record the assessment ([Step 5](5-record-and-work.md)).

### Additional controls where the AI acts rather than advises

These scale with **autonomy** rather than with any single risk rating, and apply on top. If you recorded an autonomy level of *acts with approval* or *acts autonomously* in [Step 1](1-scope.md#assess-the-level-of-autonomy):

- **Least privilege.** The AI's access should be the minimum the task needs. Review what it was actually granted, not what was intended — inherited service accounts and broad API tokens are the common failure.
- **A hard stop on irreversible actions.** Deleting data, changing access control, spending money, and communicating with the public should require a human decision, enforced in code rather than by instructing the AI to ask first.
- **A complete action log.** Every action the AI takes, and the identity it acted under, must be recorded somewhere a person can reconstruct afterwards. If you cannot answer "what did it do?" after the fact, you cannot investigate an incident.
- **A named accountable owner** for the AI's actions — a specific person, not a team.
- **A kill switch** that someone on shift can operate without a deployment.

## Part B: Reassess the residual risk

Go back through each risk you mitigated and re-rate its likelihood and impact **with the controls in place**. This is the residual risk. For each, ask:

- Does the control reduce the **likelihood** of this risk materialising?
- Does it reduce the **impact** if it does materialise?
- Is what remains at an acceptable level?

Use the same matrix from [Step 3](3-identify-risks.md). Your overall residual level is again the highest of the individual ratings.

**If any risk remains at "Do not proceed"**, the controls are insufficient — find stronger ones, change your approach, or do not proceed.

**If a risk has not moved**, either the control does not address it or it is not additional. Both are worth knowing: an unmoved rating is honest, an inflated one is not.

## Part C: Governance for the overall level

The overall **inherent** level sets the governance, because it reflects the seriousness of what you are dealing with. Residual risk confirms the controls are sufficient; it does not reduce what has to be signed off.

| Overall inherent risk | What is required |
| ---- | ---- |
| **Low** | Record the assessment. No approval needed beyond the tool check in Step 2 and standard team practice. |
| **Medium** | Approval from the **tech lead or delivery lead** before proceeding. Document the controls you applied and why. |
| **High** | Approval from the **SRO** or equivalent governance authority, and possibly the client — check with the delivery lead. Formal documentation: a **DPIA** if personal data is involved, a **model card or system documentation** for AI-powered product features, and an **ATRS record** if the use is in scope. Set a review date. |

An autonomy level of *acts autonomously* requires SRO approval and a review date **regardless of the overall level**, including where it is low or medium. Removing the human from each decision is a governance change, not just a technical one.

### Uses that should not proceed

Some uses should not go ahead whatever controls you apply:

- Processing SECRET or TOP SECRET data through any external AI service — a hard stop at [Step 1](1-scope.md#if-your-data-is-secret-or-above), listed here as a backstop
- Using AI to make automated decisions about individuals without meaningful human oversight, particularly in statutory contexts
- Using tools that are [excluded](2-check-tool.md#is-it-excluded) and cannot be brought into compliance
- Using AI on data where consent or contractual agreements explicitly prohibit it
- Any use the client has explicitly prohibited

If you believe an exception is justified, escalate to the SRO with a written justification. Do not proceed without explicit written approval.

Record both the inherent and residual levels, and the individual ratings behind them. You will use these in [Step 5](5-record-and-work.md).

---

[Next: Step 5 — Record and Do the Work >](5-record-and-work.md)
