# 🚀 Complete llama.cpp Setup & Build Guide for Ubuntu

This guide assumes you are starting with a fresh Ubuntu installation and need to use **Homebrew (Linuxbrew)** to manage development dependencies like `cmake` and `gcc`.

## Step 1: Install System Prerequisites (Ubuntu's Package Manager)

First, install the fundamental tools needed for all development tasks, including Git and the core compilation toolchain (`build-essential`).

```bash
# 1. Update package lists
sudo apt update

# 2. Install core development tools, file/curl utilities, and git
sudo apt install build-essential procps curl file git
```

## Step 2: Install and Configure Homebrew (Linuxbrew)

Because you opted to use Homebrew, we'll install and configure it to manage the specific development packages required by `llama.cpp`.

### A. Run the Homebrew Installation Script

Run the official Homebrew installation script. You will be prompted to press `ENTER` to continue and enter your password for `sudo` access.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### B. Configure Homebrew in Your PATH

After the installation succeeds, you **must** run the following three commands to make the `brew` command and all packages it installs available in your terminal. This is the fix for the **`... is not in your PATH`** warning.

```bash
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```

-----

## Step 3: Install Core Dependencies (Homebrew)

Now that Homebrew is active, we use it to install the **C++ compiler (GCC)**, the **build system (CMake)**, and the **model download client library (cURL)**. These packages were the source of your initial errors (`Could NOT find CMake`, `Could NOT find CURL`).

```bash
# 1. Install the latest GCC compiler (required for C/C++ compilation)
brew install gcc

# 2. Install CMake (the build system generator)
brew install cmake

# 3. Install cURL development libraries (fixes the 'Could NOT find CURL' error)
brew install curl
```

-----

## Step 4: Clone the `llama.cpp` Repository

Use Git to download the source code for the project.

```bash
# Clone the repository
git clone https://github.com/ggerganov/llama.cpp.git

# Navigate into the project directory
cd llama.cpp
```

-----

## Step 5: Build `llama.cpp` with CMake

The CMake process is split into two parts: configuration and compilation. We use a dedicated `build` subdirectory to keep the source directory clean.

1.  **Create the build directory:**

    ```bash
    mkdir build
    cd build
    ```

2.  **Configure the build:**
    The `cmake ..` command checks for all dependencies (`gcc`, `cmake`, `curl`) and generates the necessary build files (Makefiles). Since you installed all dependencies in the previous steps, this should now succeed.

    ```bash
    cmake ..
    ```

3.  **Compile the code:**
    The `make` command compiles the project. The `-j$(nproc)` flag tells `make` to use all available CPU cores, which significantly speeds up the compilation process.

    ```bash
    make -j$(nproc)
    ```

### ✅ Successful Build Verification

After the compilation finishes, the core binaries (like `llama-cli`, `quantize`, and `perplexity`) will be located in the **`build/bin`** directory.

## Step 6: Running Your First Model

### A. Download a GGUF Model

You need a model in the modern **GGUF** format. Many great models are available from **TheBloke** on Hugging Face. For example, a small, fast model like Mistral 7B (Q4\_K\_M quantization) is a great starting point.

```bash
# Create a dedicated directory for your models
mkdir -p ../models
cd ../models

# Example: Download a popular small model (replace URL as needed)
curl -L 'https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf' -o mistral-7b.gguf
```

### B. Run the Model

Navigate back to the binaries directory and run the model with a simple prompt.

```bash
cd ../build/bin

# Replace mistral-7b.gguf with the actual filename if you downloaded a different one
./llama-cli -m ../../models/mistral-7b.gguf -p "What is the capital of Canada?"
```

This completes the full setup and build process, resolving all the prerequisite issues encountered.