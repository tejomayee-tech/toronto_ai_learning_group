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

