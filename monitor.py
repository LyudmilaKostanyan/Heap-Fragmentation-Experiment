import subprocess
import time
import argparse
import os
import signal

def main():
    parser = argparse.ArgumentParser(description="Run top, wait 3s, then run heap fragmentation experiment.")
    parser.add_argument("--duration", type=int, required=True, help="Total duration to run (seconds)")
    parser.add_argument("--executable", type=str, default="./build/main", help="Path to the executable")
    args = parser.parse_args()

    print("Starting top to monitor memory...")
    top_proc = subprocess.Popen(["top"])

    print("Waiting 5 seconds before starting the experiment...")
    time.sleep(5)

    print(f"Starting the experiment: {args.executable}")
    experiment_proc = subprocess.Popen([args.executable])

    try:
        remaining_time = args.duration - 5
        if remaining_time > 0:
            time.sleep(remaining_time)
        else:
            print("Warning: Duration too short. Stopping immediately.")
    finally:
        print("\nStopping processes...")

        experiment_proc.send_signal(signal.SIGINT)
        top_proc.send_signal(signal.SIGINT)

        time.sleep(1)
        experiment_proc.kill()
        top_proc.kill()

        print("Done.")

if __name__ == "__main__":
    main()
