##  Comprehensive Swap Management Guide 

> **Note:** Though this document uses one Mini PC as base example, it can be used for any computer running Linux/Ubuntu.

Created using **K11 GMKtec Mini PC (Ryzen 9, Radeon 780 GPU, 64GB DDR5, 1TB SSD)** This guide is suggests optimizing & running the large **GPT-OSS:120B** model. 

While this Mini PC is able to run such large models with some delay, the goal is to establish a 40 GB memory buffer using swap while configuring the kernel to use it only when strictly necessary, preventing performance degradation and minimizing SSD wear.


### Part 1: Expand Swap Space to 40GBYou currently have an 8\text{GB} swap file. We will add a new 32\text{GB} swap file, resulting in 40\text{GB} total swap, which is a massive safety net.

| # | Action | Command | Explanation |
| --- | --- | --- | --- |
| **1.** | **Create 32\text{GB} File** | `sudo fallocate -l 32G /swapfile` | Creates the large file that will serve as the new swap area. |
| **2.** | **Set Permissions** | `sudo chmod 600 /swapfile` | Secures the file so only the system can access it. |
| **3.** | **Format as Swap** | `sudo mkswap /swapfile` | Marks the file as ready for use as swap space. |
| **4.** | **Activate Swap** | `sudo swapon /swapfile` | Immediately turns on the new 32\text{GB} swap area. |
| **5.** | **Verify Total Size** | `free -h` | Checks that the **Swap** row now shows approximately 40\text{GB}. |
| **6.** | **Make Persistent** | `echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab` |

### Part 2: Optimize Swappiness (The Crucial Fix)This is the most important step for the LLM. It stops the kernel from moving your model's 60\text{GB}+ data to the SSD, even when RAM appears free. We set the system to be **very reluctant to use swap** (`swappiness=10`).

| # | Action | Command | Explanation |
| --- | --- | --- | --- |
| **1.** | **Set Value (Temporary)** | `sudo sysctl vm.swappiness=10` | Applies the setting immediately to prioritize your 64\text{GB} RAM. |
| **2.** | **Make Permanent** | `sudo nano /etc/sysctl.conf` | Opens the configuration file to save the setting. |
| **3.** | **Add/Edit Line** | Add the line: `vm.swappiness = 10` | This ensures the setting survives reboot. |
| **4.** | **Apply Permanent Change** | `sudo sysctl -p` | Loads the new setting without requiring a reboot. |

### Part 3: Clear and Refresh SwapTo ensure the new settings are working perfectly, move any existing swapped data (like parts of your LLM) back into the faster RAM.

| # | Action | Command | Explanation |
| --- | --- | --- | --- |
| **1.** | **Disable All Swap** | `sudo swapoff -a` | Moves all data from your 40\text{GB} swap back into RAM. |
| **2.** | **Re-enable All Swap** | `sudo swapon -a` | Turns both 8\text{GB} and 32\text{GB} swap files back on, now using the **`swappiness=10`** rule. |

### Part 4: Monitor SSD HealthUse the **`smartctl`** utility to confirm that your tuning is successful by checking that the total writes to your SSD remain minimal.

| # | Action | Command | Explanation |
| --- | --- | --- | --- |
| **1.** | **Install Tool** | `sudo apt install smartmontools` | Installs the utility needed to read drive health data. |
| **2.** | **Identify Drive** | `lsblk` | Look for your SSD's name (e.g., `/dev/nvme0n1`). |
| **3.** | **Check Health** | `sudo smartctl -a /dev/nvme0n1` | Provides a full health report. Look for **Data Units Written** to track wear. |


## Linux Swap File Increase

To increase the swap memory on Zorin OS, the easiest method is to resize the existing **swap file**. Most modern Zorin installations (Zorin 15, 16, and 17) use a file located at `/swapfile` rather than a dedicated partition.

### Step 1: Check your current Swap

Open the **Terminal** (Ctrl+Alt+T) and run:

```bash
swapon --show

```

* If the **TYPE** is `file`, follow the steps below.
* If the **TYPE** is `partition`, you would typically need to use a tool like **GParted** to resize it, which is more complex. I recommend simply adding a swap file in addition to your partition if you need a quick fix.

---

### Step 2: Increase the Swap File

This process involves turning off the current swap, deleting it, and recreating a larger one.

1. **Turn off the swap:**
```bash
sudo swapoff /swapfile

```


2. **Create a new swap file:** Decide on the size. For example, to set it to **8GB**, use `8G`. (Common advice is to match your RAM or double it if you have less than 4GB).
```bash
sudo fallocate -l 8G /swapfile

```


*Note: If `fallocate` fails, you can use: `sudo dd if=/dev/zero of=/swapfile bs=1M count=8192*`
3. **Set the correct permissions:**
```bash
sudo chmod 600 /swapfile

```


4. **Format the file as swap:**
```bash
sudo mkswap /swapfile

```


5. **Enable the swap:**
```bash
sudo swapon /swapfile

```



---

### Step 3: Verify the Change

Check the new size to ensure it is active:

```bash
free -h

```

You should see the "Swap" row reflecting your new size (e.g., 8.0Gi).

### Important: Making it Permanent

Since Zorin usually already has an entry for `/swapfile` in its configuration, it should persist after a reboot. You can double-check this by running:

```bash
cat /etc/fstab

```

Look for a line that says: `/swapfile none swap sw 0 0`. If it's there, you are all set!


## Adjust the **"swappiness"** value

### 1. Check your current value

Open your terminal and run:

```bash
cat /proc/sys/vm/swappiness

```

* **Default (60):** The system starts swapping when RAM is about 40% full.
* **Higher (100):** Aggressively moves inactive data to swap.
* **Lower (1-10):** Only uses swap when RAM is nearly maxed out.

### 2. Change it Temporarily (Test it out)

To see if a lower value helps your LM Studio performance without rebooting, run:

```bash
sudo sysctl vm.swappiness=10

```

*I recommend **10** for your 64GB setup. This ensures the system uses almost all your physical RAM before touching the slower SSD swap.*

---

### 3. Change it Permanently

Once you've tested it and are happy, make it stick across reboots:

1. Open the system config file:
```bash
sudo nano /etc/sysctl.conf

```


2. Scroll to the very bottom and add this line:
```text
vm.swappiness=10

```


3. Press **Ctrl+O**, **Enter**, then **Ctrl+X** to save and exit.
4. Apply the change immediately:
```bash
sudo sysctl -p

```



---

### Understanding the Trade-off

| Swappiness Value | Behavior on your K11 | Best For... |
| --- | --- | --- |
| **vm.swappiness=100** | Uses swap almost immediately to keep RAM "empty." | Systems with very slow RAM or tiny RAM. |
| **vm.swappiness=60** | Balance; swaps out "cold" background apps (like a browser tab you haven't clicked in an hour). | General office/web use. |
| **vm.swappiness=10** | **(Recommended)** Keeps everything in RAM until it's ~90% full. | **High-RAM AI workloads (LM Studio).** |
| **vm.swappiness=1** | Avoids swap until the very last possible megabyte. | Extreme performance tuning; prevents any SSD wear. |

### Why "10" is the sweet spot for 64GB RAM

With a 30B model (17GB) and your OS overhead, you're using maybe 22-25GB of your 64GB. At a swappiness of 60, Linux might try to move some of that 17GB model into swap *just in case*, which can cause a slight stutter. At 10, it will keep the entire model in the fast DDR5 RAM of your K11, providing the fastest possible inference.
