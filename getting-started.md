# Getting Started: Applying This Framework to Your Project

This guide walks you through the practical steps of setting up AI governance on your project using this framework. It covers creating the documentation structure, populating it with the right templates, and running the process day-to-day.

## 1. Set up your documentation space

Create a dedicated area in your project's documentation tool (Confluence, SharePoint, Notion, or even a folder in your code repository) with the following structure:

```
AI Governance/
├── Introduction              ← Your project's AI policy (from the introduction template)
├── Approved Tools            ← Register of assessed and approved AI tools
├── Risk Assessments/         ← One page per assessed use case
│   ├── 2026-03 Copilot for unit tests
│   ├── 2026-03 Claude for architecture analysis
│   └── ...
└── Tool Evaluations/         ← One page per tool evaluated
    ├── GitHub Copilot Business
    └── ...
```

### In Confluence

1. Create a new space or a top-level page called **AI Governance** (or similar) under your project space.
2. Create child pages for each section above.
3. For **Risk Assessments** and **Tool Evaluations**, create them as parent pages — individual assessments will be added as child pages beneath them.
4. Consider using Confluence page templates (Space Settings > Content Templates) so that team members can create new risk assessments and tool evaluations with the correct structure pre-filled.

### In SharePoint

1. Create a folder in your project's document library, or a section in your project's SharePoint site.
2. Upload the templates as Word documents that team members can copy when creating new assessments.

### In a code repository

1. Create a directory (e.g. `docs/ai-governance/`) in your project repository.
2. Add the templates as markdown files.
3. This approach works well for technical teams — assessments are version-controlled, reviewable in pull requests, and close to the code.

## 2. Populate the introduction page

Copy the [introduction template](templates/introduction.md) into your documentation space and fill in the details for your project:

1. **Responsible people** — Identify who fills each role. Not every project will need all roles as separate people; on smaller teams one person may cover multiple roles. The important thing is that responsibilities are explicitly assigned.

2. **Approved tools** — If your organisation already has an approved tools list, reference or copy it. If not, this is the place to build one. Start with the tools your team is already using (or wants to use) and run each through the tool evaluation process ([Step 4](step-4-check-tool.md) and [Appendix A](appendix-a-tool-evaluation.md)).

3. **Review schedule** — Set a realistic cadence. Tying it to an existing ceremony (e.g. sprint retros, monthly team reviews) is more sustainable than creating a new meeting.

## 3. Create your first risk assessment

When someone on the team wants to use AI for a specific activity, create a new risk assessment page:

1. **Create a new page** under your Risk Assessments section. Name it descriptively, e.g. "2026-04 — Using Copilot for unit test generation on payments service".

2. **Work through Steps 1–5** of the framework, filling in each section of the risk assessment template ([Appendix B](appendix-b-risk-template.md)):
   - Define the use case (Step 1)
   - Document what data will be shared (Step 2)
   - Assess each risk category for likelihood and impact (Step 3)
   - Confirm the tool is approved or evaluate it (Step 4)
   - Identify mitigations and reassess the residual risk (Step 5)

3. **Get the required approval** based on the inherent risk level:
   - **Low** — Self-assessed, recorded
   - **Medium** — Reviewed by the Technical or Delivery Lead
   - **High** — Formal approval from the SRO

4. **Record it** (Step 6) — the assessment page itself serves as your record. Make sure it captures who assessed it, when, and what approvals were obtained.

### Tips for writing good assessments

- **Be specific.** "Using AI for coding" is not assessable. "Using GitHub Copilot to generate unit tests for the payments service, which processes OFFICIAL data including customer references" gives you something concrete to assess.
- **Don't over-engineer low-risk cases.** A low-risk assessment (e.g. using Copilot for boilerplate code with no sensitive data) can be a few lines. Save the detail for cases that need it.
- **Reuse where sensible.** If multiple team members are doing the same type of work with the same tool on the same data, one assessment can cover them all. Note who is covered.
- **Review and update.** Assessments are not set-and-forget. If the scope changes (different data, different tool, different context), revisit the assessment.

## 4. Evaluate and approve new tools

When someone wants to use a tool that is not on the approved list:

1. Create a new page under **Tool Evaluations**.
2. Use the tool evaluation template ([Appendix A](appendix-a-tool-evaluation.md)) to gather the required information.
3. Have the Technical Lead review the evaluation.
4. Submit to the SRO for approval.
5. If approved, add it to the **Approved Tools** table on the introduction page.

Do not let people use tools while the evaluation is in progress. This is one area where being strict up front avoids problems later.

## 5. Review assessments regularly

The collection of risk assessments in your documentation space is your record of AI use on the project. Review them periodically — for example during sprint retrospectives or monthly team reviews. Look for:

- **Patterns** — Are the same risks appearing repeatedly? Is a particular tool causing issues?
- **Gaps** — Is AI being used in ways that haven't been assessed?
- **Drift** — Are people still following the mitigations they committed to?
- **Staleness** — Have any assessments become outdated because the scope, data, or tooling has changed?

Update assessments after the work is complete with any issues encountered and learnings to share ([Step 8](step-8-share.md)).

## 6. Build the habit

The framework only works if people use it. Some practical ways to embed it:

- **Add it to onboarding.** When someone joins the project, point them to the introduction page and the relevant checklists for their role.
- **Make it visible.** Link to the AI Governance section from your project's main documentation page or README.
- **Keep it lightweight for low-risk cases.** If the process feels burdensome for routine use, people will skip it. A low-risk assessment should take minutes, not hours.
- **Celebrate good practice.** When someone's assessment catches a real issue, or their shared learnings help the team, acknowledge it.
- **Use retrospectives.** Review the assessments during retros. Ask: "What AI did we use this sprint? Did anything go wrong? Did anything go well?"

## 7. Scale as you learn

Start simple and add structure as you need it:

- **Week 1:** Set up the documentation space, fill in the introduction page, approve your initial tools.
- **Month 1:** Create assessments for your most common use cases.
- **Month 3:** Review how it is going. Are assessments being done? Are the risk levels calibrated right? Update the introduction page and any assessments that need revisiting.
- **Ongoing:** Share learnings across teams. Feed improvements back into the framework.

The goal is informed, proportionate AI use — not perfect paperwork. If the framework is helping your team make better decisions about AI, it is working.

---

[Back to the framework overview >](readme.md)
