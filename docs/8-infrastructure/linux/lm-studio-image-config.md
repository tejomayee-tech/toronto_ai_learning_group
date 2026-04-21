# 🛸 Complete LM Studio Setup Guide for Ubuntu

Follow these steps in order to ensure LM Studio runs with its own icon in your applications list and opens a terminal for logs.

## 🛠️ Step 1: Install System Dependencies

Modern Ubuntu versions (22.04 and 24.04+) do not include the old FUSE library required by AppImages by default.

1. **Open your terminal** and run:
```bash
sudo apt update
sudo apt install libfuse2

```


*Note: If you are on Ubuntu 24.04 and the above fails, use `sudo apt install libfuse2t64`.*

---

## 📂 Step 2: Organize Your Files

Create a stable home for the application to prevent path errors later.

1. **Create the directory**:
```bash
mkdir -p ~/Applications/LMStudio

```


2. **Move your files**: Move the downloaded AppImage and your `lmstudio.png` icon into that folder.
3. **Identify your username**: Run this command and remember the output (e.g., `vijay`):
```bash
whoami

```



---

## 📜 Step 3: Create the Launch Script

This script handles the `--no-sandbox` requirement and ensures the app starts in the correct directory.

1. **Create the script**:
```bash
nano ~/Applications/LMStudio/lmstudio-launch.sh

```


2. **Paste this exact content**:
```bash
#!/bin/bash
# Ensure the script runs from its own directory
cd "$(dirname "$0")"

# Match this filename to your downloaded version
APPIMAGE_FILE="LM-Studio-0.3.32-2-x64.AppImage"

# Launch with the sandbox bypass
./"$APPIMAGE_FILE" --no-sandbox

```


3. **Save and exit** (Ctrl+O, Enter, Ctrl+X).
4. **Make everything executable**:
```bash
chmod +x ~/Applications/LMStudio/*.AppImage
chmod +x ~/Applications/LMStudio/*.sh

```



---

## 🖥️ Step 4: Create the Desktop Launcher

This step makes the app appear in your "Show Applications" drawer with the correct icon and a log window.

1. **Create the `.desktop` file**:
```bash
nano ~/.local/share/applications/lmstudio.desktop

```


2. **Paste this content** (Replace **`YOUR_USERNAME`** with the name from Step 2):
```desktop
[Desktop Entry]
Name=LM Studio (Console)
Comment=Run local LLMs with terminal logs
Exec=gnome-terminal -- /bin/bash -c "/home/YOUR_USERNAME/Applications/LMStudio/lmstudio-launch.sh; echo; echo 'LM Studio process exited. Press ENTER to close.'; read"
Icon=/home/YOUR_USERNAME/Applications/LMStudio/lmstudio.png
Terminal=false
Type=Application
Categories=AI;Development;
StartupWMClass=LM Studio

```


3. **Save and exit**.
4. **Register the app**:
```bash
gio set ~/.local/share/applications/lmstudio.desktop metadata::trusted true
update-desktop-database ~/.local/share/applications/

```



---

## 🤖 Step 5: Update Continue (VS Code) Config

To use your specific models in VS Code, update your `config.yaml` to point to the LM Studio server.

1. **In LM Studio**: Go to the "Local Server" tab, load your model, and click **Start Server**.
2. **In VS Code**: Update your `models` section:

```yaml
models:
  - name: GPT-OSS 120B
    provider: lmstudio
    model: openai/gpt-oss-120B
    apiBase: http://localhost:1234/v1
  - name: GPT-OSS 20B
    provider: lmstudio
    model: openai/gpt-oss-20B
    apiBase: http://localhost:1234/v1
  - name: Magistral Small
    provider: lmstudio
    model: mistralai/Magistral-Small-2509
    apiBase: http://localhost:1234/v1

```
