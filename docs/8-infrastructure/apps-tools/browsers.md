## Browser Download Links (Official Sites)

For Ubuntu, Debian, and Linux Mint users, always choose the **.deb (64-bit)** version where available.

| Browser | Official Download Page | Description |
| --- | --- | --- |
| **Firefox** | [Download Firefox](https://www.google.com/search?q=https://www.mozilla.org/firefox/linux/) | The default open-source browser for most Linux distros; highly privacy-focused. |
| **Google Chrome** | [Download Chrome](https://www.google.com/chrome/) | The industry standard; highly compatible with all websites and Google services. |
| **Microsoft Edge** | [Download Edge](https://www.microsoft.com/edge/download) | Includes built-in AI tools and a robust performance mode for low resource usage. |
| **Brave** | [Download Brave](https://brave.com/download/) | Automatically blocks ads and trackers for a faster, more private experience. |
| **Opera** | [Download Opera](https://www.opera.com/download) | Features a built-in VPN, ad-blocker, and integrated social sidebar. |
| **Vivaldi** | [Download Vivaldi](https://vivaldi.com/download/) | Built for power users with deep customization of every interface element. |

---

## How to Install .deb Files Graphically

If you prefer using your mouse over the terminal, follow these steps to install downloaded `.deb` packages using the **App Center** (Ubuntu 23.10+) or **Software Install**.

### Step 1: Download the Package

Visit one of the official sites above and download the Linux `.deb` package. It will typically be saved in your **Downloads** folder.

### Step 2: Open with App Center

1. Open your **Files** (Nautilus) manager and go to **Downloads**.
2. **Double-click** the `.deb` file.
3. If double-clicking doesn't work, **right-click** the file and select **Open With Other Application** → **App Center** (or **Software Install**).

### Step 3: Complete the Installation

1. The **App Center** window will appear with a description of the browser.
2. Click the green **Install** button.
3. **Authenticate:** When prompted, enter your system password to authorize the installation.
4. Wait for the process to finish. Once complete, the button will change to "Open" or "Uninstall."

### Step 4: Launch the Browser

Press the **Super** key (Windows key) and type the name of your browser (e.g., "Firefox" or "Chrome") to launch it.

---

## Important Note on Firefox (.deb vs. Snap)

On modern Ubuntu versions (22.04 and later), the default Firefox is a **Snap** package. Installing a `.deb` version of Firefox directly from Mozilla's APT repository provides better performance and faster updates integrated into the Firefox release process.

**Would you like the terminal commands to switch Firefox from a Snap to the official Mozilla .deb version for better performance?**

##  Installing sepecific version 

https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/


# apt install:
```bash
sudo apt install microsoft-edge-stable=92.0.902.15-1
```
# Wget Download the specific .deb file - last known issue free version

```bash
wget https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_139.0.3405.86-1_amd64.deb

# Install the downloaded package
sudo dpkg -i microsoft-edge-stable_139.0.3405.86-1_amd64.deb
```
# Issue version

 https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_140.0.3485.54-1_amd64.deb
Issue desc: crashes while saving downloaded files