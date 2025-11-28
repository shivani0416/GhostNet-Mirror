import json
import matplotlib.pyplot as plt
from collections import Counter

def load_logs():
    with open("monitor_log.json", "r") as f:
        return json.load(f)


def format_timestamps(logs):
    """Convert HH:MM:SS → HH:MM to make graph readable"""
    return [log["timestamp"][:5] for log in logs]


def plot_bandwidth(logs):
    times = format_timestamps(logs)
    bandwidth = [log["bandwidth"] for log in logs]

    plt.figure(figsize=(10, 4))
    plt.plot(times, bandwidth)
    plt.title("Bandwidth Usage Over Time")
    plt.xlabel("Time (HH:MM)")
    plt.ylabel("KB/s")

    # show only every 4th label
    plt.xticks(times[::4], rotation=45)

    plt.tight_layout()
    plt.show()


def plot_deviation(logs):
    times = format_timestamps(logs)
    dev = [log["deviation"] for log in logs]

    plt.figure(figsize=(10, 4))
    plt.plot(times, dev)
    plt.title("Deviation Score Over Time")
    plt.ylabel("Deviation %")
    plt.xlabel("Time (HH:MM)")

    # show only every 4th label
    plt.xticks(times[::4], rotation=45)

    plt.tight_layout()
    plt.show()


def plot_app_frequency(logs):
    all_apps = []
    for log in logs:
        all_apps.extend(log["apps"])

    counts = Counter(all_apps)

    plt.figure(figsize=(8, 4))
    plt.bar(counts.keys(), counts.values())
    plt.title("App Usage Frequency")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def visualize_all():
    logs = load_logs()

    plot_bandwidth(logs)
    plot_deviation(logs)
    plot_app_frequency(logs)


if __name__ == "__main__":
    visualize_all()
