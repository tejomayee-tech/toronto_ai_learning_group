# 🚀 vLLM MASTER GUIDE — Windows (i5 / i7 • 16GB RAM)

---

# 🧭 0. What This Setup Is (and isn’t)

## ✅ What works well

* 1B → 7B parameter models
* Coding assistants (Qwen, TinyLlama, Mistral 7B)
* Local OpenAI-compatible API server
* VSCode integration (Continue / Copilot-style workflows)
* Fast inference *if model fits memory*

---

## ❌ What does NOT work well

* 14B+ models on 16GB RAM
* Very large context models (>8K) on CPU-only setups
* Heavy multi-user workloads
* Experimental quantization pipelines inside vLLM on Windows

---

# 🧩 1. Important Reality (Windows)

vLLM is primarily Linux-native. On Windows, you have 2 workable paths:

---

## 🟢 Option A — Native Windows (limited but works)

* Works for experimentation
* Best for **CPU inference or light GPU setups**

---

## 🟢 Option B — WSL2 (recommended)

* Most stable way to run vLLM on Windows
* Near-native Linux performance
* Required for GPU acceleration in most cases

👉 If unsure, use WSL2.

---

# 🖥️ 2. Install Required Tools

---

## 🧰 Install Python

Install Python 3.10 or 3.11:

* [https://www.python.org/downloads/](https://www.python.org/downloads/)

During install:

✔ Add Python to PATH

---

## 🧰 Install Git

* [https://git-scm.com/download/win](https://git-scm.com/download/win)

---

## 🧰 (Recommended) Install WSL2

PowerShell (Admin):

```powershell
wsl --install
```

Restart PC.

---

# 📁 3. Create Workspace

### PowerShell:

```powershell
mkdir $HOME\vllm
cd $HOME\vllm
```

---

# 🧪 4. Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade pip
```

---

## ✅ Verify Python

```powershell
python --version
where python
```

---

# 💾 5. Prevent Disk Overflow (VERY IMPORTANT)

Set Hugging Face cache location:

### PowerShell:

```powershell
setx HF_HOME "$HOME\vllm\models"
setx TRANSFORMERS_CACHE "$HOME\vllm\models"
setx HUGGINGFACE_HUB_CACHE "$HOME\vllm\models\hub"
setx VLLM_CACHE_ROOT "$HOME\vllm\models"
```

Restart terminal.

---

Create folders:

```powershell
mkdir $HOME\vllm\models\hub
```

---

# ⚙️ 6. Install PyTorch

---

## 🟢 CPU version (default Windows setup)

```powershell
pip install torch torchvision torchaudio
```

---

## 🟡 GPU (only if WSL2 + compatible drivers installed)

```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

## ✅ Verify

```powershell
python -c "import torch; print(torch.__version__)"
```

---

# 🔥 7. Install vLLM

```powershell
pip install vllm
```

---

# 🧪 8. First Test (tiny model)

```powershell
python - << 'EOF'
from vllm import LLM, SamplingParams

llm = LLM(model="facebook/opt-125m")

out = llm.generate(
    ["Hello from vLLM on Windows"],
    SamplingParams(max_tokens=20)
)

print(out[0].outputs[0].text)
EOF
```

---

# 🚀 9. BEST MODELS FOR 16GB WINDOWS LAPTOP

---

## 🟢 ULTRA LIGHT (instant response)

* `facebook/opt-125m`
* `TinyLlama/TinyLlama-1.1B`

👉 Use for testing & API validation

---

## 🟡 BEST BALANCE (RECOMMENDED)

* `Qwen/Qwen2.5-Coder-3B`
* `Qwen/Qwen2.5-Coder-7B`
* `mistralai/Mistral-7B-Instruct-v0.2`

👉 Best real-world usability on 16GB RAM

---

## 🔴 BORDERLINE (may struggle)

* 7B models with long context
* Anything above 7B on CPU-only setups

---

# ▶️ 10. RUN vLLM SERVER

---

## 🟡 Recommended (3B model)

```powershell
vllm serve Qwen/Qwen2.5-Coder-3B `
  --gpu-memory-utilization 0.6 `
  --max-model-len 4096
```

---

## 🟡 Better quality (7B model)

```powershell
vllm serve Qwen/Qwen2.5-Coder-7B `
  --gpu-memory-utilization 0.5 `
  --max-model-len 4096
```

---

## 🟢 CPU fallback

```powershell
vllm serve TinyLlama/TinyLlama-1.1B
```

---

# 🌐 11. Access API

Open in browser:

```
http://localhost:8000/docs
```

This is your interactive API dashboard.

---

# 🧪 12. Test API (Chat Completion)

```powershell
curl http://localhost:8000/v1/chat/completions `
  -H "Content-Type: application/json" `
  -d '{
    "model": "Qwen/Qwen2.5-Coder-3B",
    "messages": [
      {"role": "user", "content": "Write a Python FastAPI example"}
    ]
  }'
```

---

# ⚙️ 13. PERFORMANCE TUNING (IMPORTANT)

---

## 🧠 Reduce memory usage

```bash
--gpu-memory-utilization 0.4
```

---

## 📏 Reduce context length

```bash
--max-model-len 2048
```

---

## ⚡ Increase throughput (light models only)

```bash
--max-num-seqs 4
```

---

# 🧨 14. COMMON ISSUES (Windows reality)

---

## ❌ Out of Memory (OOM)

Fix:

* Use 3B model
* Reduce context:

```bash
--max-model-len 2048
--gpu-memory-utilization 0.4
```

---

## ❌ vLLM not installing

Fix:

* Use WSL2 (recommended)
* Ensure Python 3.10–3.11

---

## ❌ Very slow responses

Cause:

* CPU-only inference

Fix:

* Use smaller model (1B–3B)

---

# 🔌 15. VSCode Integration

Install **Continue extension**, then set:

```json
{
  "apiBase": "http://localhost:8000/v1",
  "apiKey": "EMPTY"
}
```

Now VSCode behaves like a local AI coding assistant.

---

# 🧹 16. Clean Up Models

```powershell
Remove-Item -Recurse -Force $HOME\vllm\models\hub\*
```

---

# 🧠 17. STRATEGY FOR i5 / i7 (16GB RAM)

---

## 🎯 Recommended workflow

| Task             | Model     |
| ---------------- | --------- |
| Fast coding help | 3B model  |
| Better reasoning | 7B model  |
| Lightweight chat | TinyLlama |

---

## 🧠 Smart usage pattern

* Daily coding → 3B model
* Debugging logic → 7B model
* Quick prompts → 1B model

---

# ⚡ 18. REALISTIC PERFORMANCE EXPECTATION

---

| Model | Experience         |
| ----- | ------------------ |
| 125M  | instant but weak   |
| 1B    | very fast          |
| 3B    | optimal balance    |
| 7B    | usable but heavier |
| 14B+  | not practical      |

---

# 💥 FINAL TAKEAWAY

---

✔ vLLM works well on Windows **if models are kept small**
✔ 3B is the sweet spot for most users
✔ 7B is the upper limit for stable daily use
✔ WSL2 improves everything significantly

---
