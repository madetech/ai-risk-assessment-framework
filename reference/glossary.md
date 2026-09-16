# Glossary

Terms are grouped by where you meet them: the assessment itself, then tools, data and law, AI concepts, and roles and standards.

## The assessment

| Term | Definition |
| ---- | ---- |
| **Risk assessment** | The record of a decision to use AI for a specific activity: what it is, what data is involved, which tool, the eight risks rated and mitigated, and who approved it. There is no separate usage log — the assessment *is* the record. One per assessed use. |
| **Use type** | One of the eleven categories of AI use the framework recognises — software development, code analysis, synthetic data generation, product feature, user-facing support, live service operations, user research, design, content, business analysis, general productivity. A thinking aid for finding the right risks quickly, not an exhaustive taxonomy. Recorded in [Step 1](../assess/1-scope.md#categorise-your-use). |
| **Autonomy level** | How much an AI is permitted to do without a person deciding each step: *suggests* (a person does the work), *drafts for review* (a person reviews before it takes effect), *acts with approval* (each action needs sign-off), or *acts autonomously* (no human in the loop per action). It is what the AI is **permitted** to do, not what you intend to let it do. Recorded in [Step 1](../assess/1-scope.md#assess-the-level-of-autonomy). |
| **Risk heatmap** | The table at the start of [Step 3](../assess/3-assess-risks.md#find-the-risks-for-your-use) showing which of the eight risks typically matter most for each use type. A starting point for where to spend effort, not a set of ratings. |
| **Likelihood** | How likely a risk is to materialise: *unlikely*, *possible*, or *likely*. One of the two inputs to a risk rating. |
| **Impact** | How serious the consequence would be if the risk did materialise: *low*, *medium*, or *high*. The other input to a risk rating. |
| **Inherent risk** | The risk level **before any mitigations** — likelihood and impact combined through the matrix in [Step 3](../assess/3-assess-risks.md#4-calculate-the-inherent-rating). Rated on your scope and the tool's design, not on supplier promises or mitigations you plan to apply. The overall inherent level is the highest across the eight risks, and it determines the approval needed. |
| **Residual risk** | The risk level **after mitigations are in place**, rated the same way. It confirms the mitigations are sufficient; it does not reduce what has to be signed off. A residual rating justified by the same fact as the inherent rating has not really moved. |
| **Mitigation** | Something you do that reduces a specific risk's likelihood or its impact. It only counts if it is **additional** to what the inherent rating already assumed — review that the autonomy level already implies has been counted once. |
| **Autonomy adjustment** | The stage in [Step 3](../assess/3-assess-risks.md#3-adjust-for-autonomy) that raises accuracy, accountability, supply chain and prompt injection as autonomy increases, because the heatmap assumes a person reviews the output before it has any effect. Bias moves on impact rather than likelihood. |
| **"Do not proceed"** | The corner of the risk matrix where a likely risk meets a high impact. If a risk sits there after mitigation, find stronger mitigations, change the approach, or do not go ahead. |
| **"Stricter wins"** | Where this framework and a client or department policy differ, the more restrictive position applies by default. A *less* restrictive approach needs a specific, documented exemption approved by the SRO. |

## Tools

| Term | Definition |
| ---- | ---- |
| **Tool profile** | The record of what an AI tool is and what its supplier promises — where data goes, what the tool can reach and do, retention, training, certifications, IP terms. Deliberately facts rather than permissions: a profile does not say what the tool may be used for. See [Step 2](../assess/2-check-tool.md). |
| **Tool register** | The project's set of tool profiles. Being on it means a tool has been assessed and is not excluded — not that any particular use of it is approved. |
| **Excluded** | A tool ruled out whatever you want to use it for: it trains on your inputs, has no adequate data processing agreement, is a consumer tier, or fails a client or department requirement. One of the two decisions in a profile that needs authority. |
| **Highest classification cleared** | The most sensitive data a tool has been signed off to handle. A decision made with authority, not inferred from the tool's facts. Recorded in its profile. |
| **Consumer AI / public AI tools** | Publicly available versions of AI tools (e.g. free ChatGPT, public Claude, Google Gemini free tier) operating under consumer terms. They typically store user inputs and may use them for model training, and must not be used for work-related information. Distinct from enterprise or approved versions of the same products. |
| **Shadow AI** | Use of AI tools without the knowledge or approval of the organisation's governance — that is, use that has never been assessed. |

## Data and law

| Term | Definition |
| ---- | ---- |
| **Data classification** | The [Government Security Classifications Policy](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1166145/Government_Security_Classifications_Policy_June_2023.pdf) categorises government information as OFFICIAL, SECRET, or TOP SECRET, based on the damage that could result from compromise. **‑SENSITIVE is a handling caveat**, applied to a subset of OFFICIAL information, not a fourth classification. |
| **PII** | Personally Identifiable Information. Any data that could be used to identify a specific individual, either directly or in combination with other data. Pseudonymised data is still personal data; only fully anonymised data falls outside UK GDPR. |
| **DPIA** | Data Protection Impact Assessment. A process required under UK GDPR to identify and minimise the data protection risks of a project or system. |
| **EIA** | Equality Impact Assessment. An assessment of how a decision or system affects people with protected characteristics, supporting the public sector equality duty under the Equality Act 2010. |
| **Article 22** | The UK GDPR provision restricting solely automated decisions that have legal or similarly significant effects on individuals. Relevant wherever AI decides rather than advises. |
| **Model card** | A document describing a model's intended use, training data, performance characteristics (including by subgroup), limitations, and ethical considerations. |

## AI concepts

| Term | Definition |
| ---- | ---- |
| **Generative AI (GenAI)** | AI models that generate new content such as text, images, code, or audio. Includes large language models and image generation models. Most AI tools used in delivery work today are generative AI. |
| **LLM** | Large Language Model. A model trained on large amounts of text, capable of generating and understanding natural language. |
| **Machine Learning (ML)** | The broader field of AI that includes systems which learn from data to make predictions, classifications, or decisions. Covers both generative AI and non-generative approaches such as classification, regression, and anomaly detection. |
| **Natural Language Processing (NLP)** | AI techniques for analysing, understanding, and generating human language — transcription, translation, sentiment analysis, summarisation. Increasingly LLM-based, but can also use traditional ML. |
| **Agentic AI** | AI that carries out multi-step tasks by taking actions in real systems — running commands, editing files, calling APIs — rather than only producing output for a person to use. Assessed here through the autonomy level rather than as a separate use type. |
| **RAG** | Retrieval Augmented Generation. A technique where a model retrieves relevant information from a knowledge base before generating a response, improving accuracy and grounding. |
| **Hallucination** | When an AI system generates content that is factually incorrect, fabricated, or unsupported by its input, but presented with apparent confidence. Inherent to current AI, not an occasional bug. |
| **Prompt injection** | An attack where adversarial content manipulates an AI tool into ignoring its instructions, revealing sensitive information, or taking unintended actions. *Direct* injection is when a user crafts their own input to override the AI's instructions. *Indirect* injection is when adversarial content is embedded in material the AI processes (code, documents, tickets, web content) — the attacker does not need direct access to the AI. Ranked #1 on the OWASP Top 10 for LLM Applications (2025). |
| **Red teaming** | Testing a system by simulating adversarial attacks, including prompt injection, to find weaknesses before deployment. |
| **Slopsquatting** | Registering malicious software packages under names that AI coding assistants are known to hallucinate, exploiting the tendency of AI to suggest non-existent packages. |
| **Data poisoning** | Influencing the data a model learns from so that its later behaviour shifts. The analogue of prompt injection for models that are trained rather than prompted. |
| **Synthetic data** | Artificially generated data that stands in for real data, typically for testing, demonstration, or model training. Data generated from real records may still be personal data: it can reproduce real records, or allow individuals to be re-identified by combining fields. |
| **Human-in-the-loop** | A system design where a person reviews and approves AI output before it is acted on or reaches end users. Corresponds to the lower autonomy levels. |

## Roles and standards

| Term | Definition |
| ---- | ---- |
| **SRO** | Senior Responsible Owner. The individual with overall accountability for a programme or project. In this framework, the approving authority for medium- and high-risk uses, for any fully autonomous use, and for the two decisions recorded in a tool profile. |
| **DPO** | Data Protection Officer. The person responsible for overseeing an organisation's data protection strategy and compliance with UK GDPR. |
| **ATRS** | Algorithmic Transparency Recording Standard. A mandatory UK government standard for recording how and why algorithmic tools are used in public services. |
| **NCSC** | National Cyber Security Centre. The UK's technical authority on cyber security; its guidance on prompt injection informs this framework's treatment of that risk. |
| **SAFE-D principles** | An ethical framework for AI developed by the Alan Turing Institute and used by the Ministry of Justice: Sustainability, Accountability, Fairness, Explainability, and Data Responsibility. |
