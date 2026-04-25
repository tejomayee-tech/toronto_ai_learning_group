# 🚀 vLLM Setup Guide (Ubuntu • i5 / i7 • 16GB RAM)

---

# 🧩 1. System Requirements

### 💻 Hardware

* Intel i5 / i7 (6+ threads recommended)
* 16GB RAM minimum
* Optional GPU (improves speed, not required for small models)

---

### 🖥️ OS

* Ubuntu 22.04 / 24.04

---

### 🐍 Python

* Python 3.10 – 3.12

```bash
python3 --version
```

---

# 📁 2. Create Project Environment

```bash
mkdir -p ~/vllm
cd ~/vllm

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
```

---

# 📦 3. Install PyTorch

---

## CPU Setup (default)

```bash
pip install torch torchvision torchaudio
```

---

## GPU Setup (optional)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

## Verify

```bash
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

---

# 📦 4. Install vLLM

```bash
pip install vllm
```

---

## Verify

```bash
python -c "import vllm; print('vLLM installed')"
```

---

# 🔐 5. Hugging Face Login

```bash
pip install huggingface_hub
huggingface-cli login
```

---

# 💾 6. Model Cache Setup

```bash
mkdir -p ~/vllm/models
```

Add to `~/.bashrc`:

```bash
export HF_HOME=~/vllm/models
export TRANSFORMERS_CACHE=~/vllm/models
export HUGGINGFACE_HUB_CACHE=~/vllm/models/hub
export VLLM_CACHE_ROOT=~/vllm/models
```

Apply:

```bash
source ~/.bashrc
```

---

# 💾 7. Swap Memory Setup (16GB Systems)

---

## Create 16GB swap

```bash
sudo fallocate -l 16G /swapfile
```

If needed:

```bash
sudo dd if=/dev/zero of=/swapfile bs=1G count=16
```

---

## Enable swap

```bash
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

---

## Make permanent

```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

---

## Optimize swap usage

```bash
sudo sysctl vm.swappiness=10
```

Permanent:

```bash
echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf
```

---

# 🧠 8. Model Options (16GB RAM)

---

## 🟢 Fast Models (recommended)

* TinyLlama 1.1B
* OPT 125M
* Qwen 1.5B

---

## 🟡 Balanced Models

* Qwen 3B
* Mistral 7B (with swap)
* Phi-3 mini (if supported)

---

## 🔴 Heavy Models

* Llama 3 8B (swap required, slower)
* Anything above 8B (not practical)

---

# ▶️ 9. Run vLLM Server

---

## 🟢 Small model (best performance)

```bash
vllm serve TinyLlama/TinyLlama-1.1B \
  --max-model-len 2048 \
  --max-num-seqs 2
```

---

## 🟡 Balanced (3B model)

```bash
vllm serve Qwen/Qwen2.5-3B \
  --max-model-len 2048 \
  --max-num-seqs 2
```

---

## 🔴 Large (7B with swap)

```bash
vllm serve Qwen/Qwen2.5-7B \
  --max-model-len 1024 \
  --max-num-seqs 1
```

---

# 🌐 10. API Access

Open:

```text
http://localhost:8000/docs
```

---

# 🧪 11. Test API

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "TinyLlama/TinyLlama-1.1B",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```

---

# ⚙️ 12. Performance Settings

---

## Reduce memory usage

```bash
--max-model-len 1024
```

---

## Limit concurrency

```bash
--max-num-seqs 1
```

---

## General safe config

```bash
--max-num-seqs 2
--max-model-len 2048
```

---

# 🧨 13. Common Issues

---

## Out of memory

Fix:

* reduce model size
* reduce context length
* reduce batch size

---

## Slow performance

Expected on CPU systems
Solution:

* use smaller model

---

## Model fails to load

Fix:

* activate virtual environment
* ensure enough swap enabled

---

# 🔄 14. Daily Workflow

---

## Start

```bash
cd ~/vllm
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

# 🚀 15. Performance Overview

| Model | CPU Speed | Quality |
| ----- | --------- | ------- |
| 125M  | very fast | low     |
| 1B    | fast      | basic   |
| 3B    | balanced  | good    |
| 7B    | slow      | strong  |

---

# 🧠 16. Operating Strategy

---

## Recommended usage

* 1B → testing / quick responses
* 3B → daily coding assistant
* 7B → complex reasoning (swap required)

---

## System rule

* smaller model = stable system
* larger model = slower but higher quality

---

# 🏁 FINAL SUMMARY

This setup supports:

* local LLM inference
* OpenAI-compatible API
* coding assistant workflows
* stable 1B–3B production use
* limited 7B usage with swap

