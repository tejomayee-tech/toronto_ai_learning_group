# Lets add: Docker + Open WebUI (Windows & Mac)

## What You're Setting Up (Simple View)

You're installing:

- **Docker Desktop** — runs apps in containers (like mini virtual machines)
- **Open WebUI** — ChatGPT-style interface
- Connect it to **Ollama** — your local AI brain

End result:
You open a browser — looks like ChatGPT — runs locally

---

## PART 1 — Windows (Step-by-Step)

### Step 1 — Install Docker Desktop

1. Go to: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Click **Download for Windows**
3. Run the installer

#### IMPORTANT (Most people get stuck here)

During install, make sure:

- "Use WSL 2 instead of Hyper-V" is enabled (default)
- Accept all prompts

#### If install fails:

Run this in PowerShell (as Admin):

```bash
wsl --install
```

Then restart your PC.

---

### Step 2 — Start Docker

1. Press `Windows Key`
2. Open **Docker Desktop**
3. Wait until it says:

   **"Docker is running"**

First launch may take 1–3 minutes

---

### Step 3 — Verify Docker Works

Open PowerShell:

```bash
docker --version
```

If you see a version → good  
If not → Docker isn't running yet

---

### Step 4 — Run Open WebUI

Now paste this EXACT command:

```bash
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

#### What this does (simple)

- Downloads WebUI
- Runs it locally
- Connects it to your system

---

### Step 5 — Open It

Open your browser and go to:

[http://localhost:3000](http://localhost:3000)

#### First Time Setup Screen

You'll see:

- Create account (just local)
- Login

---

### Step 6 — Connect to Ollama

If Ollama is already installed:

1. Go to **Settings**
2. Find:

   ```
   Ollama API URL
   ```
3. Set it to:

   ```
   http://host.docker.internal:11434
   ```

#### Test it

- Go back to chat
- Select model: `gemma4:e4b`
- Send a message

---

## PART 2 — Mac (Step-by-Step)

### Step 1 — Install Docker Desktop

1. Download from Docker website
2. Open `.dmg`
3. Drag Docker → Applications
4. Launch Docker

---

### Step 2 — Start Docker

Wait until:

**"Docker Desktop is running"**

---

### Step 3 — Verify

Open Terminal:

```bash
docker --version
```

---

### Step 4 — Run WebUI

```bash
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

---

### Step 5 — Open It

[http://localhost:3000](http://localhost:3000)

---

### Step 6 — Connect Ollama (Mac)

Set:

```
http://localhost:11434
```

---

## Everyday Usage (Super Simple)

### Start everything

1. Open Docker Desktop
2. Run:

   ```bash
   docker start open-webui
   ```

---

### Stop it

```bash
docker stop open-webui
```

---

### Restart

```bash
docker restart open-webui
```

---

## Common Problems (Fix Fast)

### "Cannot connect to localhost:3000"

- Docker not running
- Container not started

Run:

```bash
docker ps
```

---

### WebUI opens but no models

Ollama not connected

Fix URL:

- Windows:

  ```
  http://host.docker.internal:11434
  ```
- Mac:

  ```
  http://localhost:11434
  ```

---

### "Connection refused" to Ollama

Run:

```bash
ollama run gemma4:e4b
```

(Starts Ollama server)

---

### Port already in use

Run:

```bash
docker run -d -p 3001:8080 ...
```

Then open:

[http://localhost:3001](http://localhost:3001)

---

### Everything is slow

Normal if:

- 16GB RAM
- CPU only
- Large model

Use smaller model:

```
gemma4:e4b
```

---

## Mental Model (So You Don't Get Lost)

Think of it like this:

- **Ollama** — brain
- **Docker** — container box
- **WebUI** — face (ChatGPT interface)

---

## Minimum Working Setup (Fastest Path)

If you just want it working:

1. Install Docker
2. Run:

   ```bash
   docker run -d -p 3000:8080 --name open-webui ghcr.io/open-webui/open-webui:main
   ```
3. Open:

   ```
   http://localhost:3000
   ```
4. Connect Ollama

Done.

---

## What next:

- Adding **file upload (PDFs, images, RAG)**
- Running **LLaVA multimodal in WebUI**
- Using **GPU acceleration inside Docker**
- Building a **full local AI workstation (like ChatGPT Pro)**
