# Appendix A: Tool Evaluation Template

Use this template when adding an AI tool to the project's tool register — see [Step 2](../assess/2-check-tool.md) and the [baseline eligibility criteria](../reference/tool-criteria.md).

| Criterion | Details | Meets criteria? |
| ---- | ---- | ---- |
| **Tool name and provider** | | |
| **Data residency** | Where is data processed? Where is it stored? | Yes / No / Partial |
| **Data retention** | How long are inputs retained? Are they deleted after processing? | Yes / No / Partial |
| **Training data policy** | Are inputs used for model training? Can this be opted out of? | Yes / No / Partial |
| **Authentication** | SSO? MFA? Team/project-level access management? | Yes / No / Partial |
| **Audit logging** | Are queries and responses logged? Who can access logs? | Yes / No / Partial |
| **Security certifications** | ISO 27001? SOC 2? Others? | Yes / No / Partial |
| **IP terms** | Does the provider claim rights over outputs? Indemnification? | Yes / No / Partial |
| **Data processing agreement** | Is a DPA available? Does it meet GDPR requirements? | Yes / No / Partial |
| **Risk mitigation** | Does the provider acknowledge and address key AI-specific risks (hallucination, bias, data leakage, prompt injection)? Do they clearly explain how they mitigate them? | Yes / No / Partial |
| **Permissions and access** | What permissions does the tool require (e.g. calendar, contacts, files, meetings)? Are these proportionate to the intended use? Can unnecessary permissions be disabled? | Yes / No / Partial |
| **Change and notice** | Can the provider change the model or the tool's behaviour without notice? How much notice, and is it contractual? | Yes / No / Partial |
| **Control over what it can do** | For tools that can act: who defines the available actions, you or the vendor? Can the limit be enforced outside the tool's own configuration? | Yes / No / Partial / N/A |

## What this tool is eligible for

Record the limits that each use will be checked against. Going beyond any of them means the tool has not been assessed for that use.

| Limit | Value |
| ---- | ---- |
| **Tier or plan assessed** | [Enterprise and consumer versions are different tools for this purpose] |
| **Classification ceiling** | [e.g. OFFICIAL] |
| **Eligible use types** | [List them — avoid "all" unless you have genuinely considered each] |
| **Autonomy ceiling** | [Suggests / Drafts for review / Acts with approval / Acts autonomously] |
| **Conditions** | [e.g. secrets scan first, telemetry disabled, named tenancy, restricted network access] |

**Assessed by:** [Name]
**Date:** [Date]
**Approved for use on:** [Project name]
**Approved by:** [Name and role]
**SRO sign-off:** [Name and date]
**Conditions / restrictions:** [Any limitations on use]
