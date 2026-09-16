# A Practical Risk-Based Approach to the Use of AI in Projects

This is a practical framework for delivery teams to decide **whether and how** to use AI for a specific activity on government projects. The aim is informed decisions: understand the risks and apply proportionate safeguards. It is written for a UK context, but the approach should transfer to other global contexts.

It covers eleven categories of AI use: software development, code analysis, synthetic data generation, product features, user-facing support, live service operations, user research, design, content, business analysis, and general productivity. It also covers autonomy — how much the AI is allowed to do on its own — which cuts across all eleven.

## Why this exists

This framework came out of work on government IT projects, where teams wanting to use AI kept meeting the same obstacle: no one could say whether a particular use was allowed, because no one had assessed the risks. That caution is justified — without an understanding of the risks, "no" is the right default — but it leaves teams with no way to reach any other answer. This framework sets out how to understand, document and mitigate the risks of a specific use, so that the decision rests on evidence.

## How to use this

When you want to use AI for a specific activity, work through the four-step [assessment](assess/1-scope.md) below.

If you haven't used this framework before, the **[Getting Started guide](getting-started.md)** walks you through setting up AI governance on your project.

## The four steps

| Step | What you do |
| ---- | ---- |
| **[1. Scope your use](assess/1-scope.md)** | Define the activity, categorise it, record how much the AI may do on its own, and assess what code and data you will share (including its classification) |
| **[2. Check the tool](assess/2-check-tool.md)** | Confirm the tool is on your project's register and not excluded, and collect the facts about it that the risk assessment needs |
| **[3. Assess the risks](assess/3-assess-risks.md)** | Use the heatmap to identify the risks relevant to your use, then take each one through the same loop: rate it before mitigations (**inherent**), choose mitigations, and re-rate what is left (**residual**) |
| **[4. Approve, record and do the work](assess/4-record-and-work.md)** | Get the sign-off the overall inherent level requires, save the assessment (it is your record), do the work via your checklist, and share what you learned |

## Ground rules that always apply

These principles apply to all AI use:

- **You are accountable for AI outputs.** Code, analysis, content, or advice you submit, commit, or act on is your responsibility — treat it as your own work and apply the same quality standards.
- **Use only assessed tools.** Use only tools on your project's [tool register](assess/2-check-tool.md), and not above the classification a tool has been cleared for. If you need a new tool, get it profiled before use. Unassessed use ("shadow AI") bypasses these safeguards; if you spot it, raise it with your delivery lead or SRO.
- **Do not use consumer or public AI for work.** Free or consumer versions of ChatGPT, Gemini, Claude, and others must not be used for work-related information — they often store and train on your inputs. Enterprise versions with appropriate contractual terms may be acceptable — check the tool register.
- **"Stricter wins" by default.** Where this framework and a client or department policy differ, the more restrictive position applies — you do not need approval to follow the stricter rule. This framework is a baseline: taking a less restrictive approach than the applicable position requires a specific, documented exemption approved by the SRO (see [Step 4](assess/4-record-and-work.md)).

Anyone using AI on project work should understand the relevant data classifications, their data protection obligations (including when a DPIA is required), this framework, and which tools are on the register. Organisations should provide AI awareness training and consider establishing AI champions.

## Alignment with UK Government guidance

This framework applies UK Government guidance — including the AI Playbook, ATRS, NCSC guidance, the Government Security Classifications Policy, and the ICO toolkits — as an assessment process. It does not replace that guidance. See [Reference: Alignment with UK Government Guidance](reference/government-guidance.md) for the full list and a mapping to the AI Playbook's 10 principles.

**Keeping this current:** AI tools and guidance change quickly. Review this framework at least every six months, and when there are significant changes in government guidance, regulation, or the risk landscape.

## Contents

### The assessment

- [Step 1: Scope your use](assess/1-scope.md)
- [Step 2: Check the tool](assess/2-check-tool.md)
- [Step 3: Assess the risks](assess/3-assess-risks.md)
- [Step 4: Approve, record and do the work](assess/4-record-and-work.md)

### Reference library

- [Risk catalogue](reference/risk-catalogue.md) — the eight risks in depth, by use type
- [Use-type profiles](reference/use-type-profiles.md) — the eleven use types, their tools and typical risks
- [Per-use checklists](reference/checklists.md) — before / during / after, per use type
- [Worked examples](reference/worked-examples.md) — six end-to-end assessments
- [Alignment with UK Government guidance](reference/government-guidance.md)
- [Glossary](reference/glossary.md)

### Templates

- [Risk assessment template](templates/risk-assessment.md)
- [Tool profile template](templates/tool-evaluation.md)
- [Introduction template](templates/introduction.md) — adopt the framework into your own project docs
