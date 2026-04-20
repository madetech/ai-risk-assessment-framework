# Step 7: Do the Work — Per-Use Checklists

You have defined your use, assessed the data and risks, checked the tool, determined the required mitigations, and recorded your assessment. Now use AI for the task, following the checklist for your use type.

These checklists are structured as **before / during / after** to help you build good habits at each stage. They incorporate the mitigations from [Step 5](step-5-mitigate.md) — if your risk level requires enhanced controls, pay particular attention to the items marked with **(enhanced)**.

## 7a. Checklist: AI-Assisted Coding

**Before:**

- [ ] Confirm the AI tool is approved for this project ([Step 4](step-4-check-tool.md))
- [ ] Check that no secrets, credentials, or API keys are present in the code context the tool will access
- [ ] Configure the tool appropriately (e.g. disable telemetry if required, set correct organisation/workspace)
- [ ] Audit AI configuration files (`.cursorrules`, `.github/copilot-instructions.md`, or equivalent) for hidden or adversarial instructions before trusting them
- [ ] **(enhanced)** If working in a security-sensitive area, confirm enhanced review arrangements are in place

**During:**

- [ ] Review all AI-generated code as if written by an unknown contributor — do not assume it is correct
- [ ] Test AI-generated code to the same standard as human-written code
- [ ] Check for common AI coding pitfalls: insecure patterns, deprecated APIs, hardcoded values, missing error handling, incorrect business logic
- [ ] Verify any dependencies suggested by AI against known vulnerability databases and the project's dependency policy — be alert to AI-hallucinated package names that may have been registered as malicious packages
- [ ] Scrutinise any AI-generated changes to dependency files, lock files, or IDE/tool configuration files
- [ ] **(enhanced)** For security-sensitive code: get a second review from someone with security expertise
- [ ] **(enhanced)** For complex logic: ensure you understand what the code does and why, not just that it appears to work

**After:**

- [ ] Note any issues encountered (incorrect suggestions, security concerns, quality problems) for [Step 8](step-8-share.md)

## 7b. Checklist: AI-Assisted Code Analysis

**Before:**

- [ ] Assess what code and data will be sent to the AI tool — is it the full codebase or a subset?
- [ ] Check the codebase for embedded secrets or credentials that would be exposed to the tool (run a secrets scanning tool first if possible)
- [ ] Confirm the tool's data handling meets the requirements for the classification level of the code
- [ ] **(enhanced)** If the codebase is OFFICIAL-SENSITIVE or contains commercially sensitive material, confirm approval has been obtained

**During:**

- [ ] Treat AI analysis findings as hypotheses, not conclusions — they require human verification
- [ ] Validate a sample of findings through manual inspection to calibrate the AI's accuracy
- [ ] Be aware of false positives (issues flagged that aren't real) and false negatives (real issues the AI missed)
- [ ] Cross-reference AI findings with traditional static analysis (SAST) tools — do not rely solely on AI for security assessments
- [ ] Be aware that adversarial content in code comments or strings could manipulate analysis findings (prompt injection)
- [ ] **(enhanced)** Have findings reviewed by someone with domain expertise in the codebase being analysed
- [ ] **(enhanced)** Restrict the analysis tool's network access — it should not need outbound connections to arbitrary endpoints
- [ ] **(enhanced)** Document the limitations of the AI analysis — what it cannot reliably detect

**After:**

- [ ] Document the methodology: what tool was used, what was analysed, what prompts or configuration were used
- [ ] Clearly state the limitations of the analysis in any reports or findings documents
- [ ] Flag findings that need human expert verification before being acted upon
- [ ] Note any issues or learnings for [Step 8](step-8-share.md)

## 7c. Checklist: AI-Powered Product Features

**Before:**

- [ ] Complete a Data Protection Impact Assessment (DPIA) if personal data will be processed
- [ ] Define monitoring metrics: how will you measure accuracy, fairness, and performance over time?
- [ ] Document the human oversight model: who reviews AI outputs, how, and how often?
- [ ] Check ATRS requirements: does this AI feature need to be recorded on the Algorithmic Transparency Recording Standard?
- [ ] **(enhanced)** Conduct an Equality Impact Assessment considering protected characteristics
- [ ] **(enhanced)** Define fallback behaviour: what happens when the AI is wrong, unavailable, or uncertain?

**During:**

- [ ] Test with diverse inputs representative of the actual user population
- [ ] Validate accuracy against ground truth data or expert assessment
- [ ] Test for bias across protected characteristics (age, disability, gender, race, etc.)
- [ ] Test accessibility: does the AI feature meet WCAG 2.1 Level AA standards?
- [ ] **(enhanced)** Conduct adversarial testing specifically including prompt injection: test for system prompt extraction, safety filter bypass, indirect injection via processed documents, and cross-site scripting via AI output
- [ ] **(enhanced)** Sanitise all AI-generated output before rendering to users — treat AI output as untrusted, just as you would user input in a web application
- [ ] **(enhanced)** Ensure the AI cannot access data beyond what the current user is authorised to see (trust boundaries)
- [ ] **(enhanced)** Do not embed secrets, API keys, or sensitive configuration in system prompts
- [ ] **(enhanced)** Test with users from diverse backgrounds, including those with accessibility needs

**After:**

- [ ] Set up ongoing monitoring for accuracy, fairness, and performance drift
- [ ] Complete the ATRS record if applicable
- [ ] Schedule a review date to reassess the feature's performance and risk level
- [ ] Establish an incident response process: what happens when the AI produces harmful output?
- [ ] Note any issues or learnings for [Step 8](step-8-share.md)

## 7e. Checklist: AI-Assisted Support

**Before:**

- [ ] Confirm the AI tool is approved for this project ([Step 4](step-4-check-tool.md)), paying particular attention to data retention policies given the unpredictable sensitivity of ticket content
- [ ] Assess what ticket data the AI tool will access — does it process full ticket content including attachments, or only specific fields?
- [ ] Implement automatic PII detection and credential scanning on ticket content before it is sent to the AI tool
- [ ] Define which ticket types must never be handled by AI (e.g. security incidents, safeguarding concerns, data breach reports, complaints) — enforce these exclusion rules in code, not by relying on the AI's own judgement
- [ ] **(enhanced)** Conduct a DPIA for AI processing of support tickets, given the high likelihood of personal data
- [ ] **(enhanced)** Define confidence thresholds for different levels of automation (categorisation, suggested responses, automated responses)

**During:**

- [ ] Ensure AI drafts responses for human review — do not send AI-generated responses directly to users without agent approval
- [ ] Monitor AI categorisation and routing accuracy — incorrect triage can delay resolution of critical issues
- [ ] Watch for automation bias: support agents should critically evaluate AI suggestions, not accept them uncritically
- [ ] Check that the AI handles tickets from diverse users fairly — including non-native English speakers, terse or non-technical communicators, and users of assistive technology
- [ ] **(enhanced)** Audit a regular sample of AI categorisations, suggested responses, and automated actions (weekly or fortnightly)
- [ ] **(enhanced)** Test for prompt injection: could a crafted ticket cause the AI to reveal information from other tickets, bypass exclusion rules, miscategorise sensitive issues, or take unintended actions? Test with adversarial tickets regularly, not just at initial deployment
- [ ] **(enhanced)** Restrict the AI's access scope — it should only access the specific ticket it is processing, not query freely across the full ticket database

**After:**

- [ ] Monitor for model drift: are categorisation accuracy and response quality changing over time?
- [ ] Maintain fallback procedures: document and periodically practise how to operate the service desk if AI tools become unavailable
- [ ] Ensure support agents continue to develop system knowledge and diagnostic skills alongside AI tool use
- [ ] Note any issues or learnings for [Step 8](step-8-share.md)

## 7d. Checklist: AI-Assisted Research and Design

**Before:**

- [ ] Check that research participant consent covers AI processing of their data — if not, do not proceed without obtaining additional consent
- [ ] Remove or anonymise PII before submitting data to the AI tool, unless the tool meets full data handling requirements
- [ ] Confirm the tool's data handling meets the sensitivity requirements for the research data
- [ ] **(enhanced)** For sensitive research topics: get ethics review or approval before using AI

**During:**

- [ ] Validate AI-generated summaries and themes against source transcripts — check that they accurately represent what participants said
- [ ] Flag AI-generated insights separately from direct participant quotes in your notes
- [ ] Check for bias in synthesis: are all participant perspectives fairly represented, or are some systematically underweighted?
- [ ] Be aware that free-text responses (surveys, interviews) could contain adversarial content that manipulates AI analysis — particularly in contexts where participants have a strong incentive to influence outcomes
- [ ] **(enhanced)** Have a second researcher review AI-assisted analysis against source material
- [ ] **(enhanced)** Consider whether external documents being analysed could contain hidden content (white-on-white text, zero-width characters) that could skew AI summarisation
- [ ] **(enhanced)** For vulnerable populations: consider whether AI processing is appropriate at all

**After:**

- [ ] Document how AI was used in the methodology section of any research reports
- [ ] Be transparent with stakeholders about the role AI played in the analysis
- [ ] Note any issues or learnings for [Step 8](step-8-share.md)

## 7f. Checklist: AI-Assisted General Productivity

**Before:**

- [ ] Confirm the AI tool is on the approved tools list ([Step 4](step-4-check-tool.md))
- [ ] Understand what permissions the tool requires (calendar, contacts, files, meetings) — are these proportionate to your intended use? Can unnecessary permissions be disabled?
- [ ] Assess the content you will be processing — do meetings, documents, or emails contain sensitive data, PII, or commercially confidential information?
- [ ] **(enhanced)** For meetings or documents involving OFFICIAL-SENSITIVE content, confirm the tool has been approved for that classification level

**During:**

- [ ] Review all AI-generated outputs (summaries, drafts, translations) before sharing or acting on them
- [ ] Check that meeting summaries accurately reflect what was said — AI can lose context, misattribute statements, or miss key decisions
- [ ] Do not share meeting recordings or transcripts containing sensitive discussions without first assessing the data classification
- [ ] Be aware that documents from external sources may contain hidden content that could influence how the AI processes them
- [ ] **(enhanced)** For sensitive content: have a second person review AI-generated summaries against the source material
- [ ] **(enhanced)** Check that AI-generated translations preserve the intended meaning, especially for formal or legal content

**After:**

- [ ] Note any issues or learnings for [Step 8](step-8-share.md)

---

[Next: Step 8 — Share and Document Your Learnings >](step-8-share.md)
