# Step 2: Check the Tool Is Eligible

Your project keeps a **tool register**: a record of which AI tools have been assessed, and what each one may be used for. This step asks two questions of it.

1. **Is your tool on the register?** If not, it must be evaluated and added before you use it.
2. **Does its entry cover what you are doing?** Check the classification, use type and autonomy level you recorded in [Step 1](1-scope.md) against the limits the register sets for that tool.

If either answer is no, stop until it is resolved. Never use a tool first and sort out eligibility afterwards.

## Does the entry cover your use?

| Check | Against the register |
| ---- | ---- |
| **Classification** | Is your data at or below the tool's classification ceiling? A tool eligible up to OFFICIAL is not thereby eligible for OFFICIAL-SENSITIVE. |
| **Use type** | Is your [use type](../reference/use-type-profiles.md) one the tool is eligible for? A coding assistant cleared for writing code is not automatically cleared to analyse a whole codebase. |
| **Autonomy** | Is your [autonomy level](1-scope.md#assess-the-level-of-autonomy) at or below the tool's ceiling? A tool assessed while it only proposed changes for a developer to review has not been assessed as an agent that runs commands by itself. |
| **Conditions** | Are there conditions on the entry, and can you meet them? Typically: secrets scanning first, telemetry disabled, a named workspace or tenancy, named users only. |

Using a tool outside its recorded limits is the same as using one nobody assessed. If your use does not fit, you can narrow it, choose a different tool, or ask for the entry to be widened — which means a fresh assessment and SRO approval.

## Adding a new tool

Evaluate it with the [tool evaluation template](../templates/tool-evaluation.md) against the [baseline eligibility criteria](../reference/tool-criteria.md), then submit it to the SRO. The criteria come down to six questions:

- **Where your data goes** — residency, retention, and whether your inputs train the provider's models
- **What the tool can reach** — the permissions it asks for, and how access is managed
- **What you could reconstruct afterwards** — audit logging
- **Whether the supplier is credible** — certifications, and whether they engage seriously with hallucination, bias and prompt injection
- **Who owns the output, and who carries the liability** — IP terms and indemnification
- **Whether it can change under you** — notice of model changes, and for a tool that acts, who decides what it may do

Assess the specific tier you will use: enterprise and consumer versions of the same product often differ on exactly these points.

Then record what the tool is eligible for — classification ceiling, use types, autonomy ceiling, conditions, and who approved it. A blank register table is in the [introduction template](../templates/introduction.md).

Where a client or department keeps its own approved tools list, treat it as a register and apply "stricter wins": their exclusions bind you.

---

Being eligible is not permission to proceed. It means the tool is not ruled out. Whether this particular use goes ahead is decided in [Step 4](4-safeguards.md), once you know the risks.

[Next: Step 3 — Identify the Risks >](3-identify-risks.md)
