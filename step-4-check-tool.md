# Step 4: Check the Tool

Before proceeding, confirm that the specific AI tool you intend to use has been approved for use on this project.

**If the tool is already on the approved tools list**, this step is a quick confirmation — verify that it is approved for the classification level and use type you identified in Steps 1 and 2, then proceed to [Step 5](step-5-mitigate.md).

**If the tool is not on the approved list**, it must be assessed and approved before you use it. Use the evaluation template in [tool evaluation template](templates/tool-evaluation.md) to gather the necessary information, then submit it to the SRO for approval. **Do not begin using an unapproved tool.**

## AI tools as data sharing

Any AI tool that processes your data constitutes sharing that data with a third party — the AI provider. This applies even if the tool feels like a local productivity aid. This data sharing may trigger UK GDPR obligations, contractual notification requirements, or government security policy considerations.

AI tools may also require additional permissions that must be identified, controlled, and monitored. For example, a productivity assistant may request access to your calendar, meetings, email, or contact list — each of these represents additional data being shared with the provider beyond what you explicitly type into the tool.

## Criteria any AI tool must meet

| Criterion | What to check |
| ---- | ---- |
| **Data residency** | Where is data processed and stored? Does this comply with the project's data residency requirements and any client contractual obligations? For UK government work, data should typically be processed within the UK or EEA unless explicitly agreed otherwise. |
| **Data retention and training** | Does the provider retain your inputs? Are inputs used to train or improve their models? For any use involving sensitive data, the tool must offer a clear commitment not to use your data for training. Check the provider's data processing agreement, not just their marketing materials. |
| **Authentication and access controls** | Does the tool support appropriate authentication (SSO, MFA)? Can access be managed at the team or project level? Can individual usage be audited? |
| **Audit logging** | Does the tool provide logs of what was submitted and returned? This matters for accountability and incident investigation. |
| **Security certifications** | Does the provider hold relevant security certifications (e.g. ISO 27001, SOC 2)? Do they comply with the Code of Practice for the Cyber Security of AI? |
| **Contractual IP terms** | What do the terms of service say about intellectual property? Does the provider claim any rights over outputs? Do they offer IP indemnification? |
| **Risk mitigation** | Does the provider acknowledge and address key AI-specific risks (hallucination, bias, data leakage, prompt injection)? Do they clearly explain how they mitigate these risks? |
| **Permissions and access** | What permissions does the tool require (e.g. access to calendar, contacts, files, meetings)? Are these proportionate to the intended use? Can unnecessary permissions be disabled? |

**If the tool does not meet these criteria, stop.** Either choose a different tool that does, or escalate to get the criteria formally waived with appropriate justification and approval.

**Remember the "stricter wins" principle.** If the client has a list of approved AI tools, or specific requirements beyond these criteria, those take precedence. Check with the client before introducing any AI tool not already approved for the engagement.

---

[Next: Step 5 — Mitigate Risks and Reassess >](step-5-mitigate.md)
