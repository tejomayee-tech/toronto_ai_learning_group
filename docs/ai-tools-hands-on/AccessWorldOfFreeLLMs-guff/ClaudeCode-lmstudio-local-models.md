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
