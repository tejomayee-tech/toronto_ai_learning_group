## Top Free Small Language Models (SLM) Comparison

The landscape of local LLMs has evolved rapidly, with newer models like the latest iterations of **Gemma**, **Qwen**, and the open-weight release of **GPT-OSS** models offering compelling trade-offs between size, performance, and hardware requirements. The GGUF format, specifically with K-Quantizations, remains the standard for efficient CPU/GPU inference.


Here is a comprehensive, updated table focusing on top-performing small to mid-size LLMs suitable for local deployment (under 10B parameters, or notable larger efficient models).


### 1️⃣ Top General‑Purpose Small Language Models (SLMs)


**Criteria:** under ~10B parameters *or* MoE models with low active parameters, strong local performance, GGUF/Ollama support.

| Model                     | Active Params | License  | Ollama                   | Why It Matters Locally                                    | Best Runtime            | Notes                                      |
| ------------------------- | ------------- | -------- | ------------------------ | --------------------------------------------------------- | ----------------------- | ------------------------------------------ |
| **Llama‑3.1‑8B‑Instruct** | 8B            | Meta     | `ollama run llama3.1:8b` | **Best all‑around local model** (reasoning + code + chat) | Ollama, llama.cpp, vLLM | Community standard, huge tooling ecosystem |
| **Qwen3‑4B‑Instruct**     | 4B            | Apache‑2 | `ollama run qwen3:4b`    | **Best small reasoning model**                            | Ollama, vLLM            | 256K context, multilingual                 |
| **Phi‑3‑Mini (Instruct)** | 3.8B          | MIT      | `ollama run phi3:mini`   | **Top CPU‑only model**                                    | llama.cpp               | Outstanding perf/GB                        |
| **Gemma‑2‑9B**            | 9B            | Gemma    | `ollama run gemma2:9b`   | Fast, efficient, long‑context                             | Ollama                  | Excellent background / agent tasks         |
| **Mistral‑7B‑Instruct**   | 7B            | Apache‑2 | `ollama run mistral:7b`  | Fast, stable baseline                                     | Ollama, vLLM            | Very low latency                           |
| **GPT‑OSS‑20B (MoE)**     | ~3.6B active  | Apache‑2 | `ollama run gpt-oss:20b` | Enterprise‑grade reasoning                                | vLLM                    | CoT + tool calling                         |

✅ **Best General Model Recommendation (Local):**

> **Llama‑3.1‑8B‑Instruct (Q4_K_M)**

---

### 2️⃣ Best Small Model Per Specialized Use Case

#### 🧠 Coding (Best Small Code Model)

| Model                | Size | Why It Wins                               | Hardware            |
| -------------------- | ---- | ----------------------------------------- | ------------------- |
| **Qwen2.5‑Coder‑7B** | 7B   | Best open‑source code reasoning under 10B | 8GB VRAM / 16GB RAM |
| Codestral‑22B        | 22B  | Repo‑level understanding                  | 24GB+ VRAM          |

✅ **Best Small Coder:** **Qwen2.5‑Coder‑7B**

---

#### 👁️ Image → Text (Vision / OCR / VQA)

| Model                    | Size | Capability                  | Runtime            |
| ------------------------ | ---- | --------------------------- | ------------------ |
| **LLaVA‑1.6‑Mistral‑7B** | 7B   | OCR, charts, UI screenshots | Ollama / llama.cpp |
| **Llama‑3.2‑Vision‑11B** | 11B  | Strong multimodal reasoning | Ollama / HF        |

✅ **Best Small Vision Model:** **LLaVA‑1.6‑7B**

---

#### 🎨 Text → Image (Diffusion)

| Model                         | VRAM  | Why It Wins              | Tool    |
| ----------------------------- | ----- | ------------------------ | ------- |
| **SDXL‑Turbo**                | 6–8GB | Fastest high‑quality gen | ComfyUI |
| **Stable Diffusion 3‑Medium** | 10GB  | Best prompt adherence    | ComfyUI |

✅ **Best Small Image Model:** **SDXL‑Turbo** (speed/quality balance)

---

#### 🎙️ Speech → Text (STT)

| Model                | Size  | Strength               | Hardware      |
| -------------------- | ----- | ---------------------- | ------------- |
| **Whisper‑Small**    | 244M  | Accurate, multilingual | CPU/iGPU      |
| **Whisper‑Large‑v3** | 1.55B | Near‑human accuracy    | GPU preferred |

✅ **Best Small STT:** **Whisper‑Small**

---

#### 🔊 Text → Speech (TTS)

| Model       | Strength                     | Notes                   |
| ----------- | ---------------------------- | ----------------------- |
| **XTTS‑v2** | Voice cloning + multilingual | Best open‑source TTS    |
| Piper       | Ultra‑lightweight            | Embedded / Raspberry Pi |

✅ **Best TTS Overall:** **XTTS‑v2**

---

#### 🧩 Embeddings / RAG

| Model                     | Size | Why                       |
| ------------------------- | ---- | ------------------------- |
| **BGE‑Small‑EN‑v1.5**     | 33M  | Fast, accurate embeddings |
| **Nomic‑Embed‑Text‑v1.5** | 137M | Long‑context RAG          |

---

#### 🤖 Agents / Tool‑Use

| Model            | Why                          |
| ---------------- | ---------------------------- |
| **Llama‑3.1‑8B** | Strong tool calling          |
| **GPT‑OSS‑20B**  | Configurable reasoning depth |

---

### 3️⃣ Runtime Tooling (Validated)

| Tool            | Best For                    |
| --------------- | --------------------------- |
| **Ollama**      | Easiest local setup + API   |
| **llama.cpp**   | Best CPU performance        |
| **LM Studio**   | GUI users                   |
| **vLLM**        | High‑throughput GPU serving |
| **ComfyUI**     | Diffusion workflows         |
| **Whisper.cpp** | Ultra‑fast STT              |

---

### 4️⃣ Quantization Recommendation (Local Default)

| Quant      | Recommendation |
| ---------- | -------------- |
| **Q4_K_M** | ✅ Best default |
| Q8_0       | Max quality    |
| Q2_K       | Testing only   |



### Quick Guide to Local Runtime Tools

| Tool Name | Key Functionality | Primary Format | Ideal User/Use Case |
| --- | --- | --- | --- |
| **Ollama** | Single command to pull, run, and serve models (OpenAI-compatible API). | GGUF | **Beginners & Developers.** Easiest setup for Linux/macOS/Windows terminal and API integration. |
| **LM Studio** | All-in-one desktop GUI for model discovery, download, chat, and API serving. | GGUF | **Beginners & Desktop Users.** Graphical interface for exploring and managing models without the command line. |
| **`llama.cpp`** | Core inference engine (C++). Provides best-in-class performance for CPU-based GGUF inference. | GGUF | **Experts & Embedded Users.** Maximum performance optimization, minimal overhead, and portability. |
| **`vLLM`** | High-performance inference engine for maximizing GPU throughput (using PagedAttention). | FP16, AWQ, GPTQ | **High-Throughput Serving.** Running local API for multiple concurrent users or heavy agentic workflows. |
| **TGI** | Hugging Face's Dockerized Text Generation Inference server. Optimized for latency and scalability. | HF Formats | **Production Deployment.** Robust, enterprise-grade serving with Docker/Kubernetes. |
| **`text-generation-webui`** | Browser-based interface (GUI) supporting multiple backends (`llama.cpp`, `vLLM`). | GGUF, HF | **Enthusiasts.** Feature-rich interface for testing, character creation, and RAG. |

---

### GGUF Model Size and Hardware Compatibility (Q4_K_M Quantization)

| Model Name | Parameter Size (Active) | **GGUF File Size (Q4_K_M)** | **Estimated Min VRAM/RAM** | **Ollama Run Command** | **Recommended Hardware Target** |
| --- | --- | --- | --- | --- | --- |
| **Phi-3 Mini (Instruct)** | 3.8 Billion | ≈ 2.4 GB | 6 GB Total (4 GB VRAM) | `ollama run phi3:mini` | **Mac/Laptop CPU/iGPU.** Excellent on-device performance. |
| **Mistral 7B (Instruct)** | 7 Billion | ≈ 4.9 GB | 8 GB VRAM | `ollama run mistral:7b` | **Entry-Level GPU.** Fast inference on most consumer gaming GPUs (e.g., 8GB cards). |
| **Llama 3.1 – 8B (Instruct)** | 8 Billion | ≈ 4.9 GB | 8 GB VRAM | `ollama run llama3.1:8b` | **Mid-Range GPU.** High-quality output on standard gaming PCs. |
| **Llama 3.1 – 70B (Instruct)** | 70 Billion | ≈ 38 GB | 48 GB VRAM | `ollama run llama3.1:70b` | **High-End Workstation/Server.** Requires multiple GPUs (e.g., 2 x 24GB cards). |
| **Mixtral 8x22B (MoE)** | 141B Total (≈39B Active) | ≈ 86 GB | 128 GB Total (76 GB VRAM) | `ollama run mixtral:8x22b` | **High-End Server.** Requires multiple high-VRAM GPUs. |

#### Understanding the Quantization Trade-Off

Quantization reduces the bit-precision of the model's weights, which is what reduces the file size and memory footprint.

| Quantization Type | Bits per Weight | File Size & Quality | Ideal Use Case |
| --- | --- | --- | --- |
| **`F16` (Full Precision)** | 16-bit | **Largest Size (Highest Quality)** | Fine-tuning, production serving with `vLLM` and large VRAM. |
| **`Q8_0`** | 8-bit | Large Size (Near-Lossless Quality) | Max quality inference; requires substantial VRAM (e.g., 12GB+ for 8B model). |
| **`Q4_K_M`** | ≈ 4.8-bit | **Smallest Recommended Size (Good Quality)** | **Recommended Default.** Best balance of speed, quality, and consumer hardware compatibility. |
| **`Q2_K`** | ≈ 2.5-bit | Very Small Size (Lowest Quality) | Extreme memory constraints, mobile devices, or simply testing model architecture. |

This video provides a tutorial on how to [Run Codestral Locally Using Ollama In VS CODE](https://www.youtube.com/watch?v=tlx7MVACT50).