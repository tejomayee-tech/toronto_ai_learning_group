# Top Free Small Language Models (SLM) Comparison (March 2026 Update)

The landscape of local LLMs has evolved from dense models to high-efficiency **Thinking MoE** architectures. This guide reflects the **Q1 2026 frontier**, focusing on "Thinking" vs. "Non-Thinking" modes and the rise of visual agents.

---

## 1️⃣ Top General-Purpose Small Language Models (SLMs)

| Model | Active Params | License | Ollama / CLI | Why It Matters Locally | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Qwen 3.5‑Medium** | **~12B (MoE)** | Apache-2 | `ollama run qwen3.5:12b` | **New 2026 SOTA for mid-range** | Native "Thinking" mode; beats Llama-3 70B |
| **Llama‑4‑Scout** | **~9B (MoE)** | Meta | `ollama run llama4:scout` | **Fastest Reasoning** | 1M+ context; ultra-low latency |
| **Qwen 3.5‑9B** | 9B | Apache-2 | `ollama run qwen3.5:9b` | Best for Agentic workflows | Superior JSON & tool-calling stability |
| **Llama‑3.1‑8B** | 8B | Meta | `ollama run llama3.1:8b` | The "Gold Standard" Compatibility | Best ecosystem support (Tools/RAG) |
| **Mistral‑NeMo‑12B**| 12B | Apache-2 | `ollama run mistral-nemo` | Native 128K context | Collaborative build with NVIDIA |
| **Phi‑4‑Mini** | 3.8B | MIT | `ollama run phi4:mini` | **Best Sub-4B Reasoning** | Surprising math/logic for its size |

✅ **Best General Recommendation:** > **Qwen 3.5‑Medium (12B MoE)** for performance; **Llama‑4‑Scout** for speed/context.

---

## 2️⃣ Best Small Model per Specialized Use Case

### 🧠 Coding / Software Engineering
| Model | Size | Why It Wins | Hardware |
| :--- | :--- | :--- | :--- |
| **Qwen 3‑Coder‑Next** | 14B / 30B | **Top-tier Repo-level logic** | 12GB - 24GB VRAM |
| **Llama 4 Maverick** | ~10B | Best integration with IDE Agents | 12GB VRAM |
| **Qwen 2.5‑Coder‑7B** | 7B | Best "Legacy" Ultra-Light Coder | 8GB VRAM |

✅ **Best Small Coder:** **Qwen 3‑Coder‑Next (14B)**

---

### 👁️ Vision / Visual Agents (New Category)
*Qwen 3.5 has introduced "Visual Agentic" abilities—allowing models to identify and interact with UI elements.*

| Model | Size | Capability | Key Feature |
| :--- | :--- | :--- | :--- |
| **Qwen 3.5‑VL** | 7B / 14B | UI Control & Detailed OCR | Native "Agentic" UI reasoning |
| **Llama 3.2‑Vision** | 11B | Standard Image-to-Text | Excellent for general captions |
| **Moondream 3** | <2B | Tiny Mobile/Edge Vision | Runs on almost anything |

✅ **Best Visual Agent:** **Qwen 3.5‑VL (7B)**

---

### 🎙️ Speech & Audio (Multimodal)
| Model | Size | Strength |
| :--- | :--- | :--- |
| **Qwen 2.5‑Omni** | 7B | Native Audio-In/Audio-Out |
| **Whisper‑Large‑v3‑Turbo** | 1.5B | 2026 Standard for STT speed |
| **Sana‑1.1** | ~600M | High-fidelity TTS at low latency |

---

## 3️⃣ Key Technical Shifts in 2026

### 💡 The "Thinking" Switch
Most 2026 models (Qwen 3.5, Llama 4 Scout) support a **Thinking Mode** (Chain-of-Thought).
* **Enable Thinking:** High accuracy for Math/Code, but 2x-3x higher latency.
* **Disable Thinking:** Near-instant "Chat" mode for general queries.

### 🖼️ Diagram-as-Code (DaC) Preference
For technical documentation, these models now favor **Mermaid** and **D2** syntax natively over basic text descriptions.

---

## 4️⃣ Updated Hardware Cheat Sheet (Q4_K_M Quants)

| Model | Params | GGUF Size | Min RAM/VRAM | Ideal Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Phi-4 Mini** | 3.8B | ~2.6GB | 8GB (Laptop) | Basic logic / Mobile |
| **Llama-4 Scout** | 9B (MoE) | ~5.8GB | 12GB VRAM | Daily Driver / Fast RAG |
| **Qwen 3.5 Med** | 12B (MoE) | ~8.2GB | 16GB VRAM | Heavy Coding / Logic |
| **Mistral NeMo** | 12B | ~8.0GB | 16GB VRAM | Large Document RAG |

---
