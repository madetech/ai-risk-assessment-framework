# Step 4: Approve, Record and Do the Work

You have scoped the use, checked the tool, and assessed each risk through to a residual rating. This final step covers what happens around the work itself: **get the approval** the risk level requires, **record** your assessment, **do the work** following your checklist, and **share** what you learned.

## Get the approval the risk level requires

The overall **inherent** level sets the governance, because it reflects the seriousness of what you are dealing with. Residual risk confirms the mitigations are sufficient; it does not reduce what has to be signed off.

Mitigations were chosen risk by risk in [Step 3](3-assess-risks.md) — a use that is high for data leakage and low for bias needs strong data mitigations, not strong mitigations across the board. What the *overall* level determines is how much scrutiny the decision needs: who signs it off, and what has to be documented. Your engagement should agree the sign-off approach before starting to use this framework.

| Overall inherent risk | What is required |
| ---- | ---- |
| **Low** | Record the assessment. No approval normally needed beyond the tool check in [Step 2](2-check-tool.md) and standard team practice. |
| **Medium** | Approval from the **SRO** before proceeding. Document the mitigations you applied and why. |
| **High** | Approval from the **SRO**, and possibly the client — check with the delivery lead. Formal documentation: a **DPIA** if personal data is involved, a **model card or system documentation** for product features, and an **ATRS record** if the use is in scope. Set a review date. |

An autonomy level of *acts autonomously* requires SRO approval and a review date **regardless of the overall level**, including where it is low or medium. Removing the human from each decision is a governance change, not just a technical one.

### Uses that should not proceed

Some uses should not go ahead whatever mitigations you apply:

- Processing SECRET or TOP SECRET data through any external AI service — a hard stop at [Step 1](1-scope.md#if-your-data-is-secret-or-above), listed here as a backstop
- Using AI to make automated decisions about individuals without meaningful human oversight, particularly in statutory contexts
- Using tools that are [excluded](2-check-tool.md#is-it-excluded) and cannot be brought into compliance
- Using AI on data where consent or contractual agreements explicitly prohibit it
- Any use the client has explicitly prohibited

If you believe an exception is justified, escalate to the SRO with a written justification. Do not proceed without explicit written approval.

## Record your assessment

Before starting work, save the assessment you completed in Steps 1–3 in your project's documentation space (see the [Getting Started guide](../getting-started.md) for how to set this up). **The risk assessment itself is your record** — there is no separate usage log. Its purpose is transparency, audit support, and an agreed basis for the work.

Use the [risk assessment template](../templates/risk-assessment.md) to capture:

- **Date** of the assessment, **author**, and current **status** (Draft / Proposed / Approved / Rejected)
- **What** the AI will be used for, its **category** and **autonomy level**, and **what data** will be shared (Step 1)
- **Which tool** will be used, and the facts from its profile that the ratings rest on (Step 2)
- **Each risk** — its inherent rating, the mitigations applied, and the residual rating — and the **overall inherent and residual levels** (Step 3)
- **Approvals obtained** (if applicable)

## Do the work

Now use AI for the task, following the checklist for your use type in [Reference: Per-Use Checklists](../reference/checklists.md).

The checklists are structured as **before / during / after** to build good habits at each stage. They incorporate the mitigations from [Step 3](3-assess-risks.md). Items marked **(medium and high)** apply where you rated that risk medium or high.

## Share what you learned

Once the work is complete, share what you learned. The assessment records the decision, not the experience — learnings belong with your team and, where they are worth keeping, in your project documentation.

**Share with your team** at retrospectives, stand-ups, or in team channels — effective prompts and approaches others could reuse, failure modes to watch for, cases where AI output needed significant correction, and whether the risk assessment proved accurate.

**Contribute to the wider knowledge base** where relevant — add to shared documentation, update this framework if your experience reveals a gap, and feed back to the tool provider if you hit significant quality or safety issues.

For **product features, user-facing support, and live service operations**, this is ongoing rather than one-off: regular monitoring data (accuracy, fairness, user feedback, and for operations the AI's role in incidents) should be reviewed and shared at defined intervals.

## Review your assessments periodically

Review existing risk assessments at regular intervals — for example during sprint retrospectives or monthly team reviews — to:

- Identify patterns: are the same risks recurring? Are mitigations working?
- Share learnings and update assessments as the team gains experience
- Check for drift: are people still following the framework and the mitigations they committed to?
- Check for autonomy creep: is the AI now doing more on its own than the assessment assumed — an approval step switched off, or reviews that have become perfunctory?
- Check for staleness: has any assessment become outdated because the scope, data, or tooling changed?

Your collection of risk assessments supports wider governance: if the project is audited, they evidence responsible AI use; if an incident occurs, they support investigation. Sharing experiences openly, including failures, makes AI use a team capability rather than an individual one.
