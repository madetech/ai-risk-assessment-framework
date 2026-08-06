# Reference: Assessing a Tool

Use this when adding an AI tool to your project's tool register, alongside the [tool profile template](../templates/tool-evaluation.md). It sets out what disqualifies a tool, the facts to establish about the ones that survive, and the two things that are decisions rather than facts.

A profile describes what a tool **is** and what its supplier **promises**. It does not say what the tool may be used for — that is settled use by use, through the risk assessment in [Step 3](../assess/3-identify-risks.md) and [Step 4](../assess/4-safeguards.md). Recording facts rather than permissions means the profile does not have to anticipate uses nobody has proposed yet, and it stays true rather than quietly going out of date.

## What disqualifies a tool

Stop if any of these are true. They rule the tool out whatever the intended use.

- **It trains on your inputs**, or the provider will not commit not to
- **No data processing agreement**, or one that does not meet UK GDPR requirements
- **A free or consumer tier** operating under consumer terms — these typically store inputs and use them for training, and must not be used for work information
- **It fails a requirement set by your client or department** — "stricter wins" applies

Either choose a different tool, or escalate for a documented exemption with justification and SRO approval.

## Facts to record

Any AI tool that processes your data is sharing that data with a third party — the provider. That is what most of these facts are pinning down.

| Fact | What to establish |
| ---- | ---- |
| **Where data is processed and stored** | Which countries and jurisdictions? For UK government work, data should typically stay in the UK. |
| **Retention** | How long are inputs kept, and are they deleted after processing? Get this from the data processing agreement, not the marketing page. |
| **Training on inputs** | Whether inputs are used to train or improve models, and whether that is contractual or a setting someone could change. |
| **Permissions the tool holds** | What it can reach — calendar, mailbox, files, repositories, ticketing systems. Record what it *can* access, not what you intend to give it. |
| **Authentication and access management** | SSO, MFA, team or project-level access control, and whether individual use can be attributed. |
| **Audit logging** | Whether you can establish what was sent, what came back, and who did it. Who can read those logs. |
| **What the tool can do** | Whether it only produces output, or can take actions — run commands, edit files, call APIs, change records. Record the most it is capable of, regardless of how you would configure it. |
| **Control over what it can do** | For tools that can act: whether the available actions are defined by you or the vendor, and whether the limit can be enforced *outside* the tool's own configuration, in your IAM, network policy, or API scopes. A limit the tool enforces on itself is not a limit. |
| **Security certifications** | ISO 27001, SOC 2, and alignment with the Code of Practice for the Cyber Security of AI. |
| **IP terms** | Whether the provider claims rights over outputs, and whether indemnification is offered. |
| **Change and notice** | Whether the provider can change the model or the tool's behaviour without telling you, how much notice you get, and whether that notice is contractual. This is how a profile silently goes stale. |
| **Supplier's handling of AI-specific risk** | Whether they engage seriously with hallucination, bias and prompt injection, and explain how they address them — or simply gesture at them. |
| **Tier or plan assessed** | The specific version. Enterprise and consumer versions of the same product are different tools for this purpose. |

## The two decisions

Everything above is fact. These two are judgements, and need authority rather than individual opinion:

| Decision | Who makes it |
| ---- | ---- |
| **Excluded, or not** | Whoever assesses the tool, against the disqualifying list above. An exemption needs SRO approval. |
| **Highest classification cleared** | The SRO or equivalent. Do not infer it from the facts yourself — a tool with UK residency and a DPA is not thereby cleared for OFFICIAL-SENSITIVE. |

## Review

Record who gathered the facts, who signed off the decisions, and when the profile is next due for review. A profile that has not been checked recently is a starting point, not a source of truth.
