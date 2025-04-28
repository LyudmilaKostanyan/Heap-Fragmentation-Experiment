import subprocess
import time
import argparse
import os
import signal
import platform

def is_windows():
    return platform.system().lower() == "windows"

def main():
    parser = argparse.ArgumentParser(description="Run monitor, wait 5s, then run heap fragmentation experiment.")
    parser.add_argument("--duration", type=int, required=True, help="Total duration to run (seconds)")
    parser.add_argument("--executable", type=str, default="./build/main", help="Path to the executable")
    args = parser.parse_args()

    if is_windows():
        print("Starting Get-Process to monitor memory (Windows)...")
        monitor_cmd = ["powershell", "-Command", "while ($true) { Get-Process | Out-String; Start-Sleep -Seconds 1 }"]
    else:
        print("Starting top to monitor memory (Linux/macOS)...")
        monitor_cmd = ["top", "-b", "-d", "1"]

    monitor_proc = subprocess.Popen(
        monitor_cmd,
        shell=is_windows()
    )

    print("Waiting 5 seconds before starting the experiment...")
    time.sleep(5)

    print(f"Starting the experiment: {args.executable}")
    experiment_proc = subprocess.Popen(
        [args.executable],
        shell=is_windows()
    )

    try:
        remaining_time = args.duration - 5
        if remaining_time > 0:
            time.sleep(remaining_time)
        else:
            print("Warning: Duration too short. Stopping immediately.")
    finally:
        print("\nStopping processes...")

        experiment_proc.send_signal(signal.SIGINT)
        monitor_proc.send_signal(signal.SIGINT)

        time.sleep(1)
        experiment_proc.kill()
        monitor_proc.kill()

        print("Done.")

if __name__ == "__main__":
    main()
