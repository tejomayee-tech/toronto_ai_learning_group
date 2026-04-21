# 📦 Setting Up Your Linux Software Environment

Before installing the tools in the table below, ensure your system has the necessary "Package Managers" ready. On Debian-based systems like Ubuntu or Zorin OS, **APT** is built-in, while **Flatpak** and **Snap** may need a quick setup.

---

## 🛠️ Step 0: Check & Install Prerequisites

Run these commands in your terminal to see if you are ready to go.

### 1. Check if Package Managers are Installed

```bash
# Check APT (Always pre-installed on Ubuntu/Zorin)
apt --version

# Check Flatpak
flatpak --version

# Check Snap
snap --version

```

*If a command returns a version number, you are good! If it says "command not found," follow the install steps below.*

### 2. Install Missing Managers

If you need to install or enable Flatpak/Snap, use these commands:

| Manager | How to Install | Next Step (Crucial) |
| --- | --- | --- |
| **Flatpak** | `sudo apt update && sudo apt install flatpak` | `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo` |
| **Snap** | `sudo apt update && sudo apt install snapd` | *(None - Snap is ready immediately after install)* |

---

## 🔄 Windows vs. Linux: Software & Install Commands

Once your prerequisites are set, use the commands below to install your alternatives.

| Category | Windows Standard | Linux Alternative(s) | Install Command (Ubuntu/Debian) |
| --- | --- | --- | --- |
| **Photo Editing** | Photoshop | **GIMP** | `sudo apt install gimp` |
| **Digital Art** | Corel Painter | **Krita** | `sudo apt install krita` |
| **Vector Design** | Illustrator | **Inkscape** | `sudo apt install inkscape` |
| **Simple Drawing** | MS Paint | **Drawing** | `sudo apt install drawing` |
| **Video Editing** | Premiere Pro | **Kdenlive** | `sudo apt install kdenlive` |
| **Video Cutting** | Photos (Trim) | **LosslessCut** | `flatpak install flathub no.mifi.losslesscut` |
| **Audio Editing** | Audition | **Audacity** | `sudo apt install audacity` |
| **Streaming/Rec** | Bandicam | **OBS Studio** | `sudo apt install obs-studio` |
| **Media Player** | Windows Media | **VLC** | `sudo apt install vlc` |
| **Music Player** | iTunes | **Lollypop** | `sudo apt install lollypop` |
| **Camera** | Camera App | **Snapshot** | `flatpak install flathub org.gnome.Snapshot` |
| **Database GUI** | SSMS / Toad | **DBeaver** | `sudo snap install dbeaver-ce` |
| **PostgreSQL** | SQL Server | **PostgreSQL** | `sudo apt install postgresql postgresql-contrib` |
| **Virtualization** | Hyper-V | **Virt-Manager** | `sudo apt install virt-manager` |
| **Screenshots** | Snipping Tool | **GNOME Screenshot** | `sudo apt install gnome-screenshot` |

---

### 🚀 Pro-Tip: The "Master Install" Script

Want to install almost everything at once? Copy and paste this into your terminal:

```bash
# 1. Update system and install APT packages
sudo apt update && sudo apt install gimp krita inkscape drawing kdenlive audacity vlc lollypop gnome-screenshot postgresql postgresql-contrib virt-manager -y

# 2. Install Flatpak tools (Assumes Flatpak is set up)
flatpak install flathub no.mifi.losslesscut org.gnome.Snapshot -y

# 3. Install Snap tools
sudo snap install dbeaver-ce

```