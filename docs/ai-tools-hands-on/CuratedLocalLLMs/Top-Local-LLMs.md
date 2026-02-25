# Top Free Small Language Models (SLM) Comparison

The landscape of local LLMs continues to evolve rapidly. This updated document reflects **latest stable and widely adopted open‑weight models (early‑2026 ready)**, with a strong focus on **local inference, light fine‑tuning realism, hardware efficiency, and production viability**.

This guide prioritizes:

* Models that **actually run well locally**
* Clear **use‑case mapping**
* Honest **hardware and fine‑tuning limits**
* GGUF / Ollama / vLLM ecosystem maturity

---

## 1️⃣ Top General‑Purpose Small Language Models (SLMs)

**Criteria:**

* ≤10B parameters *or* MoE with low active params
* Strong reasoning + instruction following
* Proven local performance
* GGUF / Ollama / vLLM support

| Model                     | Active Params | License  | Ollama                   | Why It Matters Locally          | Best Runtime            | Notes                     |
| ------------------------- | ------------- | -------- | ------------------------ | ------------------------------- | ----------------------- | ------------------------- |
| **Llama‑3.1‑8B‑Instruct** | 8B            | Meta     | `ollama run llama3.1:8b` | **Best all‑around local model** | Ollama, llama.cpp, vLLM | Strong tools, agents, RAG |
| **Qwen3‑4B‑Instruct**     | 4B            | Apache‑2 | `ollama run qwen3:4b`    | **Best small reasoning model**  | Ollama, vLLM            | 256K context, JSON‑safe   |
| **Phi‑3‑Mini (Instruct)** | 3.8B          | MIT      | `ollama run phi3:mini`   | **Best CPU‑first model**        | llama.cpp               | Excellent perf / GB       |
| **Gemma‑2‑9B‑Instruct**   | 9B            | Gemma    | `ollama run gemma2:9b`   | Fast, efficient, agent‑friendly | Ollama                  | Strong background tasks   |
| **Mistral‑7B‑Instruct**   | 7B            | Apache‑2 | `ollama run mistral:7b`  | Ultra‑stable low latency        | Ollama, vLLM            | Production‑proven         |
| **Qwen2.5‑7B‑Instruct**   | 7B            | Apache‑2 | `ollama run qwen2.5:7b`  | Strong multilingual + reasoning | Ollama                  | Better math than Mistral  |
| **GPT‑OSS‑20B (MoE)**     | ~3.6B active  | Apache‑2 | Partial                  | Enterprise‑grade reasoning      | vLLM                    | Tool calling + CoT        |

✅ **Best General Recommendation (Local Default):**

> **Llama‑3.1‑8B‑Instruct (Q4_K_M)**

---

## 2️⃣ Best Small Model per Specialized Use Case

### 🧠 Coding / Software Engineering

| Model                | Size | Why It Wins                       | Hardware            |
| -------------------- | ---- | --------------------------------- | ------------------- |
| **Qwen2.5‑Coder‑7B** | 7B   | **Best code reasoning under 10B** | 8GB VRAM / 16GB RAM |
| DeepSeek‑Coder‑6.7B  | 6.7B | Excellent completion speed        | 8GB VRAM            |
| Codestral‑22B        | 22B  | Repo‑level understanding          | 24GB+ VRAM          |

✅ **Best Small Coder:** **Qwen2.5‑Coder‑7B**

---

### 👁️ Vision / OCR / Multimodal (Image → Text)

| Model                    | Size | Capability                  | Runtime            |
| ------------------------ | ---- | --------------------------- | ------------------ |
| **LLaVA‑1.6‑Mistral‑7B** | 7B   | OCR, charts, UI screenshots | Ollama / llama.cpp |
| **Llama‑3.2‑Vision‑11B** | 11B  | Strong multimodal reasoning | Ollama / HF        |
| Qwen‑VL‑Chat             | 7B   | Document + chart reasoning  | HF / vLLM          |

✅ **Best Small Vision Model:** **LLaVA‑1.6‑7B**

> Note: For **pure OCR accuracy**, classical OCR + LLM post‑processing still outperforms multimodal‑only models.

---

### 🎨 Text → Image (Diffusion Models)

| Model                         | VRAM  | Why It Wins               | Tool    |
| ----------------------------- | ----- | ------------------------- | ------- |
| **SDXL‑Turbo**                | 6–8GB | Fastest high‑quality gen  | ComfyUI |
| **Stable Diffusion 3‑Medium** | 10GB  | Best prompt adherence     | ComfyUI |
| Flux‑Schnell                  | 8GB   | Very fast creative drafts | ComfyUI |

✅ **Best Small Image Model:** **SDXL‑Turbo**

---

### 🎙️ Speech → Text (STT)

| Model                | Size  | Strength                       | Hardware      |
| -------------------- | ----- | ------------------------------ | ------------- |
| **Whisper‑Small**    | 244M  | Accurate, multilingual         | CPU / iGPU    |
| **Whisper‑Large‑v3** | 1.55B | Near‑human accuracy            | GPU preferred |
| Distil‑Whisper       | ~600M | Faster, slightly less accurate | CPU/GPU       |

✅ **Best Local STT:** **Whisper‑Small**

---

### 🔊 Text → Speech (TTS)

| Model       | Strength                     | Notes                   |
| ----------- | ---------------------------- | ----------------------- |
| **XTTS‑v2** | Voice cloning + multilingual | Best open‑source TTS    |
| Piper       | Ultra‑lightweight            | Embedded / Raspberry Pi |
| Bark‑Small  | Expressive voices            | Higher latency          |

✅ **Best Overall TTS:** **XTTS‑v2**

---

### 🧩 Embeddings / RAG

| Model                     | Size | Why                       |
| ------------------------- | ---- | ------------------------- |
| **BGE‑Small‑EN‑v1.5**     | 33M  | Fast, accurate embeddings |
| **Nomic‑Embed‑Text‑v1.5** | 137M | Long‑context RAG          |
| E5‑Small‑v2               | 33M  | Strong semantic search    |

---

### 🤖 Agents / Tool‑Use

| Model            | Why                           |
| ---------------- | ----------------------------- |
| **Llama‑3.1‑8B** | Best tool calling + ecosystem |
| **Qwen2.5‑7B**   | Strict JSON + schema safety   |
| **GPT‑OSS‑20B**  | Configurable reasoning depth  |

---

## 3️⃣ Runtime Tooling (Validated)

| Tool            | Best For                                    |
| --------------- | ------------------------------------------- |
| **Ollama**      | Easiest local setup + OpenAI‑compatible API |
| **llama.cpp**   | Best CPU inference                          |
| **LM Studio**   | GUI‑first users                             |
| **vLLM**        | High‑throughput GPU serving                 |
| **ComfyUI**     | Diffusion workflows                         |
| **Whisper.cpp** | Ultra‑fast STT                              |

---

## 4️⃣ Quantization Recommendation (Local Default)

| Quant      | Recommendation |
| ---------- | -------------- |
| **Q4_K_M** | ✅ Best default |
| Q8_0       | Max quality    |
| Q2_K       | Testing only   |

---

## 5️⃣ GGUF Model Size & Hardware Compatibility (Q4_K_M)

| Model         | Params | GGUF Size | Min RAM/VRAM | Ollama Command             | Target Hardware |
| ------------- | ------ | --------- | ------------ | -------------------------- | --------------- |
| Phi‑3 Mini    | 3.8B   | ~2.4GB    | 6GB total    | `ollama run phi3:mini`     | Laptop / CPU    |
| Mistral‑7B    | 7B     | ~4.9GB    | 8GB VRAM     | `ollama run mistral:7b`    | Entry GPU       |
| Llama‑3.1‑8B  | 8B     | ~4.9GB    | 8GB VRAM     | `ollama run llama3.1:8b`   | Mid‑range GPU   |
| Llama‑3.1‑70B | 70B    | ~38GB     | 48GB VRAM    | `ollama run llama3.1:70b`  | Multi‑GPU       |
| Mixtral‑8x22B | MoE    | ~86GB     | 128GB total  | `ollama run mixtral:8x22b` | Server‑only     |

---

## 6️⃣ Fine‑Tuning Reality Check (Local)

* Practical LoRA fine‑tuning: **7B–13B max**
* QLoRA requires: **16–24GB VRAM**
* `llama.cpp` & Ollama: **inference only**
* `vLLM`: **inference only (production)**
* Expect diminishing returns beyond small adapters

---

## 7️⃣ Long‑Context Caveats

* Large context ⇒ **KV cache memory explosion**
* Latency rises sharply beyond **32K tokens**
* CPU inference struggles with long context
* Prefer retrieval (RAG) over raw context

---

## 8️⃣ Quick Decision Matrix

| Goal                | Recommended Stack             |
| ------------------- | ----------------------------- |
| Laptop‑only AI dev  | Phi‑3 Mini + llama.cpp        |
| Coding workstation  | Qwen2.5‑Coder‑7B + Ollama     |
| RAG system          | Llama‑3.1‑8B + BGE embeddings |
| AI agents           | Llama‑3.1‑8B + Ollama API     |
| Multimodal analysis | LLaVA‑1.6‑7B                  |

---

**Status:** Updated, production‑realistic, and ready for GitHub / internal reference.
