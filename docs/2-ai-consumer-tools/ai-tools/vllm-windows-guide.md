# 🪟 Windows Guide (i5/i7, 16GB RAM)

## ⚠️ Reality First (IMPORTANT)

* vLLM is **NOT natively supported on Windows**
* You **MUST use Windows Subsystem for Linux (WSL2)**

👉 Think of WSL as “real Linux inside Windows”

---

# 🧩 1. Install WSL2 (MANDATORY)

Open PowerShell **as Administrator**:

```powershell
wsl --install
```

Restart your system.

---

## ✅ Verify

```powershell
wsl
```

You should see a Linux terminal.

---

# 🐧 2. Setup Ubuntu inside WSL

Inside WSL terminal:

```bash
sudo apt update && sudo apt upgrade -y
```

---

## Install Python + tools

```bash
sudo apt install python3 python3-venv python3-pip git -y
```

---

# 🧪 3. Create Clean Environment

```bash
mkdir -p ~/vllm
cd ~/vllm

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

---

# 📦 4. Install PyTorch

---

## CPU version (safe default)

```bash
pip install torch torchvision torchaudio
```

---

## GPU (ONLY if you configured WSL CUDA)

👉 Requires:

* NVIDIA GPU
* WSL CUDA drivers installed

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

# 📦 5. Install vLLM

```bash
pip install vllm
```

---

# 🔐 6. Login to Hugging Face

```bash
pip install huggingface_hub
huggingface-cli login
```

---

# 🧠 7. Test Model

```bash
python - << 'EOF'
from vllm import LLM, SamplingParams

llm = LLM(model="facebook/opt-125m")

out = llm.generate(["Hello"], SamplingParams(max_tokens=20))
print(out[0].outputs[0].text)
EOF
```

---

# ▶️ 8. Run API Server

```bash
vllm serve TinyLlama/TinyLlama-1.1B --max-model-len 1024
```

---

## 🌐 Access from Windows browser

```
http://localhost:8000
```

---

# ⚠️ Windows Pitfalls

| Problem               | Fix               |
| --------------------- | ----------------- |
| vLLM fails on Windows | Use WSL           |
| GPU not detected      | Install WSL CUDA  |
| Slow performance      | Use smaller model |

---

# 🧠 Windows Summary

👉 Best architecture:

```
Windows → WSL (Linux) → vLLM → Hugging Face models
```

---
