

## Top Free Small Language Models (SLM) Comparison

The landscape of local LLMs has evolved rapidly, with newer models like the latest iterations of **Gemma**, **Qwen**, and the open-weight release of **GPT-OSS** models offering compelling trade-offs between size, performance, and hardware requirements. The GGUF format, specifically with K-Quantizations, remains the standard for efficient CPU/GPU inference.

Here is a comprehensive, updated table focusing on top-performing small to mid-size LLMs suitable for local deployment (under 10B parameters, or notable larger efficient models).

## 🚀 Top LLMs for Local Use (GGUF/Ollama Focused)

| Model Name (Hugging Face Repo) | P. Size (Active) | License | Key Capabilities (Local Focus) | Primary Local Runtime Tool(s) | Tool Type (Format Focus) | Validation & Use Case Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gemma 3 - 270M** | 270 Million | Gemma | **Ultra-Compact, Edge AI.** Fastest inference on all hardware (including mobile/Raspberry Pi). Basic chat/summarization. | **Ollama**, LM Studio, $\text{llama.cpp}$ | GGUF (CPU/iGPU) | Best for extreme low-resource environments and fast, simple tasks. |
| **Phi-3 Mini (Instruct)** | 3.8 Billion | MIT | **7B-Class Reasoning on 4B Hardware.** Excellent logic, math, and instruction-following on limited memory. | **LM Studio**, Ollama, $\text{llama.cpp}$ | GGUF (CPU/iGPU) | Exceptional performance per parameter. The top choice for CPU-only and on-device privacy. |
| **Qwen3 - 4B-Instruct-2507** | 4 Billion | Tongyi Qianwen | **Multilingual, Long Context (256K).** Strong logic, coding, and **Thinking Mode** for complex tasks. | **Ollama**, LM Studio, $\text{vLLM}$ | GGUF/HF (CPU/GPU) | High quality, extremely versatile, and runs efficiently on consumer GPUs. |
| **Mistral 7B (Instruct)** | 7 Billion | Apache 2.0 | **Speed, Coherence, Tool Calling.** The established benchmark for compact performance. Perfect for API serving. | **Ollama**, $\text{llama.cpp}$, LM Studio, $\text{vLLM}$ | GGUF/HF (CPU/GPU) | Fast single-user experience via GGUF; high-throughput server via $\text{vLLM}$. |
| **Llama 3.1 – 8B (Instruct)** | 8 Billion | Llama | **SOTA Generalist in its Class.** Top-tier reasoning, code generation, and massive community support for resources. | **Ollama**, $\text{vLLM}$, LM Studio, TGI | GGUF/HF (CPU/GPU) | The best balance of quality and resource usage for general-purpose local AI. |
| **Gemma 2 – 9B** | 9 Billion | Gemma | **New Efficiency King, Long Context.** Optimized architecture for speed. Strong math, code, and deep RAG workflows. | **Ollama**, LM Studio, $\text{llama.cpp}$ | GGUF (CPU/iGPU) | Excellent speed/watt, making it ideal for always-on background tasks. |
| **GPT-OSS 20B (MoE)** | 21B Total ($\approx$3.6B Active) | Apache 2.0 | **MoE Efficiency & Enterprise Reasoning.** High-quality tool-use, code, and configurable reasoning effort (CoT). | **vLLM**, Ollama, LM Studio | GGUF/HF (GPU/CPU) | MoE architecture allows high performance to be achieved with lower *active* memory usage. |
| **Mixtral 8x22B (MoE)** | 141B Total ($\approx$39B Active) | Apache 2.0 | **High-End Open Source SOTA.** Best reasoning and quality available on high-end consumer GPUs (multi-GPU or 48GB+ VRAM). | **vLLM**, $\text{llama.cpp}$, TGI | GGUF/HF (GPU) | Requires substantial VRAM, but delivers near-GPT-4 level quality locally. |
| **Codestral-22B** | 22 Billion | M-Code | **Dedicated High-Performance Coder.** Specialized for long-context (32K) code, repo-level understanding, and code generation. | **vLLM**, Ollama, TGI | HF (GPU) | Top-tier local coding assistant; runs well on single high-end GPU (e.g., RTX 4090). |

---

### 📚 Quick Guide to Local Runtime Tools

| Tool Name | Key Functionality | Primary Format | Ideal User/Use Case |
| :--- | :--- | :--- | :--- |
| **Ollama** | Single command to pull, run, and serve models (OpenAI-compatible API). | GGUF | **Beginners & Developers.** Easiest setup for Linux/macOS/Windows terminal and API integration. |
| **LM Studio** | All-in-one desktop GUI for model discovery, download, chat, and API serving. | GGUF | **Beginners & Desktop Users.** Graphical interface for exploring and managing models without the command line. |
| **$\text{llama.cpp}$** | Core inference engine (C++). Provides best-in-class performance for CPU-based GGUF inference. | GGUF | **Experts & Embedded Users.** Maximum performance optimization, minimal overhead, and portability. |
| **$\text{vLLM}$** | High-performance inference engine for maximizing GPU throughput (using PagedAttention). | FP16, AWQ, GPTQ | **High-Throughput Serving.** Running local API for multiple concurrent users or heavy agentic workflows. |
| **TGI** | Hugging Face's Dockerized Text Generation Inference server. Optimized for latency and scalability. | HF Formats | **Production Deployment.** Robust, enterprise-grade serving with Docker/Kubernetes. |
| **text-generation-webui** | Browser-based interface (GUI) supporting multiple backends ($\text{llama.cpp}$, $\text{vLLM}$). | GGUF, HF | **Enthusiasts.** Feature-rich interface for testing, character creation, and RAG. |


## Model's GGUF size & its compatibility with your machine's

The rule of thumb for best performance (fastest speed) is to choose a GGUF file size that is **1-2 GB smaller than your GPU's total VRAM**, to leave space for the KV Cache and system overhead.

Here is a summary table with typical file sizes for the popular **$\text{Q4\_K\_M}$** quantization (which offers a great balance of quality and size) for key models, along with the estimated minimum VRAM and total memory required.

## 💾 GGUF Model Size and Hardware Compatibility (Q4\_K\_M Quantization)

| Model Name | Parameter Size (Active) | **GGUF File Size ($\text{Q4\_K\_M}$)** | **Estimated Min VRAM/RAM** | **Recommended Hardware Target** |
| :--- | :--- | :--- | :--- | :--- |
| **Phi-3 Mini (Instruct)** | 3.8 Billion | $\approx$ 2.4 GB | 6 GB Total (4 GB VRAM) | **Mac/Laptop CPU/iGPU.** Excellent on-device performance. |
| **Mistral 7B (Instruct)** | 7 Billion | $\approx$ 4.9 GB | 8 GB VRAM | **Entry-Level GPU.** Fast inference on most consumer gaming GPUs (e.g., 8GB cards). |
| **Llama 3.1 – 8B (Instruct)** | 8 Billion | $\approx$ 4.9 GB | 8 GB VRAM | **Mid-Range GPU.** High-quality output on standard gaming PCs. |
| **Llama 3.1 – 70B (Instruct)** | 70 Billion | $\approx$ 38 GB | 48 GB VRAM | **High-End Workstation/Server.** Requires multiple GPUs (e.g., 2 x 24GB cards). |
| **Mixtral 8x22B (MoE)** | 141B Total ($\approx$39B Active) | $\approx$ 86 GB | 128 GB Total (76 GB VRAM) | **High-End Server.** Requires multiple high-VRAM GPUs. |

### Understanding the Quantization Trade-Off

Quantization reduces the bit-precision of the model's weights, which is what reduces the file size and memory footprint. 

| Quantization Type | Bits per Weight | File Size & Quality | Ideal Use Case |
| :--- | :--- | :--- | :--- |
| **$\text{F16}$ (Full Precision)** | 16-bit | **Largest Size (Highest Quality)** | Fine-tuning, production serving with $\text{vLLM}$ and large VRAM. |
| **$\text{Q8\_0}$** | 8-bit | Large Size (Near-Lossless Quality) | Max quality inference; requires substantial VRAM (e.g., 12GB+ for 8B model). |
| **$\text{Q4\_K\_M}$** | $\approx$ 4.8-bit | **Smallest Recommended Size (Good Quality)** | **Recommended Default.** Best balance of speed, quality, and consumer hardware compatibility. |
| **$\text{Q2\_K}$** | $\approx$ 2.5-bit | Very Small Size (Lowest Quality) | Extreme memory constraints, mobile devices, or simply testing model architecture. |

