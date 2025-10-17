## n8n one step deploy on docker with docker-compose



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