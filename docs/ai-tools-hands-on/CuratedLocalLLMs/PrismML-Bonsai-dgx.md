# **DGX Spark running PrismML Bonsai locally**, the cleaner architecture is:

```
                 Claude Code CLI
                       |
                       |
          ANTHROPIC_BASE_URL
                       |
                       |
        PrismML llama-server (Anthropic API)
                       |
                       |
              Bonsai-27B Q1_0
                       |
                       |
                 DGX Spark GPU
```

The key point:

**Claude Code does not need OpenAI API compatibility if your backend exposes the Anthropic Messages API.** Claude Code is designed around Anthropic's API format and can route through custom gateways using `ANTHROPIC_BASE_URL`. ([Claude Platform Docs][1])

So the preferred setup is:

1. Run PrismML Bonsai server
2. Enable Anthropic-compatible endpoint
3. Point Claude Code directly to it
4. Set local model name

No LiteLLM required.

---

# Correct DGX Spark + Claude Code Architecture

## Final Design

```
+----------------------+
| Claude Code CLI      |
|                      |
| MCP                  |
| Skills               |
| File Editing         |
| Terminal Commands    |
+----------+-----------+
           |
           |
           |
 ANTHROPIC_BASE_URL
           |
           |
+----------v-----------+
| PrismML llama-server |
|                      |
| /v1/messages         |
| Anthropic API        |
+----------+-----------+
           |
           |
+----------v-----------+
| Bonsai 27B Q1_0      |
| CUDA Enabled         |
+----------+-----------+
           |
           |
+----------v-----------+
| NVIDIA DGX Spark     |
| Blackwell GPU        |
+----------------------+
```

---

# Step 1 - Install Claude Code

On DGX Spark:

```bash
npm install -g @anthropic-ai/claude-code
```

Verify:

```bash
claude --version
```

---

# Step 2 - Build PrismML llama.cpp

Clone:

```bash
cd ~/models

git clone https://github.com/PrismML-Eng/Bonsai-demo.git

cd Bonsai-demo
```

Set:

```bash
export BONSAI_FAMILY=bonsai
export BONSAI_MODEL=27B
```

Run:

```bash
./setup.sh
```

---

# Step 3 - Verify Model

Find:

```bash
find . -name "*.gguf"
```

Example:

```
./models/Bonsai-27B-Q1_0.gguf
```

---

# Step 4 - Start llama-server

For DGX Spark:

```bash
./build/bin/llama-server \
-m ./models/Bonsai-27B-Q1_0.gguf \
-ngl 999 \
-c 32768 \
--host 0.0.0.0 \
--port 8080
```

Explanation:

| Option        | Purpose        |
| ------------- | -------------- |
| `-ngl 999`    | GPU all layers |
| `-c 32768`    | 32K context    |
| `--port 8080` | local API      |

---

# Step 5 - Verify Server

Test:

```bash
curl http://localhost:8080/health
```

Expected:

```
OK
```

---

# Step 6 - Configure Claude Code

Create:

```bash
mkdir -p ~/.claude

nano ~/.claude/settings.json
```

Add:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:8080",
    "ANTHROPIC_AUTH_TOKEN": "local",
    "ANTHROPIC_MODEL": "Bonsai-27B-Q1_0"
  }
}
```

Claude Code supports endpoint overrides through `ANTHROPIC_BASE_URL`, with authentication configured through environment variables such as `ANTHROPIC_AUTH_TOKEN`. ([Claude][2])

---

# Step 7 - Disable Cloud Calls

For a fully local setup:

```bash
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```

Add permanently:

```bash
nano ~/.bashrc
```

Add:

```bash
export ANTHROPIC_BASE_URL=http://localhost:8080
export ANTHROPIC_AUTH_TOKEN=local
export ANTHROPIC_MODEL=Bonsai-27B-Q1_0
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```

Reload:

```bash
source ~/.bashrc
```

---

# Step 8 - Start Claude Code

Navigate to your project:

```bash
cd ~/projects/my-csharp-framework
```

Run:

```bash
claude
```

You should now have:

```
Claude Code
     |
     |
Bonsai-27B
     |
     |
DGX Spark GPU
```

---

# Step 9 - Verify Model Routing

Inside Claude Code:

```
/status
```

You should see:

```
Model:
Bonsai-27B-Q1_0

Endpoint:
localhost:8080
```

Claude Code supports `/model` and model configuration through environment variables/settings. ([Claude Help Center][3])

---

# Step 10 - Recommended DGX Spark Settings

For coding agents:

```bash
-ngl 999
```

Context:

```
32768
```

Temperature:

```
0.2
```

Max tokens:

```
8192
```

---

# Optional: Enable DSpark

Unlike your Dell, DGX Spark has enough memory.

Run:

```bash
export BONSAI_USE_DSPARK=true
```

Then:

```bash
./scripts/run_llama.sh --draft
```

Expected:

* higher tokens/sec
* lower latency

---

# Claude Code + Bonsai Best Practices

## Good prompts

Example:

```
Analyze this repository.

1. Identify architecture
2. Find SOLID violations
3. Suggest refactoring
4. Create implementation plan
```

---

## For your C# automation framework

Your setup is actually a very good fit:

```
Claude Code
 |
 |
Bonsai 27B
 |
 |
C# Repository
 |
 |
Reqnroll
Selenium
RestSharp
NUnit
PostgreSQL
```

Use commands like:

```
Review this API automation framework.

Check:
- SOLID violations
- Dependency Injection
- Test maintainability
- Configuration design
- Reporting architecture
```

---

# Why this is better than LiteLLM

Previous architecture:

```
Claude Code
 |
LiteLLM
 |
llama-server
 |
Bonsai
```

Pros:

* multiple models
* routing
* enterprise auth

Cons:

* extra moving part
* extra latency
* unnecessary for one DGX Spark

For your use case:

**Direct Claude Code → PrismML server is the better design.**

---

The one thing I would verify before finalizing is whether your specific PrismML llama-server build exposes:

```
/v1/messages
```

(Anthropic format)

or only:

```
/v1/chat/completions
```

(OpenAI format)

If it only exposes OpenAI format, then **LiteLLM becomes necessary**. But the first thing I would test on DGX Spark is:

```bash
curl http://localhost:8080/v1/models
```

and:

```bash
curl http://localhost:8080/v1/messages
```

That determines the correct Claude Code connection path.

[1]: https://docs.anthropic.com/en/docs/claude-code/llm-gateway?utm_source=chatgpt.com "LLM gateway configuration - Anthropic"
[2]: https://code.claude.com/docs/en/env-vars?utm_source=chatgpt.com "Environment variables - Claude Code Docs"
[3]: https://support.anthropic.com/en/articles/11940350-claude-code-model-configuration?utm_source=chatgpt.com "Claude Code Model Configuration | Anthropic Help Center"



# PrismML Bonsai 27B Q1_0 on NVIDIA DGX Spark

## Complete Setup Guide + OpenAI API Endpoint + Claude Code Integration

This guide is optimized for **NVIDIA DGX Spark** rather than your Dell Latitude.

DGX Spark is a much better target for Bonsai 27B because it has:

* **128GB unified LPDDR5x memory**
* **Blackwell GPU architecture**
* **20-core Grace CPU**
* **CUDA acceleration**
* **273 GB/s memory bandwidth**
  ([NVIDIA][1])

The DGX Spark can comfortably handle:

* Bonsai 27B Q1_0 ✅
* Ternary Bonsai 27B ✅
* DSpark speculative decoding ✅
* Large context windows ✅
* Claude Code agent workflows ✅

Architecture:

```
                 Claude Code
                      |
                      |
             Anthropic Compatible API
                      |
                      |
                 LiteLLM Proxy
                      |
                      |
              OpenAI Compatible API
                 localhost:8080
                      |
                      |
             PrismML llama-server
                      |
                      |
             Bonsai-27B-Q1_0.gguf

                      |
                      |
              NVIDIA Blackwell GPU
```

PrismML's Bonsai demo repository provides scripts for setup, model download, llama.cpp execution, and server startup. ([GitHub][2])

---

# 1. Verify DGX Spark Environment

SSH into DGX Spark or open terminal.

Check OS:

```bash
cat /etc/os-release
```

Expected:

```
Ubuntu / DGX OS
```

Check GPU:

```bash
nvidia-smi
```

Expected:

```
NVIDIA GB10
CUDA Version xx.x
```

Check memory:

```bash
free -h
```

Expected:

```
Mem:
128G
```

---

# 2. Install Dependencies

Update packages:

```bash
sudo apt update

sudo apt upgrade -y
```

Install tools:

```bash
sudo apt install -y \
git \
wget \
curl \
cmake \
build-essential \
python3 \
python3-pip \
python3-venv
```

Verify CUDA:

```bash
nvcc --version
```

---

# 3. Clone PrismML Bonsai Repository

Go to workspace:

```bash
mkdir -p ~/ai-models

cd ~/ai-models
```

Clone:

```bash
git clone https://github.com/PrismML-Eng/Bonsai-demo.git

cd Bonsai-demo
```

The repository supports selecting model family and size using environment variables. ([GitHub][2])

---

# 4. Select Bonsai 27B Model

For DGX Spark I recommend starting with the binary 1-bit model:

```bash
export BONSAI_FAMILY=bonsai

export BONSAI_MODEL=27B
```

Confirm:

```bash
echo $BONSAI_FAMILY

echo $BONSAI_MODEL
```

Output:

```
bonsai
27B
```

---

# 5. Run Setup

Execute:

```bash
./setup.sh
```

This will:

* install Python environment
* download dependencies
* download model files
* build/download llama.cpp runtime

([GitHub][2])

---

# 6. Verify Model Files

Find GGUF:

```bash
find . -name "*.gguf"
```

Expected:

```
Bonsai-27B-Q1_0.gguf
```

Example:

```
./models/Bonsai-27B-Q1_0.gguf
```

---

# 7. Build CUDA llama.cpp Runtime (Recommended)

For DGX Spark do NOT use CPU-only runtime.

Clone PrismML llama.cpp fork:

```bash
cd ~/ai-models

git clone https://github.com/PrismML-Eng/llama.cpp.git prism-llama.cpp

cd prism-llama.cpp
```

Build CUDA:

```bash
cmake -B build \
-DGGML_CUDA=ON \
-DCMAKE_BUILD_TYPE=Release
```

Compile:

```bash
cmake --build build \
--config Release \
-j$(nproc)
```

Verify:

```bash
ls build/bin
```

You should see:

```
llama-cli
llama-server
```

---

# 8. Test Model Inference

Before creating API endpoint, test locally.

Example:

```bash
./build/bin/llama-cli \
-m ~/ai-models/Bonsai-demo/models/Bonsai-27B-Q1_0.gguf \
-p "Explain dependency injection in C#"
```

Expected:

```
Dependency injection is a design pattern...
```

---

# 9. Enable GPU Offload

For DGX Spark use:

```bash
./build/bin/llama-cli \
-m ~/ai-models/Bonsai-demo/models/Bonsai-27B-Q1_0.gguf \
-ngl 999 \
-c 16384 \
-p "Explain SOLID principles"
```

Parameters:

| Parameter  | Meaning                   |
| ---------- | ------------------------- |
| `-ngl 999` | offload all layers to GPU |
| `-c 16384` | 16K context               |

---

# 10. Enable DSpark Speculative Decoding

Unlike your Dell laptop, DGX Spark has enough memory.

Enable:

```bash
export BONSAI_DSPARK=true
```

Run:

```bash
./scripts/run_llama.sh \
--draft \
-p "Generate a C# API framework"
```

Expected improvement:

* lower latency
* higher tokens/sec

---

# 11. Start OpenAI Compatible Server

Create:

```bash
nano start-bonsai-server.sh
```

Add:

```bash
#!/bin/bash


MODEL_PATH=$HOME/ai-models/Bonsai-demo/models/Bonsai-27B-Q1_0.gguf


~/ai-models/prism-llama.cpp/build/bin/llama-server \
-m $MODEL_PATH \
--host 0.0.0.0 \
--port 8080 \
-ngl 999 \
-c 32768 \
--parallel 4
```

Save.

Make executable:

```bash
chmod +x start-bonsai-server.sh
```

Start:

```bash
./start-bonsai-server.sh
```

Expected:

```
server listening on:
http://0.0.0.0:8080
```

---

# 12. Test OpenAI API

From another terminal:

```bash
curl http://localhost:8080/v1/models
```

Expected:

```json
{
 "data":[
   {
    "id":"Bonsai-27B"
   }
 ]
}
```

---

Test chat:

```bash
curl http://localhost:8080/v1/chat/completions \
-H "Content-Type: application/json" \
-d '
{
 "model":"Bonsai-27B",
 "messages":[
 {
  "role":"user",
  "content":"Write a C# REST API client using SOLID principles"
 }
 ]
}'
```

---

# 13. Install LiteLLM Adapter

Claude Code expects Anthropic style endpoints.

Install:

```bash
pip install litellm
```

Create config:

```bash
nano litellm.yaml
```

Add:

```yaml
model_list:

  - model_name: claude-local

    litellm_params:
      model: openai/Bonsai-27B
      api_base: http://localhost:8080/v1
      api_key: dummy
```

---

# 14. Start LiteLLM Proxy

Run:

```bash
litellm \
--config litellm.yaml \
--port 4000
```

Architecture now:

```
Claude Code

    |
    |
localhost:4000

    |
    |
LiteLLM

    |
    |
localhost:8080

    |
    |
Bonsai llama-server
```

---

# 15. Configure Claude Code

Install:

```bash
npm install -g @anthropic-ai/claude-code
```

Set:

```bash
export ANTHROPIC_BASE_URL=http://localhost:4000

export ANTHROPIC_API_KEY=dummy
```

Start:

```bash
claude
```

Test:

```
Analyze this C# automation framework and suggest improvements.
```

---

# 16. Configure Cline / Roo Code / Continue

Use:

```
Provider:
OpenAI Compatible

Base URL:
http://localhost:8080/v1

Model:
Bonsai-27B

API Key:
dummy
```

---

# 17. Recommended DGX Spark Settings

Unlike your Dell:

## Context

Start:

```
32768
```

Possible:

```
65536
```

---

## GPU

Always:

```
-ngl 999
```

---

## Parallel requests

For coding agents:

```
--parallel 4
```

---

## Temperature

Coding:

```
0.2 - 0.5
```

Creative:

```
0.7
```

---

# 18. Performance Expectations

DGX Spark should be dramatically faster than your i5 laptop.

Expected:

| Workload          | Result      |
| ----------------- | ----------- |
| Chat              | Fast        |
| Code generation   | Good        |
| Repo analysis     | Good        |
| Claude Code agent | Practical   |
| 32K context       | Comfortable |
| Multiple agents   | Possible    |

---

# Recommended Final Production Configuration

```
Model:
PrismML Bonsai 27B Q1_0

Runtime:
PrismML llama.cpp CUDA build

GPU:
Blackwell GB10

Layers:
-ngl 999

Context:
32768

Speculative decoding:
Enabled

Server:
llama-server

API:
OpenAI compatible

Adapter:
LiteLLM

Client:
Claude Code
Cline
Roo Code
Continue
```

This is the setup where Bonsai 27B starts becoming a realistic local Claude-style coding assistant rather than just a model demo. ([GitHub][2])

[1]: https://www.nvidia.com/en-gb/products/workstations/dgx-spark/?utm_source=chatgpt.com "Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark"
[2]: https://github.com/PrismML-Eng/Bonsai-demo/?utm_source=chatgpt.com "GitHub - PrismML-Eng/Bonsai-demo: Bonsai Demo · GitHub"
