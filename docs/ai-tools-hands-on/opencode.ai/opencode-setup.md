# **OpenCode.ai** 

OpenCode with local models (via Ollama or LM Studio) transforms your terminal into a private, agentic coding powerhouse.

Since OpenCode uses the Vercel AI SDK, it can connect to any OpenAI-compatible endpoint. Here is the step-by-step tutorial to get it running.

---

## 1. Install OpenCode CLI

The OpenCode CLI is the primary "engine" that interacts with your local models.

* **macOS / Linux:**
```bash
curl -fsSL https://opencode.ai/install | bash

```


* **Windows (via PowerShell):**
```powershell
# Using npm (recommended if you have Node.js)
npm install -g opencode-ai

```



---

## 2. Prepare Your Local Server

You can use either **Ollama** or **LM Studio**. Ensure only one is using the default port (usually `11434` for Ollama or `1234` for LM Studio) at a time.

### Option A: Ollama (Recommended)

1. **Pull the model:** Use Gemma 2 (9B) or Gemma 3 for the best results.
```bash
ollama pull gemma2:9b

```


2. **Verify the endpoint:** Ollama runs automatically on `http://localhost:11434/v1`.

### Option B: LM Studio

1. Search and download **Gemma 2** or **Gemma 3** in LM Studio.
2. Go to the **Local Server** tab (↔️ icon).
3. Click **Start Server**. Note the URL (usually `http://localhost:1234/v1`).

---

## 3. Configure OpenCode

OpenCode needs a configuration file to know where your local "API" is.

1. **Locate the config:** * **Mac/Linux:** `~/.config/opencode/opencode.json`
* **Windows:** `C:\Users\<User>\.config\opencode\opencode.json`


2. **Edit the file:** Add a custom provider entry.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "local-ollama/gemma2",
  "provider": {
    "local-ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama Gemma",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "gemma2": {
          "name": "Gemma 2 (Local)",
          "tool_call": true
        }
      }
    }
  }
}

```

> **Note:** If using **LM Studio**, change the `baseURL` to `http://localhost:1234/v1` and the model ID to match the one loaded in LM Studio.

---

## 4. IDE & Terminal Integration

The goal is to have OpenCode living inside your workflow rather than in a separate window.

### VS Code / Cursor Integration

1. **Install the Extension:** Search for **"OpenCode"** in the VS Code Marketplace and install it.
2. **Launch from Terminal:** Open your project in VS Code, open the integrated terminal (`Ctrl + ``), and type:
```bash
opencode

```


3. **Split View (The "Magic" Key):**
* **Windows/Linux:** Press `Ctrl + Esc`
* **Mac:** Press `Cmd + Esc`
This will open OpenCode in a dedicated side panel inside your IDE, allowing it to "see" your current file and context.



### Terminal Best Practices

* **Plan Mode vs. Build Mode:** Use the **Tab** key to toggle.
* **Plan:** Ask "How would I add a login page?" to get a strategy.
* **Build:** Tell it "Add the login page" to have it actually write files.


* **File Context:** Type `@` in the OpenCode prompt to fuzzy-search and attach specific files to your query.

---

## 5. Optimization for Gemma

Local models can sometimes be "forgetful" with complex tools. To improve Gemma’s performance:

1. **Increase Context:** In Ollama, use `/set parameter num_ctx 16384` to ensure it can read larger files.
2. **Initialize Project:** Run `/init` inside your project folder. This creates an `AGENTS.md` file that helps Gemma understand your specific tech stack.


To unlock the true "agentic" power of Gemma with OpenCode, you need to move beyond simple chat. In an agentic workflow, the AI doesn't just suggest code; it plans, writes, runs tests, and fixes errors in a loop.

Here is the setup for a professional-grade local agentic environment.

# Agentic Coding

## 1. The `AGENTS.md` File

Think of this as the "Onboarding Manual" for your AI. It tells Gemma exactly how to behave in your specific project. Create a file named `AGENTS.md` in your project root:

```markdown
# Project Intelligence: [Project Name]

## Tech Stack
- **Frontend:** React + Tailwind
- **Backend:** Node.js (Express)
- **Testing:** Jest

## Rules & Conventions
- Use functional components only.
- Prefer `async/await` over `.then()`.
- Always include error handling in API routes.

## Local Commands for Agent
- **Build:** `npm run build`
- **Test:** `npm test`
- **Lint:** `npm run lint`

## Project Structure
- `/src/components`: UI components
- `/src/lib`: Logic and utility functions
- `/docs`: Architecture notes

```

> **Pro Tip:** Run `/init` in OpenCode, and it will often help you scaffold this file by scanning your directory.

---

## 2. Setting Up "Agentic" Configuration

To make Gemma act like an agent, you need to define its "Mode" in your `opencode.json`. Agents in OpenCode are usually divided into **Plan** (thinking) and **Build** (doing).

Open your `~/.config/opencode/opencode.json` and add an `agent` section:

```json
{
  "agent": {
    "build": {
      "mode": "primary",
      "model": "local-ollama/gemma2",
      "tools": {
        "write": "allow",
        "bash": "ask",
        "edit": "allow"
      },
      "maxSteps": 10
    },
    "plan": {
      "mode": "primary",
      "model": "local-ollama/gemma2",
      "tools": {
        "read": "allow",
        "bash": "deny"
      }
    }
  }
}

```

* **`write/edit: "allow"`**: Lets the agent modify files without asking every time (speed).
* **`bash: "ask"`**: Important for security! It will ask you before running terminal commands.
* **`maxSteps: 10`**: Tells the agent it can try up to 10 "loops" (Code -> Test -> Fix) to solve a task.

---

## 3. The Agentic Workflow (How to use it)

Once you've run `opencode` in your terminal:

### Step A: The Planning Phase

Start in **Plan** mode (use `Tab` to switch).

* **Prompt:** `How should I implement a search filter for the user list?`
* **Gemma's Action:** It will read your files, find the user list component, and give you a step-by-step strategy without changing your code yet.

### Step B: The Building Phase

Switch to **Build** mode (use `Tab`).

* **Prompt:** `Go ahead and implement that search filter now.`
* **Gemma's Action:** It will write the code to the files.

### Step C: The "Self-Healing" Loop

This is where agentic coding shines.

* **Prompt:** `Run the tests and fix anything that breaks.`
* **Gemma's Action:** 1.  It runs `npm test` via the `bash` tool.
2.  It sees the error log in the terminal.
3.  It realizes it missed an import.
4.  It edits the file to add the import.
5.  It runs the test again until it sees "PASS".

---

## 4. IDE Integration: Using the "Split View"

If you prefer coding in **VS Code**, you don't have to stay in a raw terminal window.

1. Open VS Code and press `Ctrl + ` ` to open the integrated terminal.
2. Type `opencode`.
3. Press **`Cmd + Esc`** (Mac) or **`Ctrl + Esc`** (Windows).
4. **The Sidebar:** OpenCode will pop into a sidebar. You can now type `@filename` to attach a file you are looking at to the conversation, and Gemma will use that context to perform its agentic tasks.

---

## 5. Troubleshooting Local Gemma

If Gemma feels "stuck" or produces garbled tool calls:

* **Memory:** Ensure your local server (Ollama/LM Studio) has at least 8GB of RAM for Gemma 9B.
* **Context:** If your project is huge, Gemma might lose its "memory." Periodically use the `/compact` command to summarize the conversation and free up space.

> You can also write a custom Bash script tool that OpenCode can use to automatically run your specific linting and formatting rules