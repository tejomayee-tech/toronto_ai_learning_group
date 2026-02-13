# UBUNTU Linux

<img src="../images/Ubuntu.png" alt="ubuntu" width="500">


## Special Notes

### 1. Linux manages all application updates centrally

<img src="../images/CollectiveUpdates.png" alt="ubuntu-apps-collective-update" width="400" style="border-radius: 8px;">

### 2. Ubuntu studio comes pre-installed with tons of free multimedia software

<img src="../images/Ubuntu-Studio.png" alt="ubuntu-studio" width="500" style="border-radius: 8px;">

### 3. Linux powers most cloud infrastructure

<img src="../images/Ubuntu-on-cloud.png" alt="ubuntu-on-cloud" width="500" style="border-radius: 8px;">


Setting up Ubuntu alongside Windows 11 or 10 is the best way to get the power of Linux without losing your Windows environment. This setup is called "dual-booting." Here is your updated, step-by-step guide tailored for both versions of Windows!

## Your Guide to Dual-Booting Ubuntu with Windows 11/10

This guide covers everything from prepping your hard drive to choosing your OS when you flip the power switch.

---

### What You'll Need (Requirements):

1. **A Computer with Windows 11 or 10 Installed:** Ensure your system is up to date.
2. **Ubuntu ISO Image:** Go to [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop).
* **LTS (Long Term Support):** **Highly Recommended.** It’s the most stable and receives security updates for years.


3. **USB Stick (8GB or larger):** This will be your "installer." **Warning:** Everything on this USB will be erased.
4. **Rufus Software (Free):** To turn the ISO file into a bootable USB.
5. **Important:** **Backup Your Important Files!** While this process is standard, moving partitions always carries a small risk. Save your documents to an external drive or cloud storage first.

---

### Step 1: Prepare Windows 11/10

We need to make room for Ubuntu by shrinking the space Windows currently uses.

#### 1.1 Create Free Space (Shrink Partition)

1. **Open Disk Management:** Right-click the **Start button** and select **Disk Management**.
2. **Identify Your Main Drive:** Look for your **(C:)** drive.
3. **Shrink the Volume:** * Right-click the **(C:)** partition and select **Shrink Volume...**
* **How much space?** Enter the amount in MB. 1024MB = 1GB.
* **Recommendation:** Use at least **50,000 MB (50GB)** for a comfortable experience.
* Click **Shrink**.


4. **The Result:** You will now see a block of black space labeled **"Unallocated."** Leave it exactly like that.

#### 1.2 Disable Fast Startup

Windows "locks" the hard drive during a fast shutdown, which can prevent Ubuntu from installing correctly.

1. Open the **Start Menu**, search for **Control Panel**, and open it.
2. Go to **Hardware and Sound > Power Options**.
3. Click **Choose what the power buttons do**.
4. Click **Change settings that are currently unavailable** at the top.
5. Uncheck **Turn on fast startup (recommended)** and click **Save changes**.

---

### Step 2: Create the Bootable USB

1. Download **Rufus** from [rufus.ie](https://rufus.ie).
2. Plug in your USB stick and open Rufus.
3. **Device:** Select your USB stick.
4. **Boot selection:** Click **SELECT** and choose the Ubuntu `.iso` file you downloaded.
5. **Partition scheme:** * For almost all Windows 11 and modern Windows 10 PCs, select **GPT**.
* **Target system** should stay as **UEFI (non CSM)**.


6. Click **START**. If asked to write in "ISO Image mode," click **OK**.

---

### Step 3: Boot from USB

1. Keep the USB plugged in and **Restart** your PC.
2. As soon as the screen lights up, tap your **Boot Menu Key** repeatedly.
* *Common keys:* **F12** (Dell/Lenovo), **F9** (HP), **F8** (Asus), or **F11/F12** (Acer).


3. Select your USB stick (often labeled **UEFI: [USB Brand Name]**) and press **Enter**.

---

### Step 4: The Ubuntu Installation

1. **Try or Install:** Select **"Try or Install Ubuntu"** from the menu.
2. **Welcome:** Select your language and click **Install Ubuntu**.
3. **Updates:** Select **"Normal installation"** and check the box for **"Install third-party software for graphics and Wi-Fi."** This is vital for drivers!
4. **Installation Type:** This is the most important part.
* Look for the option: **"Install Ubuntu alongside Windows Boot Manager."**
* **Select this.** It will automatically detect the "Unallocated Space" you made in Step 1.


5. **User Setup:** Enter your name, a name for your PC, and a **strong password**. You will need this password every time you install software in Ubuntu!

---

### Step 5: Finishing Up

1. The installation will run. Once it's done, click **Restart Now**.
2. **Remove the USB:** When you see a message on a black screen, pull out the USB drive and press **Enter**.
3. **The GRUB Menu:** Now, every time you start your computer, a menu will appear:
* **Ubuntu:** Boots your new Linux system.
* **Windows Boot Manager:** Boots your Windows 11/10 system.

### Step 6: At Start, if you given Linux and Windows choice to enter


#### Option 1: The Windows Fix (No USB needed)

Windows has the power to tell the motherboard which "door" to open first.

1. Open the **Start Menu**, type `cmd`, right-click **Command Prompt**, and select **Run as Administrator**.
2. Type this exact command and press Enter:
`bcdedit /set {bootmgr} path \EFI\ubuntu\grubx64.efi`
3. **Restart your computer.** 4.  If it worked, the purple Ubuntu/Zorin menu will appear. Now you can select Ubuntu, log in, and perform **Step 1** (the `sudo` commands) from my previous message to make the fix permanent.

---

#### Option 2: The USB Fix (If Option 1 fails)

If Windows refuses to change the boot path, you have to "chroot" (teleport) into your installed Linux using the USB stick.

1. **Boot from your Ubuntu/Zorin USB** (Select "Try Ubuntu").
2. Open the **Terminal** and find your Linux partition:
`sudo fdisk -l`
*(Look for the 200GB partition labeled "Linux filesystem", e.g., `/dev/nvme0n1p4`)*.
3. **Mount your Linux system** so the USB can see it:
`sudo mount /dev/nvme0n1p4 /mnt` *(Replace with your actual partition name)*
4. **Mount the EFI partition** (the tiny ~100-500MB one):
`sudo mount /dev/nvme0n1p1 /mnt/boot/efi`
5. **Teleport into your installed system:**
```bash
for i in /dev /dev/pts /proc /sys /run; do sudo mount -B $i /mnt$i; done
sudo chroot /mnt

```


6. **Now you are "inside" your installed Linux!** You can now run the repair commands:
```bash
nano /etc/default/grub  # (Make the changes I mentioned before)
update-grub
exit

```


7. **Reboot** and unplug the USB.

---

#### Summary for your future "Clean Install"

When you do your final clean install:

1. Install **Windows 11** first.
2. Install **Ubuntu** second.
3. **Immediately after Ubuntu finishes**, if it boots straight to Windows, use **Option 1** above. It is the fastest way to "knock" on the motherboard's door and tell it to let Ubuntu handle the boot menu.

### Mount windows drive's to share data and AI models (avoid duplicate instance and save disk space)

To mount your **530 GB NTFS Common Data** drive so it appears automatically in Ubuntu with full read/write permissions, follow these steps.

#### 1. Identify the Drive's "ID" (UUID)

Every partition has a unique ID called a UUID. We need this so Ubuntu knows exactly which drive to mount.

1. Open the **Terminal** in Ubuntu (`Ctrl + Alt + T`).
2. Type this command:
`lsblk -f`
3. Look for the partition that is roughly **530G** and has the **FSTYPE** `ntfs`.
4. Copy the long code under the **UUID** column (it looks like `519CB82E5888AD0F`).

---

#### 2. Create a "Mount Point"

A mount point is just a folder where the data will appear.

1. In the terminal, create a folder named `Common_Data`:
`sudo mkdir -p /media/Common_Data`

---

#### 3. Configure the Auto-Mount (Edit fstab)

Now we tell Ubuntu to "plug in" that drive to that folder every time you turn on the PC.

1. Open the configuration file:
`sudo nano /etc/fstab`
2. Use the arrow keys to go to the very bottom of the file and add this **exact** line (replace `YOUR-UUID-HERE` with the code you copied in Step 1):
`UUID=YOUR-UUID-HERE  /media/Common_Data  ntfs-3g  defaults,uid=1000,gid=1000,umask=000,nofail  0  0`
> **What this does:** > * `uid=1000,gid=1000`: Makes **you** the owner of the files.
> * `umask=000`: Gives you full Read/Write/Execute permissions.
> * `nofail`: If the drive is missing for some reason, the PC will still boot instead of getting stuck.
> 
> 


3. Press `Ctrl + O` then `Enter` to save, and `Ctrl + X` to exit.

---

#### 4. Test it Immediately

Before you restart, tell Ubuntu to try mounting everything in the file we just edited:
`sudo mount -a`

Now, open your **File Manager**. You should see **Common_Data** in the left sidebar. If you can create a folder inside it, you have successfully set it up!

---

#### ⚠️ One Critical Troubleshooting Step

If you get an error saying **"The disk contains an unclean file system"** or **"Operation not permitted"**:
It means Windows is still "holding" the drive.

1. Reboot into **Windows**.
2. Go to **Control Panel > Power Options > Choose what the power buttons do**.
3. Uncheck **"Turn on fast startup"**.
4. **Shut down** completely (do not just Restart), then boot back into Ubuntu.

**Would you like me to show you how to bookmark this drive in your Ubuntu sidebar so it’s always one click away?**

**Success!** You’ve officially entered the world of dual-booting.



