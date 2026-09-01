# DGX Spark model collection

## 2025:

```text
Qwen
├── qwen2.5:3b
├── qwen2.5:7b
├── qwen2.5:14b
├── qwen2.5-coder:7b
├── qwen2.5-coder:14b
├── qwen2.5-coder:32b
├── qwen3:14b
├── qwen3.6:27b
├── qwen3.6:35b
├── qwen3.6:35b-a3b
├── qwen3.8:27b
├── qwen3-coder
├── qwen3-coder:30b
├── qwen3-coder-next
└── qwen3-coder-next:q4_K_M

Gemma
├── gemma4:e2b
├── gemma4:e4b
├── gemma4:12b
├── gemma4:26b
└── gemma4:31b

Coding
├── codeqwen:7b
├── codegeex4:9b
├── starcoder2:15b
├── codegemma:7b
├── deepseek-coder:6.7b
├── deepseek-coder:33b
├── deepseek-coder-v2:16b
├── codellama:70b
└── codestral:22b

Reasoning / general
├── deepseek-r1:32b
├── gpt-oss:120b
├── glm-4.7-flash
├── nemotron-3-super
└── dolphin-mixtral:8x22b
```

# 🔥 The models I would add first

## Tier 1 — Highest priority

### 1. `nemotron-3.5-lightning`

This is probably my **#1 recommendation for your Spark**.

It's a:

```text
30B total parameters
3B active parameters
MoE
```

NVIDIA describes it as being designed for **always-on agents**. Ollama currently lists it as a local model with tools and thinking capabilities. ([Ollama][2])

Why it's particularly interesting on your machine:

```text
Your current:
qwen3.6:35b-a3b

New:
nemotron-3.5-lightning
30B / 3B active
```

This gives you an excellent opportunity to compare **Qwen's 3B-active architecture against NVIDIA's newer Nemotron MoE architecture**.

**Install:**

```bash
ollama pull nemotron-3.5-lightning
```

---

# 2. `laguna-xs-2.1`

This one is extremely interesting for your **agentic coding experiments**.

It's:

```text
33B total
3B active
MoE
```

and Ollama specifically describes it as being designed for **agentic coding and long-horizon work on a local machine**. ([Ollama][2])

That makes it a much more interesting Spark model than another generic 30B dense model.

```bash
ollama pull laguna-xs-2.1
```

---

# 3. `north-mini-code-1.0`

Another model I would definitely add.

```text
30B total
3B active
MoE
Agentic software engineering
```

It is Cohere's developer-oriented model specifically designed for agentic software engineering. ([Ollama][2])

For your Playwright/C#/NUnit/API/framework work, this is particularly relevant.

```bash
ollama pull north-mini-code-1.0
```

---

# 4. `qwen3.5:27b`

This is probably the biggest Qwen-family hole in your current list.

You have:

```text
qwen3.6
qwen3.8
qwen3-coder
qwen3-coder-next
```

but you're missing the **Qwen3.5 family**.

Ollama currently lists:

```text
qwen3.5:0.8b
qwen3.5:2b
qwen3.5:4b
qwen3.5:9b
qwen3.5:27b
qwen3.5:35b
qwen3.5:122b
```

with vision, tools and thinking capabilities. ([Ollama][2])

For your Spark:

```bash
ollama pull qwen3.5:27b
```

would be my first Qwen3.5 installation.

---

# 5. `qwen3.5:35b`

I'd also test the 35B version.

Your current:

```text
qwen3.6:35b
qwen3.6:35b-a3b
```

gives you a great baseline.

Adding:

```text
qwen3.5:35b
```

lets you construct a very useful Qwen evolution benchmark:

```text
Qwen3.5 35B
       ↓
Qwen3.6 35B
       ↓
Qwen3.8 27B
       ↓
Qwen3-Coder 30B
       ↓
Qwen3-Coder-Next
```

That's much more valuable than simply collecting models.

---

# 6. `glm-5.3-flash`

This is another **very high-priority** addition.

Ollama currently describes GLM-5.3-Flash as a natively multimodal model with **18B active parameters**, aimed at coding and agentic workloads. ([Ollama][2])

Your existing:

```text
glm-4.7-flash
```

makes this particularly interesting because you can directly compare:

```text
GLM-4.7 Flash
       ↓
GLM-5.3 Flash
```

I'd definitely put it on your Spark.

```bash
ollama pull glm-5.3-flash
```

---

# 7. `muse-glimmer`

Another newer 30B local-agent model.

Ollama describes it as a **30B model for always-on local agents**, with tool use, long tasks and failure recovery. ([Ollama][2])

That makes it relevant to the kind of local autonomous coding/automation environment you're building.

```bash
ollama pull muse-glimmer
```

---

# 8. `qwen3.8-flash-next`

This is more experimental.

Ollama currently describes it as an **experimental preview of the architecture that will underpin Qwen4**, with vision, tools and thinking. ([Ollama][2])

Given that you're experimenting with cutting-edge local inference, I'd absolutely test it.

```bash
ollama pull qwen3.8-flash-next
```

But I wouldn't use it as your primary production coding model yet.

Think:

**research/benchmark model**, not necessarily **daily driver**.

---

# 9. `kimi-k3`

Kimi K3 is another newer multimodal agentic model.

Ollama lists it as:

```text
native multimodal
agentic
open-weight
vision
tools
thinking
```

([Ollama][2])

This is worth testing on the Spark because your 128 GB memory gives you substantially more headroom than ordinary consumer systems.

---

# 10. `minimax-m3`

This is another interesting omission.

Ollama currently describes MiniMax M3 as:

> Coding & Agentic Frontier

and lists a **1M-token context window** plus native multimodality. ([Ollama][2])

For long-running coding-agent experiments, that's potentially much more interesting than another conventional chat model.

---

# 🧠 The REALLY interesting part: 120B models

This is where your DGX Spark becomes different from most local AI machines.

You already have:

```text
gpt-oss:120b
```

That's excellent.

But you're missing some other large models that are worth investigating.

## `qwen3.5:122b`

Ollama currently lists a 122B Qwen3.5 variant. ([Ollama][2])

This is exactly the sort of model your 128 GB Spark makes interesting.

However, **don't assume "128 GB RAM = 122B model fits comfortably."**

You still need memory for:

* model weights
* KV cache
* runtime
* CUDA/driver overhead
* context
* application processes

So I'd treat it as a **benchmark/large-model experiment**, not something I'd leave running continuously.

---

# `nemotron-3-super`

You already have:

```text
nemotron-3-super:latest
```

And I would **keep it**.

Ollama currently describes it as:

```text
120B total
12B active
MoE
```

designed for complex multi-agent applications. ([Ollama][2])

That's actually one of the most appropriate models for your DGX Spark.

Your current collection therefore already has an excellent large-MoE model.

---

# 🏆 My recommended DGX Spark collection

Rather than downloading everything, I'd build this **focused benchmark fleet**.

## A. Coding / Software Engineering

```text
qwen3-coder:30b
qwen3-coder-next
qwen3.6:35b
qwen3.6:35b-a3b
qwen3.8:27b

north-mini-code-1.0
laguna-xs-2.1
nemotron-3.5-lightning

glm-5.3-flash
muse-glimmer
```

This would be an **excellent agentic coding laboratory**.

---

# B. General reasoning

I'd use:

```text
qwen3.8:27b
qwen3.6:35b
gemma4:31b
deepseek-r1:32b

gpt-oss:120b
nemotron-3-super
```

Your `gpt-oss:120b` and `nemotron-3-super` are particularly valuable because they give you a large-model tier.

---

# C. Multimodal

Your collection should become:

```text
gemma4:31b
qwen3.5:27b
qwen3.5:35b
qwen3.8:27b
glm-5.3-flash
kimi-k3
```

This is an area where your current collection has more room for improvement.

---

# D. Experimental / bleeding edge

I'd have:

```text
qwen3.8-flash-next
qwen3.5:122b
kimi-k3
muse-glimmer
```

These are the models I'd use to investigate where local models are going rather than necessarily using them every day.

---

# ⭐ My final priority list for YOUR Spark

If you don't want to fill 128 GB with dozens of models, install these first:

| Priority | Model                      | Why                                     |
| -------: | -------------------------- | --------------------------------------- |
|       🥇 | **nemotron-3.5-lightning** | 30B/3B MoE, agentic, NVIDIA ecosystem   |
|       🥈 | **laguna-xs-2.1**          | 33B/3B MoE, local agentic coding        |
|       🥉 | **north-mini-code-1.0**    | 30B/3B MoE, software engineering        |
|        4 | **qwen3.5:27b**            | New Qwen multimodal baseline            |
|        5 | **qwen3.5:35b**            | Stronger Qwen3.5 comparison             |
|        6 | **glm-5.3-flash**          | New multimodal/agentic GLM              |
|        7 | **muse-glimmer**           | Local agent / failure recovery          |
|        8 | **qwen3.8-flash-next**     | Experimental Qwen4 architecture preview |
|        9 | **kimi-k3**                | Multimodal agentic model                |
|       10 | **qwen3.5:122b**           | Big Spark experiment                    |

---

# 🚀 And here's how I'd organize your Spark

You don't actually need to think of the DGX Spark as an "Ollama model box."

I'd use it as a **local AI benchmark and agent platform**:

```text
                    DGX SPARK
                   128 GB Unified
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Ollama          SGLang          vLLM
          │              │              │
      Quick tests    High perf       Serving
          │              │              │
          └──────────────┼──────────────┘
                         │
                  Model Benchmark
                         │
        ┌────────────────┼────────────────┐
        │                │                │
      Coding          Reasoning        Agents
        │                │                │
     Qwen/North       GPT-OSS        Nemotron
     Laguna/GLM       DeepSeek       Qwen
                                      GLM
```

This is particularly relevant because NVIDIA currently provides DGX Spark workflows for **vLLM, SGLang, llama.cpp, speculative decoding and Nemotron**, rather than positioning Spark as simply an Ollama appliance. ([NVIDIA NIM APIs][3])

And you've already been investigating **DFlash/DSpark**, which makes this even more relevant. There are current DGX Spark experiments showing Qwen3.8 27B reaching roughly **34 tok/s with SGLang + NVFP4 + DSpark**, compared with roughly 27 tok/s using llama.cpp + MTP in the same reported test. ([NVIDIA Developer Forums][4])

So I'd actually recommend **not replacing your existing Ollama collection**. Keep Ollama for convenient model management, but start benchmarking your best models through **SGLang/vLLM + NVIDIA's optimized inference paths**.

### My "golden 10" for your DGX Spark

If I were setting up your exact machine today, I'd make these the core collection:

```text
1. qwen3.8:27b
2. qwen3.6:35b-a3b
3. qwen3-coder-next
4. nemotron-3.5-lightning
5. laguna-xs-2.1
6. north-mini-code-1.0
7. glm-5.3-flash
8. gemma4:31b
9. nemotron-3-super
10. gpt-oss:120b
```

And then keep these as **experimental models**:

```text
qwen3.5:27b
qwen3.5:35b
qwen3.5:122b
qwen3.8-flash-next
muse-glimmer
kimi-k3
```

That gives you a much more purposeful DGX Spark lab: **small-active MoE vs dense models, coding vs reasoning, 30B vs 120B, multimodal vs text-only, and Ollama vs SGLang/vLLM/DSpark inference.** ([Ollama][2])

[1]: https://developer.nvidia.com/topics/ai/local-ai?utm_source=chatgpt.com "NVIDIA Local AI: Build and Run AI on Your GPU"
[2]: https://ollama.com/library?sort=newest&utm_source=chatgpt.com "library"
[3]: https://build.nvidia.com/spark/vllm?utm_source=chatgpt.com "vLLM for Inference"
[4]: https://forums.developer.nvidia.com/t/qwen3-8-27b-at-34-38-tok-s-on-dgx-spark-open-source-one-command-setup-sglang-nvfp4-dspark/380257?utm_source=chatgpt.com "Qwen3.8-27B at 34–38 tok/s on DGX Spark — open-source one-command setup (SGLang + NVFP4 + DSpark)"
