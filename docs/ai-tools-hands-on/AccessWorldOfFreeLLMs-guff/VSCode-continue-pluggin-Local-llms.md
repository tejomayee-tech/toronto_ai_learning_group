# VSCode Continue Plugin - Local LLMs

## Using **Ollama Service** local models with the **Continue VS Code extension**


#### 1\. Start the Ollama Server

Before configuring Continue, ensure the Ollama server is running on your machine.

  * **Open your terminal** and run the command: `ollama serve` (or ensure the Ollama desktop application is running in the background, as it typically starts the server automatically).

#### 2\. Open the Continue Configuration File

The easiest way to access the correct file is through the Continue sidebar in VS Code:

1.  **Open VS Code** and navigate to the **Continue Sidebar** (usually the spiral/infinity icon in the Activity Bar).
2.  In the Continue panel, look for the **Agent Selector** dropdown (it might say "Default Assistant" or your current model name).
3.  Click the Agent Selector, and then click the **gear icon ($\text{⚙️}$)** next to the **"Local Config"** option.
      * *This action will open the correct `config.yaml` file.*

#### 3\. Insert the Ollama Model Configuration

Once `config.yaml` is open, you will find a section for defining models.

1.  **Locate the `models:` section.** It should look like this:

    ```yaml
    models:
    ```

2.  **Paste your provided configuration** directly under the `models:` key, ensuring proper YAML indentation (two spaces for each level):

    ```yaml
    models:
      # --- ADD THIS AUTODETECT ENTRY ---
      - name: Ollama Autodetect Models # This is the display name in VS Code
        provider: ollama
        model: AUTODETECT             # This tells Continue to scan Ollama
        apiBase: http://localhost:11434
        roles:
          - chat
          - edit
          - apply
    ```

3.  **Save the `config.yaml` file.**

#### 4\. Select the New Model in Continue

The Continue extension should automatically detect the changes and refresh the model list.

1.  Go back to the **Continue Sidebar** in VS Code.
2.  Click the **Agent Selector** dropdown again.
3.  You should now see the new entry: **"Ollama Autodetect Models"** (or whatever you set for the `name:` field).
4.  **Select this new entry.**

-----


## Using **LM Studio** local models with the **Continue VS Code extension**

Unfortunately, **Continue does not have a direct, built-in `provider: lmstudio`** option like it does for `provider: ollama`.

However, you can often connect to LM Studio by treating it as a **standard OpenAI-compatible API server** if you run it in that mode.

Here is the most common way to configure your `config.json` (or `~/.continue/config.json`) file to connect to LM Studio:

### 🛠️ Connecting to LM Studio via OpenAI Provider

LM Studio's local server runs an API that is designed to be compatible with the OpenAI API format. You will use the `openai` provider and point the `apiBase` to your LM Studio server's address.

1.  **Start the Server in LM Studio:**

      * Open LM Studio.
      * Go to the **"Local Server"** tab (usually the 4th icon down).
      * Select the model you want to use.
      * Make sure the **"OpenAI Compatible Server"** option is enabled (or that the server is generally running on the expected port).
      * By default, the server usually runs on **`http://localhost:1234`**.

2.  **Add the Configuration to your `config.json`:**

      * Modify the `models:` section of your Continue config file (usually called `config.json` or `config.yaml` depending on your setup) to include this entry:

<!-- end list -->

```yaml
# ----------------------------------------
# REQUIRED HEADER
# ----------------------------------------
name: Local Config
version: 1.0.0
schema: v1

# ----------------------------------------
# MODELS SECTION
# ----------------------------------------
models:
  # LM Studio Qwen3-Coder-30B Configuration
  - name: LM Studio Qwen3 Coder 30B          # Descriptive display name
    provider: openai                         # Use 'openai' provider for LM Studio API
    model: qwen/qwen3-coder-30b              # The model identifier for Qwen3-Coder-30B
    apiBase: http://localhost:1234/v1        # Default LM Studio server address + /v1 path
    apiKey: not-needed
    roles:
      - chat
      - edit
      - apply

  # --- Include your Ollama Autodetect entry here if you are using it as well ---
  # - name: Ollama Autodetect Models 
  #   provider: ollama
  #   model: AUTODETECT             
  #   apiBase: http://localhost:11434
  #   roles:
  #     - chat
  #     - edit
  #     - apply
```

### 📝 Key Differences from Your Ollama Config

| Feature | Your Ollama Config | LM Studio (via OpenAI) Config | Reason |
| :--- | :--- | :--- | :--- |
| **Provider** | `ollama` | `openai` | Continue uses the `openai` provider to connect to any OpenAI-compatible API, which includes LM Studio. |
| **API Base** | `http://localhost:11434` | `http://localhost:1234/v1` | This is the default port for the LM Studio server, and the `/v1` path is often required for OpenAI compatibility. |
| **Model** | `AUTODETECT` | Specific Name | LM Studio doesn't have an autodetect feature in Continue; you must define each model you want to use. |

-----

### ➡️ Next Steps

1.  **Confirm the Port:** Double-check in the **LM Studio Local Server tab** what port it is running on. If it's not `1234`, change the `apiBase` in the config accordingly.
2.  **Restart VS Code:** After saving your Continue config, you may need to reload your VS Code window for the changes to take effect.
3.  **Select the Model:** The new name ("LM Studio Model...") should now appear in the model selection dropdown within the Continue pane in VS Code.
