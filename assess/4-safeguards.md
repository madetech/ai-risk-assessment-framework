# Step 4: Safeguards and Approvals

You now have an inherent risk level from [Step 3](3-identify-risks.md) — the risk before any mitigations. This step has three parts: determine mitigations proportionate to that inherent risk, apply them, and reassess the residual risk to confirm they are sufficient. It ends with the required approvals.

## Part A: Determine mitigations based on the inherent risk level

The principle is proportionality: higher inherent risk requires more rigorous controls.

**Inherent risk: Low**

- Confirm the tool is on the register and cleared for your data's classification (see [Step 2](2-check-tool.md))
- Human review of all AI outputs before they are used, committed, or acted upon — **but only count this as a mitigation if it goes beyond what your autonomy level already assumes.** A use scoped at *suggests* or *drafts for review* has review built into its inherent rating, so claiming it again here counts it twice and makes the residual look better than it is. What does count is review that is genuinely additional: a second reviewer, a domain expert rather than the author, or review against the source material rather than a read-through
- Record the AI use as a risk assessment (see [Step 5](5-record-and-work.md))
- Follow the relevant per-use [checklist](../reference/checklists.md)
- Comply with data handling policies — do not share data above the classification the tool is cleared for

No additional approval is required beyond the tool check in Step 2 and following standard team practices.

**Inherent risk: Medium**

All low-risk mitigations, plus:

- Specific additional controls determined by the risk assessment — for example: anonymise or redact sensitive data before submitting; enhanced code review for security-sensitive areas; peer review of AI-assisted research findings against source material; additional testing or validation of outputs
- Approval from the **tech lead or delivery lead** before proceeding
- Document the specific enhanced controls being applied and why

**Inherent risk: High**

All medium-risk mitigations, plus:

- Formal documentation:
  - **Data Protection Impact Assessment (DPIA)** if personal data is involved
  - **Model card or system documentation** for AI-powered product features
  - **ATRS record** if the use falls within the scope of the Algorithmic Transparency Recording Standard
- Approval from the **senior responsible owner** or equivalent governance authority
- **Client approval** may be required — check with the delivery lead
- A defined review date to reassess the risk level and mitigations

**Inherent risk: Do not proceed**

Some uses should not proceed regardless of mitigations, including:

- Processing SECRET or TOP SECRET data through any external AI service — a hard stop at [Step 1](1-scope.md#if-your-data-is-secret-or-above), listed here as a backstop
- Using AI to make automated decisions about individuals without meaningful human oversight, particularly in statutory contexts
- Using tools that are [excluded](2-check-tool.md#is-it-excluded) and cannot be brought into compliance
- Using AI on data where consent or contractual agreements explicitly prohibit it
- Any use the client has explicitly prohibited

If you believe an exception is justified, escalate to the senior responsible owner with a written justification. Do not proceed without explicit written approval.

### Additional controls where the AI acts rather than advises

The mitigations above scale with the risk level. These scale with **autonomy**, and apply on top, regardless of the risk level. If you recorded an autonomy level of "acts with approval" or "acts autonomously" in [Step 1](1-scope.md#assess-the-level-of-autonomy):

- **Least privilege.** The AI's access should be the minimum the task needs. Review what it was actually granted, not what was intended — inherited service accounts and broad API tokens are the common failure.
- **A hard stop on irreversible actions.** Deleting data, changing access control, spending money, and communicating with the public should require a human decision, enforced in code rather than by instructing the AI to ask first.
- **A complete action log.** Every action the AI takes, and the identity it acted under, must be recorded somewhere a person can reconstruct afterwards. If you cannot answer "what did it do?" after the fact, you cannot investigate an incident.
- **A named accountable owner** for the AI's actions — a specific person, not a team.
- **A kill switch** that someone on shift can operate without a deployment.

For **"acts autonomously"**, SRO approval is required regardless of the overall risk level, along with a defined review date. Removing the human from each decision is a governance change, not just a technical one, and should be decided at that level.

## Part B: Reassess the residual risk

With the mitigations identified, go back through each risk category and re-rate the likelihood and impact **with the mitigations in place**. This is the residual risk. For each category, ask:

- Does this mitigation reduce the **likelihood** of the risk materialising? (e.g. anonymising data before processing reduces the likelihood of a PII breach)
- Does this mitigation reduce the **impact** if it does materialise? (e.g. a domain expert checking outputs against source material limits the impact of hallucination)
- Is the residual risk now at an acceptable level?
- **Is this mitigation genuinely additional**, or is it something the inherent rating already assumed? Anything baked into your autonomy level or your tool's design has already been counted, and counting it again inflates the improvement.

Use the same risk matrix from [Step 3](3-identify-risks.md) to determine the residual level for each category and overall.

**If the residual risk for any category remains at "Do not proceed"**, the mitigations are insufficient — identify stronger mitigations, change your approach, or do not proceed.

**If the residual risk is no lower than the inherent risk**, the mitigations are not adding value — reconsider whether the right mitigations have been chosen, or whether the risk genuinely cannot be reduced.

## Part C: Obtain approvals

Approvals are determined by the **inherent** risk level — because it reflects the seriousness of what you are dealing with and the rigour of governance needed. The residual risk confirms the mitigations are sufficient but does not reduce the approval requirements. An autonomy level of "acts autonomously" requires SRO approval even where the inherent risk is low or medium.

Record both the inherent and residual risk levels. You will use these in [Step 5](5-record-and-work.md).

---

[Next: Step 5 — Record and Do the Work >](5-record-and-work.md)
