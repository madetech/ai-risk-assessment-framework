# Step 2: Check the Tool

Your project should keep a **tool register**: a record of the AI tools that have been assessed, and what is true about each one.

This step has two jobs — confirm your tool is not excluded, and pick up the facts you will need for the rest of the assessment. It comes before the risk work because those facts feed straight into it.

## Is the tool on the register?

If it is, you have its profile. Move on.

If it is not, it must be assessed and added before you use it. Gather the facts using the [tool profile template](../templates/tool-evaluation.md), following [Reference: Assessing a Tool](../reference/tool-criteria.md). Anyone can gather facts; the two decisions in a profile need sign-off.

Never use a tool first and add it to the register afterwards.

## Is it excluded?

A few facts disqualify a tool outright, whatever you intend to use it for:

- It trains on your inputs, or will not commit not to
- There is no data processing agreement, or it does not meet UK GDPR requirements
- It is a free or consumer tier operating under consumer terms
- It fails a requirement your client or department has set

🛑 If any of these are true, stop. Choose a different tool, or escalate for a documented exemption.

Then check the **highest classification the tool has been cleared for**. That is a decision made with authority, not a judgement to make for yourself. If the data you scoped in [Step 1](1-scope.md) sits above it, escalate to the SRO before going further.

## What the profile tells you

Everything else in a profile is fact, not permission. It does not tell you whether you may proceed — it tells you what you are dealing with, so the rest of the assessment can be specific rather than generic.

The facts come in two kinds, and they are used in different places:

| Kind of fact | Examples | Where it is used |
| ---- | ---- | ---- |
| **What the tool is** — its design | Data leaves your estate to a third party; it holds standing access to your repositories; it can execute commands and open pull requests | [Step 3](3-identify-risks.md) — design shapes the **inherent** risk |
| **What the supplier promises** — its terms | Inputs are not used for training; data stays in the UK; 30-day retention; IP indemnified; 30 days' notice of model changes | [Step 4](4-safeguards.md) — promises are **mitigations**, and move the residual risk |

Carry both forward. A tool running in your own tenancy genuinely presents a smaller risk than one that does not. A tool with a no-training commitment presents the same risk with a control on it. Those are different things, and the assessment should show which is which.

Note also that a profile records what a tool **can** do, not what you will let it do. Whether you enable an agent mode that runs commands is your autonomy decision from [Step 1](1-scope.md#assess-the-level-of-autonomy) — but if the capability exists and can be switched on, the profile should say so.

## Keeping the register honest

Facts go stale. Suppliers change terms, models are updated, and tiers are renamed. Every profile needs a review date, and a profile that has not been checked recently should be treated as a starting point rather than a source of truth.

Assess the specific tier you will use: enterprise and consumer versions of the same product routinely differ on exactly the facts that matter.

Where a client or department keeps its own approved AI tools list, apply "stricter wins" — their exclusions bind you. Their inclusions do not tell you what the tool does, so you will still need a profile.

---

[Next: Step 3 — Identify the Risks >](3-identify-risks.md)
