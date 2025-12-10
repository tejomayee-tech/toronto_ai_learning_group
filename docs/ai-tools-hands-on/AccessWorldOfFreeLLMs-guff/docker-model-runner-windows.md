This guide is tailored for a clean Windows environment where **Docker is not installed at all**. It focuses purely on installing and using **Docker Desktop**, which is the required platform to run the integrated **Docker Model Runner (DMR)** on Windows.

When you install Docker Desktop, it installs its own dedicated Docker Engine, so you don't need a separate installation.

-----

## 🖥️ Docker Desktop & Model Runner: Quick Start Guide (Windows)

### I. Prerequisites & System Setup

Docker Desktop relies on Windows virtualization features. Before you start, ensure your system is ready:

1.  **System Requirements:** You need Windows 10/11 64-bit and at least 4GB of RAM.
2.  **Virtualization Enabled:** Ensure **Hardware Virtualization** (Intel VT-x or AMD-V) is enabled in your computer's BIOS/UEFI settings.
3.  **WSL 2 Integration (Recommended):** Docker Desktop's modern backend uses the **Windows Subsystem for Linux (WSL 2)**. While the installer can prompt you to enable it, you can ensure it's up-to-date by running this in an **Administrator PowerShell** window:
    ```powershell
    wsl --update
    ```
    *(You may need to restart your PC after running this.)*

### II. Installation of Docker Desktop

1.  **Download:** Go to the official Docker website and download the **Docker Desktop for Windows installer** (`Docker Desktop Installer.exe`).
2.  **Install:** Double-click the installer and run it.
      * **Crucial Step:** On the configuration screen, ensure the option **"Use WSL 2 instead of Hyper-V (recommended)"** is checked.
      * The installer will install the Docker Engine, Docker CLI, and set up the necessary WSL components.
3.  **Launch:** After the installation finishes, launch **Docker Desktop** from your Start menu. It will take a minute or two to start the embedded Docker Engine.

### III. Enable Docker Model Runner (DMR)

DMR is built into Docker Desktop and must be enabled through its settings interface.

1.  **Open Settings:** Click the **Docker whale icon** in the system tray, then click the **Settings** gear icon.
2.  **Navigate to AI:** In the left sidebar, click the **AI** tab (or **Features in development** in older versions).
3.  **Enable DMR:** Check the box next to **Enable Docker Model Runner**.
      * **Optional: GPU Acceleration:** If you have a supported NVIDIA GPU, you will see an option to **Enable GPU-backed inference**. Check this for faster model performance.
      * **Optional: API Access:** If you plan to access the model's API from a web app on your Windows host, check **Enable host-side TCP support**.
4.  **Apply:** Click **Apply & Restart** at the bottom right.

### IV. Running Your First AI Model

Once Docker Desktop has restarted and the Model Runner is enabled, you can interact with it directly from your command line (PowerShell or Command Prompt).

1.  **Check Docker Status:** Open PowerShell and verify Docker is running.

    ```bash
    docker info
    ```

    *If successful, you will see detailed information about the Docker Engine.*

2.  **Check Model Runner Status:**

    ```bash
    docker model status
    # Output should confirm: Docker Model Runner is running.
    ```

3.  **Pull a Model:** Use the `docker model pull` command to download a model (like Llama 2 or Gemma) from Docker Hub's `ai/` namespace.

    ```bash
    docker model pull ai/llama2:7b-chat
    ```

    *(This downloads the model file and makes it ready for inference.)*

4.  **Run the Model (Interactive Chat):** This will start a conversation right in your terminal window.

    ```bash
    docker model run ai/llama2:7b-chat
    # Prompt: Hello! I'm a user.
    ```

    *Type `/bye` to exit the chat session.*

**You are now successfully running AI models locally on Windows using Docker Desktop and Model Runner, without having any prior standalone Docker installation\!**

-----
That's the ultimate goal of the Model Runner—to provide a simple API for your applications\!

Docker Model Runner (DMR) exposes an **OpenAI-compatible API**. This is the key feature, as it means you can use existing code, libraries (like the Python OpenAI SDK), and tools built for OpenAI to interact with your local models.

Here is the simple guide on how to access the model API from your browser or application, which requires enabling **Host-Side TCP Support**.

-----

## 🌐 Accessing the Model Runner API

You have two main ways to access the running model, depending on whether the request originates from a **container** or your **Windows host machine**.

### 1\. Access from your Windows Host (Browser, Postman, Python Script)

To access the model from an application or browser *directly on your Windows machine*, you must enable the TCP port in Docker Desktop settings.

#### A. Enable Host-Side TCP Support

1.  **Open Docker Desktop Settings:** Click the whale icon $\rightarrow$ **Settings** (gear icon).
2.  **Go to AI Tab:** Navigate to the **AI** tab.
3.  **Enable TCP:** Check the box next to **Enable host-side TCP support**.
      * The default port is **12434**. You can change this if the port is already in use by another application.
4.  **Apply:** Click **Apply & Restart**.

#### B. The API Endpoint

Once enabled, the base URL for accessing the model API from your host machine is:

$$
\text{http://localhost:12434/}
$$

This base URL has the standard **OpenAI API Endpoints** appended to it.

| API Function | Full URL Endpoint (Example) |
| :--- | :--- |
| **Chat Completions** | `http://localhost:12434/engines/llama.cpp/v1/chat/completions` |
| **List Available Models** | `http://localhost:12434/engines/llama.cpp/v1/models` |

> **Note:** The `/engines/llama.cpp/v1` part specifies the inference backend (which is usually `llama.cpp` for GGUF models). You can often omit this part and use the shorter URL: `http://localhost:12434/v1/chat/completions`.

#### C. Testing in PowerShell/Command Prompt

You can send a request using `curl` to test if the Model Runner is reachable:

```powershell
# This command checks if the Model Runner service is running and listening on the port
curl http://localhost:12434/
```

**Expected Response:** You should see a simple message confirming the service is running, such as: `Docker Model Runner. The service is running.`

### 2\. Access from within a Container (Docker Compose)

If you are building an application in a Docker container (e.g., a FastAPI server), the container needs a different hostname to reach the Model Runner on the host.

#### A. The API Endpoint

The special DNS name for containers to reach the host-side Model Runner is:

$$
\text{[http://model-runner.docker.internal/](http://model-runner.docker.internal/)}
$$

The full URL for a chat completion endpoint from *inside* your container would look like this:

$$
\text{[http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions](http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions)}
$$

#### B. Example in a Docker Compose File

If you are using Docker Compose to run a web application that needs the model, you would configure its service like this:

```yaml
version: '3.8'
services:
  # Your Web Application Container
  frontend-app:
    image: my-app-image:latest
    ports:
      - "80:8000"
    environment:
      # Use the special hostname for the model runner
      OPENAI_BASE_URL: http://model-runner.docker.internal/engines/llama.cpp/v1
```

By enabling the TCP host support and knowing these two hostnames, you can easily integrate your local models into any development project\!