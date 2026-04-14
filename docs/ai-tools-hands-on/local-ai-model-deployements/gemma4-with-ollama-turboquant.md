# Beginner-Friendly Guide: Run Gemma 4 Locally (Windows & Mac)

## What You're Actually Doing (Simple Explanation)

You're setting up 3 things:

1. **Ollama** — runs the AI model locally
2. **Gemma 4 model** — the brain
3. **Open WebUI (optional)** — a ChatGPT-style interface

---

## PART 1 — Windows Setup (Step-by-Step)

### Step 1 — Install Ollama

1. Go to: [https://ollama.com](https://ollama.com)
2. Click **Download for Windows**
3. Run the `.exe` installer
4. Finish install (just click Next → Install)

#### Verify it works

1. Press `Windows Key`
2. Type **PowerShell** → open it
3. Run:

```bash
ollama --version
```

If you see a version number → you're good  
If "command not found" → restart your PC and try again

---

### Step 2 — Download a Model (This Is Important)

In PowerShell, run:

#### Beginner (FAST, recommended)

```bash
ollama pull gemma4:e4b
```

#### Advanced (SMARTER but slower)

```bash
ollama pull gemma4:26b
```

This takes time (5–20 minutes depending on internet)

---

### Step 3 — Run the AI

After download finishes:

```bash
ollama run gemma4:e4b
```

You'll see:

```
>>> Send a message:
```

Now just type:

```
Explain quantum computing simply
```

That's it — you're running AI locally.

---

### Step 4 — (Optional) ChatGPT-like UI

#### Install Docker Desktop

1. Go to: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Install it
3. Open Docker Desktop
4. Wait until it says **Running**

#### Run Open WebUI

In PowerShell:

```bash
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

#### Open it in browser:

[http://localhost:3000](http://localhost:3000)

You now have a ChatGPT-like interface.

---

## PART 2 — Mac Setup (Step-by-Step)

### Step 1 — Install Ollama

1. Go to [https://ollama.com](https://ollama.com)
2. Download for Mac
3. Open `.dmg`
4. Drag Ollama → Applications

#### Verify

Open **Terminal** and run:

```bash
ollama --version
```

---

### Step 2 — Download Model

Same as Windows:

```bash
ollama pull gemma4:e4b
```

---

### Step 3 — Run It

```bash
ollama run gemma4:e4b
```

---

### Step 4 — (Optional UI)

#### Install Docker Desktop (Mac)

1. Download Docker Desktop
2. Open it
3. Wait until running

#### Run WebUI

```bash
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

Open: [http://localhost:3000](http://localhost:3000)

---

## Common Beginner Issues (And Fixes)

### "ollama not recognized"

- Restart your computer
- Reinstall Ollama

---

### Docker fails to start

- Enable virtualization in BIOS (Windows)
- Make sure Docker Desktop is running

---

### Model is VERY slow

That's normal if:

- You chose `26b`
- You only have 16GB RAM
- No GPU acceleration

Solution: Use:

```
gemma4:e4b
```

---

### Out of memory / freezing

- Close Chrome tabs
- Use smaller model
- Don't run other heavy apps

---

## What TurboQuant Actually Does (Simple)

Without TurboQuant:

- AI memory fills up fast → crashes or slows

With TurboQuant:

- Compresses memory → lets you have **long conversations**

You don't need to enable anything — it's automatic.

---

## What You Should Do First (Simple Path)

If you want the **easiest success path**:

1. Install Ollama
2. Run:

   ```bash
   ollama pull gemma4:e4b
   ```
3. Run:

   ```bash
   ollama run gemma4:e4b
   ```
