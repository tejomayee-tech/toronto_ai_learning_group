# Claude Code setup to use LMStudio free models - unlimited

## Part 1: Quick Install & Configure

Follow these steps in order to set up the environment from scratch.

### 1. Install Claude Code

Run the official installer for your operating system:

* **macOS / Linux:** `curl -fsSL https://claude.ai/install.sh | bash`
* **Windows (PowerShell):** `irm https://claude.ai/install.ps1 | iex`

### 2. Bypass Onboarding (The "Trick")

Claude Code usually forces a browser login. To bypass this for local use, run this command:

```bash
echo '{"hasCompletedOnboarding": true}' > ~/.claude.json

```

### 3. Create the Settings File

Create a dedicated settings file for LM Studio to keep your local config separate from potential cloud use.

```bash
mkdir -p ~/.claude
nano ~/.claude/lmstudio.settings.json

```

**Paste this exact JSON:**

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:1234/v1",
    "ANTHROPIC_AUTH_TOKEN": "lmstudio",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "ANTHROPIC_MODEL": "default_model"
  }
}

```

### 4. Create a Launch Alias

Add a shortcut to your shell profile (`~/.zshrc` or `~/.bashrc`) so you don't have to remember the flags:

```bash
alias claude-local="claude --settings ~/.claude/lmstudio.settings.json --model default_model"

```

*Reload your shell:* `source ~/.zshrc` (or restart terminal).

---

## Part 2: Validate Your Setup

Before running Claude, run these tests to ensure the bridge is solid.

### Test 1: Is the Server Listening?

Run this to see if LM Studio is broadcasting correctly:

```bash
curl http://localhost:1234/v1/models

```

* **Success:** You see a long JSON list of models.
* **Failure:** `Connection Refused`. **Fix:** Open LM Studio > Local Server > Start Server.

### Test 2: Is the Anthropic Endpoint Active?

Claude Code requires the `/v1/messages` endpoint (introduced in LM Studio 0.4.1+).

```bash
curl http://localhost:1234/v1/messages \
     -H "Content-Type: application/json" \
     -H "x-api-key: lmstudio" \
     -d '{
       "model": "default_model",
       "messages": [{"role": "user", "content": "Hi"}],
       "max_tokens": 10
     }'

```

* **Success:** You get a JSON response with text.
* **Failure:** `404 Not Found`. **Fix:** Ensure your `ANTHROPIC_BASE_URL` in the JSON ends in `/v1`.

---

## Part 3: Troubleshooting Scenarios

| Issue | Symptom | Solution |
| --- | --- | --- |
| **Login Loop** | CLI asks to open browser or "Paste code here." | Your `~/.claude.json` fix failed. Re-run Step 2 in the Install guide. |
| **Model Not Found** | Error: "Model 'default_model' not found." | In LM Studio **Local Server** tab, find your loaded model and set the **Identifier/Alias** field to `default_model`. |
| **Immediate Crash** | CLI starts but crashes after one prompt. | **Context Window** is too small. In LM Studio sidebar, change **Context Length** from 2048 to **32768**. |
| **Permission Denied** | Error when trying to edit files. | Claude Code is strict. Run with `--dangerously-skip-permissions` if you trust your local model. |
| **Laggy/Slow** | Responses take minutes. | 1. Ensure **GPU Offload** is set to Max in LM Studio. 2. Use a smaller model (e.g., `Qwen2.5-Coder-7B` instead of `32B`). |

---

# Reason for Longer promt processing times

Claude Code loops into more tasks because its core **"Agentic Loop"** is designed to be autonomous: it doesn't just answer questions; it explores, plans, implements, and then verifies its own work.

When you give it a task like "fix the bug," it doesn't stop at the code edit. It triggers a multi-step cycle:

1. **Gather Context**: Searches and reads files to understand the problem.
2. **Take Action**: Edits files or runs bash commands.
3. **Verify Results**: Automatically runs tests or linters to ensure its "fix" didn't break anything else.

If the verification fails (e.g., a test fails), Claude views this as a "new task" to solve the failure, restarting the loop.

### Why This Happens More with Local Models (LM Studio)

While Claude 3.7 Sonnet manages this loop gracefully, local models often get "stuck" for a few specific reasons:

* **Context Saturation**: Local models have smaller effective context windows. As the loop grows, the model "forgets" your original instruction or the fact that it already tried a specific fix, causing it to repeat steps.
* **Instruction Adherence**: The "System Prompt" for Claude Code is massive (~16.5k tokens). Local models can get overwhelmed by these instructions, leading them to hallucinate new sub-tasks or "anxiously" over-complicate the solution to satisfy the agentic requirements.
* **Infinite Read Loops**: There is a known behavior where the agent re-reads the same files after context compaction, effectively getting stuck in a "preparation phase" without ever writing code.

---

### How to Break the Loop

To keep your local agent focused and prevent it from "going rogue" into infinite tasks:

* **Use "Plan Mode" (Shift+Tab)**: Always start in Plan Mode. This forces Claude to show you its intended steps *before* it starts executing them, allowing you to prune unnecessary tasks early.
* **Be Hyper-Specific**: Instead of "Improve the auth," say "Add a null check to the login function in `auth.ts`. Do not run full integration tests".
* **Aggressive Context Resets**: Use the `/clear` command between tasks. This wipes the conversation history and prevents "ghost" tasks from previous sessions from influencing the current one.
* **Set Manual Constraints**: Add a "Behavioral Rule" to your `CLAUDE.md` file:
> "You must only perform the specific task requested. Do not initiate refactors or additional tests unless explicitly asked."



Yes, **`CLAUDE.md` should be placed at the root level of your project** (e.g., `~/my-awesome-app/CLAUDE.md`).

Claude Code is designed to look for this specific file at the start of every session to "onboard" itself to your codebase. It acts as the model's primary memory for project-specific rules, tech stack details, and command patterns.

### Why the Root Level?

* **Automatic Discovery**: The CLI automatically pulls this file into context as part of its system prompt.
* **Multi-Level Support**: While the root is the standard, you can also have a "Global" version at `~/.claude/CLAUDE.md` for rules that apply to every project you work on.
* **Modular Sub-folders**: For massive projects (like monorepos), you can place additional `CLAUDE.md` files in subdirectories to provide more granular context for specific modules.

---

### Sample `CLAUDE.md` for Local Models

Since you are using a local model via LM Studio, your `CLAUDE.md` should be more "restrictive" to help the model stay focused and avoid the infinite task loops we discussed.

```markdown
# Project: [Your Project Name]

## Tech Stack
- **Language**: [e.g., Python / TypeScript]
- **Framework**: [e.g., FastAPI / Next.js]
- **Package Manager**: [e.g., pip / bun]

## Development Workflow
- **Build**: `[Your build command]`
- **Test**: `[Your test command]`
- **Lint**: `[Your lint command]`

## Safety & Operational Constraints (CRITICAL)
- **Confirmation Required**: ALWAYS ask for permission before modifying files or running bash commands. Never assume consent for "Yes for this session."
- **Destructive Commands**: You are strictly FORBIDDEN from running `rm -rf` on any directory.
- **Dependency Guard**: Do not install new packages or modify `package.json`/`requirements.txt` without explaining why first.
- **Sensitive Files**: Do not read or output the contents of `.env` files or any file containing "key", "secret", or "password".
- **Infinite Loop Prevention**: If a command fails twice, STOP and ask for guidance. Do not try to "fix" it by guessing.

## Local Model Guidance (Optimization)
- **Conciseness**: Give direct code solutions. Avoid long preambles or "As an AI..." explanations.
- **Verification**: When you finish a task, provide a single bash command I can run to verify the result (e.g., a specific test or `grep`).
- **File Access**: Only read the files directly related to the current task. Do not scan the entire `node_modules` or `dist` folders.

## Project Structure
- `/src`: Application source code
- `/docs`: Project documentation
- `/tests`: Test suites
```

### Pro Tip: Using `/init`

If you want a head start, you can run the command **`/init`** inside the Claude Code terminal.

* **What it does**: It scans your files and generates a customized `CLAUDE.md` for you.
* **Warning**: Since you're on a local model, keep the generated file short (under 150 lines) so it doesn't eat up your context window.
