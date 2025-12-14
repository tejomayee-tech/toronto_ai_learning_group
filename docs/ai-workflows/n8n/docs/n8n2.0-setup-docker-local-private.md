# N8N 2.0 Setup on Docker

Here is a step-by-step guide focusing on the most robust method for local deployment: **using `docker-compose`** for easier configuration and persistent data storage.

## Guide: Deploy n8n 2.0 Locally with Docker Compose

This method ensures your workflows, credentials, and settings persist even if you stop and restart the container.

### Phase 1: Prerequisites

1.  **Install Docker:** Ensure you have **Docker Desktop** (for Windows/macOS) or **Docker Engine and Docker Compose** (for Linux) installed and running on your system.
      * *You can verify this by running `docker --version` and `docker compose version` in your terminal.*
2.  **Create Project Directory:** Create a dedicated directory for your n8n setup to keep things organized.
    ```bash
    mkdir ~/n8n-local
    cd ~/n8n-local
    ```

### Phase 2: Create Configuration Files

In your `~/n8n-local` directory, you will create two files:

#### 1\. `.env` file (Environment Variables)

This file stores your configuration settings, making them easy to change without editing the main Docker configuration.

**File: `.env`**

```ini
# Core Configuration
N8N_HOST=localhost
N8N_PORT=5678
N8N_PROTOCOL=http
GENERIC_TIMEZONE=Europe/Berlin # CHANGE ME to your timezone (e.g., America/New_York)

# Security and Persistence (Crucial for production, but good practice locally)
# N8N_ENCRYPTION_KEY=YourStrongRandomStringHere # Recommended for production!

# Enable Task Runners (Recommended for n8n 2.0+)
N8N_RUNNERS_ENABLED=true
```

#### 2\. `docker-compose.yml` file

This file defines the n8n service, maps the ports, and sets up persistent storage.

**File: `docker-compose.yml`**

```yaml
version: '3.7'

services:
  n8n:
    # Use the official n8n image, which defaults to the latest version (2.x)
    image: n8nio/n8n:latest
    container_name: n8n_local
    restart: always # Always restart the container if it fails or the host reboots
    ports:
      # Maps the container port 5678 to the host port 5678 (http://localhost:5678)
      - "5678:5678"
    environment:
      # Loads all variables from the .env file
      - .env
    volumes:
      # Persist your workflows and credentials in a local folder
      - ./data:/home/node/.n8n
```

### Phase 3: Launch n8n

1.  **Start the containers:** Run the following command in your `~/n8n-local` directory.

    ```bash
    docker compose up -d
    ```

      * The `-d` flag runs the containers in "detached" (background) mode.

2.  **Check the logs (Optional but Recommended):** You can monitor the startup process. Look for the message `n8n listening on port 5678`.

    ```bash
    docker compose logs -f n8n
    ```

### Phase 4: Access n8n

1.  **Open your browser** and navigate to:
    **`http://localhost:5678`**

2.  **Initial Setup:** On your first visit, n8n will guide you through creating your administrator account.

Congratulations, you are now running the latest n8n 2.0 Community Edition locally with persistent storage\!

### Commands to Manage Your n8n Instance

| Action | Command | Notes |
| :--- | :--- | :--- |
| **Start** (after stopping) | `docker compose up -d` | Starts the containers defined in the `docker-compose.yml` file. |
| **Stop** (keep data) | `docker compose stop` | Stops the containers but keeps the data volume and configuration intact. |
| **Update n8n** | `docker compose pull n8n` <br> `docker compose up -d` | Pulls the latest `n8nio/n8n:latest` image and restarts your container with the new version. |
| **Remove** (erase all data) | `docker compose down -v` | **Warning:** Stops the container and **removes the data volume** (`-v`), deleting all workflows and credentials. |

To get a visual walk-through of this process and see n8n in action, you can watch this tutorial. [Self-Host Your Own Automation Platform with n8n + Docker](https://www.youtube.com/watch?v=gyn8bcOLdcA).

http://googleusercontent.com/youtube_content/1
