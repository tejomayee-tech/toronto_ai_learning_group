## GUFF Formats

### What is GGUF format

**GGUF (GPT-Generated Unified Format)** is a single-file format designed to make it easy and efficient to run large language models on consumer hardware, particularly using a CPU or a mix of CPU and GPU. It's a binary format that bundles the model's weights, its architecture, and the tokenizer into one file, so you don't have to manage multiple files. Its main strength is efficient memory usage and support for various levels of **quantization**, which reduces the model's file size.

**Popular GGUF Examples:** Llama 3 (8B and 70B), Mixtral 8x7B, and many fine-tuned models from creators like "TheBloke" on Hugging Face.

### Comparison of GGUF with Other Model Formats

| Format | Purpose & Best Use Case | Popular Examples | Key Advantage |
| :--- | :--- | :--- | :--- |
| **GGUF** | **Inference** on consumer hardware. Optimized for local use via tools like `llama.cpp` and Ollama. | **Llama 3 GGUF**, **Mixtral 8x7B GGUF** (from TheBloke). | **Accessibility:** Runs well on most computers, even without a high-end GPU. |
| **PyTorch / TensorFlow** | **Training and Research**. The original formats used by developers for fine-tuning. | **Meta Llama 3**, **Mistral 7B**, **Gemma 2B** (in their original PyTorch format). | **Flexibility:** The standard for fine-tuning and development, offering full control. |
| **SafeTensors** | **Secure Storage** of model weights. Great for sharing models safely on platforms like Hugging Face. | **Stable Diffusion** models, like DreamShaper and Realistic Vision. | **Safety:** Prevents malicious code from executing when you load the model. |
| **GPTQ, AWQ, EXL2** | **Inference** with extreme efficiency, but typically **GPU-only**. | **Mixtral 8x7B GPTQ**, **Llama 2 AWQ**. | **Speed:** Best performance and lowest VRAM usage if the model fits entirely on the GPU. |

### Ollama for pulling GUFF models

Ollama's model library, which you access with `ollama pull <model_name>`, is built on top of GGUF models. When you pull a model from the Ollama library, it's essentially downloading a GGUF file and its associated manifest and configuration files. This process is handled seamlessly by the `ollama` CLI. 

However, you can also use Ollama to run any GGUF model you've downloaded from other sources, like Hugging Face, by using a `Modelfile`. This gives you the flexibility to use models not yet in the official Ollama library.

***

### Filtering GGUF Models on Hugging Face 🔎

To filter for GGUF models on Hugging Face, you can use the built-in search filters. The easiest way is to use the **`library:gguf`** filter directly in the search bar. This will show you all models that have GGUF files associated with them.

Here's how to do it:

1.  Go to the Hugging Face **Models** page: `huggingface.co/models`.
2.  In the search bar, type `library:gguf` and press Enter.

Alternatively, you can navigate to the **Libraries** filter on the left-hand side of the page and select "GGUF" from the list.

Many popular models on Hugging Face, especially those from creators like TheBloke, are offered in the GGUF format, often with different quantization levels (e.g., Q4_K_M, Q8_0). These are ready to be used with tools like Ollama and `llama.cpp`.
