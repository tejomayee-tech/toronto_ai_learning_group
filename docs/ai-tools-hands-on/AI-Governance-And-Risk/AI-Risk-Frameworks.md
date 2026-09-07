## AI Governance and Risk Frameworks 

AI governance is the operating system for making AI accountable: defining who may build or approve an AI use case, what risks are acceptable, what evidence is required, and how the system is monitored and corrected after release. For your background, treat it as an extension of QE, DevSecOps, model risk management, and production SRE—not as a policy-only function. Your hands-on experience with local models, Kubernetes, CI/CD, agent workflows, and enterprise testing is directly relevant.

A strong starting framework is the NIST AI Risk Management Framework (AI RMF), which organizes work into four connected functions: **Govern, Map, Measure, and Manage**. It is voluntary and intended to incorporate trustworthiness into AI design, development, use, and evaluation. [airc.nist](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

## Core frameworks to know

| Framework | What it contributes | Practical artifact |
|---|---|---|
| NIST AI RMF | A lifecycle model: establish accountability, understand context, assess risks, then treat and monitor them.  [airc.nist](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | AI system inventory, risk register, evaluation evidence, incident process |
| NIST GenAI Profile | A GenAI-focused application of AI RMF—useful for RAG, copilots, agents, hallucinations, misuse, and content risks. | Threat and misuse cases, grounding evaluation suite |
| ISO/IEC 42001 | AI management-system standard: governance roles, policies, controls, continual improvement. | Auditable AI management system and control mapping |
| EU AI Act | Regulatory risk-based approach; high-risk systems need lifecycle risk management, documentation, logging, human oversight, accuracy, robustness, and cybersecurity controls.  [ai-act-service-desk.ec.europa](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9) | Compliance assessment, technical file, traceability and monitoring records |
| OWASP GenAI/LLM guidance | Application-security lens for prompt injection, data leakage, insecure tool use, excessive agency, and supply-chain threats. | AI threat model and red-team test suite |

Do not start by trying to “implement a framework.” Start with one AI system and produce evidence that you understand its purpose, users, data, failure modes, approvals, and production behavior.

## Open-source tool stack

- **Observability and audit evidence:** **Langfuse** is self-hostable and supports traces, evaluations, datasets, prompt management, metrics, and OpenTelemetry-oriented integrations. Use it to record agent/tool calls, model versions, prompts, latency, cost, and evaluation outcomes. [github](https://github.com/langfuse/langfuse)
- **LLM security testing:** **NVIDIA garak** is an LLM vulnerability scanner that probes for issues including prompt injection, data leakage, jailbreaks, hallucination, misinformation, and unsafe outputs. Treat it like security regression testing for models and AI applications. [github](https://github.com/NVIDIA/garak)
- **Model supply-chain security:** **ModelScan** scans common serialized model formats for unsafe code, helping reduce risk when ingesting third-party ML artifacts. [github](https://github.com/protectai/modelscan)
- **Fairness for classical ML:** **Fairlearn** and IBM **AIF360** provide metrics and mitigation approaches for group fairness, especially for classification and regression systems where protected-group outcome analysis is appropriate. [verifywise](https://verifywise.ai/de/ai-governance-library/open-source-projects)
- **Evaluation harnesses:** Add application-specific tests for groundedness, answer quality, refusal behavior, tool-authorization boundaries, PII exposure, and agent task completion. A governance program needs repeatable tests, not one-time demos.

For Ollama/vLLM environment, a practical baseline is: instrument an application with OpenTelemetry and Langfuse; run deterministic eval datasets in CI; run garak before releases; scan any downloaded model artifact; store reports alongside GitLab pipeline evidence. [github](https://github.com/langfuse/langfuse)
