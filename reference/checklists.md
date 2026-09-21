# Reference: Per-Use Checklists

Once you have completed the assessment and recorded it, use the checklist for your use type to do the work. This is [Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md) in the assessment flow. Find your checklist here and follow it.

These checklists are structured as **before / during / after** to help you build good habits at each stage. They incorporate the mitigations from [Step 3: Assess the Risks](../assess/3-assess-risks.md). Items marked **(medium and high)** apply where your assessment rated that risk medium or high; the rest apply whatever the rating.

The eleven use types are defined in [Reference: Use-Type Profiles](use-type-profiles.md). If your use involves AI that acts rather than advises, also apply the autonomy mitigations in [Step 3: Assess the Risks](../assess/3-assess-risks.md).

## Checklist: Software development

**Before:**

- [ ] Confirm the tool is on the register, not excluded, and cleared for your data's classification ([Step 2](../assess/2-check-tool.md))
- [ ] Check that no secrets, credentials, or API keys are present in the code context the tool will access
- [ ] Configure the tool appropriately (e.g. disable telemetry if required, set correct organisation/workspace)
- [ ] Audit AI configuration files (`.cursorrules`, `.github/copilot-instructions.md`, or equivalent) for hidden or adversarial instructions before trusting them
- [ ] If the tool can act rather than suggest (running commands, editing files across the repository, opening pull requests), confirm its actual configuration matches the autonomy level recorded in [Step 1](../assess/1-scope.md#assess-the-level-of-autonomy)
- [ ] **(medium and high)** If working in a security-sensitive area, confirm a second reviewer is arranged

**During:**

- [ ] Review all AI-generated code as if written by an unknown contributor. Do not assume it is correct
- [ ] Test AI-generated code to the same standard as human-written code
- [ ] Check for common AI coding pitfalls: insecure patterns, deprecated APIs, hardcoded values, missing error handling, incorrect business logic
- [ ] Verify any dependencies suggested by AI against known vulnerability databases and the project's dependency policy. Be alert to AI-hallucinated package names that may have been registered as malicious packages
- [ ] Scrutinise any AI-generated changes to dependency files, lock files, or IDE/tool configuration files
- [ ] **(medium and high)** For security-sensitive code: get a second review from someone with security expertise
- [ ] **(medium and high)** For complex logic: ensure you understand what the code does and why, not just that it appears to work

**After:**

- [ ] Note any issues encountered (incorrect suggestions, security concerns, quality problems) for your learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: Code analysis

**Before:**

- [ ] Assess what code and data will be sent to the AI tool. Is it the full codebase or a subset?
- [ ] Check the codebase for embedded secrets or credentials that would be exposed to the tool (run a secrets scanning tool first if possible)
- [ ] Confirm the tool's data handling meets the requirements for the classification level of the code
- [ ] **(medium and high)** If the codebase is OFFICIAL-SENSITIVE or contains commercially sensitive material, confirm approval has been obtained

**During:**

- [ ] Treat AI analysis findings as hypotheses, not conclusions. They require human verification
- [ ] Validate a sample of findings through manual inspection to calibrate the AI's accuracy
- [ ] Be aware of false positives (issues flagged that aren't real) and false negatives (real issues the AI missed)
- [ ] Cross-reference AI findings with traditional static analysis (SAST) tools. Do not rely solely on AI for security assessments
- [ ] Be aware that adversarial content in code comments or strings could manipulate analysis findings (prompt injection)
- [ ] **(medium and high)** Have findings reviewed by someone with domain expertise in the codebase being analysed
- [ ] **(medium and high)** Restrict the analysis tool's network access. It should not need outbound connections to arbitrary endpoints
- [ ] **(medium and high)** Document the limitations of the AI analysis: what it cannot reliably detect

**After:**

- [ ] Document the methodology: what tool was used, what was analysed, what prompts or configuration were used
- [ ] Clearly state the limitations of the analysis in any reports or findings documents
- [ ] Flag findings that need human expert verification before being acted upon
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: Synthetic data generation

**Before:**

- [ ] Confirm the tool is on the register, not excluded, and cleared for your data's classification ([Step 2](../assess/2-check-tool.md))
- [ ] Determine whether the dataset can be generated from the schema alone. If it can, do that, and record why real data was not needed
- [ ] If real data must seed the generation, confirm the tool is cleared for that data's classification and apply the same mitigations you would to the source system
- [ ] Define what the dataset must represent: which edge cases, character sets, field lengths, and demographic distributions matter for this service
- [ ] Decide in advance what classification the output will carry, and who owns that decision
- [ ] **(medium and high)** Where the seed data contains personal data, complete or update a DPIA. Generating from personal data is processing it

**During:**

- [ ] Check the output for verbatim reproduction of real records. Search for known real values from the seed data
- [ ] Run a re-identification check: can an individual be singled out by combining fields in the generated set?
- [ ] Compare the generated distribution against the real one for the characteristics that matter: name forms, missing values, field lengths, protected characteristics
- [ ] Confirm the edge cases you defined are actually present in the output rather than assuming the generator produced them
- [ ] **(medium and high)** Have someone other than the generator's author verify the re-identification and distribution checks
- [ ] **(medium and high)** Where the dataset will train or evaluate a model, assess distribution skew against the real population and document the gap

**After:**

- [ ] Label the dataset with its assigned classification, what it represents, and what it does not
- [ ] Record how it was generated: tool, seed data, prompts or configuration, and the checks performed
- [ ] Set a review point. Regenerate or re-verify when the source schema or the real-world data changes
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: Product feature

**Before:**

- [ ] Complete a Data Protection Impact Assessment (DPIA) if personal data will be processed
- [ ] Define monitoring metrics: how will you measure accuracy, fairness, and performance over time?
- [ ] Document the human oversight model: who reviews AI outputs, how, and how often?
- [ ] Check ATRS requirements: does this AI feature need to be recorded on the Algorithmic Transparency Recording Standard?
- [ ] **(medium and high)** Conduct an Equality Impact Assessment considering protected characteristics
- [ ] **(medium and high)** Define fallback behaviour: what happens when the AI is wrong, unavailable, or uncertain?

**During:**

- [ ] Test with diverse inputs representative of the actual user population
- [ ] Validate accuracy against ground truth data or expert assessment
- [ ] Test for bias across protected characteristics (age, disability, gender, race, etc.)
- [ ] Test accessibility: does the AI feature meet WCAG 2.1 Level AA standards?
- [ ] **(medium and high)** Conduct adversarial testing specifically including prompt injection: test for system prompt extraction, safety filter bypass, indirect injection via processed documents, and cross-site scripting via AI output
- [ ] **(medium and high)** Sanitise all AI-generated output before rendering to users. Treat AI output as untrusted, just as you would user input in a web application
- [ ] **(medium and high)** Ensure the AI cannot access data beyond what the current user is authorised to see (trust boundaries)
- [ ] **(medium and high)** Do not embed secrets, API keys, or sensitive configuration in system prompts
- [ ] **(medium and high)** Test with users from diverse backgrounds, including those with accessibility needs

**After:**

- [ ] Set up ongoing monitoring for accuracy, fairness, and performance drift
- [ ] Complete the ATRS record if applicable
- [ ] Schedule a review date to reassess the feature's performance and risk level
- [ ] Establish an incident response process: what happens when the AI produces harmful output?
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: User-facing support

**Before:**

- [ ] Confirm the tool is on the register, not excluded, and cleared for your data's classification ([Step 2](../assess/2-check-tool.md)), paying particular attention to data retention policies given the unpredictable sensitivity of ticket content
- [ ] Assess what ticket data the AI tool will access. Does it process full ticket content including attachments, or only specific fields?
- [ ] Implement automatic PII detection and credential scanning on ticket content before it is sent to the AI tool
- [ ] Define which ticket types must never be handled by AI (e.g. security incidents, safeguarding concerns, data breach reports, complaints). Enforce these exclusion rules in code, not by relying on the AI's own judgement
- [ ] **(medium and high)** Conduct a DPIA for AI processing of support tickets, given the high likelihood of personal data
- [ ] **(medium and high)** Define confidence thresholds for different levels of automation (categorisation, suggested responses, automated responses)

**During:**

- [ ] Ensure AI drafts responses for human review. Do not send AI-generated responses directly to users without agent approval
- [ ] Monitor AI categorisation and routing accuracy. Incorrect triage can delay resolution of critical issues
- [ ] Watch for automation bias: support agents should critically evaluate AI suggestions, not accept them uncritically
- [ ] Check that the AI handles tickets from diverse users fairly, including non-native English speakers, terse or non-technical communicators, and users of assistive technology
- [ ] **(medium and high)** Audit a regular sample of AI categorisations, suggested responses, and automated actions (weekly or fortnightly)
- [ ] **(medium and high)** Test for prompt injection: could a crafted ticket cause the AI to reveal information from other tickets, bypass exclusion rules, miscategorise sensitive issues, or take unintended actions? Test with adversarial tickets regularly, not just at initial deployment
- [ ] **(medium and high)** Restrict the AI's access scope. It should only access the specific ticket it is processing, not query freely across the full ticket database

**After:**

- [ ] Monitor for model drift: are categorisation accuracy and response quality changing over time?
- [ ] Maintain fallback procedures: document and periodically practise how to operate the service desk if AI tools become unavailable
- [ ] Ensure support agents continue to develop system knowledge and diagnostic skills alongside AI tool use
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: Live service operations

**Before:**

- [ ] Confirm the tool is on the register, not excluded, and cleared for your data's classification ([Step 2](../assess/2-check-tool.md)) at the classification of production telemetry, which is usually higher than teams assume
- [ ] Decide, before any incident, what may and may not be shared with an AI tool, and put it somewhere a responder can find at 3am
- [ ] Identify and restrict credential-bearing log fields (tokens, session identifiers, connection strings, authorisation headers) before they can reach the tool
- [ ] Confirm the autonomy level recorded in [Step 1](../assess/1-scope.md#assess-the-level-of-autonomy) matches what the tool is actually permitted to do
- [ ] **(medium and high)** Where the tool can execute actions, apply least privilege, require approval for anything destructive or irreversible, and check the granted permissions against what it genuinely needs
- [ ] **(medium and high)** Confirm a documented and periodically practised fallback exists for operating without the tool

**During:**

- [ ] Treat proposed root causes as hypotheses to test, not conclusions. Confirm against evidence before acting
- [ ] Route AI-proposed infrastructure changes through normal change control and peer review; an AI-suggested Terraform change is a production change
- [ ] Watch for pressure eroding review. The moment nobody has time to check the suggestion is the moment checking matters most
- [ ] Record in the incident log that AI was used, what it proposed, and what the team decided
- [ ] Be aware that log, alert, and webhook content is partly attacker-controlled and may carry injected instructions
- [ ] **(medium and high)** Require a second responder to confirm any AI-proposed remediation that is destructive, irreversible, or affects data
- [ ] **(medium and high)** Log every action the AI takes to the incident record, including the identity it acted under

**After:**

- [ ] Cover AI's role in the incident review: what it got right, what it got wrong, and whether it changed the outcome
- [ ] Check whether autonomy has crept. Is the tool being used with less oversight than was assessed?
- [ ] Ensure on-call engineers are still building system knowledge rather than deferring to the tool
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: User research

**Before:**

- [ ] Check that research participant consent covers AI processing of their data. If not, do not proceed without obtaining additional consent. This is a hard constraint, not a risk to be mitigated
- [ ] Remove or anonymise PII before submitting data to the AI tool, unless the tool meets full data handling requirements
- [ ] Confirm the tool's data handling meets the sensitivity requirements for the research data
- [ ] **(medium and high)** For sensitive research topics: get ethics review or approval before using AI

**During:**

- [ ] Validate AI-generated summaries and themes against source transcripts. Check that they accurately represent what participants said
- [ ] Flag AI-generated insights separately from direct participant quotes in your notes
- [ ] Check the synthesis against the sessions that were *hardest* to summarise, not the easiest: participants who spoke through an interpreter, took longer to make a point, or used non-standard English are the ones most likely to be smoothed out
- [ ] Check for bias in synthesis: are all participant perspectives fairly represented, or are some systematically underweighted?
- [ ] Be aware that free-text responses (surveys, interviews) could contain adversarial content that manipulates AI analysis. Particularly where participants have a strong incentive to influence outcomes
- [ ] **(medium and high)** Have a second researcher review AI-assisted analysis against source material
- [ ] **(medium and high)** Consider whether external documents being analysed could contain hidden content (white-on-white text, zero-width characters) that could skew AI summarisation
- [ ] **(medium and high)** For vulnerable populations: consider whether AI processing is appropriate at all

**After:**

- [ ] Document how AI was used in the methodology section of any research reports
- [ ] Be transparent with stakeholders about the role AI played in the analysis
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: Design

**Before:**

- [ ] Confirm the tool is on the register, not excluded, and cleared for your data's classification ([Step 2](../assess/2-check-tool.md))
- [ ] Establish the project's position on AI-generated imagery and illustration in public-facing output *before* producing any
- [ ] Check what research findings or prototype data you are about to share. Summarised findings and realistic-looking prototype data can carry more than intended

**During:**

- [ ] Check AI suggestions against the GOV.UK Design System rather than accepting generic commercial web patterns
- [ ] Watch for accessibility antipatterns in generated designs: colour as the only carrier of meaning, insufficient contrast, vague link text, unlabelled imagery, form patterns that break with assistive technology
- [ ] Treat any AI accessibility assessment as a prompt to test, never as evidence of compliance
- [ ] Keep AI in the divergent part of the work, generating options, and converge through research and testing
- [ ] **(medium and high)** For designs affecting a statutory or high-consequence journey, have an accessibility specialist review before user testing

**After:**

- [ ] Confirm accessibility has been tested with assistive technology and with disabled users, not assessed by AI alone
- [ ] Record the provenance of any AI-generated visual material used in public-facing output
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: Content

**Before:**

- [ ] Confirm the tool is on the register, not excluded, and cleared for your data's classification ([Step 2](../assess/2-check-tool.md))
- [ ] Identify the authoritative source for every rule, entitlement, deadline, or statutory duty the content will state
- [ ] Check whether the content is sensitive before publication. Content for an unannounced service or policy change usually is
- [ ] Establish the project's position on AI-generated copy in published material
- [ ] **(medium and high)** For content carrying a Welsh Language Standards or equivalent duty, arrange qualified human translation verification before you start

**During:**

- [ ] Check the draft against the GOV.UK style guide and the service's reading age target. AI writes fluently well above a reading age of nine, in a register that drifts corporate
- [ ] Trace every factual claim about rules, entitlements, and deadlines back to the authoritative source. A model's recollection of policy is not a source
- [ ] Have a content designer review it as content, not merely proofread it
- [ ] For content about bereavement, debt, immigration status, or a refused application, check the tone is plain and direct rather than bright and reassuring
- [ ] Remove AI tells that breach the style guide: "please note", "utilise", unnecessary passive constructions, and headings that state nothing
- [ ] **(medium and high)** Test content on difficult subjects with users, not just with colleagues
- [ ] **(medium and high)** For any translation carrying a statutory duty, obtain qualified human verification. An AI translation is not a compliance artefact until it has been confirmed

**After:**

- [ ] Confirm a named person has approved the published wording and can account for its factual claims
- [ ] Record the provenance of any AI-generated copy used in published or press material
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: Business analysis

**Before:**

- [ ] Confirm the tool is on the register, not excluded, and cleared for your data's classification ([Step 2](../assess/2-check-tool.md))
- [ ] Identify who will be named as the author of the resulting requirement, decision record, or assurance artefact, and is accountable for its content
- [ ] Check whether the source material is sensitive before a decision is announced. Draft business cases, commercial information, and pre-decision policy material usually are

**During:**

- [ ] Trace any AI-stated rule, entitlement, or statutory duty back to the authoritative source before it enters the backlog or a decision document. Treat it as unverified until you have
- [ ] Mark AI-drafted acceptance criteria as unverified until someone has checked them against the source
- [ ] Confirm the named author can defend every claim in the document without referring back to the tool. The artefact exists to show that reasoning happened
- [ ] Use AI to structure and express your reasoning, not to supply it
- [ ] Be alert to hidden instructions in external material: policy documents, supplier responses, and stakeholder submissions from a party with an interest in the outcome
- [ ] **(medium and high)** For artefacts going to a governance body, have a second person check the factual claims independently of the author

**After:**

- [ ] Be transparent with governance bodies about AI involvement where it is material to how the artefact was produced
- [ ] Check that requirements derived with AI assistance survived contact with the source. Flag any that turned out to be invented
- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))

## Checklist: General productivity

**Before:**

- [ ] Confirm the tool is on the register, not excluded, and cleared for your data's classification ([Step 2](../assess/2-check-tool.md))
- [ ] Confirm the task genuinely belongs in this category. If the output will be read as evidence that someone reasoned a decision through, use the business analysis checklist instead
- [ ] Understand what permissions the tool requires (calendar, contacts, files, meetings). Are these proportionate to your intended use? Can unnecessary permissions be disabled?
- [ ] Assess the content you will be processing. Do meetings, documents, or emails contain sensitive data, PII, or commercially confidential information?
- [ ] **(medium and high)** For meetings or documents involving OFFICIAL-SENSITIVE content, confirm the tool has been approved for that classification level

**During:**

- [ ] Review all AI-generated outputs (summaries, drafts, translations) before sharing or acting on them
- [ ] Check that meeting summaries accurately reflect what was said. AI can lose context, misattribute statements, or miss key decisions
- [ ] Do not share meeting recordings or transcripts containing sensitive discussions without first assessing the data classification
- [ ] Be aware that documents from external sources may contain hidden content that could influence how the AI processes them
- [ ] **(medium and high)** For sensitive content: have a second person review AI-generated summaries against the source material
- [ ] **(medium and high)** Check that AI-generated translations preserve the intended meaning, especially for formal or legal content

**After:**

- [ ] Note any issues or learnings ([Step 4: Approve, Record and Do the Work](../assess/4-record-and-work.md))
