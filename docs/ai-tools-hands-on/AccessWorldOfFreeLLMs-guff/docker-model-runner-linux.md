# **Docker Model Runner (DMR)** 

## 🚀 The Docker Coexistence Guide with Model Runner

You might have **standalone Docker Engine (Host Engine)** already installed, **Docker Desktop**, and the **Docker Model Runner (DMR)** can also run in parallel.

The core concept is to use **Docker Contexts** to switch the target of your `docker` CLI, and **Systemd** commands to manage the Host Engine service.

### I. Setup: Install and Enable Components

1.  **Install Docker Desktop:** Follow the official instructions to install Docker Desktop.
2.  **Enable Model Runner (DMR):**
      * Launch **Docker Desktop**.
      * Go to **Settings** $\rightarrow$ **AI** (or **Features in development**).
      * Check **Enable Docker Model Runner**.
      * Click **Apply & Restart**.

### II. Managing the Host Docker Engine Service (The Golden Rule)

When you install Docker Engine on Ubuntu, it typically sets itself up as a **systemd service** that starts automatically at boot (`docker.service`, `docker.socket`, and `containerd.service`).

To prevent conflicts with Docker Desktop's engine, you should manage this service.

| Goal | Command | Description |
| :--- | :--- | :--- |
| **Stop Temporarily** (For the current session) | `sudo systemctl stop docker docker.socket containerd` | Shuts down the Host Engine immediately. This is the command you run daily before using Docker Desktop. |
| **Disable Permanently** (Prevent autostart on boot) | `sudo systemctl disable docker.service docker.socket containerd.service` | Prevents the Host Engine from starting automatically when you reboot your machine. |
| **Enable Permanently** (Restore autostart) | `sudo systemctl enable docker.service docker.socket containerd.service` | Re-enables the Host Engine to start automatically when you reboot. |
| **Start/Restart** (To use the Host Engine) | `sudo systemctl start docker` | Starts the Host Engine service (if it was disabled or stopped). |

### III. Switching Between Engine Environments with Docker Contexts

The `docker` CLI uses a **context** to determine which Docker Engine daemon it should communicate with.

#### 1\. To Work in **Docker Desktop** (and use Model Runner)

This environment is ideal for using the GUI, Kubernetes, and the integrated Model Runner features.

1.  **Stop the Host Engine (Crucial):** If it's running, shut down the standalone service.
    ```bash
    sudo systemctl stop docker docker.socket containerd
    ```
2.  **Switch the CLI to Docker Desktop:** The `desktop-linux` context points to the VM-based engine.
    ```bash
    docker context use desktop-linux
    ```
3.  **Verify:** Check the currently active context.
    ```bash
    docker context ls
    ```
    *(The `desktop-linux` entry should have the `*`.)*

#### 2\. To Work in the **Standalone Host Engine**

This environment is useful if you need to run containers directly on your host or troubleshoot the base installation.

1.  **Stop Docker Desktop:** Quit the application from the tray icon or command line.
    ```bash
    systemctl --user stop docker-desktop
    ```
2.  **Ensure Host Engine is Running:** Start the service if it was stopped or disabled.
    ```bash
    sudo systemctl start docker
    ```
3.  **Switch the CLI to the Host Engine:** The `default` context points to the host's daemon.
    ```bash
    docker context use default
    ```
4.  **Verify:** Check the currently active context.
    ```bash
    docker context ls
    ```
    *(The `default` entry should have the `*`.)*

### IV. Running Models with Docker Model Runner (DMR)

The Model Runner service is tightly integrated with the Docker Desktop environment.

1.  **Ensure you are in the `desktop-linux` context.**
2.  **Pull a Model:**
    ```bash
    docker model pull ai/llama2:7b-chat
    ```
3.  **Run a Model (Interactive Chat):**
    ```bash
    docker model run ai/llama2:7b-chat
    ```
4.  **Check Status:** The Model Runner service itself runs outside the main Docker Desktop VM but is managed by it.
    ```bash
    docker model status
    ```

# #########################################################################

Yes, you can run and manage all three: your **standalone Docker Engine**, **Docker Desktop**, and **Docker Model Runner** on Ubuntu.

**Docker Model Runner (DMR)** is a feature of Docker Desktop (and also available as a plugin for Docker Engine CE) that allows you to run local AI models (like LLMs) using familiar `docker model` CLI commands.

Here is the regenerated guide, including the Model Runner steps and how it interacts with the two Docker environments.

-----

## 🚀 The Docker Coexistence Guide with Model Runner

The core concept for managing these environments is **Context Switching** using the `docker context` command.

### I. Setup: Enable Model Runner

Docker Model Runner (DMR) is typically enabled through the Docker Desktop application settings.

1.  **Install Docker Desktop:** Complete the installation as you have done.
2.  **Enable DMR:**
      * Launch **Docker Desktop** (from the Applications Menu).
      * Go to **Settings** (gear icon) $\rightarrow$ **AI** (or **Features in development** in older versions).
      * Ensure **Enable Docker Model Runner** is checked.
      * **Recommended:** Select **Enable host-side TCP support** (default port 12434) if you plan to access the model API from applications *outside* of a container (e.g., a local web app).
      * Click **Apply & Restart**.

Once enabled, the `docker model` CLI command becomes available for both the Docker Desktop and the standalone Engine (though the Model Runner service itself runs outside the Docker Desktop VM).

### II. The Golden Rule: Stop the Host Engine

To prevent conflicts (especially on ports) and resource contention, you should **stop** your standalone Docker Engine service when you are using Docker Desktop and its related tools like Model Runner.

| Scenario | Action | Command |
| :--- | :--- | :--- |
| **Using Docker Desktop/Model Runner** | **Stop** the Host Engine | `sudo systemctl stop docker docker.socket containerd` |
| **Using Standalone Host Engine** | **Stop** Docker Desktop | `systemctl --user stop docker-desktop` |

### III. Switching Between Engine Environments

The `docker context` command is your control panel for directing the `docker` CLI.

#### 1\. To Use **Docker Desktop** (and Model Runner)

This is the context you use for GUI management, Kubernetes, and local AI model running.

```bash
# 1. Ensure the Host Engine is stopped
sudo systemctl stop docker

# 2. Start Docker Desktop and switch the CLI context
docker context use desktop-linux
```

  * **Result:** The `docker` commands now target the Docker Engine inside the Docker Desktop VM. The `docker model` commands will use the Model Runner service managed by Docker Desktop.

#### 2\. To Use the **Standalone Host Engine**

This is the context you use for traditional container workloads running directly on your Ubuntu host.

```bash
# 1. Stop Docker Desktop (quitting the application is sufficient)
systemctl --user stop docker-desktop

# 2. Switch the CLI to the Host Engine
docker context use default

# 3. Ensure the Host Engine is running
sudo systemctl start docker
```

  * **Result:** The `docker` commands now target your system's `/var/run/docker.sock`. Note that if you use Model Runner via Docker Engine CE instead of Desktop, the `default` context is where you would access it, but managing both is less common.

### IV. Running Models with Docker Model Runner (DMR)

DMR uses the **`docker model`** CLI command and typically runs the inference server natively on the host machine for optimal performance.

1.  **Verify DMR is Active:** Ensure you are using the `desktop-linux` context and Docker Desktop is running.

    ```bash
    docker model status
    # Output should confirm: Docker Model Runner is running.
    ```

2.  **Pull a Model:** Models are pulled from Docker Hub (or other OCI registries) using the `docker model pull` command.

    ```bash
    docker model pull ai/smollm2:latest
    ```

3.  **Run a Model (Interactive Chat):** This will start an interactive chat session in your terminal, similar to using a local LLM application.

    ```bash
    docker model run ai/smollm2:latest
    ```

4.  **Run a Model (One-Shot Prompt):** You can also send a single prompt from the command line.

    ```bash
    docker model run ai/smollm2:latest "Explain the difference between a container and an image."
    ```

5.  **Access Model API from a Container:** Your application running in a container can access the model using the internal DNS name: `http://model-runner.docker.internal/`.

      * For example, a `docker run` command for an app would target an API endpoint like: `http://model-runner.docker.internal/engines/v1/chat/completions`.

This setup allows you to keep your traditional Docker development flow separate from your new GenAI/LLM local model experimentation, all managed through the same `docker` command line tool.

-----

Would you like a brief guide on how to integrate a locally run model into a containerized application using Docker Compose?