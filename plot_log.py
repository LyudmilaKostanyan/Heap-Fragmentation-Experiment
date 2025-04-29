import matplotlib.pyplot as plt
import csv
import argparse

def parse_monitor_output(log_file):
    memory_usage = []
    timestamps = []

    with open(log_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # Skip header
        for row in reader:
            if len(row) != 2:
                continue
            try:
                time_sec = int(row[0])
                mem_mb = float(row[1])
                timestamps.append(time_sec)
                memory_usage.append(mem_mb)
            except ValueError:
                continue
    return timestamps, memory_usage

def plot_memory_usage(timestamps, memory_usage, output_file):
    plt.figure(figsize=(10,6))
    plt.plot(timestamps, memory_usage, marker='o', linestyle='-')
    plt.title("Heap Memory Usage Over Time")
    plt.xlabel("Elapsed Time (seconds)")
    plt.ylabel("Memory Usage (MB)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Plot memory usage over time from monitor output.")
    parser.add_argument("--log-file", required=True, help="CSV log file created by monitor.py")
    parser.add_argument("--output", required=True, help="Output PNG file")
    args = parser.parse_args()

    timestamps, memory_usage = parse_monitor_output(args.log_file)

    if not timestamps:
        print(f"No data found in {args.log_file}")
        return

    plot_memory_usage(timestamps, memory_usage, args.output)

if __name__ == "__main__":
    main()
