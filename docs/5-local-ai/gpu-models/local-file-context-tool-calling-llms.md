## Small models with File in Context support

## 🗄️ Most Efficient Small LLMs for 128K Context (File-in-Context RAG)

| Model Name (Hugging Face / Ollama Tag) | P. Size | Context Window | GGUF Size ($\text{Q4\_K\_M}$) | Min VRAM/RAM (Full Context) | Key Capabilities / Focus |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phi-3 Mini 128K Instruct** ($\text{phi3:mini-128k}$) | 3.8 Billion | **128K** Tokens | **$\approx$ 2.4 GB** | **6 GB RAM** (Runs well on CPU/iGPU) | **Ultra-Small RAG.** The smallest, most efficient model capable of 128K context. Exceptional performance/watt for laptops. |
| **Gemma 3 - 4B-IT** ($\text{gemma3:4b}$) | 4 Billion | **128K** Tokens | **$\approx$ 2.5 GB** | **8 GB RAM** (Good for CPU/iGPU) | **Multimodal & Efficient RAG.** Supports text + image input (Multimodal). Excellent all-around performance and reasoning. |
| **Llama 3.1 – 8B Instruct** ($\text{llama3.1:8b}$) | 8 Billion | **128K** Tokens | **$\approx$ 4.9 GB** | **12 GB VRAM/RAM** | **Best Performance/Quality.** Highest quality generalist model for this context size. A safe bet for complex, high-stakes analysis. |
| **Qwen3 - 8B** ($\text{qwen3:8b-instruct}$) | 8 Billion | **131K** Tokens | **$\approx$ 5.2 GB** | **12 GB VRAM/RAM** | **Multilingual Excellence.** Excels in multilingual tasks and has unique "Dual-Mode" operation for flexible reasoning. |

***

### 💡 Why These Models Are Ideal for Local "File in Context"

1.  **Tiny Footprint:** The **Phi-3 Mini** and **Gemma 3 - 4B** models are the breakthrough examples. At just $\approx$2.5 GB GGUF size, they can be run on almost any modern laptop's integrated GPU (iGPU) or even a device with only 8GB of system RAM, making genuine "File in Context" RAG truly accessible.
2.  **Specialized Training:** The search confirms these models are *specifically trained* for long context handling (e.g., Phi-3's 128K variant) to maintain high recall accuracy even deep within the 128K token sequence, which is a known challenge for extending older architectures.
3.  **Efficiency:** Their small parameter count combined with the GGUF quantization means that while they process the large 128K context, the actual memory usage for the weights remains low, leaving enough memory for the enormous Key-Value (KV) cache that a 128K context window requires.

Given your emphasis on **most efficient and smallest size**, the **Phi-3 Mini 128K Instruct** is the current champion for local file-in-context analysis.
