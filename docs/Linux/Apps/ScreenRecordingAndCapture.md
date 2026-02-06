Here is a dedicated guide for screen recording, broadcasting, and screenshot tools, formatted to match your previous documentation.

# 🖥️ Linux Screen Capture & Broadcasting Tools

This guide covers the best tools for recording your desktop, live streaming, and taking high-quality screenshots.

---

## 1. OBS Studio (Professional Streaming & Recording)

**Purpose:** The industry standard for open-source screen recording and live streaming.

**Features:**

* **Scene Composition:** Mix multiple sources (webcam, windows, images) into one layout.
* **Virtual Camera:** Use your OBS scene as a webcam in Zoom, Discord, or Teams.
* **Audio Mixing:** High-fidelity audio control with noise suppression and gain filters.

### Installation (Ubuntu, Zorin OS, Mint)

To ensure the Virtual Camera and the latest features work correctly, use the official PPA:

```bash
# 1. Install the Virtual Camera driver
sudo apt install v4l2loopback-dkms

# 2. Add the official OBS repository
sudo add-apt-repository ppa:obsproject/obs-studio

# 3. Update and Install
sudo apt update
sudo apt install obs-studio

```

---

## 2. GNOME Screenshot (Simple & Reliable)

**Purpose:** A classic, lightweight utility for capturing static images of your screen.

**Features:**

* **Flexible Capture:** Take a screenshot of the whole screen, a specific window, or a custom area.
* **Timed Delay:** Set a 5-second delay to open menus before the shot is taken.
* **Effects:** Option to include or exclude the mouse pointer and window borders.

### Installation

```bash
# Ubuntu/Debian/Zorin
sudo apt update && sudo apt install gnome-screenshot

```

**How to Use:**

* Search for **"Screenshot"** in your app menu.
* **Shortcut Tip:** On many Linux distros, pressing `PrtSc` (Print Screen) will trigger this tool automatically.

---

## 3. GNOME Snapshot (Modern Camera Tool)

**Purpose:** A modern, minimal camera application for taking pictures and videos from your webcam.

**Features:**

* **Simple Interface:** Optimized for modern desktop environments.
* **Fast Switching:** Toggle between photo and video mode instantly.

### Installation

```bash
# Recommended via Flatpak
flatpak install flathub org.gnome.Snapshot

```

---

## 🧹 How to Clean Up and Fix Common Issues

If you find that screen tools are not working correctly (especially on Zorin OS or Ubuntu), or if you want to remove old configurations, follow these steps:

### A. Resetting OBS Configurations

If OBS is acting glitchy, you can reset its settings without uninstalling the app:

```bash
# Move old settings to a backup folder
mv ~/.config/obs-studio ~/.config/obs-studio-backup

```

### B. Fixing "Virtual Camera" Permissions

If OBS cannot start the Virtual Camera, ensure your user has permission to use video devices:

```bash
sudo usermod -aG video $USER

```

*(You must log out and log back in for this to take effect.)*

### C. Uninstalling/Cleaning Up

If you want to remove these tools and clean up the system:

```bash
# Remove OBS and its repository
sudo apt remove --autoremove obs-studio
sudo add-apt-repository --remove ppa:obsproject/obs-studio

# Remove GNOME Screenshot
sudo apt remove --autoremove gnome-screenshot

# Clean up unused dependencies
sudo apt autoremove && sudo apt autoclean

```

---

## 🚀 Recommended Workflow

| Task | Recommended Tool |
| --- | --- |
| **Live Streaming** | **OBS Studio** |
| **Video Tutorials** | **OBS Studio** |
| **Quick Webcam Photo** | **GNOME Snapshot** |
| **Technical Screenshot** | **GNOME Screenshot** |

**Would you like me to add a section on how to configure "Global Hotkeys" so you can start recording or take screenshots with a single keypress?**