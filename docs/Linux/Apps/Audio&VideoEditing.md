# Linux Audio & Video Editing Tools

## Audio Editing

### Audacity

**Purpose:** Professional audio editing and recording software

**Features:**

* Multi-track audio recording and editing
* Noise reduction and effects
* Audio format conversion
* Export to various formats including MP3

**Installation:**

```bash
# Ubuntu/Debian
sudo apt install audacity

# Fedora
sudo dnf install audacity

# Arch Linux
sudo pacman -S audacity

```

**Use Cases:**

* MP3 editing and manipulation
* Audio cleanup and restoration
* Creating podcasts and voice recordings
* Audio mixing and mastering

---

## Video Editing

### Kdenlive

**Purpose:** Professional video editing software for Linux

**Features:**

* Non-linear video editing
* Multi-track timeline
* Color correction and grading
* Effects and transitions
* Export to various formats

**Installation:**

```bash
# Ubuntu/Debian
sudo apt install kdenlive

# Fedora
sudo dnf install kdenlive

# Arch Linux
sudo pacman -S kdenlive

```

**Use Cases:**

* Professional video production
* YouTube content creation
* Film editing
* Tutorial creation

### Shotcut

**Purpose:** Open-source video editor with a wide range of features

**Features:**

* Hardware-accelerated playback
* Support for many video and audio formats
* Filters and effects
* Color correction

**Installation:**

```bash
# Ubuntu/Debian
sudo apt install shotcut

# Fedora
sudo dnf install shotcut

# Arch Linux
sudo pacman -S shotcut

```

---

## Screen Recording & Broadcasting

### OBS Studio

**Purpose:** The industry standard for open-source screen recording and live streaming.

**Features:**

* **Scene Composition:** Mix multiple sources like webcams, window captures, and images into one layout.
* **Advanced Audio Mixer:** Per-source filters like noise gates and suppression.
* **Studio Mode:** Preview your scenes before pushing them "Live."
* **Broadcasting:** Native support for Twitch, YouTube, and Facebook Live.

**Installation:**

```bash
# Ubuntu/Debian (Official PPA for latest version)
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt update && sudo apt install obs-studio

# Fedora
sudo dnf install obs-studio

# Arch Linux
sudo pacman -S obs-studio

```

**Use Cases:**

* Live streaming games or webinars.
* Recording high-quality video tutorials with screen-sharing.
* Setting up a "Virtual Camera" for professional-looking Zoom or Teams meetings.

---

## Quick Video Editing Tools

### LosslessCut

**Purpose:** Simple, fast, and lossless video editing tool

**Features:**

* Lossless video editing
* Simple drag-and-drop interface
* Add or replace audio tracks
* Fast processing
* No quality loss

**Installation:**

```bash
# Ubuntu/Debian
flatpak install flathub no.mifi.losslesscut

```

**Use Cases:**

* Quick video trimming
* Adding audio to videos
* Simple video editing without quality loss
* Faster alternative to full-featured editors for basic tasks

**Comparison:**

* **LosslessCut vs Shotcut:** LosslessCut is simpler and faster for basic tasks, while Shotcut offers more advanced features and format support.

---

## Recommended Workflow

### For Simple Audio Tasks

1. Use **Audacity** for MP3 editing and audio manipulation.
2. Use **LosslessCut** for quick video editing with audio.

### For Recording & Streaming

1. Use **OBS Studio** to capture your screen, webcam, and microphone.
2. Use **Audacity** if you need to perform deep cleanup on the recorded audio later.

### For Professional Video Production

1. Use **OBS Studio** for raw footage capture.
2. Use **Kdenlive** for comprehensive video editing and transitions.
3. Use **Audacity** for audio editing and mixing.
4. Use **LosslessCut** for quick, lossless edits when needed.

### For Quick, Lossless Edits

1. Use **LosslessCut** for simple trimming and audio addition.
2. Avoid complex editors for basic tasks to save time.

[OBS Studio Linux Installation & Setup](https://www.youtube.com/watch?v=xuVNs78ju0g)

This video provides a step-by-step walkthrough for installing the official version of OBS Studio on Linux and configuring basic screen capture settings.