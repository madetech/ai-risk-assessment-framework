# A Practical Risk-Based Approach to the Use of AI in Projects

This is a practical framework for delivery teams to decide **whether and how** to use AI for a specific activity on a government IT project. It is not about preventing AI use — used well, AI tools can significantly improve the quality and efficiency of delivery work. It is about making informed decisions: understanding the risks and applying proportionate safeguards.

It covers the full range of AI use teams encounter: **coding**, **code analysis**, **synthetic data generation**, **product features**, **user-facing support**, **live service operations**, **user research**, **design**, **content**, **business analysis**, and **general productivity** — and, cutting across all of them, how much the AI is allowed to do on its own.

## How to use this

When you want to use AI for a specific activity, work through the five-step [assessment](assess/1-scope.md) below. Each step builds on the previous one, taking you from scoping the use to recording your decision. Keep it proportionate — a genuinely low-risk case can be assessed in minutes; save the detail for cases that need it.

New to this? The **[Getting Started guide](getting-started.md)** walks you through setting up AI governance on your project.

## The assessment at a glance

| Step | What you do |
| ---- | ---- |
| **[1. Scope your use](assess/1-scope.md)** | Define the activity, categorise it, record how much the AI may do on its own, and assess what code and data you will share (including its classification) |
| **[2. Check the tool is eligible](assess/2-check-tool.md)** | Confirm the tool is on your project's register, and that its entry covers your classification, use type and autonomy level |
| **[3. Identify the risks](assess/3-identify-risks.md)** | Use the heatmap to find the risks that matter for your use, rate each, adjust for autonomy, and take the highest as your **inherent** risk level |
| **[4. Safeguards and approvals](assess/4-safeguards.md)** | Apply mitigations proportionate to the inherent risk, reassess the **residual** risk, and get the required sign-off |
| **[5. Record and do the work](assess/5-record-and-work.md)** | Save the assessment (it is your record), do the work via your checklist, and share what you learned |

The two hard stops come first, so you fail fast. Step 1: SECRET or above, or data whose consent or contract terms prohibit AI processing, means do not proceed. Step 2: a tool that is not on the register, or whose entry does not cover your use, must be assessed before you use it.

**Tools are eligible. Uses are approved.** Clearing Step 2 means the tool is not ruled out. Whether your use goes ahead is decided at Step 4, on the basis of risk.

## Ground rules that always apply

Whichever path you take, these hold:

- **You are accountable for AI outputs.** Code, analysis, content, or advice you submit, commit, or act on is your responsibility — treat it as your own work and apply the same quality standards.
- **Eligible tools only, within their recorded limits.** Use only tools on your project's [tool register](assess/2-check-tool.md), and only for what their entry covers — going beyond it is the same as using a tool nobody assessed. Need a new tool, or a wider entry? Get it assessed *before* use, never after. Unassessed use ("shadow AI") bypasses these safeguards; if you spot it, raise it with your delivery lead or SRO.
- **No consumer or public AI for work.** Free or consumer versions of ChatGPT, Gemini, Claude, and others must not be used for work-related information — they often store and train on your inputs. Enterprise or approved versions are different.
- **"Stricter wins" by default.** Where this framework and a client or department policy differ, the more restrictive position applies automatically — you never need approval to follow the stricter rule. This framework is a baseline: taking a *less* restrictive approach than the applicable position is only permitted with a specific, documented exemption approved by the SRO (see [Step 4](assess/4-safeguards.md)). Never treat the framework as justification for a looser approach.

Anyone using AI on project work should understand the relevant data classifications, their data protection obligations (including when a DPIA is required), this framework, and which tools are eligible. Organisations should provide AI awareness training and consider establishing AI champions.

## Alignment with UK Government guidance

This framework operationalises UK Government guidance — including the **AI Playbook**, **ATRS**, **NCSC** guidance, the **Government Security Classifications Policy**, and the **ICO** toolkits — into a practical assessment process. It does not replace that guidance. See [Reference: Alignment with UK Government Guidance](reference/government-guidance.md) for the full list and a mapping to the AI Playbook's 10 principles.

**Keeping this current:** the AI landscape evolves rapidly. Review this framework at least every six months and when significant changes occur in government guidance, regulation, or the risk landscape.

## Contents

### The assessment

- [Step 1: Scope your use](assess/1-scope.md)
- [Step 2: Check the tool is eligible](assess/2-check-tool.md)
- [Step 3: Identify the risks](assess/3-identify-risks.md)
- [Step 4: Safeguards and approvals](assess/4-safeguards.md)
- [Step 5: Record and do the work](assess/5-record-and-work.md)

### Reference library

- [Risk catalogue](reference/risk-catalogue.md) — the eight risks in depth, by use type
- [Use-type profiles](reference/use-type-profiles.md) — the eleven use types, their tools and typical risks
- [Per-use checklists](reference/checklists.md) — before / during / after, per use type
- [Tool baseline criteria](reference/tool-criteria.md) — what a tool must meet
- [Worked examples](reference/worked-examples.md) — six end-to-end assessments
- [Alignment with UK Government guidance](reference/government-guidance.md)
- [Glossary](reference/glossary.md)

### Templates

- [Risk assessment template](templates/risk-assessment.md)
- [Tool evaluation template](templates/tool-evaluation.md)
- [Introduction template](templates/introduction.md) — adopt the framework into your own project docs
