# 🚀 vLLM Setup Guide for i5 / i7 Laptops (16GB RAM)

### Efficient Hugging Face Model Inference (No Assumptions)

---

# 🧩 1. System Requirements (STRICT)

Before starting, ensure:

### 💻 Hardware

* Intel i5 / i7 CPU (6+ threads recommended)
* 16 GB RAM
* (Optional) NVIDIA GPU (4–8GB VRAM helps but NOT required)

---

### 🖥️ OS

* Ubuntu 22.04 / 24.04 (recommended)

---

### 🐍 Python

* Python 3.10–3.12

Check:

```bash
python3 --version
```

---

# ⚠️ 2. CRITICAL RULE (MOST IMPORTANT)

> ❗ ALWAYS use a virtual environment
> ❗ NEVER use system Python
> ❗ ALWAYS activate before running anything

---

# 🧪 3. Create Clean Environment (MANDATORY)

```bash
mkdir -p ~/vllm-cpu
cd ~/vllm-cpu

python3 -m venv venv
```

---

## ▶️ Activate environment

```bash
source venv/bin/activate
```

---

## ✅ Verify activation

```bash
which python
```

Expected:

```bash
/home/<user>/vllm-cpu/venv/bin/python
```

---

## Upgrade pip

```bash
pip install --upgrade pip
```

---

# 📦 4. Install PyTorch (CPU or GPU)

---

## 🟢 Option A — CPU ONLY (recommended baseline)

```bash
pip install torch torchvision torchaudio
```

---

## 🟡 Option B — NVIDIA GPU (if available)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

## ✅ Verify installation

```bash
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

---

# 📦 5. Install vLLM

```bash
pip install vllm
```

---

## ✅ Verify

```bash
python -c "import vllm; print('vLLM OK')"
```

---

# 🔐 6. Login to Hugging Face

```bash
pip install huggingface_hub
huggingface-cli login
```

Paste your token.

---

# 🧠 7. FIRST TEST (Minimal Model — MUST PASS)

Run:

```bash
python - << 'EOF'
from vllm import LLM, SamplingParams

llm = LLM(model="facebook/opt-125m")

out = llm.generate(
    ["Hello, my name is"],
    SamplingParams(max_tokens=20)
)

print(out[0].outputs[0].text)
EOF
```

---

## ✅ If this works

👉 Your system is correctly configured

---

# ⚠️ 8. IMPORTANT LIMITATIONS (16GB RAM)

You CANNOT run large models directly.

---

## 🚫 Avoid:

* 13B+ models (OOM)
* FP16 large models
* long context (>4K)

---

## ✅ Use:

* 0.5B → 3B models (best)
* some 7B (with tuning)

---

# 📦 9. Best Models for 16GB Systems

---

## 🟢 Small (FASTEST)

```text
facebook/opt-125m
TinyLlama/TinyLlama-1.1B
```

---

## 🟡 Medium (RECOMMENDED)

```text
microsoft/phi-2
mistralai/Mistral-7B-Instruct-v0.2
```

---

## 🔴 Use carefully

```text
meta-llama/Meta-Llama-3-8B
```

👉 Only with tuning

---

# ▶️ 10. Run API Server (MAIN USAGE)

---

```bash
vllm serve TinyLlama/TinyLlama-1.1B \
  --max-model-len 2048 \
  --gpu-memory-utilization 0.6
```

---

## 🌐 Endpoint

```text
http://localhost:8000
```

---

# 🧪 11. Test API

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "TinyLlama/TinyLlama-1.1B",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

---

# ⚙️ 12. CRITICAL PERFORMANCE SETTINGS (FOR LOW RAM)

---

## 🧠 Reduce memory

```bash
--max-model-len 1024
```

---

## ⚡ Control batching

```bash
--max-num-seqs 2
```

---

## 💾 Reduce GPU/CPU load

```bash
--gpu-memory-utilization 0.5
```

---

# 🧨 13. Common Errors + Fixes

---

## ❌ OOM (out of memory)

Fix:

```bash
--max-model-len 1024
```

or switch to smaller model

---

## ❌ Slow inference

👉 Expected on CPU
👉 Use smaller model

---

## ❌ Module not found

👉 Forgot venv:

```bash
source venv/bin/activate
```

---

## ❌ Hugging Face error

```bash
huggingface-cli login
```

---

# 🔄 14. Daily Workflow (IMPORTANT)

---

## Start session

```bash
cd ~/vllm-cpu
source venv/bin/activate
```

---

## Run model

```bash
vllm serve TinyLlama/TinyLlama-1.1B
```

---

## Stop

CTRL + C

---

# 🚀 15. Performance Expectations

---

## CPU (i5/i7)

| Model | Tokens/sec |
| ----- | ---------- |
| 125M  | 20–50      |
| 1B    | 10–25      |
| 7B    | 2–8        |

---

## With GPU

2–5× faster

---

# 🧠 16. Strategy for Best Results

---

## ✅ DO

* use small models
* reduce context
* run API mode
* batch requests

---

## ❌ DON’T

* run large models blindly
* mix environments
* ignore memory usage

---

# 🔥 17. Advanced Optimization (OPTIONAL)

---

## Run multiple requests (boost throughput)

vLLM shines with batching:

```bash
--max-num-seqs 4
```

---

## Use quantized models (if available)

* AWQ
* GPTQ

---

# 🧠 18. Architecture Insight

---

| Layer  | Tool              |
| ------ | ----------------- |
| Model  | Hugging Face      |
| Engine | vLLM              |
| API    | OpenAI-compatible |

---

# 🏁 FINAL CHECKLIST

---

✅ venv activated
✅ torch installed
✅ vllm installed
✅ HF login done
✅ test model runs
✅ API server working

---

# 💥 FINAL TAKEAWAY

Even on **i5/i7 + 16GB RAM**, you can:

* run real LLMs
* serve APIs
* build AI apps

👉 The key is:

> **small models + correct tuning + vLLM efficiency**

