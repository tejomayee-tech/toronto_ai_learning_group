The **Meta-Harness** project, recently released (March/April 2026), is an automated system for "harness engineering." Instead of just optimizing a prompt, it uses an agentic proposer (like Claude Code) to rewrite the actual Python/Bash code that manages an LLM's context, retrieval, and tool usage.

Based on the research paper and the project artifacts from Yoonho Lee (Stanford), here are the details and the step-by-step instructions for implementing the Meta-Harness loop.

---

## Core Architecture
Meta-Harness operates as an **outer-loop optimizer**. It follows a "Filesystem-First" design:
1.  **Filesystem (D):** A growing directory containing every prior candidate's source code, execution logs, and scores.
2.  **Proposer (P):** A coding agent that uses `grep` and `cat` to read past failures and proposes a new version of the harness code.
3.  **Evaluator:** Runs the new harness on a search set and logs the results back to the filesystem.

---

## Step-by-Step Implementation Instructions

If you are looking to set this up using the official [GitHub artifact](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact), follow these steps:

### 1. Environment Setup
You need a coding agent (the paper highlights **Claude Code** or **GPT-OSS**) and a task environment (like TerminalBench-2).
* **Clone the repository:** `git clone https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact`
* **Install dependencies:** Ensure you have the necessary benchmarks and the agentic proposer configured with filesystem permissions.

### 2. Initialize the Filesystem
Create a directory structure to hold the "Evolutionary History."
* **Seed Harness:** Start with a baseline (e.g., a simple zero-shot or few-shot harness).
* **Initial Eval:** Run the baseline and save the output to `history/candidate_000/`. You must save the **full execution trace** (every prompt and model response), not just the final score.

### 3. Configure the Proposer (The "Meta" Step)
The proposer needs a specific "Meta-Prompt" that tells it how to act as an optimizer.
* **Permissions:** Give the agent access to the `history/` directory.
* **Task:** "Analyze the execution traces in `history/`. Identify why the model failed in tasks X and Y. Propose a code change to the harness in `current_harness/` to fix this."

### 4. The Optimization Loop
Run a script to automate the following cycle:
1.  **Search:** The Proposer reads past code and traces $\tau$ from the filesystem.
2.  **Propose:** The Proposer writes a new version of the harness code (e.g., changing how RAG retrieves documents or how the system prompt is formatted).
3.  **Validate:** Run a quick "Interface Validation" to ensure the new code doesn't crash.
4.  **Evaluate:** Run the harness on the search set.
5.  **Log:** Save the new code, the score, and the **uncompressed execution logs** back to the filesystem.

### 5. Final Selection
After $N$ iterations (the paper suggests 20–40 iterations), select the harness from the **Pareto frontier** that best balances:
* **Accuracy:** (Pass rate)
* **Cost:** (Total tokens used)

---

## Performance Summary
| Task | Baseline | Meta-Harness Result | Improvement |
| :--- | :--- | :--- | :--- |
| **Text Classification** | 40.9% (ACE) | **48.6%** | +7.7 pts |
| **Math Reasoning** | Baseline | **+4.7 pts avg** | (Across 5 models) |
| **Agentic Coding** | 28.5% | **46.5%** | (Iterative gain) |

> **Key Takeaway:** Unlike previous optimizers (like TextGrad or OPRO) that use short summaries of performance, Meta-Harness succeeds because it gives the AI agent **raw logs**. The agent can see exactly where a retrieval failed or where a prompt was confusing, allowing it to perform "surgical" code edits.
