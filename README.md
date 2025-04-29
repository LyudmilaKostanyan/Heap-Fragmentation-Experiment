# Heap Fragmentation Experiment

## Overview
This project simulates dynamic memory allocation and deallocation in an infinite loop to create and study heap fragmentation. It monitors real-time memory usage and generates a graph to visualize memory behavior over time on different operating systems like Linux and macOS.

The project is written in C++ and Python, and is designed to highlight how memory allocation patterns can influence heap memory usage.

---

## Problem Description
Heap fragmentation occurs when memory allocations and deallocations happen in such a way that free memory becomes split into small, non-contiguous blocks. This leads to inefficient use of memory and can prevent large memory requests from succeeding even if the total free memory is sufficient.

The goal of this project is to:
- Dynamically allocate and free random-sized memory blocks at runtime.
- Observe how memory usage changes over time depending on the operating system.
- Understand differences between Linux and macOS heap management behavior.
- Visualize memory usage through generated plots.

---

## Example Output

Here are examples of generated graphs:

**Linux**
![heap_plot_linux](https://github.com/user-attachments/assets/22ad7ff1-6603-457b-bc06-0842b197d9a3)

**macOS**
![heap_plot_macos](https://github.com/user-attachments/assets/4a3ee61c-1196-4e71-879c-38b5f0a455b2)

**Linux (Ubuntu):**
- Memory usage increases steadily over time, reflecting persistent heap growth due to fragmentation and system memory allocation behavior.

**macOS:**
- Memory usage remains almost flat with small jumps. macOS memory allocator aggressively reuses memory regions, reducing observable heap growth even with heavy allocations and deallocations.

Graphs are saved as `heap_plot.png` and show:

- X-axis: Elapsed time (seconds)
- Y-axis: Memory usage (MB)

Example visual difference:

| Linux Example | macOS Example |
|:--------------|:--------------|
| Memory increases gradually and irregularly | Memory remains low and mostly stable |

---

## Explanation of Key Topics

- **Heap Fragmentation**: Fragmentation occurs when free memory is divided into many small, non-contiguous blocks, leading to inefficient memory use.
- **Resident Set Size (RSS)**: We measure physical memory currently held in RAM (RSS) rather than total virtual memory.
- **`new` and `delete[]` Behavior**: In C++, `new` and `delete[]` are used for dynamic memory management. They internally rely on the OS allocator, which behaves differently across platforms.
- **Monitoring with `psutil`**: Instead of relying on platform-specific tools like `top`, we use the Python `psutil` library for cross-platform, reliable memory tracking.

---

## How to Compile and Run

### 1. Clone the Repository

```bash
git clone https://github.com/username/Heap-Fragmentation-Simulation.git
cd Heap-Fragmentation-Simulation
```

---

### 2. Build the Project
Use CMake to configure and build:

```bash
cmake -S . -B build
cmake --build build
```
Make sure CMake, a C++ compiler (e.g., g++, clang++), and Python 3 with `psutil` and `matplotlib` installed.

If `psutil` and `matplotlib` are missing, install them:

```bash
pip3 install psutil matplotlib --break-system-packages  # On macOS
pip3 install psutil matplotlib                           # On Linux
```

---

### 3. Run the Program

You need to run two scripts in sequence:

#### a) Start Monitoring and Run Experiment

```bash
python3 monitor.py --duration 30 --executable ./build/main --log-file monitor_output.txt
```

- `--duration`: Duration in seconds to monitor the memory usage.
- `--executable`: Path to the compiled executable (`./build/main`).
- `--log-file`: Where to save the monitoring output.

Example:

```bash
python3 monitor.py --duration 30 --executable ./build/main --log-file monitor_output.txt
```

#### b) Plot the Memory Usage

```bash
python3 plot_log.py --log-file monitor_output.txt --output heap_plot.png
```

- `--log-file`: The file created by monitor.py.
- `--output`: Name of the output PNG file with the graph.

Example:

```bash
python3 plot_log.py --log-file monitor_output.txt --output heap_plot.png
```

---

## Important Notes
- **Fragmentation behavior varies across OSes**: macOS aggressively reuses memory, Linux allows more visible fragmentation.
- **The program runs indefinitely**: it must be manually terminated if you want to stop it earlier (Ctrl+C).
- **Graphs show memory usage but not fragmentation structure**: true fragmentation would require deeper heap analysis.
