import time
import json
import random
from utils import calculate_deviation

# ----------------------------------------
# Load baseline fingerprint
# ----------------------------------------
with open("data.json", "r") as f:
    baseline = json.load(f)["baseline"]

# ----------------------------------------
# Function: simulate live network snapshot
# ----------------------------------------
def get_live_snapshot():
    apps = ["Chrome", "YouTube", "Discord", "Instagram", "VSCode", "Spotify"]
    
    # randomly choose active apps
    active_apps = random.sample(apps, k=random.randint(1, 4))

    snapshot = {
        "apps": active_apps,
        "bandwidth": random.randint(10, 350),      # KB/s
        "connections": random.randint(2, 15),      # active processes
    }
    return snapshot


# ----------------------------------------
# Function: log results for visualization
# ----------------------------------------
def log_data(snapshot, deviation, alert):
    try:
        with open("monitor_log.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append({
        "timestamp": time.strftime("%H:%M:%S"),
        "apps": snapshot["apps"],
        "bandwidth": snapshot["bandwidth"],
        "connections": snapshot["connections"],
        "deviation": deviation,
        "alert": alert
    })

    with open("monitor_log.json", "w") as f:
        json.dump(logs, f, indent=4)


# ----------------------------------------
# Main monitoring loop
# ----------------------------------------
def start_monitoring():
    print("\n=== GhostNet Mirror – Real-Time Monitoring ===\n")

    while True:
        snapshot = get_live_snapshot()

        deviation = calculate_deviation(baseline, snapshot)

        alert = None

        if deviation > 70:
            alert = "⚠ HIGH anomaly — possible hijack!"
            print(f"\n{alert}")
        elif deviation > 40:
            alert = "⚠ Moderate deviation — unusual activity."
            print(f"\n{alert}")

        print(f"\nLive Snapshot @ {time.strftime('%H:%M:%S')}")
        print(f"Apps: {snapshot['apps']}")
        print(f"Bandwidth: {snapshot['bandwidth']} KB/s")
        print(f"Connections: {snapshot['connections']}")
        print(f"Deviation Score: {deviation}%")

        # log data
        log_data(snapshot, deviation, alert)

        time.sleep(3)   # run every 3 seconds


# ----------------------------------------
# Run program
# ----------------------------------------
if __name__ == "__main__":
    start_monitoring()
