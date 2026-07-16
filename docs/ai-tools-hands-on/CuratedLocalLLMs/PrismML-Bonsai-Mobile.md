# **PrismML Bonsai 27B** (1-bit binary variant) on your **Dell Latitude (i5 CPU, 16GB RAM)** laptop, with the goal of integrating it into Claude-based tools.

---

# Post-Incident & Setup Documentation

**Target Model:** `PrismML Bonsai 27B` (1-Bit Binary GGUF)

**Target Hardware:** Dell Latitude Laptop (Intel Core i5 CPU, 16GB RAM)

**Primary Goal:** Local execution with API compatibility for Claude-based IDE/developer agents.

---

## 1. The Core Issues Faced

### Issue A: Ollama Fails to Load Experimental 1-Bit / Ternary Quants

* **Symptom:** Running the default `ollama run hf.co/prism-ml/Bonsai-27B-gguf:Q1_0` successfully downloaded the layers but crashed immediately upon initialization with an `Error: 500 Internal Server Error: unable to load model`.
* **Symptom 2:** Trying to bypass the Hugging Face manifest wrapper using a custom `Modelfile` built locally resulted in the same `500 Internal Server Error: model failed to load`.
* **Root Cause:** Mainline Ollama releases package a version of `llama.cpp` that lacks support for PrismML’s custom, newly-released 1-bit (`Q1_0_g128` format) and 1.58-bit ternary layouts. Ollama's model runner panics when trying to map these non-standard quantized layers into RAM.

### Issue B: RAM and Swap Saturation

* **Symptom:** The system froze, and resource monitors showed Physical Memory pinned at **12.2 GB (73%) of 16.6 GB** alongside a completely saturated swap space of **12.4 GB (98.6%) of 12.6 GB**.
* **Root Cause 1 (Desktop Overhead):** Your Dell Latitude’s host operating system and background applications were already occupying roughly 6 to 8 GB of RAM.
* **Root Cause 2 (Bundle Overhead):** PrismML's default `./setup.sh` script automatically downloaded and loaded a highly bloated target footprint (reaching over **7.15 GB** of files). This bundle loaded the 3.8 GB core language model alongside the **1.79 GB DSpark speculative decoder** and a **629 MB Vision tower (mmproj)**. Loading both the core and speculative models concurrently pushed the required execution RAM past the system's limits, forcing heavy swap usage and freezing the system.

### Issue C: Invalid CLI Arguments in Setup Modelfile

* **Symptom:** Copy-pasting the `Modelfile` contents directly into the bash terminal triggered `command not found: FROM` and `command not found: PARAMETER` errors.
* **Root Cause:** The syntax inside a `Modelfile` consists of local instructions meant only for `ollama create` parsing, not direct execution in a Unix Shell.

---

## 2. Workarounds Attempted

### Workaround 1: Creating a Local `Modelfile` for Ollama

* **Steps Taken:** We wrote a shell heredoc (`cat << 'EOF' > Modelfile`) to properly write a file pointing to the offline `.gguf` weight format.
* **Result:** Successfully bypassed the bash syntax errors and built the model locally, but the target `ollama run` still failed with a 500 error due to Ollama's internal compiler limitation (Issue A).

### Workaround 2: Using the Official CLI (`Bonsai-demo`)

* **Steps Taken:** Switched to the official `PrismML-Eng/Bonsai-demo` repository which bundles a tailored fork of `llama.cpp` natively supporting 1-bit and ternary mathematical structures.
* **Result:** The script initially defaulted to downloading the heavier **Ternary (~10.7 GB total bundle)** format. We aborted this to protect your system's resources.

### Workaround 3: Forcing the 1-Bit "Bonsai" Family Configuration

* **Steps Taken:** We modified the environment variables to force the script to select the lightweight 1-bit binary weights:
```bash
export BONSAI_FAMILY=bonsai
export BONSAI_MODEL=27B
./setup.sh

```


*(Note: The family value had to be mapped to `bonsai` instead of `binary` as the script rejected `binary` as an unrecognized tag).*
* **Result:** Successfully downloaded the ~3.8 GB core language file.

### Workaround 4: Disabling Speculative Decoding (`DSpark`)

* **Steps Taken:** To stop the 1.79 GB speculative decoder from exhausting your remaining RAM, we configured the execution to run in a strict text-only, single-model mode:
```bash
BONSAI_MODEL=27B ./scripts/run_llama.sh --no-draft -p "Prompt here"

```


* **Result:** Successfully reduced the memory pressure, keeping the execution layer to under **4.5 GB of active RAM** and preventing your laptop's swap space from overflowing.

---

## 3. Final Architecture for Claude / IDE Tooling

Since Ollama is currently a dead-end for this specific model, the recommended production route is to bypass Ollama entirely and point your developer tools (like Cline, Roo Code, or Continue) to the custom, optimized API server:

1. **Spin up the Prism-supported server:**
```bash
# In the llama.cpp repository cloned from the PrismML fork:
./build/bin/llama-server \
  -m /path/to/Bonsai-27B-Q1_0.gguf \
  --port 8080 \
  --host 0.0.0.0 \
  -c 8192

```


2. **Configure your Claude Tooling:**
Set the provider in your extension settings to `OpenAI-Compatible`, pointing the Base URL to `http://localhost:8080/v1`. This allows you to leverage the model’s built-in tool calling capabilities directly through the optimized local server.



Here is a complete, consolidated documentation of the issues we faced and the workarounds we tried while attempting to run the newly released **PrismML Bonsai 27B** (1-bit binary variant) on your **Dell Latitude (i5 CPU, 16GB RAM)** laptop, with the goal of integrating it into Claude-based tools.

---

# Post-Incident & Setup Documentation

**Target Model:** `PrismML Bonsai 27B` (1-Bit Binary GGUF)

**Target Hardware:** Dell Latitude Laptop (Intel Core i5 CPU, 16GB RAM)

**Primary Goal:** Local execution with API compatibility for Claude-based IDE/developer agents.

---

## 1. The Core Issues Faced

### Issue A: Ollama Fails to Load Experimental 1-Bit / Ternary Quants

* **Symptom:** Running the default `ollama run hf.co/prism-ml/Bonsai-27B-gguf:Q1_0` successfully downloaded the layers but crashed immediately upon initialization with an `Error: 500 Internal Server Error: unable to load model`.
* **Symptom 2:** Trying to bypass the Hugging Face manifest wrapper using a custom `Modelfile` built locally resulted in the same `500 Internal Server Error: model failed to load`.
* **Root Cause:** Mainline Ollama releases package a version of `llama.cpp` that lacks support for PrismML’s custom, newly-released 1-bit (`Q1_0_g128` format) and 1.58-bit ternary layouts. Ollama's model runner panics when trying to map these non-standard quantized layers into RAM.

### Issue B: RAM and Swap Saturation

* **Symptom:** The system froze, and resource monitors showed Physical Memory pinned at **12.2 GB (73%) of 16.6 GB** alongside a completely saturated swap space of **12.4 GB (98.6%) of 12.6 GB**.
* **Root Cause 1 (Desktop Overhead):** Your Dell Latitude’s host operating system and background applications were already occupying roughly 6 to 8 GB of RAM.
* **Root Cause 2 (Bundle Overhead):** PrismML's default `./setup.sh` script automatically downloaded and loaded a highly bloated target footprint (reaching over **7.15 GB** of files). This bundle loaded the 3.8 GB core language model alongside the **1.79 GB DSpark speculative decoder** and a **629 MB Vision tower (mmproj)**. Loading both the core and speculative models concurrently pushed the required execution RAM past the system's limits, forcing heavy swap usage and freezing the system.

### Issue C: Invalid CLI Arguments in Setup Modelfile

* **Symptom:** Copy-pasting the `Modelfile` contents directly into the bash terminal triggered `command not found: FROM` and `command not found: PARAMETER` errors.
* **Root Cause:** The syntax inside a `Modelfile` consists of local instructions meant only for `ollama create` parsing, not direct execution in a Unix Shell.

---

## 2. Workarounds Attempted

### Workaround 1: Creating a Local `Modelfile` for Ollama

* **Steps Taken:** We wrote a shell heredoc (`cat << 'EOF' > Modelfile`) to properly write a file pointing to the offline `.gguf` weight format.
* **Result:** Successfully bypassed the bash syntax errors and built the model locally, but the target `ollama run` still failed with a 500 error due to Ollama's internal compiler limitation (Issue A).

### Workaround 2: Using the Official CLI (`Bonsai-demo`)

* **Steps Taken:** Switched to the official `PrismML-Eng/Bonsai-demo` repository which bundles a tailored fork of `llama.cpp` natively supporting 1-bit and ternary mathematical structures.
* **Result:** The script initially defaulted to downloading the heavier **Ternary (~10.7 GB total bundle)** format. We aborted this to protect your system's resources.

### Workaround 3: Forcing the 1-Bit "Bonsai" Family Configuration

* **Steps Taken:** We modified the environment variables to force the script to select the lightweight 1-bit binary weights:
```bash
export BONSAI_FAMILY=bonsai
export BONSAI_MODEL=27B
./setup.sh

```


*(Note: The family value had to be mapped to `bonsai` instead of `binary` as the script rejected `binary` as an unrecognized tag).*
* **Result:** Successfully downloaded the ~3.8 GB core language file.

### Workaround 4: Disabling Speculative Decoding (`DSpark`)

* **Steps Taken:** To stop the 1.79 GB speculative decoder from exhausting your remaining RAM, we configured the execution to run in a strict text-only, single-model mode:
```bash
BONSAI_MODEL=27B ./scripts/run_llama.sh --no-draft -p "Prompt here"

```


* **Result:** Successfully reduced the memory pressure, keeping the execution layer to under **4.5 GB of active RAM** and preventing your laptop's swap space from overflowing.

---

## 3. Final Architecture for Claude / IDE Tooling

Since Ollama is currently a dead-end for this specific model, the recommended production route is to bypass Ollama entirely and point your developer tools (like Cline, Roo Code, or Continue) to the custom, optimized API server:

1. **Spin up the Prism-supported server:**
```bash
# In the llama.cpp repository cloned from the PrismML fork:
./build/bin/llama-server \
  -m /path/to/Bonsai-27B-Q1_0.gguf \
  --port 8080 \
  --host 0.0.0.0 \
  -c 8192

```


2. **Configure your Claude Tooling:**
Set the provider in your extension settings to `OpenAI-Compatible`, pointing the Base URL to `http://localhost:8080/v1`. This allows you to leverage the model’s built-in tool calling capabilities directly through the optimized local server.









For your Dell Latitude (i5 CPU, 16GB RAM), you should definitely start with the **1-Bit Binary Variant (3.9 GB)**.

Here is why this is the best fit for your specific laptop:

### 1. RAM Headroom

On a 16GB laptop, your operating system and open apps (like Chrome or Slack) usually eat up 6GB to 8GB of RAM. This leaves you with roughly 8GB to 10GB of actual free memory.

* **The 1-Bit version (~3.9 GB)** fits comfortably inside your free RAM, leaving plenty of room for your system to run smoothly and hold a decent conversation history (context window) without lagging.
* **The Ternary version (~5.9 GB)** will technically fit, but it will push your system right to the edge. If your RAM fills up, your laptop will start swapping memory to your hard drive, which will slow the model down to a crawl.

### 2. Speed and CPU Performance

Your i5 CPU does not have a dedicated high-end GPU with fast VRAM; it relies entirely on your system's RAM bandwidth.

* To generate text, your CPU has to read the entire model from your RAM for *every single token* it generates.
* Because the 1-bit model is only 3.9 GB, your CPU has to move 33% less data per token compared to the 5.9 GB Ternary version. This translates directly to faster generation speeds on standard laptop processors.

---

### Realistic Performance Expectations

Because you are running a massive 27B-parameter model on a standard laptop CPU (instead of an Apple Silicon chip or an Nvidia GPU), it will be heavy.

* **Speed:** Expect a modest speed of roughly **1 to 3 tokens per second**. It will feel more like a slow typewriter than instant streaming, but it is incredible that a 27B-class model can run on an i5 laptop at all.
* **Fan Noise:** Your CPU will run at 100% capacity during inference, so expect your laptop fans to kick up to maximum speed.

### How to run it:

Open your terminal and use Ollama to pull and run the 1-bit version directly:

```bash
ollama run hf.co/prism-ml/Bonsai-27B-gguf:Q1_0

```

That **500 Internal Server Error** after a successful pull is a known issue when trying to run these cutting-edge, low-bit models natively inside Ollama.

The error is happening because **Ollama's internal runner (`llama.cpp`) does not yet natively support the custom binary/ternary weight layout or the extreme `Q1_0` packing of Qwen 3.6**. Ollama downloads the layers successfully (hence the `success` message), but when it tries to initialize the weights into memory, the loader crashes because it doesn't recognize the file format.

You have two excellent ways to solve this and get the model running:

---

### Method 1: The Fast, Frictionless Path (Use LM Studio)

If you want to play with Bonsai 27B right now without fighting terminal configs, **LM Studio** is the easiest route.

Because LM Studio uses a much more frequently updated `llama.cpp` runtime, it natively parses these experimental low-bit GGUFs without throwing errors.

1. Download and open **LM Studio** (if you don't have it, grab it from [lmstudio.ai](https://lmstudio.ai)).
2. Skip the search bar and go to the **Local Folder** icon on the left panel.
3. Since Ollama already downloaded the actual 3.8 GB GGUF file to your system, you don't need to redownload it! You can find it in your Ollama cache.
* **On Linux:** `/usr/share/ollama/.ollama/models/blobs/`
* **On Windows:** `C:\Users\<YourUsername>\.ollama\models\blobs\`
* **On macOS:** `~/.ollama/models/blobs/`


4. Find the large `~3.8 GB` file in that folder (it will have a long SHA-256 hash name like `sha256-17ef842...`).
5. Copy that file, paste it into your LM Studio models folder (usually inside `~/.cache/lm-studio/models/`), and rename it to `bonsai-27b-q1.gguf`.
6. Select it in LM Studio and hit **Load**.

---

### Method 2: Force Ollama via a Custom Modelfile

If you are determined to keep your workflow strictly inside Ollama, you can bypass its automated Hugging Face parser by downloading the GGUF file manually and pointing Ollama directly to it with a local `Modelfile`.

#### Step 1: Download the raw GGUF directly

Download the raw `.gguf` file using `wget` or your browser so Ollama doesn't have to resolve the Hugging Face manifest:

```bash
wget https://huggingface.co/prism-ml/Bonsai-27B-gguf/resolve/main/Bonsai-27B-Q1_0.gguf

```

#### Step 2: Create a local Modelfile

In the same folder, create a plain text file named `Modelfile` with the following content:

```dockerfile
# Point to the exact file you just downloaded
FROM ./Bonsai-27B-Q1_0.gguf

# Set the context parameters
PARAMETER num_ctx 8192
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"

```

#### Step 3: Build and Run

Tell Ollama to compile the model from your file, then run it:

```bash
ollama create bonsai-local -f Modelfile
ollama run bonsai-local

```

*(Note: If Ollama still throws a 500 error during `ollama create`, it means the specific version of Ollama installed on your system hasn't merged the Qwen 3.6 binary patch yet. If this happens, fallback to Method 1; LM Studio will run it seamlessly).*