import matplotlib.pyplot as plt
import argparse
import platform

def parse_mem_field(field):
    """Parse memory field from top output, e.g., 1.9M, 300K, 0B, or 123456 (assumed KB)."""
    try:
        if field.endswith("M"):
            return float(field[:-1])
        elif field.endswith("K"):
            return float(field[:-1]) / 1024
        elif field.endswith("G"):
            return float(field[:-1]) * 1024
        elif field.endswith("B"):
            return 0.0
        else:
            return int(field) / 1024  # assume KB
    except (ValueError, IndexError):
        return 0.0

def parse_top_output(log_file, process_name):
    memory_usage = []
    timestamps = []
    current_time = 0

    with open(log_file, "r") as f:
        for line in f:
            if process_name in line:
                parts = line.split()
                if len(parts) < 6:
                    continue
                mem_mb = parse_mem_field(parts[5])
                memory_usage.append(mem_mb)
                timestamps.append(current_time)
                current_time += 1
    return timestamps, memory_usage

def plot_memory_usage(timestamps, memory_usage, process_name, output_file):
    plt.figure(figsize=(10,6))
    plt.plot(timestamps, memory_usage, marker='o', linestyle='-')
    plt.title(f"Memory usage of {process_name} over time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Memory (MB)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Plot memory usage over time from top log.")
    parser.add_argument("--log-file", required=True, help="Log file created by monitor.py with top output")
    parser.add_argument("--process-name", required=True, help="Name of the process to track")
    parser.add_argument("--output", required=True, help="Output PNG file")
    args = parser.parse_args()

    timestamps, memory_usage = parse_top_output(args.log_file, args.process_name)

    if not timestamps:
        print(f"No data found for process {args.process_name}")
        return

    plot_memory_usage(timestamps, memory_usage, args.process_name, args.output)

if __name__ == "__main__":
    main()
