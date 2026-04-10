This is your "Clean Sheet" guide. We’ve filtered out the noise and errors from our previous attempts to give you a perfect baseline for your **i5 Latitude**.

### 🏗️ Phase 1: The Linux Engine (Ubuntu)
Before coding, the underlying "brain" must be correctly set up to handle 2026's security and performance requirements.

1.  **Download the Engine:**
    ```bash
    wget https://lmstudio.ai/download/latest/linux/x64?format=AppImage -O ~/Downloads/LM_Studio.AppImage
    chmod +x ~/Downloads/LM_Studio.AppImage
    ```
2.  **Fix the Ubuntu Sandbox Wall:**
    Ubuntu 24.04+ blocks AppImages by default. Run this to allow the AI to start:
    ```bash
    sudo sysctl -w kernel.unprivileged_userns_clone=1
    # Make it permanent
    echo 'kernel.unprivileged_userns_clone=1' | sudo tee /etc/sysctl.d/99-appimage-sandbox.conf
    ```
3.  **Bootstrap & Start:**
    Open the GUI first to let it initialize, then go to the terminal:
    ```bash
    lms bootstrap
    lms server start
    ```

---

### 📦 Phase 2: Model & Environment (uv)
We will use **uv** for speed and the specific **Gemma 2 2B** build optimized for local memory.

1.  **Download the Model:**
    ```bash
    lms get lmstudio-community/gemma-2-2b-it-GGUF
    ```
2.  **Set up your Python Project:**
    ```bash
    mkdir ~/turbo_project && cd ~/turbo_project
    uv init
    uv venv --python 3.12
    source .venv/bin/activate
    uv add lmstudio
    ```

---

### 📜 Phase 3: The Validated Python Script
This is the **"2026 Scoped Client"** version that successfully bypassed the connection errors and attribute bugs.

**File: `run_turbo.py`**
```python
import lmstudio as lms

# 1. Use the Scoped Client (Zero-Config v1.5.0)
print("Connecting to LM Studio...")

with lms.Client() as client:
    model_path = "lmstudio-community/gemma-2-2b-it-GGUF"
    
    try:
        # 2. load_new_instance (The replacement for .load)
        print(f"Loading {model_path} with TurboQuant 3-bit...")
        model = client.llm.load_new_instance(
            model_path,
            config={
                "kv_cache": {"type": "turboquant_3bit"},
                "gpu": {"ratio": 0}  # Force CPU for i5 benchmark
            }
        )
        print("Model is ready!")

        # 3. Inference with Result Extraction
        prompt = "Explain why local AI is secure in one sentence."
        response = model.respond(prompt)
        
        # Accessing content via .content is the 1.5.0 standard
        print(f"\nAI: {response.content}")
        
    except Exception as e:
        print(f"Error: {e}")
```
**To Run:** `uv run run_turbo.py`



---

### 📉 Post-Mortem: What Failed (and Why)
| Error / Issue | Why it happened | The Fix |
| :--- | :--- | :--- |
| **"No valid installation found"** | The CLI couldn't find the `.AppImage` engine. | Manual download and `lms bootstrap`. |
| **"Chrome-sandbox aborting"** | Ubuntu's new kernel security blocked the app. | `kernel.unprivileged_userns_clone=1`. |
| **`AttributeError: .load`** | The SDK (v1.5.0) renamed the loading method. | Used `load_new_instance` instead. |
| **`unexpected keyword 'host'`** | `Client()` now uses zero-config/auto-discovery. | Removed `host="localhost"` from the call. |
| **"Port not yet resolved"** | The script was too fast for the network sync. | Used the `with lms.Client()` scoped pattern. |

### 🚀 Next Step: Android Integration
Now that you have this working on Ubuntu, you can confidently move this `run_turbo.py` logic into your **Chaquopy** setup. Your Kotlin code will act as the "UI wrapper" that calls this Python logic.

**Would you like me to help you draft the `MainActivity.kt` code to display this TurboQuant response in your app UI?**