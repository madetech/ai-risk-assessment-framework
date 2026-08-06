# Appendix A: Tool Profile Template

Use this when adding an AI tool to the project's tool register — see [Step 2](../assess/2-check-tool.md) and [Reference: Assessing a Tool](../reference/tool-criteria.md).

This records what the tool **is** and what its supplier **promises**. It does not say what the tool may be used for: that is settled use by use, in each risk assessment.

| | |
| ---- | ---- |
| **Tool** | [Name and provider] |
| **Tier or plan assessed** | [Enterprise and consumer versions are different tools for this purpose] |
| **Facts gathered by** | [Name] |
| **Date** | [Date] |
| **Next review** | [Date] |

---

## Is it excluded?

Any "yes" rules the tool out, whatever the intended use.

| | Yes / No | Notes |
| ---- | ---- | ---- |
| Trains on your inputs, or will not commit not to | | |
| No DPA, or one that does not meet UK GDPR requirements | | |
| A free or consumer tier under consumer terms | | |
| Fails a client or department requirement | | |

**Excluded:** [Yes / No] — _if yes, stop here unless a documented exemption is approved by the SRO._

---

## What the tool is

_Design facts. These shape the **inherent** risk in [Step 3](../assess/3-identify-risks.md)._

| Fact | Details |
| ---- | ---- |
| **Where data is processed and stored** | [Countries and jurisdictions] |
| **Permissions the tool holds** | [What it can reach — calendar, mailbox, files, repositories, ticketing systems. What it can access, not what you intend to give it] |
| **What it can do** | [Produces output only, or can take actions — run commands, edit files, call APIs, change records. Record the most it is capable of] |
| **Control over what it can do** | [For tools that can act: who defines the available actions, and whether the limit can be enforced outside the tool's own configuration] |
| **Authentication and access management** | [SSO, MFA, team/project access control, attribution of individual use] |
| **Audit logging** | [What is logged, and who can read it] |

## What the supplier promises

_Contractual and configurable guarantees. These are **mitigations** in [Step 4](../assess/4-safeguards.md)._

| Fact | Details |
| ---- | ---- |
| **Training on inputs** | [Contractual commitment, or a changeable setting?] |
| **Retention** | [How long inputs are kept; deletion after processing] |
| **Data processing agreement** | [Available? Meets UK GDPR?] |
| **Security certifications** | [ISO 27001, SOC 2, Code of Practice for the Cyber Security of AI] |
| **IP terms** | [Rights claimed over outputs; indemnification] |
| **Change and notice** | [Can the model or behaviour change without notice? How much notice, and is it contractual?] |
| **Handling of AI-specific risk** | [How the provider addresses hallucination, bias, prompt injection] |

---

## Decision

_A judgement, not a fact. Needs authority._

**Highest classification cleared:** [e.g. OFFICIAL] — _do not infer this from the facts above; UK residency and a DPA do not by themselves clear a tool for OFFICIAL-SENSITIVE._

| Role | Name | Decision | Date |
| ---- | ---- | ---- | ---- |
| Assessed by | | | |
| Approved by | | | |
