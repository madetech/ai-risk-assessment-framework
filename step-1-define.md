# Step 1: Define What You Want to Do

Before assessing risks or choosing tools, clearly describe the specific AI use you are considering. Being precise at this stage makes the rest of the assessment more straightforward.

**Describe your intended use by answering these questions:**

1. **What activity will AI assist with?** Be specific. "Using AI for coding" is too broad. "Using an AI coding assistant to generate unit tests for the payments service" is better.

2. **What data will be involved?** What will you send to or share with the AI tool? This might be source code, user research transcripts, database schemas, or design briefs.

3. **What will you do with the AI's output?** Will it go directly into production? Inform a design decision? Be reviewed and edited first? The further the output is from a human review step, the higher the stakes.

4. **Who is affected?** Just you and your team? End users of the service? Members of the public whose data is being processed?

## Types of AI

Before categorising your use, it helps to understand the types of AI involved. Different types have different risk profiles:

- **Generative AI (GenAI)** — models that generate new content such as text, images, or code. This includes most of the AI tools used in delivery work today (ChatGPT, Claude, Gemini, GitHub Copilot, Microsoft 365 Copilot). The key risks are hallucination (plausible but wrong outputs), data leakage (what you share becomes an input to a third-party service), and prompt injection.

- **Large Language Models (LLMs)** — a subset of generative AI focused on text. Most coding assistants, chatbots, and summarisation tools are LLM-based. LLMs have specific risks around prompt injection (because they cannot distinguish instructions from data) and hallucination (because they generate statistically plausible text, not verified facts).

- **Machine Learning (ML)** — the broader category that includes classification, prediction, anomaly detection, and pattern recognition. ML models may not be generative — they may classify inputs or predict outcomes. The risk profile is different: bias and fairness are typically higher concerns, while prompt injection is less relevant (though data poisoning applies).

- **Natural Language Processing (NLP)** — text analysis, transcription, translation, and sentiment analysis. These capabilities are increasingly LLM-based, but can also use traditional ML. The risks depend on the underlying technology and what data is being processed.

Many tools combine multiple types. A support ticket triage system might use an LLM for summarisation and a traditional ML model for classification. Assess the risks of each component.

## Categorise your use

Most AI use on delivery projects falls into one of six categories. Some uses may span more than one — if so, assess against each relevant category.

## AI-assisted coding

Using AI tools to help write, complete, review, test, or debug code. This includes code generation from prompts, inline code completion, AI-assisted code review, test generation, and using AI to help debug issues.

The key characteristic is that **AI is generating or modifying code** that may end up in the product.

Common tools: GitHub Copilot, Cursor, Claude Code, Amazon CodeWhisperer.

## AI-assisted code analysis

Using AI to analyse existing codebases — identifying patterns, mapping dependencies, assessing architecture, finding technical debt, detecting security issues, or building understanding of legacy systems.

The key characteristic is that **large volumes of existing code are being sent to the AI tool**, and the output is analytical (findings, assessments, recommendations) rather than code destined for production. This category is distinct from AI-assisted coding because the risk profile is different: the primary concerns are about the sensitivity of the code being shared and the reliability of the analysis, rather than the quality of generated code.

Common tools: Claude, ChatGPT Enterprise, Gemini, SonarQube AI.

## AI-powered product features

Building AI capabilities into the product or service being delivered — chatbots, content summarisation, document classification, triage systems, recommendation engines, or automated decision support.

The key characteristic is that **AI will directly interact with or affect end users** of the service. This carries the highest governance requirements because of the potential impact on members of the public.

Common tools: Claude API, Azure OpenAI Service, AWS Bedrock, Google Vertex AI.

## AI-assisted support

Using AI to help manage support and service desk operations — auto-categorising and routing tickets, suggesting or drafting responses for agents, providing first-line chatbot support, summarising ticket history, generating knowledge base articles, or predicting escalations and SLA risks.

The key characteristic is that **AI is processing operational support data to help teams respond to and resolve requests**. This is distinct from AI-powered product features: support AI is an internal/operational tool that assists the team, whereas product features are capabilities delivered directly to end users. The risks here are about the unpredictable sensitivity of support ticket content (users routinely paste credentials, PII, and system details into tickets), the consequences of incorrect triage or advice, and the potential for automation to act without adequate human oversight.

Common tools: Microsoft Copilot for Service, Zendesk AI, ServiceNow AI.

## AI-assisted research and design

Using AI to support user research synthesis (summarising transcripts, identifying themes), content drafting, translation, design exploration, or accessibility assessment.

The key characteristic is that **AI is informing decisions about what to build and for whom**. The risks here are about the quality and representativeness of insights, and about the handling of research participant data. Be aware that AI-generated summaries can lose important context — always validate against the source material.

Common tools: Claude, ChatGPT Enterprise, Otter.ai, Dovetail.

## AI-assisted general productivity

Using AI for routine office tasks — drafting or summarising reports, emails, and meeting notes; transcribing meetings and calls; translating documents; generating images for presentations; extracting data from documents; or formatting and restructuring content.

The key characteristic is that **AI is assisting with everyday work tasks** that are not code, research, or product development. This may seem low-risk, but the same risk assessment applies. Meeting transcriptions may contain sensitive discussions, PII, or commercially confidential information. Email drafts may inadvertently include information that should not be shared. AI tools used for these tasks often require additional permissions — such as access to calendars, meetings, or contact lists — that must be identified, controlled, and monitored.

Common tools: Microsoft 365 Copilot, ChatGPT Enterprise, Claude, Google Gemini for Workspace.

---

[Next: Step 2 — Understand What You Are Sharing >](step-2-understand-data.md)
