## n8n one step deploy on docker with docker-compose


### 🛠️ Required Tools

1.  **Docker Engine:** The core virtualization platform that manages and runs the containers.
2.  **Docker Compose:** A tool for defining and running multi-container Docker applications (like the one you provided) using the YAML file format.

-----

#### ⚙️ Step-by-Step Setup on Ubuntu

##### 1\. Install Docker Engine

You should install Docker from the official Docker repository to ensure you get the latest version.

1.  **Update Package Index:**

    ```bash
    sudo apt update
    ```

2.  **Install Prerequisites:** Install packages that allow `apt` to use a repository over HTTPS.

    ```bash
    sudo apt install ca-certificates curl gnupg lsb-release
    ```

3.  **Add Docker's Official GPG Key:**

    ```bash
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ```

4.  **Set Up the Repository:**

    ```bash
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

5.  **Install Docker Engine:**

    ```bash
    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

##### 2\. Configure Docker Permissions (Post-Installation)

By default, running Docker commands requires `sudo`. To run Docker commands without prepending `sudo`, you must add your user to the `docker` group.

1.  **Create the `docker` group (if it doesn't exist):**

    ```bash
    sudo groupadd docker
    ```

2.  **Add your current user to the `docker` group:**

    ```bash
    sudo usermod -aG docker $USER
    ```

3.  **Activate the changes:** You must **log out and log back in** (or simply restart your terminal session) for the group membership change to take effect.

4.  **Verify the installation:** After logging back in, run a test command. It works without `sudo` now.

    ```bash
    docker run hello-world
    ```

    > Note: Even if it doesnt work without sudo, user can still use sudo to run commands, e.g. `sudo docker run hello-world`

##### 3\. Install Docker Compose

In modern Docker installations (post-2022), **Docker Compose is included as a plugin** (`docker-compose-plugin`) with the Docker Engine installation (as done in Step 1.5).

  * **Verification:** You should be able to run `docker compose` (with the space, not the hyphen) directly:
    ```bash
    docker compose version
    ```
  * *(Optional: If you need the legacy hyphenated `docker-compose` command for older scripts, you would install it separately using `pip` or download the binary, but this is generally not recommended for new setups.)*


Running a multi-container application like your n8n/Ollama/Python stack on Windows is best achieved using **Docker Desktop with the WSL 2 backend**. This method provides the full power of the Linux Docker Engine while keeping the development environment seamlessly integrated into Windows.

Here is a step-by-step guide for setting up Windows, WSL 2, and Docker Desktop, and then running your `docker-compose.yml` file.

#### ⚙️ Step-by-Step Setup on Windows with WSL

You must be running **Windows 10 (version 2004 or higher) or Windows 11** with hardware virtualization enabled in your computer's BIOS/UEFI.

##### 1\. Install WSL 2

1.  **Open PowerShell or Command Prompt** as **Administrator**.
2.  Run the simplified install command:
    ```powershell
    wsl --install
    ```
    *This command automatically enables the necessary Windows features (WSL and Virtual Machine Platform), installs the latest Linux kernel, sets WSL 2 as the default, and installs an **Ubuntu** distribution.*
3.  **Restart your computer** when prompted.
4.  After the restart, the Ubuntu window will open automatically. Follow the prompts to **create a Linux username and password**.

##### 2\. Verify WSL Version

1.  Open PowerShell and run:
    ```powershell
    wsl --list --verbose
    ```
2.  Ensure that your Ubuntu distribution shows a **VERSION** of **2** and a **STATE** of **Running**.


##### 3\. Install Docker Desktop

1.  **Download Docker Desktop** from the official Docker website.
2.  Run the installer:
      * Ensure the option **"Use WSL 2 instead of Hyper-V"** is checked during the installation.
3.  **Restart your computer** if prompted by the installer.

##### 4\. Configure WSL 2 Integration

1.  **Launch Docker Desktop** (it may start automatically).
2.  Go to **Settings** (gear icon) \> **Resources** \> **WSL INTEGRATION**.
3.  Ensure that **"Enable WSL integration"** is checked.
4.  **Crucially, ensure your installed Ubuntu distribution is toggled ON in the list.**
5.  Click **Apply & Restart**. Docker Desktop will now share its Docker Engine daemon with your WSL 2 Ubuntu instance.

##### 5\. Verify Docker in WSL

1.  Open your **Ubuntu (WSL)** terminal.
2.  Run a simple Docker command to verify the connection:
    ```bash
    docker run hello-world
    ```
    You should see a message confirming the installation is working correctly.

##### Run the n8n/Ollama Stack


Create a folder for your project and navigate into it.

```bash
mkdir ~/n8n-ollama-project
cd ~/n8n-ollama-project
```

##### 2\. Create the `docker-compose.yml` File

Using a Linux text editor like `nano` or `vi`, create the file:

```bash
nano docker-compose.yml
```

Paste your exact YAML content into the file:

### 3\. Start the Services

In your Ubuntu terminal (within the project directory), run the command to start the stack:

```bash
docker compose up -d
```



## run with docker compose

### Step 1: Open Your Terminal or Command Prompt
First, you need to open a terminal (on Linux or macOS) or a command prompt/PowerShell (on Windows).

### Step 2: Navigate to the File's Directory
Using the `cd` (change directory) command, navigate to the folder where you saved your `docker-compose.yml` file. For example, if you saved the file in a folder called `n8n-project` on your desktop, you would use a command like this:

`cd ~/Desktop/n8n-project`

#### create a file on your machine as 'docker-compose.yml' below content
```yml

services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
    environment:
      - N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true
      # No need for N8N_LLM_SERVER_URL for Ollama integration >>       http://host.docker.internal:11434
      - N8N_LLM_SERVER_URL=http://ollama:11434
    depends_on:
      - ollama
    networks:
      - n8n-ollama-network


  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    restart: unless-stopped
    ports:
      - "11434:11434"  # Expose Ollama on the default port
    volumes:
      - ollama_data:/root/.ollama

    networks:
      - n8n-ollama-network

volumes:
  n8n_data:
  ollama_data:

networks:
  n8n-ollama-network:

```


### Step 3: Run the Docker Compose Command
Once you are in the correct directory, you can use the following command to start n8n. This command tells Docker Compose to read the `docker-compose.yml` file and start the services defined within it.

`docker compose up -d`

* `docker compose up`: This part of the command initiates the process of creating and starting the containers.
* `-d`: This flag stands for "detached mode." It runs the container in the background, so you can continue to use your terminal for other tasks without keeping it open to manage the running container.

### Step 4: Access N8N
After running the command, Docker will download the n8n image (if it's not already on your system) and start the container. You can then access the n8n web interface by opening your web browser and navigating to `http://localhost:5678`.


## Local LLMs

```shell
$ docker exec -ti ollama /bin/bash
root@b65cb311556b:/# ollama pull llama3.2
```

Several other GGUF models support tool use and function calling, which are essential for building agents that can interact with external APIs and services. The ability to use tools is a rapidly evolving area in the world of open-source LLMs.

### Step5: Login and create workflows

Follow the steps from Step 5 onwards in [docker-desktop-based-setup](./Step-by-step-guide-to-setup-n8n-locally-with-llm.md)