# End-to-End PrismML Bonsai Setup and Understanding Guide for NVIDIA DGX Spark

## Overview

This guide documents an end-to-end local setup flow for running PrismML Bonsai models on an NVIDIA DGX Spark system using the `Bonsai-demo` repository, based only on the verified repository structure, scripts, commands, and outputs observed during the setup session. [github](https://github.com/PrismML-Eng/Bonsai-demo/)

The documented setup reached a working CUDA-backed `llama.cpp` runtime under `bin/cuda/`, confirmed the presence of `llama-server` and CUDA shared libraries, and established that the repository exposes an OpenAI-compatible API server through `scripts/start_llama_server.sh` rather than an Anthropic Messages API endpoint. [docs.prismml](https://docs.prismml.com/run/llamacpp)

This guide avoids assumptions where repository behavior, model IDs, or framework compatibility were not directly confirmed during the setup. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

## What this setup achieved

The completed setup established the following:

- The `Bonsai-demo` repository was cloned and inspected. [github](https://github.com/PrismML-Eng/Bonsai-demo/)
- The repo contained CPU binaries under `bin/cpu/` after setup, plus model files under `models/ternary-gguf/27B/`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- CUDA binaries were successfully built into `bin/cuda/`, including `llama-server`, `llama-cli`, and `libggml-cuda.so`. [docs.prismml](https://docs.prismml.com/run/llamacpp)
- The server entrypoint `scripts/start_llama_server.sh` was verified to expose an OpenAI-compatible API at `http://localhost:8080/v1/chat/completions`. [docs.prismml](https://docs.prismml.com/run/server)
- The script logic was verified to prefer `bin/cuda/llama-server` over `bin/cpu/llama-server` once the CUDA backend exists. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

## Model families and likely use cases

The repository supports at least two model families through environment variables: `bonsai` and `ternary`, with size values such as `27B`, `8B`, `4B`, and `1.7B` documented in the shared scripts. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

The observed local setup specifically downloaded and exposed **Ternary Bonsai 27B** GGUF model files under `models/ternary-gguf/27B/`, including a main quantized model, multimodal projector files, and a DSpark-related file. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### Model comparison

| Model family / size | What was directly observed | Likely role in local setup | Use cases that fit the evidence |
|---|---|---|---|
| Ternary Bonsai 27B | `models/ternary-gguf/27B/Ternary-Bonsai-27B-Q2_0.gguf`, `...Q4_1.gguf`, `...mmproj...`, `...dspark...` were present locally. [docs.prismml](https://docs.prismml.com/get-started/quickstart) | Primary verified model in this setup. [docs.prismml](https://docs.prismml.com/get-started/quickstart) | Coding, reasoning, multimodal/vision experiments, local agent backends where a large local model is acceptable. [docs.prismml](https://docs.prismml.com/models/bonsai-27b) |
| Bonsai 27B | Supported by `BONSAI_MODEL=27B` and `BONSAI_FAMILY=bonsai` in repo scripts, but not downloaded or run in this setup. [docs.prismml](https://docs.prismml.com/get-started/quickstart) | Alternate family option, not verified locally here. [docs.prismml](https://docs.prismml.com/get-started/quickstart) | Similar large-model use cases, but no local evidence in this session beyond repo support. [docs.prismml](https://docs.prismml.com/get-started/quickstart) |
| Smaller sizes: 8B / 4B / 1.7B | Enumerated as valid values in `scripts/common.sh`, but not downloaded or tested here. [docs.prismml](https://docs.prismml.com/get-started/quickstart) | Lower-memory and likely lower-latency options, not validated in this run. [docs.prismml](https://docs.prismml.com/get-started/quickstart) | Faster local iteration, lighter coding assistant scenarios, experimentation on constrained hardware; this is an architectural interpretation of size tiers rather than a measured result from this session. [docs.prismml](https://docs.prismml.com/get-started/quickstart) |

### Practical interpretation

For this setup, **Ternary Bonsai 27B** is the only model family and size directly confirmed by local file listings, so it should be treated as the reference target for the DGX Spark guide. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

The presence of `mmproj` files indicates that the 27B path includes multimodal support in the repository flow, and the server script explicitly searches for an `mmproj` file when `BONSAI_MODEL=27B`. [docs.prismml](https://docs.prismml.com/models/bonsai-27b)

The presence of a `dspark`-named GGUF file indicates that DSpark-related artifacts may be downloaded into the model directory, but this session did not verify that DSpark or DFlash can be enabled directly inside the current `llama-server` path. [docs.prismml](https://docs.prismml.com/run/llamacpp)

## Architecture options clarified during setup

Two possible client architectures were discussed during the session: direct Anthropic-compatible routing for Claude Code, and OpenAI-compatible local serving for tools that can use `/v1/chat/completions`. [docs.prismml](https://docs.prismml.com/run/server)

The verified repository evidence supports the second path, not the first: `scripts/start_llama_server.sh` explicitly describes itself as an OpenAI-compatible chat server and prints the API path `http://localhost:8080/v1/chat/completions`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### Verified architecture

```text
Coding tool or client
        |
        |
OpenAI-compatible HTTP API
http://localhost:8080/v1/chat/completions
        |
        |
PrismML Bonsai-demo -> llama-server
        |
        |
Ternary Bonsai 27B GGUF
        |
        |
DGX Spark CUDA backend
```

This architecture is directly supported by the repository scripts and observed file layout. [docs.prismml](https://docs.prismml.com/run/server)

### What was not verified

The setup did **not** verify that the local server exposes Anthropic `/v1/messages`, so a direct `ANTHROPIC_BASE_URL=http://localhost:8080` integration for Claude Code should not be assumed from this guide. [docs.prismml](https://docs.prismml.com/run/server)

If Claude Code must be used against this server, an adapter layer such as LiteLLM or another Anthropic-to-OpenAI gateway would still need separate validation. [docs.prismml](https://docs.prismml.com/run/server)

## Repository structure that was actually found

The repository did not contain a `llama.cpp` directory immediately after clone, which initially caused confusion when searching for directories named `*llama*`. [github](https://github.com/PrismML-Eng/Bonsai-demo/)

That was expected behavior for this repo: PrismML documents `Bonsai-demo` as a wrapper/demo repository that downloads binaries into backend folders such as `bin/cpu/`, `bin/cuda/`, and similar locations, rather than embedding the full `llama.cpp` source tree by default. [github](https://github.com/PrismML-Eng/Bonsai-demo/)

### Verified file layout highlights

- `bin/cpu/...` contained the CPU runtime and tools, including `llama-server`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `models/ternary-gguf/27B/...` contained the downloaded Ternary Bonsai 27B GGUF weights. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `scripts/` contained `build_cuda_linux.sh`, `run_llama.sh`, `start_llama_server.sh`, and related helper scripts. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `llama.cpp` was cloned later by `./scripts/build_cuda_linux.sh` when the CUDA build was requested. [docs.prismml](https://docs.prismml.com/run/llamacpp)

## Step-by-step setup flow

### 1. Clone the repo

The repository was cloned into a local models workspace. [github](https://github.com/PrismML-Eng/Bonsai-demo/)

```bash
cd ~/models
git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo
```

This repository is the operational wrapper used throughout the guide. [github](https://github.com/PrismML-Eng/Bonsai-demo/)

### 2. Understand the model-selection variables

The scripts use environment variables to select the model family and size, including `BONSAI_FAMILY` and `BONSAI_MODEL`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

The shared script content showed:

- valid size values include `27B`, `8B`, `4B`, `1.7B`, and `all`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `BONSAI_MODEL` defaults to `27B`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- the model family controls whether paths resolve to `models/gguf/...` or `models/ternary-gguf/...`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

Example environment selection:

```bash
export BONSAI_FAMILY=ternary
export BONSAI_MODEL=27B
```

This exact combination matched the verified local model directory contents in this setup. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### 3. Run setup

The setup path described by PrismML quickstart is to run the repository setup command so it can download model assets and binaries. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

```bash
./setup.sh
```

The setup behavior documented by PrismML is that it downloads prebuilt inference binaries when available, rather than requiring a source build in every case. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### 4. Inspect what was downloaded

The first important verification step was to inspect the repo contents rather than assume CUDA support was already present.

Commands used:

```bash
find bin -maxdepth 3 -type f | sort
find models -maxdepth 4 -type f | sort | head -n 50
ls -R scripts | head -n 100
```

This showed that the initial setup had produced a **CPU-only backend** under `bin/cpu/`, while the model files under `models/ternary-gguf/27B/` were already present. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

Key observed files included:

- `bin/cpu/llama-server`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `models/ternary-gguf/27B/Ternary-Bonsai-27B-Q2_0.gguf`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `models/ternary-gguf/27B/Ternary-Bonsai-27B-Q4_1.gguf`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `models/ternary-gguf/27B/Ternary-Bonsai-27B-mmproj-Q8_0.gguf`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `scripts/build_cuda_linux.sh` and `scripts/start_llama_server.sh`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### 5. Inspect the server script before making assumptions

The next step was to read the actual `scripts/start_llama_server.sh` and inspect its environment variable references in `scripts/common.sh`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

Commands used:

```bash
head -n 80 scripts/start_llama_server.sh
grep -n BONSAI_BACKEND scripts/common.sh scripts/start_llama_server.sh
grep -n BONSAI_MODEL scripts/common.sh scripts/start_llama_server.sh
```

Important verified findings:

- The server identifies itself as an **OpenAI-compatible chat server**. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- It binds to `127.0.0.1` by default, with `BONSAI_HOST=0.0.0.0` as an override. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- It searches for `llama-server` in `bin/mac`, `bin/cuda`, `bin/rocm`, `bin/hip`, `bin/vulkan`, `bin/cpu`, and several `llama.cpp/build*` paths. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- It selects the first backend that exists, which means CUDA will be preferred over CPU once built. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- For `BONSAI_MODEL=27B`, it separately searches for an `mmproj` file and warns if none is found. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- It advertises the API endpoint `http://localhost:8080/v1/chat/completions`. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### 6. Build the CUDA backend

Because only `bin/cpu/` existed initially, the CUDA backend had to be built manually using the provided repository script. [docs.prismml](https://docs.prismml.com/run/llamacpp)

Command used:

```bash
./scripts/build_cuda_linux.sh
```

On first run, the script cloned `./llama.cpp` from PrismML and attempted a CUDA 13.0 multi-architecture build. [docs.prismml](https://docs.prismml.com/run/llamacpp)

The initial build attempt failed with CMake messages indicating problems with Ninja and compiler detection. [docs.prismml](https://docs.prismml.com/run/llamacpp)

### 7. Verify the host build toolchain instead of guessing

To avoid assuming a missing dependency, the system toolchain was checked directly.

Commands used:

```bash
which gcc g++ cmake ninja
gcc --version
g++ --version
cmake --version
ninja --version
nvcc --version
```

The environment was confirmed to have:

- `/usr/bin/gcc` and `/usr/bin/g++`. [oneuptime](https://oneuptime.com/blog/post/2026-03-02-how-to-compile-software-from-source-on-ubuntu/view)
- `/usr/bin/cmake` and `/usr/bin/ninja`. [oneuptime](https://oneuptime.com/blog/post/2026-03-02-how-to-compile-software-from-source-on-ubuntu/view)
- GCC 13.3.0, CMake 3.28.3, Ninja 1.11.1, and CUDA `nvcc` 13.0.88. [oneuptime](https://oneuptime.com/blog/post/2026-03-02-how-to-compile-software-from-source-on-ubuntu/view)

This established that the DGX Spark host already had a valid compile toolchain and CUDA compiler available at that point in the session. [oneuptime](https://oneuptime.com/blog/post/2026-03-02-how-to-compile-software-from-source-on-ubuntu/view)

### 8. Clean stale build directories only

The recommended cleanup did **not** include deleting CPU binaries, because the repo is designed to support multiple backends side by side. [docs.prismml](https://docs.prismml.com/download/formats)

Only previous build directories were cleaned:

```bash
cd ~/models/Bonsai-demo
rm -rf llama.cpp/build llama.cpp/build-cuda
./scripts/build_cuda_linux.sh
```

This was the correct cleanup scope because `start_llama_server.sh` is written to select `bin/cuda` before `bin/cpu`, making the CPU backend a harmless fallback rather than a conflict. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### 9. Confirm successful CUDA output

After rerunning the build, the CUDA runtime appeared under `bin/cuda/`. [docs.prismml](https://docs.prismml.com/run/llamacpp)

Verification command:

```bash
find bin/cuda -maxdepth 2 -type f | sort | head -n 50
```

Verified outputs included:

- `bin/cuda/libggml-cuda.so.0.13.1`. [docs.prismml](https://docs.prismml.com/run/llamacpp)
- `bin/cuda/llama-server`. [docs.prismml](https://docs.prismml.com/run/llamacpp)
- `bin/cuda/llama-cli`. [docs.prismml](https://docs.prismml.com/run/llamacpp)
- `bin/cuda/llama-speculative`. [docs.prismml](https://docs.prismml.com/run/llamacpp)

This was the key evidence that the DGX Spark environment now had a working CUDA-enabled `llama.cpp` runtime for PrismML Bonsai models. [docs.prismml](https://docs.prismml.com/run/llamacpp)

## Starting the local server

Once the CUDA backend existed, the documented run path was to launch the server script with explicit family and size variables matching the downloaded model layout. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

```bash
cd ~/models/Bonsai-demo
export BONSAI_FAMILY=ternary
export BONSAI_MODEL=27B
BONSAI_BACKEND=llama ./scripts/start_llama_server.sh
```

This command is consistent with the verified script logic and local file layout from the session. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### What the server script is expected to do

Based on the script content, the run sequence is:

1. Validate the family and model values. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
2. Resolve the demo directory and confirm the GGUF model is present. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
3. Select the correct quantized model file while skipping `mmproj`, `dspark`, and `kv-bias` files for the main model. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
4. Locate the multimodal projector when present for the 27B path. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
5. Search backend locations and prefer CUDA if available. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
6. Set `LD_LIBRARY_PATH` to the chosen binary directory. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
7. Expose a server on port `8080` with an OpenAI-compatible API. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

### API path

The documented API path from the script is:

```text
http://localhost:8080/v1/chat/completions
```

That API contract was directly verified from the script output text and PrismML server documentation. [docs.prismml](https://docs.prismml.com/run/server)

## Verifying model routing and connectivity

The first validation step after the server starts is to inspect the models endpoint. [docs.prismml](https://docs.prismml.com/run/server)

```bash
curl http://localhost:8080/v1/models
```

The exact returned model ID was not captured in the session, so this guide does not assume the final value. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

A generic chat-completions probe can then be used:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<model-id-from-v1-models>",
    "messages": [
      {"role": "user", "content": "Explain SOLID principles in C# test automation."}
    ]
  }'
```

Using the model ID returned by `/v1/models` is safer than hardcoding a guessed value. [docs.prismml](https://docs.prismml.com/run/server)

## CPU and CUDA backends together

The CPU artifacts should be kept in place unless disk cleanup is explicitly required, because the repository’s backend selection logic is intentionally multi-backend. [docs.prismml](https://docs.prismml.com/download/formats)

This means:

- `bin/cpu` is not a problem after `bin/cuda` exists. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- `bin/cuda` will be preferred automatically by the server script. [docs.prismml](https://docs.prismml.com/get-started/quickstart)
- deleting CPU binaries is unnecessary for correctness and removes a fallback path. [docs.prismml](https://docs.prismml.com/download/formats)

## Throughput expectations and speculative decoding notes

After CUDA was enabled, the observed practical result was that tokens-per-second did **not** increase dramatically.

That led to a comparison between DFlash and DSpark, but the key architectural conclusion for this setup was narrower: the current `Bonsai-demo` path is based on `llama.cpp` tooling, and the repository evidence only confirmed standard `llama-server` plus local speculative binaries such as `llama-speculative`. [docs.prismml](https://docs.prismml.com/run/llamacpp)

### What was verified about DFlash and DSpark in this setup

- DFlash is documented externally as a block-diffusion speculative decoding method integrated into frameworks such as vLLM and SGLang rather than the basic `Bonsai-demo` server flow. [arxiv](https://arxiv.org/html/2602.06036v2)
- DSpark is described externally as a more advanced speculative decoding approach focused on accuracy and dynamic scheduling, again associated with dedicated speculative-serving stacks rather than the plain `llama-server` path verified here. [webscraft](https://webscraft.org/blog/dspark-vid-deepseek-v4-shvidshe-na-6085-bez-novogo-zaliza?lang=en)
- The local repository build did produce `bin/cuda/llama-speculative`, but this session did not verify that DFlash or DSpark can be enabled directly inside the current `scripts/start_llama_server.sh` path. [docs.prismml](https://docs.prismml.com/run/llamacpp)

### Safe conclusion

Within the limits of this setup, it is safe to say that:

- CUDA acceleration is enabled and working at the binary level. [docs.prismml](https://docs.prismml.com/run/llamacpp)
- advanced speculative systems such as DFlash or DSpark were **not** validated as part of the working `llama-server` flow in this guide. [docs.vllm](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/algorithms/dflash/)
- further work would be required to move Bonsai models into a framework that explicitly supports those speculative engines. [arxiv](https://arxiv.org/html/2602.06036v2)

## Client integration guidance

### Clients that can use the current setup directly

Any local tool that can talk to an OpenAI-compatible endpoint should be able to use this server after the model ID is confirmed from `/v1/models`. [docs.prismml](https://docs.prismml.com/run/server)

Examples include local coding tools or adapters that accept:

- Base URL: `http://localhost:8080/v1`. [docs.prismml](https://docs.prismml.com/run/server)
- Chat endpoint: `/chat/completions`. [docs.prismml](https://docs.prismml.com/run/server)

### Claude Code caveat

The verified repo and script evidence does **not** show Anthropic Messages API support at `/v1/messages`. [docs.prismml](https://docs.prismml.com/run/server)

Because of that, a direct Claude Code integration using only `ANTHROPIC_BASE_URL=http://localhost:8080` should not be treated as part of this verified setup. [docs.prismml](https://docs.prismml.com/run/server)

If Claude Code must be connected, an adapter such as LiteLLM would need separate setup and validation outside this guide. [docs.prismml](https://docs.prismml.com/run/server)

## Command reference

### Clone and initialize

```bash
cd ~/models
git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo
./setup.sh
```

### Inspect repo contents

```bash
find bin -maxdepth 3 -type f | sort
find models -maxdepth 4 -type f | sort | head -n 50
ls -R scripts | head -n 100
```

### Inspect server logic

```bash
head -n 80 scripts/start_llama_server.sh
grep -n BONSAI_BACKEND scripts/common.sh scripts/start_llama_server.sh
grep -n BONSAI_MODEL scripts/common.sh scripts/start_llama_server.sh
```

### Check toolchain

```bash
which gcc g++ cmake ninja
gcc --version
g++ --version
cmake --version
ninja --version
nvcc --version
```

### Clean old build dirs and build CUDA

```bash
cd ~/models/Bonsai-demo
rm -rf llama.cpp/build llama.cpp/build-cuda
./scripts/build_cuda_linux.sh
```

### Confirm CUDA runtime

```bash
find bin/cuda -maxdepth 2 -type f | sort | head -n 50
```

### Start the server

```bash
cd ~/models/Bonsai-demo
export BONSAI_FAMILY=ternary
export BONSAI_MODEL=27B
BONSAI_BACKEND=llama ./scripts/start_llama_server.sh
```

### Probe the API

```bash
curl http://localhost:8080/v1/models
```

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<model-id-from-v1-models>",
    "messages": [
      {"role": "user", "content": "Explain SOLID principles in C# test automation."}
    ]
  }'
```

## Common misunderstandings resolved during setup

### “There is no GPU support because `find *llama*` returned nothing”

That result did not indicate missing GPU support; it only showed that the wrapper repo did not contain a `llama.cpp` source directory at that time. [github](https://github.com/PrismML-Eng/Bonsai-demo/)

GPU support in this repository is expressed through backend binaries in directories like `bin/cuda/`, and `build_cuda_linux.sh` clones and builds `llama.cpp` when required. [docs.prismml](https://docs.prismml.com/run/llamacpp)

### “The CPU backend should be removed after CUDA is built”

That is unnecessary and not supported by the script design, because backend selection is already ordered to prefer CUDA over CPU. [docs.prismml](https://docs.prismml.com/download/formats)

### “Claude Code can be pointed directly at this server”

That was not verified by the repository evidence in this setup; the local server path that was confirmed is OpenAI-compatible, not Anthropic-compatible. [docs.prismml](https://docs.prismml.com/run/server)

### “DFlash or DSpark can be turned on in the current server script”

That was not verified in this setup. External sources describe DFlash and DSpark in other serving stacks, and this guide should not assume those features are available in `scripts/start_llama_server.sh` without further integration work. [we0](https://we0.ai/articles-v2/deepseek-dspark-apple-silicon-mlx-dflash)

## Final understanding

The DGX Spark setup successfully moved from a CPU-only PrismML demo checkout to a CUDA-backed local Bonsai runtime by inspecting the repository structure, reading the actual launch scripts, confirming the host toolchain, and building the CUDA backend with the repository’s provided build script. [oneuptime](https://oneuptime.com/blog/post/2026-03-02-how-to-compile-software-from-source-on-ubuntu/view)

The verified, end-to-end outcome is a local OpenAI-compatible `llama-server` running PrismML Bonsai GGUF models from the `Bonsai-demo` repository with CUDA artifacts under `bin/cuda/` and model artifacts under `models/ternary-gguf/27B/`. [docs.prismml](https://docs.prismml.com/run/server)

The most important operational rule from this guide is to trust the repository’s actual scripts and discovered file layout over generic assumptions: inspect `scripts/common.sh`, inspect `scripts/start_llama_server.sh`, confirm the exact backend path in `bin/`, and use `/v1/models` to discover the live model ID before wiring clients. [docs.prismml](https://docs.prismml.com/run/server)


# Network access Prism Models:
Yes — the clean way is to put a small gateway on your **laptop** that speaks Anthropic Messages API to Claude Code and forwards requests to your PrismML server’s OpenAI-compatible endpoint at `http://localhost:8080/v1`. Claude Code expects an Anthropic-style `/v1/messages` interface, while your PrismML `start_llama_server.sh` exposes `/v1/chat/completions`, so a direct `ANTHROPIC_BASE_URL=http://localhost:8080` setup is not the verified path. [code.claude](https://code.claude.com/docs/en/llm-gateway)

## Architecture

Use this flow:

```text
Claude Code on laptop
        |
ANTHROPIC_BASE_URL=http://localhost:4000
        |
Anthropic-compatible gateway on laptop
        |
OpenAI-compatible upstream
http://<DGX-SPARK-IP>:8080/v1
        |
PrismML llama-server on DGX Spark
```

Claude Code’s docs explicitly support pointing the CLI at an LLM gateway using `ANTHROPIC_BASE_URL`, as long as that gateway exposes the Anthropic Messages API that Claude Code expects. [code.claude](https://code.claude.com/docs/id/llm-gateway)

## Network step

First, make sure your DGX Spark server is reachable from your laptop, because `localhost:8080` on the DGX is only local to the DGX itself. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

On DGX Spark, start the PrismML server bound to all interfaces:

```bash
cd ~/models/Bonsai-demo
export BONSAI_FAMILY=ternary
export BONSAI_MODEL=27B
BONSAI_HOST=0.0.0.0 BONSAI_BACKEND=llama ./scripts/start_llama_server.sh
```

The script defaults to `127.0.0.1`, and it explicitly says `BONSAI_HOST=0.0.0.0` is the override for LAN or remote access. [docs.prismml](https://docs.prismml.com/get-started/quickstart)

Then, from your laptop, test connectivity:

```bash
curl http://<DGX-SPARK-IP>:8080/v1/models
```

If that fails, you need to fix firewall/routing before touching Claude Code.

## Gateway choice

A practical option is **agentgateway**, because its Claude Code integration docs explicitly show routing Claude Code to an OpenAI-compatible backend through an Anthropic-facing gateway. It is a better fit here than trying to point Claude Code directly at LiteLLM, because the Claude Code docs and gateway examples are centered on Anthropic `/v1/messages` semantics. [agentgateway](https://agentgateway.dev/docs/standalone/main/integrations/llm-clients/claude-code/)

## Laptop setup

Install Claude Code if needed:

```bash
npm install -g @anthropic-ai/claude-code
```

Then install or obtain `agentgateway` on your laptop, following its platform-specific install method from the project docs. [agentgateway](https://agentgateway.dev/docs/standalone/main/integrations/llm-clients/claude-code/)

Create a config file on your laptop, for example `config.yaml`:

```yaml
llm:
  models:
    - name: "*"
      provider: openAI
      params:
        baseURL: "http://<DGX-SPARK-IP>:8080/v1"
        apiKey: "mock-key"
```

This is the documented pattern for routing Claude Code through agentgateway to any OpenAI-compatible local provider such as vLLM or similar backends; your PrismML server fits that same upstream shape because it exposes `/v1/chat/completions` under `/v1`. [agentgateway](https://agentgateway.dev/docs/standalone/main/integrations/llm-clients/claude-code/)

Start the gateway on your laptop:

```bash
agentgateway -f config.yaml
```

The docs show using the gateway locally and then pointing Claude Code to it with `ANTHROPIC_BASE_URL`. [agentgateway](https://agentgateway.dev/docs/standalone/main/integrations/llm-clients/claude-code/)

## Claude Code configuration

In the same laptop shell:

```bash
export ANTHROPIC_BASE_URL="http://localhost:4000"
export ANTHROPIC_AUTH_TOKEN="local"
```

Claude Code’s gateway docs state that it reads endpoint and auth from environment variables, including `ANTHROPIC_BASE_URL`, and custom gateways commonly use `ANTHROPIC_AUTH_TOKEN` for local auth plumbing. [fazm](https://fazm.ai/t/claude-code-llm-gateway-anthropic-base-url-official-docs)

Then launch Claude Code:

```bash
claude
```

Or do a quick non-interactive test:

```bash
claude -p "Say hello in one sentence."
```

If the gateway is working, Claude Code should route through the laptop gateway to the DGX Spark PrismML endpoint. [agentgateway](https://agentgateway.dev/docs/standalone/main/integrations/llm-clients/claude-code/)

## Persisting config

You can persist the gateway settings in `~/.claude/settings.json` on your laptop, because Claude Code supports storing env overrides there. [morphllm](https://www.morphllm.com/use-different-llm-claude-code)

Example:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:4000",
    "ANTHROPIC_AUTH_TOKEN": "local"
  }
}
```

That keeps the Claude-specific settings scoped to Claude Code instead of exporting them globally in your shell. [abliteration](https://abliteration.ai/docs/claude-code)

## Troubleshooting sequence

Use this order so you only debug one layer at a time:

1. **DGX server**
   - From DGX: `curl http://localhost:8080/v1/models`
   - From laptop: `curl http://<DGX-SPARK-IP>:8080/v1/models` [docs.prismml](https://docs.prismml.com/get-started/quickstart)

2. **Gateway**
   - Start `agentgateway -f config.yaml`
   - Confirm the process is listening on laptop port 4000 according to its default runtime behavior and logs. [agentgateway](https://agentgateway.dev/docs/standalone/main/integrations/llm-clients/claude-code/)

3. **Claude Code**
   - `echo $ANTHROPIC_BASE_URL`
   - `claude -p "ping"`

If Claude Code fails but the laptop can hit the DGX server, the issue is almost certainly the gateway config rather than PrismML itself. [code.claude](https://code.claude.com/docs/en/llm-gateway)

## Important limitation

This setup gives Claude Code a path to use your PrismML model, but it does **not** mean the model behaves like Claude in tool use quality, planning depth, or coding-agent reliability. It only means Claude Code can be wired to a non-Anthropic backend through a compatible gateway interface. [fazm](https://fazm.ai/t/claude-code-llm-gateway-anthropic-base-url-official-docs)

If you want, I can generate:
- a laptop-side `config.yaml` for agentgateway with your DGX IP placeholder, and
- a matching `~/.claude/settings.json` example for a persistent setup.