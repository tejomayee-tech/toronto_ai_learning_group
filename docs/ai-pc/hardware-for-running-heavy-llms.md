

### Hardware Configuration for Medium to Heavy LLMs

| Component | For 20B Parameter Models | For 80B Parameter Models |
| :--- | :--- | :--- |
| **GPU (NVIDIA)** | **Higher Cost:** NVIDIA RTX 4090 (24 GB VRAM)<br>**Budget:** NVIDIA RTX 3090 (24 GB VRAM) on the used market, or NVIDIA RTX 4080 (16 GB VRAM) for a new card. | **Higher Cost:** NVIDIA RTX 5090 (32 GB VRAM)<br>**Budget:** Dual NVIDIA RTX 3090s (24 GB VRAM each) or a professional card like the NVIDIA RTX A6000 (48 GB VRAM) if available. |
| **GPU (AMD)** | **Best Value:** AMD Radeon RX 7900 XTX (24 GB VRAM)<br>**Budget:** AMD Radeon RX 7900 XT (20 GB VRAM) | **Higher Cost:** AMD Instinct MI300X (192 GB VRAM)<br>**Budget:** Dual AMD Radeon RX 7900 XTX (24 GB VRAM each) |
| **GPU Interconnect** | N/A | High-speed links like **NVLink** (for NVIDIA) or a motherboard with **PCIe 4.0/5.0** for efficient communication between GPUs. |
| **CPU (Central Processing Unit)** | **Higher Cost:** AMD Ryzen 9 9950X3D or Intel Core i9-14900K.<br>**Budget:** AMD Ryzen 7 7800X3D or Intel Core i7-14700K. | **Higher Cost:** AMD Ryzen 9 9950X3D or Intel Core i9-14900K. The new AMD Ryzen AI 9 395+ processors also offer excellent performance-per-watt for AI tasks. |
| **System RAM** | **Higher Cost:** 64 GB+ of DDR5 RAM (e.g., 6000MHz+)<br>**Budget:** 32 GB of DDR5 RAM (e.g., 5600MHz) | **Higher Cost:** 128 GB+ of DDR5 ECC RAM<br>**Budget:** 64 GB of DDR5 RAM (e.g., 5600MHz) |
| **Storage (NVMe SSD)** | **Higher Cost:** A PCIe 5.0 NVMe SSD (e.g., Crucial T705) with sequential read/write speeds of up to 14,000 MB/s.<br>**Budget:** A high-end **PCIe 4.0 NVMe** SSD (e.g., Samsung 990 Pro or WD Black SN850X) with speeds of \~7,000 MB/s. | **Higher Cost:** Multiple high-capacity **PCIe 5.0 NVMe** SSDs in a RAID configuration for maximum throughput.<br>**Budget:** A high-capacity PCIe 4.0 NVMe SSD (e.g., Samsung 990 Pro 4TB) with a capacity of 4 TB+. |
| **Power Supply** | A high-wattage PSU (850W+) is recommended. | A high-wattage PSU (1000W+) is essential for multi-GPU setups. |
| **Cooling** | Robust cooling for the GPU and CPU is important to prevent performance throttling. | Robust cooling for the GPU and CPU is essential to handle the heat from a multi-GPU setup. |



| Interconnect | Description | Primary Use Case in AI/LLMs | Key Advantage | Supported GPUs |
| :--- | :--- | :--- | :--- | :--- |
| **NVLink** | A high-bandwidth, low-latency GPU-to-GPU interconnect developed by NVIDIA. It allows GPUs to directly share memory and data. | Training large models (e.g., LLMs) on multiple GPUs and high-performance computing. | Extremely fast direct GPU-to-GPU communication for memory pooling and data sharing. | NVIDIA GPUs (specifically data center and high-end workstation models like A100, H100, and some RTX cards) |
| **PCIe (PCI Express)** | A high-speed serial computer expansion bus standard. It is the primary way GPUs connect to a motherboard. | Connecting a single GPU to a CPU for both training and inference. Used for multi-GPU setups where the model is too large for one GPU but communication overhead is not a critical bottleneck. | Ubiquitous, industry standard, and widely compatible with all consumer and professional GPUs. | Both NVIDIA and AMD GPUs |
| **Infinity Fabric** | A cache-coherent interconnect protocol developed by AMD. It provides high-speed communication between different components, including multiple GPUs and CPU dies. | Multi-GPU setups for AI workloads on AMD hardware. It allows for efficient data and memory sharing between compatible GPUs. | High-speed, low-latency communication specifically designed for AMD's hardware ecosystem. | AMD GPUs (Radeon Instinct and some Radeon Pro series) |
| **OCuLink** | An external physical connector for a PCIe channel. It enables a high-speed, direct PCIe connection to an external device, such as an eGPU enclosure. | Connecting external GPUs to devices that are not standard desktop PCs (e.g., mini PCs, laptops) for high-performance AI inference or gaming. | Provides a pure, low-latency PCIe connection externally, often outperforming alternatives like Thunderbolt for raw bandwidth. | Both NVIDIA and AMD GPUs via eGPU docks |
