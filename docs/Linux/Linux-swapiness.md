Running large AI models (like LLMs or Stable Diffusion) is a memory-heavy game. When your physical RAM fills up, Linux uses **Swap**—a space on your drive that acts as "overflow" RAM. While slower than hardware RAM, a well-configured swap on an SSD can be the difference between a model loading or your system crashing.

Since Zorin OS is based on Ubuntu, these steps work identically for both.

---

## Phase 1: Assessment

Before making changes, check your current status. Open your terminal (**Ctrl+Alt+T**) and run:

```bash
swapon --show

```

* **If you see output:** You have an active swap file or partition.
* **If it's empty:** You have no swap enabled.

---

## Phase 2: Creating a New Swap File on a Desired SSD

If you want to move or increase swap on a specific SSD, follow these steps. Let's assume you want a **32GB swap file** to handle large models.

### 1. Prepare the Location

If you have a secondary SSD mounted at `/mnt/data`, navigate there. Otherwise, we will use the root `/`.

### 2. Create the Swap File

We use `fallocate` because it’s nearly instant. Replace `32G` with your desired size.

```bash
sudo fallocate -l 32G /swapfile

```

**Validation:** Run `ls -lh /swapfile` to ensure it shows the correct size.

### 3. Set Permissions

For security, only the root user should be able to read this file.

```bash
sudo chmod 600 /swapfile

```

### 4. Format as Swap

```bash
sudo mkswap /swapfile

```

### 5. Enable the Swap

```bash
sudo swapon /swapfile

```

**Verification Point:** Run `free -h`. You should see the "Swap" total increase by the amount you just created.

---

## Phase 3: Making it Permanent

If you restart now, the swap will disappear. We need to add it to the file system table (`fstab`).

1. **Backup your fstab first:** `sudo cp /etc/fstab /etc/fstab.bak`
2. **Add the entry:**
```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

```



---

## Phase 4: Tuning "Swappiness"

**Swappiness** is a kernel parameter (0–100) that defines how aggressively the system moves data from RAM to Swap.

* **Low (e.g., 10):** The system avoids swap until RAM is almost full. **Best for SSDs and AI performance.**
* **High (e.g., 60+):** The system swaps early and often.

### 1. Check current Swappiness

```bash
cat /proc/sys/vm/swappiness

```

*(Default is usually 60)*

### 2. Set it for AI Workloads

For AI, we want the system to prioritize physical RAM as much as possible to maintain speed, but keep the swap ready. A value of **10** is generally the "sweet spot" for SSD users.

```bash
sudo sysctl vm.swappiness=10

```

### 3. Make Swappiness Permanent

Open the sysctl configuration file:

```bash
sudo nano /etc/sysctl.conf

```

Scroll to the bottom and add:
`vm.swappiness=10`
*(Press **Ctrl+O**, **Enter**, then **Ctrl+X** to save and exit.)*

---

## Phase 5: Troubleshooting & Restarts

* **Restart Needed?** Technically, no. Linux applies these changes instantly. However, a reboot is the best way to **validate** that your `/etc/fstab` edits were correct.
* **Out of Space?** If `fallocate` fails, you don't have enough room on that SSD.
* **Removing Old Swap:** If you have an old, small swap file you want to delete to save space:
1. `sudo swapoff /swapfile_old`
2. `sudo rm /swapfile_old`
3. Remove the corresponding line from `/etc/fstab`.



---

### Final Verification

Run this command one last time:

```bash
swapon --show

```

If you see your new file path and the correct size, you are ready to load those heavy tensors.


# Minitoring Swap memory

To monitor your system while running AI models, you need a way to see **System RAM/Swap** and **GPU/VRAM** at the same time. Since AI models often "spill over" from VRAM to System RAM and finally to Swap, tracking this flow is crucial.

Here are the best tools to use on Ubuntu and Zorin.

---

## 1. `nvtop` (The Best All-in-One for AI)

`nvtop` (Neat Videocard TOP) is like `htop` but designed for GPUs. It shows CPU, System RAM, Swap, and GPU VRAM all in one window.

### **Installation**

```bash
sudo apt update
sudo apt install nvtop

```

### **How to use it**

Just type `nvtop` in your terminal.

* **Top Bar:** Displays graphs for GPU usage and **VRAM** usage.
* **Middle Bar:** Shows your **System RAM** and **Swap** usage side-by-side.
* **Bottom List:** Shows which specific AI process (like `python3` or `ollama`) is eating the most memory.

---

## 2. `btop` (The Modern Visual Choice)

If you want a high-tech "dashboard" feel that includes disk I/O (to see if your SSD swap is being hammered), `btop` is the winner.

### **Installation**

```bash
sudo apt install btop

```

### **How to use it**

Run `btop`. It is fully mouse-interactive. You can see:

* Real-time Swap graphs.
* Disk read/write speeds (crucial for monitoring Swap performance).
* Process trees to see exactly what child processes your AI model is spawning.

---

## 3. The "No-Install" Quick Check

If you don't want to install anything new, you can use a "watch" loop with the built-in `free` command. This will refresh every 1 second:

```bash
watch -n 1 free -h

```

**What to look for:**

* **Mem / available:** If this hits near 0, your system will start using Swap.
* **Swap / used:** If this starts climbing rapidly, your model is larger than your RAM, and you are now relying on the SSD swap file we configured.

---

## 4. Troubleshooting "Out of Memory" (OOM)

When running AI models, if your terminal suddenly says `Killed`, it means the **OOM Killer** stepped in because even your Swap was full.

**Validation Step:**
If a model crashes, run this immediately to see if it was a memory issue:

```bash
sudo dmesg | grep -i "oom-killer"

```

* If you see "Out of memory: Killed process," you need to **increase your swap file size** using the steps from the previous guide.

---