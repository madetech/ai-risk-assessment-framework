# Step 5: Mitigate Risks and Reassess

You now have an inherent risk level from [Step 3](step-3-assess-risks.md) — the risk before any mitigations are applied. This step has three parts: determine mitigations proportionate to the inherent risk, apply them, and then reassess the residual risk to confirm the mitigations are sufficient.

## Part A: Determine mitigations based on the inherent risk level

The principle is proportionality: higher inherent risk requires more rigorous controls.

**Inherent risk: Low**

Required mitigations:

- Confirm the AI tool is on the approved tools list (see [Step 4](step-4-check-tool.md))
- Human review of all AI outputs before they are used, committed, or acted upon
- Record the AI use in the project's AI usage log (see [Step 6](step-6-record.md))
- Follow the relevant per-use checklist in [Step 7](step-7-checklists.md)
- Comply with the project's data handling policies — do not share data beyond the classification level the tool has been approved for

No additional approval required beyond confirming the tool is approved and following standard team practices.

**Inherent risk: Medium**

All low-risk mitigations apply, plus:

- Specific additional controls determined by the risk assessment — for example:
  - Anonymise or redact sensitive data before submitting to the AI tool
  - Enhanced code review for security-sensitive areas (second pair of eyes, security-focused review)
  - Peer review of AI-assisted research findings against source material
  - Additional testing or validation of AI outputs
- Approval from the **tech lead or delivery lead** before proceeding
- Document the specific enhanced controls being applied and why

**Inherent risk: High**

All medium-risk mitigations apply, plus:

- Formal documentation:
  - **Data Protection Impact Assessment (DPIA)** if personal data is involved
  - **Model card or system documentation** for AI-powered product features
  - **ATRS record** if the AI use falls within the scope of the Algorithmic Transparency Recording Standard
- Approval from the **senior responsible owner** or equivalent governance authority
- **Client approval** may be required — check with the delivery lead
- A defined review date to reassess the risk level and mitigations

**Inherent risk: Do not proceed**

Some uses of AI should not proceed regardless of mitigations. Examples include:

- Processing SECRET or TOP SECRET data through any external AI service
- Using AI to make automated decisions about individuals without meaningful human oversight, particularly in statutory contexts
- Using AI tools that do not meet the baseline criteria in [Step 4](step-4-check-tool.md) and cannot be brought into compliance
- Using AI on data where consent or contractual agreements explicitly prohibit it
- Any use where the client has explicitly prohibited AI

If you believe an exception is justified, escalate to the senior responsible owner with a written justification. Do not proceed without explicit written approval.

## Part B: Reassess the residual risk

With the mitigations identified, go back through each risk category and re-rate the likelihood and impact **with the mitigations in place**. This is the residual risk — the risk that remains after safeguards are applied.

For each risk category, ask:

- Does this mitigation reduce the **likelihood** of the risk materialising? (e.g. anonymising data before AI processing reduces the likelihood of a PII breach)
- Does this mitigation reduce the **impact** if the risk does materialise? (e.g. human review of all AI outputs limits the impact of hallucination)
- Is the residual risk now at an acceptable level?

Use the same risk matrix from [Step 3](step-3-assess-risks.md) to determine the residual risk level for each category and the overall residual risk.

**If the residual risk for any category remains at "Do not proceed"**, the mitigations are insufficient. You must either identify stronger mitigations, change your approach, or not proceed.

**If the residual risk is no lower than the inherent risk**, the mitigations are not adding value. Reconsider whether the right mitigations have been identified, or whether the risk genuinely cannot be reduced.

## Part C: Obtain approvals

Approvals are determined by the **inherent** risk level — because the inherent risk reflects the seriousness of what you are dealing with and determines the rigour of governance needed. The residual risk confirms whether the mitigations are sufficient, but does not reduce the approval requirements.

Record both the inherent and residual risk levels. You will use these in [Step 6](step-6-record.md).

---

[Next: Step 6 — Record Your Assessment >](step-6-record.md)
