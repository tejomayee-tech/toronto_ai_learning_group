# Complete Dual-Boot Guide: Windows 11 & Linux (Zorin/Ubuntu)

**Target Device:** Minisforum X1 Pro (AMD Ryzen AI 9 HX 370)

## Phase 1: Prepare the Windows 11 Installer

1. **Download:** Get the Windows 11 ISO from Microsoft’s official site.
2. **Rufus Settings:** Insert a USB drive and open **Rufus**.
* **Device:** Select your USB.
* **Boot selection:** Select the Windows 11 ISO.
* **Partition scheme:** Must be **GPT**.
* **Target system:** Must be **UEFI (non CSM)**.


3. **Windows User Experience (Rufus Pop-up):** I recommend checking "Remove requirement for 4GB+ RAM, Secure Boot and TPM 2.0" and "Disable BitLocker automatic device encryption" to prevent access issues later.

---

## Phase 2: Install Windows 11 (The Partitioning Secret)

1. **Boot from USB:** Tap `F7` or `F12` on your Minisforum to select the Rufus USB.
2. **Custom Install:** When asked "Which type of installation do you want?", select **"Custom: Install Windows only (advanced)"**.
3. **Manual Partitioning:**
* You will see the 1TB of "Unallocated Space."
* Select it and click **New**.
* **Size:** Enter **204800 MB** (this equals exactly 200 GB).
* Windows will create a few small "System" and "MSR" partitions automatically—this is normal.
* Select the **200 GB Primary Partition** you just made and click **Next** to install Windows.



---

## Phase 3: Create the Shared Data Drive in Windows

Once Windows is installed and you are at the desktop:

1. **Right-click Start** and select **Disk Management**.
2. Find the large block of **Unallocated Space** (~731 GB remaining).
3. Right-click it and select **New Simple Volume**.
* **Size:** Enter **542720 MB** (this equals 530 GB).
* **Format:** NTFS.
* **Label:** `Common_Data`.


4. **Crucial Step:** Leave the remaining space (~201 GB) as **Unallocated**. Do not touch it!
5. **Disable Fast Startup:** * Go to *Control Panel > Power Options > Choose what the power buttons do*.
* Click "Change settings that are currently unavailable."
* **Uncheck "Turn on fast startup"**. (If you skip this, Linux cannot write to your 530 GB Data drive).



---

## Phase 4: BIOS Tweaks for Linux

Restart and tap `Del` or `F2`:

* **Disable Secure Boot:** Found under the **Security** tab.
* **VRAM:** Under **Advanced > GFX Configuration**, set "UMA Frame Buffer Size" to **4GB or 8GB**.


## 1. Hardware Compatibility & BIOS Setup

The Minisforum X1 Pro is a "bleeding-edge" machine. To ensure Linux (Zorin, Ubuntu, etc.) runs correctly:

* **Kernel Requirement:** Use a modern kernel (6.10+) for full support of the Ryzen AI 9 and Radeon 890M. (Zorin OS 17+ or Ubuntu 24.04/24.10 are recommended).
* **BIOS Settings:**
* Tap `Del` or `F2` at startup.
* **Disable Secure Boot:** Found under the **Security** tab.
* **VRAM Allocation:** Under **Advanced > GFX Configuration**, set "UMA Frame Buffer Size" to **4GB or 8GB** for better GPU performance.
* **Boot Priority:** Ensure the "UEFI NVME Drive BBS Priorities" lists your Linux bootloader (GRUB) at the top.



---

## 2. Partitioning for Three-Way Success

To have Windows, Linux, and a Shared Data drive on a 1TB disk (approx. 931 GB usable), use this layout:

### Step A: Prepare in Windows (Disk Management)

Before installing Linux, open **Disk Management** in Windows and create this structure:

| Partition | Size | Format | Purpose |
| --- | --- | --- | --- |
| **Windows 11** | 200 GB | NTFS | OS & Windows Apps |
| **Common Data** | ~531 GB | **NTFS** | Shared files (Accessible by both OS) |
| **Linux Space** | **200 GB** | **Unallocated** | Leave this raw/empty |

> [!IMPORTANT]
> **Disable Fast Startup:** In Windows, go to *Control Panel > Power Options > Choose what the power buttons do* and **Uncheck "Turn on fast startup"**. If you don't do this, Windows "locks" the shared drive, making it read-only in Linux.

---

## 3. Installing Zorin OS (or Ubuntu)

1. Boot from your Linux USB.
2. At the **Installation Type** screen, choose **"Something Else"**.
3. Select the **200 GB Free Space**.
4. Click **+** to create a new partition:
* **Size:** Use all available space (~200,000 MB).
* **Use as:** Ext4 journaling file system.
* **Mount point:** `/` (the root).


5. Install and restart.

---

## 4. Auto-Mounting the Shared Data Drive

Linux will see your 531 GB partition, but you must tell it to "attach" automatically at every boot:

1. Open the **Disks** application in Linux.
2. Select the **NTFS Common Data partition**.
3. Click the **Gears icon** > **Edit Mount Options**.
4. Turn **OFF** "User Session Defaults".
5. Ensure **"Mount at system startup"** is checked.
6. Set **Display Name** to `Common_Data`.
7. Click OK. Now this drive behaves like a local hard drive in Linux.

---

## 5. Replacing one Linux with another (Zorin to Ubuntu)

If you decide to switch Linux distributions later, you can do so without losing Windows or your Data:

1. Boot from the **Ubuntu USB**.
2. Choose **"Something Else"** at the installation screen.
3. Locate your **200 GB Ext4 partition** (where Zorin lives).
4. Select it, click **Change**, and:
* Set Use as to **Ext4**.
* Check the **Format partition** box.
* Set Mount point to `/`.


5. **Do NOT touch** the NTFS partitions (Windows or Common Data).
6. Finish the install. Ubuntu will overwrite the Zorin boot entry but leave Windows and your Data untouched.

---

## 6. Summary Table: Why This Works

* **Windows 11:** Stays safe on its own 200GB slice.
* **Shared Data:** Uses **NTFS** because Windows cannot read Linux (Ext4) files, but Linux reads Windows files easily.
* **Linux:** Stays contained in its 200GB slice.

**Would you like me to show you how to link your Linux "Documents" folder directly to a folder on the Shared Data drive so your files stay synced?**
