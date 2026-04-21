# Setting up Playwright's autonomous agents (Planner, Generator, and Healer) with **Claude Code** 

This setup is part of the new agentic testing workflow introduced in Playwright v1.56. 
This workflow leverages the Model Context Protocol (MCP) to allow Claude to interact directly with your browser and codebase.

Here is the step-by-step guide to setting up and using this local agentic loop.

---

## Phase 1: Environment Setup

Before you can run the agents, you need to ensure Playwright and Claude Code are installed and configured to communicate.

1. **Install Playwright (Latest):**
Ensure you are on at least version 1.56.
```bash
npm install -D @playwright/test@latest
npx playwright install

```


2. **Install Claude Code:**
Claude Code is the CLI tool from Anthropic. If you haven't installed it yet:
```bash
npm install -g @anthropic-ai/claude-code

```


3. **Add Playwright MCP to Claude:**
This allows Claude Code to "see" and control the browser via the Model Context Protocol.
```bash
claude mcp add playwright npx @playwright/mcp@latest

```



---

## Phase 2: Initialize Playwright Agents

Playwright provides a specific command to generate the agent definitions (Markdown-based instructions) specifically for the Claude "loop."

1. **Run the Init Command:**
In your project root, run:
```bash
npx playwright init-agents --loop=claude

```


This creates a `.github/chatmodes/` (or similar project-specific) directory containing the system instructions for the **Planner**, **Generator**, and **Healer**.
2. **Create a Seed File (Recommended):**
Create a `seed.spec.ts` file. This acts as a template for the agents, teaching them your specific project's authentication, fixtures, and coding style.

---

## Phase 3: Developing Tests with the Agent Trio

Once initialized, you launch `claude` in your terminal and interact with the specific agents.

### 1. The Planner

**Role:** Explores the app and writes a Markdown test plan.

* **Action:** Launch Claude and say:
> "Use the Playwright **Planner** agent to explore the 'Shopping Cart' flow. Refer to `seed.spec.ts` for auth. Save the plan to `specs/cart-plan.md`."


* **Result:** Claude will open a browser, click through your app, and generate a human-readable Markdown file detailing the test steps.

### 2. The Generator

**Role:** Converts the Markdown plan into executable `.spec.ts` code.

* **Action:** In the same (or new) Claude session:
> "Use the Playwright **Generator** agent to implement the tests described in `specs/cart-plan.md`. Use the Page Object Model (POM) pattern."


* **Result:** Claude will generate the test files and any necessary Page Objects.

### 3. The Healer

**Role:** Fixes tests that fail due to UI changes or flakiness.

* **Action:** If a test fails, tell Claude:
> "Use the Playwright **Healer** agent to run the failing test `tests/cart.spec.ts` and fix any broken locators or timing issues."


* **Result:** The Healer runs the test in a "debug" state, observes why it failed (e.g., a button ID changed), and automatically applies a code fix.

---

### Summary Table: Agent Workflow

| Agent | Input | Output |
| --- | --- | --- |
| **Planner** | URL + User Intent | `test-plan.md` |
| **Generator** | `test-plan.md` | `test.spec.ts` |
| **Healer** | Failing Test Code | Patched/Passing Test Code |

---

### Pro-Tips for Local Deployment

* **Permission Mode:** If you want Claude to work faster without asking for every file edit, you can start it with `claude --permission-mode auto`.
* **Update Agents:** Whenever you update the Playwright npm package, re-run `npx playwright init-agents --loop=claude` to ensure the agents have the latest MCP tool definitions.

Would you like me to help you draft a specific `seed.spec.ts` file for your application to get the agents started correctly?

[Playwright v1.56: From MCP to Playwright Agents](https://www.youtube.com/watch?v=_AifxZGxwuk)
This official video walkthrough demonstrates how to initialize the agentic loop and shows the Planner, Generator, and Healer in action.