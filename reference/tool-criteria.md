# Reference: Baseline Eligibility Criteria

These are the baseline criteria any AI tool must meet to be **eligible** for use on a project. Use them in [Step 2](../assess/2-check-tool.md) when adding a tool to the project's tool register, alongside the [tool evaluation template](../templates/tool-evaluation.md).

## AI tools as data sharing

Any AI tool that processes your data constitutes sharing that data with a third party — the AI provider. This applies even if the tool feels like a local productivity aid. This data sharing may trigger UK GDPR obligations, contractual notification requirements, or government security policy considerations.

AI tools may also require additional permissions that must be identified, controlled, and monitored. For example, a productivity assistant may request access to your calendar, meetings, email, or contact list — each of these represents additional data being shared with the provider beyond what you explicitly type into the tool.

## Criteria any AI tool must meet

| Criterion | What to check |
| ---- | ---- |
| **Data residency** | Where is data processed and stored? Does this comply with the project's data residency requirements and any client contractual obligations? For UK government work, data should typically be processed within the UK. |
| **Data retention and training** | Does the provider retain your inputs? Are inputs used to train or improve their models? For any use involving sensitive data, the tool must offer a clear commitment not to use your data for training. Check the provider's data processing agreement, not just their marketing materials. |
| **Authentication and access controls** | Does the tool support appropriate authentication (SSO, MFA)? Can access be managed at the team or project level? Can individual usage be audited? |
| **Audit logging** | Does the tool provide logs of what was submitted and returned? This matters for accountability and incident investigation. |
| **Security certifications** | Does the provider hold relevant security certifications (e.g. ISO 27001, SOC 2)? Do they comply with the Code of Practice for the Cyber Security of AI? |
| **Contractual IP terms** | What do the terms of service say about intellectual property? Does the provider claim any rights over outputs? Do they offer IP indemnification? |
| **Risk mitigation** | Does the provider acknowledge and address key AI-specific risks (hallucination, bias, data leakage, prompt injection)? Do they clearly explain how they mitigate these risks? |
| **Permissions and access** | What permissions does the tool require (e.g. access to calendar, contacts, files, meetings)? Are these proportionate to the intended use? Can unnecessary permissions be disabled? |
| **Change and notice** | Can the provider change the underlying model, or the tool's behaviour, without telling you? What notice do you get, and is it contractual or a courtesy? A tool assessed on today's model may behave differently next month with no change on your side — this is how an assessment silently goes stale. |
| **Control over what it can do** | For tools that can take actions rather than only produce output: is the set of available actions defined by you or by the vendor? Can you constrain it *outside* the tool's own configuration — in your IAM, network policy, or API scopes — so that a change at the vendor's end cannot widen it? A limit the tool enforces on itself is not a limit. |

**If the tool does not meet these criteria it is excluded.** 🛑 Stop. Either choose a different tool that does meet them, or escalate to get a criterion formally waived with appropriate justification and approval.

## Recording what the tool is eligible for

Meeting the criteria is not the whole entry. Also record the limits that each use will be checked against:

| Field | What to record |
| ---- | ---- |
| **Classification ceiling** | The highest classification the tool's data handling supports — typically OFFICIAL unless it has been specifically assessed higher |
| **Eligible use types** | Which of the [use types](use-type-profiles.md) this assessment covers. Do not write "all" unless you have genuinely considered each one |
| **Autonomy ceiling** | The highest [autonomy level](../assess/1-scope.md#assess-the-level-of-autonomy) the tool may be configured to. A tool assessed while it only suggested things has not been assessed as an agent |
| **Conditions** | Anything that must be true in use — secrets scanning first, telemetry disabled, a named tenancy or workspace, restricted network access, named users only |
| **Tier or plan** | The specific version assessed. Enterprise and consumer versions of the same product are different tools for this purpose |
| **Review** | Who assessed it, who approved it, and when it is next due for review |

**Remember the "stricter wins" principle.** If the client has its own list of approved AI tools, or requirements beyond these criteria, those take precedence. Treat their list as an eligibility register: their exclusions bind you, but their inclusions do not authorise your specific use. Check with the client before introducing any AI tool not already on it.
