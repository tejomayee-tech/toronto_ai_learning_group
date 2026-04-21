# Linux Audio & Video Editing Tools

## Audio Editing

### Audacity

**Purpose:** Professional audio editing and recording software.

* **Features:** Multi-track recording, noise reduction, format conversion, and VST plugin support.
* **Installation:** * `sudo apt install audacity` (Debian/Ubuntu)
* `sudo dnf install audacity` (Fedora)
* `sudo pacman -S audacity` (Arch)



---

## Video Editing

### Kdenlive

**Purpose:** Professional-grade non-linear video editor.

* **Features:** Multi-track timeline editing, color correction, grading, and a massive library of effects/transitions.
* **Installation:** * `sudo apt install kdenlive` (Debian/Ubuntu)
* `sudo dnf install kdenlive` (Fedora)
* `sudo pacman -S kdenlive` (Arch)



### Shotcut

**Purpose:** Feature-rich, open-source editor with broad format support.

* **Features:** Hardware-accelerated playback, intuitive filters, and native timeline editing (no import required).
* **Installation:** * `sudo apt install shotcut` (Debian/Ubuntu)
* `sudo dnf install shotcut` (Fedora)
* `sudo pacman -S shotcut` (Arch)



---

## Screen Recording & Broadcasting

### OBS Studio

**Purpose:** The industry standard for recording and live streaming.

* **Features:** Scene composition, advanced audio mixing, studio mode, and virtual camera support.
* **Installation:** * `sudo add-apt-repository ppa:obsproject/obs-studio && sudo apt update && sudo apt install obs-studio` (Ubuntu)
* `sudo dnf install obs-studio` (Fedora)



---

## Quick & Utility Tools

### LosslessCut

**Purpose:** Ultra-fast, "lossless" trimming and cutting.

* **Features:** Cuts video without re-encoding (no quality loss), extremely fast, supports adding/replacing audio tracks.
* **Installation:** `flatpak install flathub no.mifi.losslesscut`

### Media Players

* **VLC Media Player:** The "Swiss Army Knife" for playing any obscure file format.
* **Lollypop:** A modern, sleek music player for organizing local audio libraries.

---

## Recommended Workflows

### 1. Recording & Content Creation

* **Capture:** Use **OBS Studio** to record your screen and microphone.
* **Audio Cleanup:** Use **Audacity** to remove background hiss or normalize volume levels.
* **Editing:** Import footage into **Kdenlive** for the final cut and transitions.

### 2. The "Quick Edit" (Social Media/Trimming)

* **Trim:** Use **LosslessCut** to instantly shave off the beginning or end of a clip.
* **Audio Swap:** Use **LosslessCut** to attach a new music track to a video without waiting for a long render.

### 3. Professional Production

* **Assets:** Prepare audio in **Audacity**.
* **Assembly:** Use **Kdenlive** or **Shotcut** for complex layering and color grading.
* **Preview:** Use **VLC** to verify the final exported file.
