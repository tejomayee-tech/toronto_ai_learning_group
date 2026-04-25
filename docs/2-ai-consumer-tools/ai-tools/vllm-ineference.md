# 🚀 vLLM MASTER GUIDE — i5 / i7 (16GB RAM)

---

# 🧭 0. What This Setup Is (and isn’t)

### ✅ What works well

* 1B → 7B models
* Coding assistants (Qwen, TinyLlama, etc.)
* API + VSCode integration
* Fast inference (especially with GPU)

---

### ❌ What does NOT work well

* 14B+ models (unless high VRAM GPU)
* 30B / 70B (forget it on 16GB RAM)
* FP8 / experimental repos

---

# 🧩 1. System Types (choose your path)

---

## 🟢 Case A — CPU only (no GPU)

* vLLM will run ⚠️ but slow
* Use **very small models only (≤3B)**

---

## 🟢 Case B — Laptop with NVIDIA GPU (BEST)

* RTX 3050 / 3060 / 4060 etc.
* vLLM shines here

---

## 🔍 Check GPU

```bash
nvidia-smi
```

---

# 📁 2. Setup Workspace

```bash
mkdir -p ~/vllm
cd ~/vllm
```

---

# 🧪 3. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

---

## ✅ Verify

```bash
which python
```

---

# 💾 4. Fix Storage (VERY IMPORTANT for laptops)

Prevent disk filling:

```bash
nano ~/.bashrc
```

Add:

```bash
export HF_HOME=~/vllm/models
export TRANSFORMERS_CACHE=~/vllm/models
export VLLM_CACHE_ROOT=~/vllm/models
export HUGGINGFACE_HUB_CACHE=~/vllm/models/hub
```

Apply:

```bash
source ~/.bashrc
mkdir -p ~/vllm/models/hub
```

---

# 🔥 5. Install PyTorch

---

## 🟢 CPU version

```bash
pip install torch torchvision torchaudio
```

---

## 🟢 GPU (CUDA)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

## ✅ Verify

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

---

# ⚙️ 6. Install vLLM

```bash
pip install vllm
```

---

# 🧪 7. First Test

```bash
python - << 'EOF'
from vllm import LLM, SamplingParams

llm = LLM(model="facebook/opt-125m")

out = llm.generate(["Hello"], SamplingParams(max_tokens=20))
print(out[0].outputs[0].text)
EOF
```

---

# 🚀 8. BEST MODELS FOR 16GB LAPTOP

---

## 🟢 ULTRA LIGHT (fastest)

* `facebook/opt-125m`
* `TinyLlama/TinyLlama-1.1B`

👉 Use for testing / UI

---

## 🟡 BEST BALANCE (RECOMMENDED)

* **Qwen / Qwen2.5-Coder-3B**
* **Qwen / Qwen2.5-Coder-7B**
* **Mistral AI / Mistral-7B-Instruct-v0.2**

👉 These are your **daily drivers**

---

## 🔴 ONLY IF STRONG GPU (8GB+ VRAM)

* Qwen2.5-Coder-14B-Instruct (tight fit)
* Llama-3-8B

---

# ▶️ 9. RUN vLLM SERVER

---

## ✅ Recommended (3B model)

```bash
vllm serve Qwen/Qwen2.5-Coder-3B \
  --gpu-memory-utilization 0.7 \
  --max-model-len 4096
```

---

## ✅ Better (7B model)

```bash
vllm serve Qwen/Qwen2.5-Coder-7B \
  --gpu-memory-utilization 0.6 \
  --max-model-len 4096
```

---

## ⚠️ If CPU only

```bash
vllm serve TinyLlama/TinyLlama-1.1B
```

---

# 🌐 10. Access UI (IMPORTANT)

---

👉 Open:

```text
http://localhost:8000/docs
```

NOT:

```text
http://localhost:8000
```

---

# 🧪 11. Test API

---

## ✅ Chat request

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen2.5-Coder-3B",
    "messages": [
      {"role": "user", "content": "Write Python code for API"}
    ]
  }'
```

---

# ⚙️ 12. PERFORMANCE TUNING (VERY IMPORTANT)

---

## 🧠 Memory control

```bash
--gpu-memory-utilization 0.5
```

---

## 📏 Reduce context

```bash
--max-model-len 2048
```

---

## ⚡ Throughput

```bash
--max-num-seqs 4
```

---

# 🧨 13. COMMON FAILURES

---

## ❌ OOM (most common)

Fix:

```bash
--gpu-memory-utilization 0.5
--max-model-len 2048
```

---

## ❌ Slow performance

Cause:

* CPU mode

Fix:

* Use GPU OR smaller model

---

## ❌ Model too big

Reality:

👉 16GB RAM ≠ enough for big LLMs

---

# 🔌 14. CONNECT TO VSCode (AGENTIC CODING)

---

Use Continue plugin:

```json
{
  "apiBase": "http://localhost:8000/v1",
  "apiKey": "EMPTY"
}
```

---

# 🧹 15. DELETE MODELS

---

```bash
rm -rf ~/vllm/models/hub/*
```

---

# 🧠 16. STRATEGY FOR THIS MACHINE

---

## Best setup:

👉 3B model for speed
👉 7B model for quality

---

## Smart workflow:

* Coding → Qwen 3B
* Complex tasks → Qwen 7B
* Background tasks → TinyLlama

---

# ⚡ 17. HONEST PERFORMANCE EXPECTATION

---

| Model | Speed              | Quality |
| ----- | ------------------ | ------- |
| 1B    | 🔥 very fast       | low     |
| 3B    | ⚡ fast             | good    |
| 7B    | 🟡 medium          | strong  |
| 14B   | 🐢 slow / unstable | high    |

---

# 💥 FINAL TAKEAWAYS

---

👉 vLLM WILL outperform Ollama on GPU
👉 But ONLY if model fits in memory

👉 Best combo for your machine:

✔️ Qwen2.5-Coder-3B
✔️ Qwen2.5-Coder-7B

---
