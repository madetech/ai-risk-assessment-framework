# Step 2: Check the Tool

Your project should keep a **tool register**: a record of the AI tools that have been assessed, and what is true about each one. Each entry is a **profile** — what the tool *is*, and what its supplier *promises*.

A profile deliberately does not say what the tool may be used for. That is settled use by use, through the risk assessment in [Step 3](3-assess-risks.md). Recording facts rather than permissions means a profile does not have to anticipate uses nobody has proposed yet, and it stays true instead of quietly going out of date.

This step has two jobs — confirm your tool is not excluded, and pick up the facts you will need for the rest of the assessment. It comes before the risk work because those facts feed straight into it.

## Is the tool already on the register?

If it is, you can move on to the next step: [Assess the Risks](3-assess-risks.md)

If it is not, it must be assessed and added before you use it. Gather the facts set out below, using the [tool profile template](../templates/tool-evaluation.md). Anyone can gather facts; the two decisions at the end need sign-off.

Never use a tool first and add it to the register afterwards.

## Is it excluded?

A few facts disqualify a tool outright, whatever you intend to use it for:

- **It trains on your inputs**, or the provider will not commit not to
- **No data processing agreement**, or one that does not meet UK GDPR requirements
- **A free or consumer tier** operating under consumer terms — these typically store inputs and use them for training, and must not be used for work information
- **It fails a requirement set by your client or department** — "stricter wins" applies

🛑 If any of these are true, stop. Choose a different tool, or escalate for a documented exemption with justification and SRO approval.

Then check the **highest classification the tool has been cleared for**. That is a decision made with authority, not a judgement to make for yourself. If the data you scoped in [Step 1](1-scope.md) sits above it, escalate to the SRO before going further.

## What a profile records

Any AI tool that processes your data is sharing that data with a third party — the provider. Most of these facts are pinning down what that means in practice.

They come in two kinds, and the difference matters. A tool running in your own tenancy genuinely presents a smaller risk than one that does not. A tool with a no-training commitment presents the same risk with a mitigation on it. Those are different things, so the two kinds are recorded separately and used in different places.

### What the tool is

Design facts. These shape the **inherent** risk you rate in [Step 3](3-assess-risks.md) — they change how big the risk fundamentally is.

| Fact | What to establish |
| ---- | ---- |
| **Whether data leaves your estate** | Does the tool send your data to a third party at all, or does it run inside your own tenancy or on your own hardware? This one fact does more to determine data leakage risk than anything else in the profile. |
| **Where it is processed and stored** | Which countries and jurisdictions. For UK government work, data should typically stay in the UK. |
| **What it can reach** | Calendar, mailbox, files, repositories, ticketing systems, production telemetry. Record what it *can* access, not what you intend to give it. |
| **What it can do** | Whether it only produces output, or can take actions — run commands, edit files, call APIs, change records. Record the most it is capable of, regardless of how you would configure it. |
| **Whether its actions can be constrained from outside** | For tools that can act: are the available actions defined by you or by the vendor, and can the limit be enforced *outside* the tool's own configuration — in your IAM, network policy, or API scopes? A limit the tool enforces on itself is not a limit. |

### What the supplier promises

Contractual and configurable guarantees. These are **mitigations**, applied in [Step 3](3-assess-risks.md#5-choose-mitigations-that-address-this-risk) — they shrink a risk that already exists.

| Fact | What to establish |
| ---- | ---- |
| **Training on inputs** | Whether inputs are used to train or improve models, and whether that is contractual or a setting someone could change. |
| **Retention** | How long inputs are kept, and whether they are deleted after processing. Take this from the data processing agreement, not the marketing page. |
| **Data processing agreement** | Whether one is available, and whether it meets UK GDPR requirements. |
| **Authentication and access management** | SSO, MFA, team or project-level access control, and whether individual use can be attributed. |
| **Audit logging** | Whether you can establish what was sent, what came back, and who did it — and who can read those logs. |
| **Security certifications** | ISO 27001, SOC 2, and alignment with the Code of Practice for the Cyber Security of AI. |
| **IP terms** | Whether the provider claims rights over outputs, and whether indemnification is offered. |
| **Change and notice** | Whether the provider can change the model or the tool's behaviour without telling you, how much notice you get, and whether that notice is contractual. This is how a profile silently goes stale. |
| **Handling of AI-specific risk** | Whether the provider engages seriously with hallucination, bias and prompt injection and explains how they address them — or simply gestures at them. |

Note also that a profile records what a tool **can** do, not what you will let it do. Whether you enable an agent mode that runs commands is your autonomy decision from [Step 1](1-scope.md#assess-the-level-of-autonomy) — but if the capability exists and can be switched on, the profile should say so.

## The two decisions

Everything above is fact. These two are judgements, and need authority rather than individual opinion:

| Decision | Who makes it |
| ---- | ---- |
| **Excluded, or not** | Whoever assesses the tool, against the list above. An exemption needs SRO approval. |
| **Highest classification cleared** | The SRO or equivalent. Do not infer it from the facts yourself — UK residency and a DPA do not by themselves clear a tool for OFFICIAL information carrying a ‑SENSITIVE marking. |

## Keeping the register honest

Facts go stale. Suppliers change terms, models are updated, and tiers are renamed. Record who gathered the facts, who signed off the decisions, and when the profile is next due for review. A profile that has not been checked recently is a starting point, not a source of truth.

Assess the specific tier you will use: enterprise and consumer versions of the same product routinely differ on exactly the facts that matter, so treat them as different tools.

Where a client or department keeps its own approved AI tools list, apply "stricter wins" — their exclusions bind you. Their inclusions do not tell you what the tool does, so you will still need a profile.

---

[Next: Step 3 — Assess the Risks >](3-assess-risks.md)
