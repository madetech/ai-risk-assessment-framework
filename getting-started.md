# Getting Started: Applying This Framework to Your Project

This guide walks you through the practical steps of setting up AI governance on your project using this framework. It covers creating the documentation structure, populating it with the right templates, and running the process day-to-day.

## 1. Set up your documentation space

Create a dedicated area in your project's documentation tool (Confluence, SharePoint, Notion, or even a folder in your code repository) with the following structure:

```
AI Governance/
├── Introduction              ← Your project's AI policy (from the introduction template)
├── Tool Register             ← Profiles of the AI tools that have been assessed
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
3. For **Risk Assessments** and **Tool Evaluations**, create them as parent pages. Individual assessments will be added as child pages beneath them.
4. Consider using Confluence page templates (Space Settings > Content Templates) so that team members can create new risk assessments and tool profiles with the correct structure pre-filled.

### In SharePoint

1. Create a folder in your project's document library, or a section in your project's SharePoint site.
2. Upload the templates as Word documents that team members can copy when creating new assessments.

### In a code repository

1. Create a directory (e.g. `docs/ai-governance/`) in your project repository.
2. Add the templates as markdown files.
3. This approach works well for technical teams, because assessments are version-controlled, reviewable in pull requests, and close to the code.

## 2. Populate the introduction page

Copy the [introduction template](templates/introduction.md) into your documentation space and fill in the details for your project:

1. **Responsible people.** Identify who fills each role. Not every project will need all roles as separate people; on smaller teams one person may cover multiple roles. The important thing is that responsibilities are explicitly assigned.

2. **Tool register.** If your organisation already has an approved AI tools list, reference or copy it, but record what each tool actually *does* rather than just that it is on the list. If there is no list, this is the place to build one. Start with the tools your team is already using (or wants to use) and write a profile for each ([Step 2](assess/2-check-tool.md) and [tool profile template](templates/tool-evaluation.md)).

3. **Review schedule.** Set a realistic cadence. Tying it to an existing ceremony (e.g. sprint retros, monthly team reviews) is more sustainable than creating a new meeting.

## 3. Create your first risk assessment

When someone on the team wants to use AI for a specific activity, create a new risk assessment page:

1. **Create a new page** under your Risk Assessments section using the [risk assessment template](templates/risk-assessment.md). Name it descriptively, e.g. "2026-04: Using Copilot for unit test generation on payments service".

2. **Work through each section** of the template, using the framework for detailed guidance:
   - Scope the use, defining it and assessing what code and data you will share (Step 1)
   - Check the tool is on the register, not excluded, and cleared for your classification, or profile it (Step 2)
   - Assess the risks, finding them with the heatmap, then take each one through inherent rating, mitigations, and residual rating (Step 3)
   - Get approval, record the assessment, and do the work (Step 4)

3. **Get the required approval** based on the overall inherent risk level:
   - **Low**: self-assessed, recorded
   - **Medium**: approval from the SRO
   - **High**: approval from the SRO, with formal documentation
   - Any use where the AI **acts autonomously**: SRO approval regardless of the risk level

4. **Record it** (Step 4). The assessment page itself serves as your record. Make sure it captures who assessed it, when, and what approvals were obtained.

### Tips for writing good assessments

- **Be specific.** "Using AI for coding" is not assessable. "Using GitHub Copilot to generate unit tests for the payments service, which processes OFFICIAL data including customer references" gives you something concrete to assess.
- **Don't over-engineer low-risk cases.** A low-risk assessment (e.g. using Copilot for boilerplate code with no sensitive data) can be a few lines. Save the detail for cases that need it.
- **Reuse where sensible.** If multiple team members are doing the same type of work with the same tool on the same data, one assessment can cover them all. Note who is covered.
- **Review and update.** If the scope changes (different data, different tool, different context), revisit the assessment.

## 4. Evaluate and approve new tools

When someone wants to use a tool that is not on the register, or needs a wider envelope than an existing entry allows:

1. Create a new page under **Tool Evaluations**.
2. Use the [tool profile template](templates/tool-evaluation.md) to gather the facts.
3. Have the Technical Lead review the evaluation.
4. Submit to the SRO for approval.
5. If signed off, add it to the **Tool register** on the introduction page, with a link to its full profile and the highest classification it is cleared for.

Do not let people use tools while the evaluation is in progress.

## 5. Review assessments regularly

The collection of risk assessments in your documentation space is your record of AI use on the project. Review them periodically, for example during sprint retrospectives or monthly team reviews. Look for:

- **Patterns.** Are the same risks appearing repeatedly? Is a particular tool causing issues?
- **Gaps.** Is AI being used in ways that haven't been assessed?
- **Drift.** Are people still following the mitigations they committed to?
- **Staleness.** Have any assessments become outdated because the scope, data, or tooling has changed?

Share what you learned once the work is complete, and revisit the assessment if the scope, data, or tooling has changed ([Step 4](assess/4-record-and-work.md)).

## 6. Build the habit

The framework only works if people use it. Some practical ways to embed it:

- **Add it to onboarding.** When someone joins the project, point them to the introduction page and the relevant checklists for their role.
- **Make it visible.** Link to the AI Governance section from your project's main documentation page or README.
- **Keep it lightweight for low-risk cases.** If the process feels burdensome for routine use, people will skip it. A low-risk assessment should take minutes, not hours.
- **Recognise good practice.** When someone's assessment catches a real issue, or their shared learnings help the team, acknowledge it.
- **Use retrospectives.** Review the assessments during retros. Ask: "What AI did we use this sprint? Did anything go wrong? Did anything go well?"

---

[Back to the framework overview >](readme.md)
