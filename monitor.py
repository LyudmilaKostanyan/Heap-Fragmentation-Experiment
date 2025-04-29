import subprocess
import time
import argparse
import signal
import psutil

def main():
    parser = argparse.ArgumentParser(description="Run monitor with psutil and run heap fragmentation experiment.")
    parser.add_argument("--duration", type=int, required=True, help="Total duration to run (seconds)")
    parser.add_argument("--executable", type=str, default="./build/main", help="Path to the executable")
    parser.add_argument("--log-file", type=str, default="monitor_output.txt", help="File to save memory usage log")
    args = parser.parse_args()

    print(f"Starting the experiment: {args.executable}")
    experiment_proc = subprocess.Popen(
        [args.executable],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    process = psutil.Process(experiment_proc.pid)

    print(f"Monitoring process {experiment_proc.pid} for {args.duration} seconds...")
    with open(args.log_file, "w") as log:
        log.write("time_sec,memory_mb\n")
        for t in range(args.duration):
            if experiment_proc.poll() is not None:
                print("Experiment process ended early.")
                break
            try:
                rss = process.memory_info().rss / (1024 * 1024)
            except psutil.NoSuchProcess:
                rss = 0
            log.write(f"{t},{rss:.6f}\n")
            time.sleep(1)

    print("\nStopping process...")
    try:
        experiment_proc.send_signal(signal.SIGINT)
        time.sleep(1)
        experiment_proc.kill()
    except Exception:
        pass

    print("Done.")

if __name__ == "__main__":
    main()
