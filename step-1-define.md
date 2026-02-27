# Step 1: Define What You Want to Do

Before assessing risks or choosing tools, clearly describe the specific AI use you are considering. Being precise at this stage makes the rest of the assessment more straightforward.

**Describe your intended use by answering these questions:**

1. **What activity will AI assist with?** Be specific. "Using AI for coding" is too broad. "Using an AI coding assistant to generate unit tests for the payments service" is better.

2. **What data will be involved?** What will you send to or share with the AI tool? This might be source code, user research transcripts, database schemas, or design briefs.

3. **What will you do with the AI's output?** Will it go directly into production? Inform a design decision? Be reviewed and edited first? The further the output is from a human review step, the higher the stakes.

4. **Who is affected?** Just you and your team? End users of the service? Members of the public whose data is being processed?

**Now categorise your use.** Most AI use on delivery projects falls into one of five categories. Some uses may span more than one — if so, assess against each relevant category.

## AI-assisted coding

Using AI tools to help write, complete, review, test, or debug code. This includes code generation from prompts, inline code completion, AI-assisted code review, test generation, and using AI to help debug issues.

The key characteristic is that **AI is generating or modifying code** that may end up in the product.

## AI-assisted code analysis

Using AI to analyse existing codebases — identifying patterns, mapping dependencies, assessing architecture, finding technical debt, detecting security issues, or building understanding of legacy systems.

The key characteristic is that **large volumes of existing code are being sent to the AI tool**, and the output is analytical (findings, assessments, recommendations) rather than code destined for production. This category is distinct from AI-assisted coding because the risk profile is different: the primary concerns are about the sensitivity of the code being shared and the reliability of the analysis, rather than the quality of generated code.

## AI-powered product features

Building AI capabilities into the product or service being delivered — chatbots, content summarisation, document classification, triage systems, recommendation engines, or automated decision support.

The key characteristic is that **AI will directly interact with or affect end users** of the service. This carries the highest governance requirements because of the potential impact on members of the public.

## AI-assisted support

Using AI to help manage support and service desk operations — auto-categorising and routing tickets, suggesting or drafting responses for agents, providing first-line chatbot support, summarising ticket history, generating knowledge base articles, or predicting escalations and SLA risks.

The key characteristic is that **AI is processing operational support data to help teams respond to and resolve requests**. This is distinct from AI-powered product features: support AI is an internal/operational tool that assists the team, whereas product features are capabilities delivered directly to end users. The risks here are about the unpredictable sensitivity of support ticket content (users routinely paste credentials, PII, and system details into tickets), the consequences of incorrect triage or advice, and the potential for automation to act without adequate human oversight.

## AI-assisted research and design

Using AI to support user research synthesis (summarising transcripts, identifying themes), content drafting, translation, design exploration, or accessibility assessment.

The key characteristic is that **AI is informing decisions about what to build and for whom**. The risks here are about the quality and representativeness of insights, and about the handling of research participant data.

---

[Next: Step 2 — Understand What You Are Sharing >](step-2-understand-data.md)
