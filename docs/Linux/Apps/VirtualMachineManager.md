
https://virt-manager.org/

https://www.virtualbox.org/wiki/Linux_Downloads


That’s great to hear! Moving the file to `/var/lib/libvirt/images/` is the most stable approach because it places the ISO in a directory that **libvirt** is specifically designed to manage.


# virt-manager

## Step 1: Move the ISO to the System Storage

Since `/var/lib/libvirt/images/` is a protected system directory, you must use `sudo` to move your file there.

1. Open your **Terminal**.
2. Run the following command (replace `os.iso` with your actual filename):
```bash
sudo mv /home/user1/download/os.iso /var/lib/libvirt/images/

```


3. **Verify the move** and ensure the permissions are readable by the system:
```bash
sudo ls -lh /var/lib/libvirt/images/

```



---

## Step 2: Create a New Virtual Machine

1. Open **Virt-Manager** (Virtual Machine Manager).
2. Click the **"Create a new virtual machine"** icon (the computer monitor with a sparkle) in the top-left corner.
3. Choose **"Local install media (ISO image or CDROM)"** and click **Forward**.

---

## Step 3: Select the ISO from the System Pool

This is the part where most people get stuck. Since you moved the file manually, you need to tell Virt-Manager to find it.

1. Click **Browse...**
2. On the left-hand side, click on the **default** storage pool.
* *Note: This pool points directly to `/var/lib/libvirt/images/`.*


3. You should now see your `os.iso` listed in the main window. Select it and click **Choose Volume**.
4. Virt-Manager will usually detect the OS (e.g., "Ubuntu 22.04" or "Windows 10"). If it doesn't, uncheck "Automatically detect" and type the name of the OS to find a match. Click **Forward**.

---

## Step 4: Configure Hardware

1. **Memory and CPU:** Assign your RAM (e.g., 4096 MiB for 4GB) and the number of CPU cores. Click **Forward**.
2. **Storage:** Choose the disk size for your VM's hard drive (e.g., 25 GiB). This creates a `.qcow2` file in that same `/var/lib/libvirt/images/` folder. Click **Forward**.

---

## Step 5: Finalize and Install

1. Give your VM a name (no spaces).
2. Click **Finish**.
3. A new window will open showing the VM console. It will "boot" from the ISO just like a physical computer starting from a USB drive.
4. Follow the on-screen instructions of your OS (Ubuntu, Windows, etc.) to complete the installation.

---

### Pro Tip: The "Refresh" Button

If you move a file into `/var/lib/libvirt/images/` while Virt-Manager is already open, it might not show up immediately. In the **Browse** window, click the **Refresh icon** (circular arrow) next to the "default" pool to force it to scan for new files.

**Would you like me to show you how to enable "Shared Folders" so you can easily move files between your Ubuntu host and your new Virtual Machine?**