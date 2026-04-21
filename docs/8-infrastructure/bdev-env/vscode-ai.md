## VS Code with Local AI

---
Setting up **Tab-Autocomplete** (inline suggestions) is a game-changer for a local coding setup. It uses a specialized "Fill-in-the-Middle" (FIM) technique to predict code as you type.

To get this working with **LM Studio**, you need to add a specific section to your `config.yaml` and ensure LM Studio is configured to handle the requests.

---

### 1. Update your `config.yaml`

In VS Code, open your Continue config file (Command Palette → **Continue: View Settings**). Add the `tabAutocompleteModel` block at the **top level** (outside of the `models:` list).

Replace `YOUR_MODEL_ID` with the identifier for your **GPT-OSS 20B** or a smaller model.

```yaml
name: Local Config
version: 1.0.0
schema: v1

# --- TAB AUTOCOMPLETE CONFIGURATION ---
tabAutocompleteModel:
  title: LM Studio Autocomplete
  provider: lmstudio
  model: openai/gpt-oss-20B  # Use your 20B model for now
  apiBase: http://localhost:1234/v1

# (Optional) Tweak performance settings
tabAutocompleteOptions:
  debounceDelay: 350         # Delay in ms before triggering (higher = less lag)
  maxPromptTokens: 1024      # Keeps context small for speed
  multilineCompletions: auto # "always" for bigger suggestions

models:
  - name: GPT-OSS 120B
    provider: lmstudio
    # ... rest of your existing config

```

---

### 2. Tips for a "Snappy" Experience

Autocomplete needs to be **fast** (ideally < 200ms) to feel natural. If the 20B model feels "laggy" while you're typing, here is the professional way to optimize:

1. **Download a "Tiny" Coder Model**:
Search LM Studio for **`Qwen2.5-Coder-1.5B-Instruct`** or **`StarCoder2-3B`**. These models are specifically designed for autocomplete and will give you near-instant suggestions.
2. **Multi-Model Setup (Advanced)**:
If you have high VRAM (e.g., an NVIDIA 3090/4090), LM Studio allows you to load **multiple models** simultaneously. You can run the **120B** in Slot 1 for Chat and the **1.5B** in Slot 2 for Autocomplete.
* *Note:* You will need to change the port for the second model (e.g., `1235`) and update the `apiBase` in the config accordingly.



### 3. Verification Steps

* **Check the Status Bar**: In VS Code, look at the bottom right. You should see a **Continue icon** with a checkmark. Click it to ensure "Enable Tab Autocomplete" is active.
* **The "Read" Fix**: Remember that because we used the `gnome-terminal` fix, you can see the requests hitting LM Studio in real-time in that terminal window. Every time you pause typing, you should see an `/v1/completions` log.


Running two models simultaneously is the "pro" way to use LM Studio and Continue. It allows your high-quality "Chat" model to stay ready for big questions while a lightweight "Autocomplete" model handles your typing suggestions in the background without any lag.

### Step 1: Load Multiple Models in LM Studio

In LM Studio (version 0.3.x), you don't need to start two separate servers. The single server on port `1234` can serve multiple models at once as long as they are both loaded into memory.

1. **Open the Developer Tab**: Click the **Developer** (wrench/code) icon on the left sidebar.
2. **Load Model 1 (Chat)**: In the top model selection dropdown, select your **GPT-OSS 120B** and click **Load Model**.
3. **Load Model 2 (Autocomplete)**: This is the key part. Look for a **"+"** icon or a second model selection slot in the top bar. Select your **Magistral Small** (or a smaller coder model) and load it into this second "slot."
4. **Check Memory**: Watch the "System Resources" monitor. Ensure both models fit within your VRAM (GPU) or System RAM.
> **Tip**: If memory is tight, go to the "GPU Offload" settings for the Autocomplete model and lower the number of layers offloaded to the GPU to keep the main Chat model fast.


5. **Start Server**: Ensure the server is running on `localhost:1234`.

---

### Step 2: Update Continue `config.yaml`

Now, tell Continue which model to use for which task. Open your `config.yaml` in VS Code and use the following structure. Replace `YOUR_USERNAME` with your actual Linux username.

```yaml
name: Local Config
version: 1.0.0
schema: v1

# --- TAB AUTOCOMPLETE (Always Running) ---
tabAutocompleteModel:
  title: Magistral (Fast)
  provider: lmstudio
  # Use the EXACT Model Identifier from the LM Studio Server tab
  model: mistralai/Magistral-Small-2509 
  apiBase: http://localhost:1234/v1

models:
  # --- MAIN CHAT MODEL ---
  - name: GPT-OSS 120B (Heavy)
    provider: lmstudio
    model: openai/gpt-oss-120B
    apiBase: http://localhost:1234/v1
    roles:
      - chat
      - edit
      - apply

  # --- OPTIONAL: SECONDARY CHAT MODEL ---
  - name: GPT-OSS 20B (Balanced)
    provider: lmstudio
    model: openai/gpt-oss-20B
    apiBase: http://localhost:1234/v1
    roles:
      - chat

```

---

### Step 3: Verification

1. **Look at your LM Studio Terminal**: When you type in VS Code, you should see quick "Completion" requests hitting the **Magistral** model.
2. **Open Continue Chat**: When you ask a question in the sidebar, you should see a "Chat" request hitting the **GPT-OSS 120B** model.
3. **Check for "Model Not Found" Errors**: If Continue says it can't find a model, go back to LM Studio's **Server tab**. Look for the **"Model Identifier"** column—that string must match exactly what you typed in the `model:` field in your YAML.

### Why this works

By loading both, LM Studio keeps them both active in your RAM/VRAM. When Continue sends a request, it includes the `model` name. LM Studio sees the name, routes it to the correct loaded instance, and returns the result. This eliminates the "loading..." delay you get when switching models manually.

Would you like me to help you set up a **keyboard shortcut** to quickly toggle autocomplete on and off if it ever gets distracting?

[Using multiple local LLMs at once with LM Studio](https://www.youtube.com/watch?v=OIhf0wbT-FU)

This video explains the most efficient ways to manage and expose multiple models simultaneously using LM Studio's server features.