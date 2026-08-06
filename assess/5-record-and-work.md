# Step 5: Record and Do the Work

You have scoped the use, identified and rated the risks, checked the tool, and determined the mitigations and approvals. This final step covers the three things that bookend the actual work: **record** your assessment, **do the work** following your checklist, and **share** what you learned.

## Record your assessment

Before starting work, save the assessment you completed in Steps 1–4 in your project's documentation space (see the [Getting Started guide](../getting-started.md) for how to set this up). **The risk assessment itself is your record** — there is no separate usage log. Its purpose is transparency, audit support, and an agreed basis for the work.

Use the [risk assessment template](../templates/risk-assessment.md) to capture:

- **Date** of the assessment, **author**, and current **status** (Draft / Proposed / Approved / Rejected)
- **Who** it covers (one person, or several doing the same type of work)
- **What** the AI will be used for, its **category** and **autonomy level**, and **what data** will be shared (Step 1)
- **Which tool** will be used (Step 3)
- **Inherent risk level** and the individual ratings (Step 2)
- **Mitigations to be applied** and the **residual risk level** (Step 4)
- **Approvals obtained** (if applicable)

## Do the work

Now use AI for the task, following the checklist for your use type in [Reference: Per-Use Checklists](../reference/checklists.md).

The checklists are structured as **before / during / after** to build good habits at each stage. They incorporate the mitigations from [Step 4](4-safeguards.md) — if your risk level requires enhanced controls, pay particular attention to the items marked **(enhanced)**.

## Share what you learned

Once the work is complete, update the assessment and share your learnings. This is how the team and organisation get better at using AI.

**Update your assessment record** with:

- Issues encountered (incorrect outputs, quality problems, unexpected behaviour)
- What worked well and what you would do differently
- Whether the risk level and mitigations were appropriate in practice

**Share with your team** at retrospectives, stand-ups, or in team channels — effective prompts and approaches others could reuse, failure modes to watch for, cases where AI output needed significant correction, and whether the risk assessment proved accurate.

**Contribute to the wider knowledge base** where relevant — add to shared documentation, update this framework if your experience reveals a gap, and feed back to the tool provider if you hit significant quality or safety issues.

For **AI-powered product features, user-facing support, and live service operations**, this is ongoing rather than one-off: regular monitoring data (accuracy, fairness, user feedback, and for operations the AI's role in incidents) should be reviewed and shared at defined intervals.

## Review your assessments periodically

Review existing risk assessments at regular intervals — for example during sprint retrospectives or monthly team reviews — to:

- Identify patterns: are the same risks recurring? Are mitigations working?
- Share learnings and update assessments as the team gains experience
- Check for drift: are people still following the framework and the mitigations they committed to?
- Check for autonomy creep: is the AI now doing more on its own than the assessment assumed — an approval step switched off, or reviews that have become perfunctory?
- Check for staleness: has any assessment become outdated because the scope, data, or tooling changed?

Your collection of risk assessments supports wider governance: if the project is audited, they evidence responsible AI use; if an incident occurs, they support investigation. The goal is to make AI use a team capability, not an individual one — the more openly teams share their experiences, including failures, the faster everyone learns to use AI effectively and safely.
