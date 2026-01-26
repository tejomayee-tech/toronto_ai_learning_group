# Manage Ollama Service

## 🚀 Ollama installation

### 1. Run the Official Install Script

```bash
curl -fsSL https://ollama.com/install.sh | sh

```

### 2. Verify the New Version

Check that the installation succeeded and that you are no longer on 0.14.2.

```bash
ollama --version

```

---

## Part 3: Post-Install Verification

To ensure everything is running smoothly, check the service status:

```bash
systemctl status ollama

```

You should see **active (running)** in green text.

## 🛑 Stop Ollama


You can use `systemctl` commands, which manage system services on Ubuntu.

### 1\. Stop the Currently Running Service

This command immediately stops the Ollama server process.

```bash
sudo systemctl stop ollama.service
```

### 2\. Disable Auto-Start on Boot

This command prevents the `ollama.service` from automatically starting when your system boots up.

```bash
sudo systemctl disable ollama.service
```

### 3\. Verify the Status (Optional)

You can check if the service is stopped and disabled using this command:

```bash
sudo systemctl status ollama.service
```

Look for **"Active: inactive (dead)"** and **"Loaded: ...; disabled;"** in the output.

-----

## ▶️ Start Ollama On Demand

When you need to use Ollama (e.g., for LM Studio or a CLI session), you have a couple of options:

### Option 1: Start as a System Service (Recommended)

This is the cleanest way, as it runs in the background and is managed by systemd, just like before, but only when you manually start it.

```bash
sudo systemctl start ollama.service
```

After using it, you can stop it again with `sudo systemctl stop ollama.service`.

### Option 2: Run Manually in the Foreground

If you prefer to run it in your current terminal session and see the logs directly, you can run the `ollama serve` command. *Note: If you close the terminal window, the server will stop.*

```bash
ollama serve
```

To stop it when running in the foreground, you typically press **Ctrl + C**.

---

# Use Symbolic links

While LM Studio and Ollama are two different tools, they both deal with LLMs, and you can definitely **integrate them to share models and functionality**. The integration falls into two main categories:

1.  **Model Sharing (The Hard Way/The Tool Way):** Making models downloaded by Ollama visible inside LM Studio.
2.  **API Serving (The Easy Way):** Using the model server in LM Studio to expose models to Ollama (or vice versa, though less common).

Here is the most common and effective way to connect them, especially since you prefer to control the services manually.

-----

## 🔗 Method 1: Sharing Models via Symbolic Links (Linux Solution)

This method allows models you download with Ollama to be used directly by LM Studio, avoiding the need to download the same large files twice. This is an advanced technique common among Linux users.

### The Problem

  * **Ollama** and **LM Studio** use different internal directories to store models.
  * They both primarily use the **GGUF** model format, which makes sharing possible.

### The Solution: Create Symlinks

Since you are on Ubuntu, you can use the `ln` command to create **symbolic links** (shortcuts) that point LM Studio's model directory to Ollama's model files.

1.  **Ensure Ollama is running** (temporarily) to download a model if you haven't already:

    ```bash
    sudo systemctl start ollama.service
    ollama pull llama3:8b # Example model
    sudo systemctl stop ollama.service
    ```

2.  **Locate the directories:**

      * **Ollama Model Directory (Blobs):** Models are stored as large, hashed files here:
          * `~/.ollama/models/blobs/`
      * **LM Studio Model Directory:** This is where LM Studio expects to find its models:
          * `~/.lmstudio/models/` or `~/.cache/lm-studio/models/` (check your specific version, but `~/.lmstudio/models/` is common)

3.  **Use a dedicated script (Recommended):**

    Since the process of finding the specific GGUF file inside Ollama's structure and linking it to the correct LM Studio subfolder is complex, many users rely on community scripts to automate this.

    Search for tools like **`ollama-to-lmstudio-symlinks`** or simple Python scripts on GitHub that perform this action. These tools will automatically:

      * List the models Ollama has downloaded.
      * Create a matching directory structure inside the LM Studio directory.
      * Create a symlink from Ollama's model file (blob) to the new LM Studio file path.

    > **Note:** If you choose to attempt this manually, be aware it can be tedious and depends on the exact model file naming conventions of both tools. Using a community-developed utility script (search is necessary) is highly recommended.

-----

## 🔌 Method 2: Use LM Studio as an OpenAI-Compatible Server

This method is simpler and uses the API capability of **LM Studio** to expose models to other applications, like Ollama (though Ollama usually acts as the server). This is great if you want to use the models you downloaded in LM Studio with the Ollama command-line tools.

### 1\. Start a Server in LM Studio

  * Open **LM Studio**.
  * Click the **Server icon** ($\text{< >}$ or a gear/port icon) on the left sidebar.
  * Select the model you want to run from the dropdown.
  * Click **Start Server**.
      * LM Studio runs an OpenAI-compatible API server, usually on **`http://localhost:1234`**.

### 2\. Use the LM Studio API

Any application (including Python scripts, web UIs, or even a tool that *expects* Ollama) can now talk to the LM Studio server using the standard OpenAI API endpoints on `http://localhost:1234`.

Since you have full control over starting and stopping Ollama, using the `systemctl` commands you learned is the perfect workflow:

1.  **Stop Ollama** when you want to use models managed by LM Studio:
    ```bash
    sudo systemctl stop ollama.service
    ```
2.  **Start LM Studio's Server** (via the GUI).
3.  **Run your application/code** against LM Studio's server (port 1234).
4.  **Stop LM Studio's Server** (via the GUI) when finished.
5.  **Restart Ollama** when you need it:
    ```bash
    sudo systemctl start ollama.service
    ```

In summary, for **model file sharing** use **Symbolic Links** (with a helper script). For **running a server** with your preferred models, you can choose to run **LM Studio's server** *or* **Ollama's server** and use your applications against the one that is currently running.


## 🗑️ Clean Uninstallation

Since you were running an older version, a clean wipe ensures no "zombie" binaries or old service configurations interfere with the new installation.

### 1. Stop and Disable the Service

This stops the current background process and prevents it from starting on reboot.

```bash
sudo systemctl stop ollama
sudo systemctl disable ollama
sudo rm /etc/systemd/system/ollama.service

```

### 2. Remove the Binary

Locate and delete the executable.

```bash
sudo rm $(which ollama)

```

### 3. Wipe Data and User (The "Clean Slate" Step)

Ollama stores massive model files in `/usr/share/ollama`. We also need to remove the dedicated system user.

```bash
sudo rm -rf /usr/share/ollama
sudo userdel ollama

```

> **Note on Groups:** If you see an error like `group ollama not removed because it has other members`, it means your own user account is likely still linked to it. You can ignore this or run `sudo groupdel ollama` to finish it off.

### 4. Optional: Clear Personal Configs

If you want to delete your personal chat history and local settings, remove the hidden directory in your home folder:

```bash
rm -rf ~/.ollama

```

---


### Summary of Commands

| Action | Command |
| --- | --- |
| **Uninstall** | Stop service  Delete binary  Wipe `/usr/share/ollama` |
| **Reinstall** | `curl -fsSL https://ollama.com/install.sh |
| **Check Version** | `ollama --version` |

---