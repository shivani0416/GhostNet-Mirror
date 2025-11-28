import json
import os

BASELINE_FILE = "data.json"

# ----------------------------------------------------
# Load and Save Baseline
# ----------------------------------------------------
def load_baseline():
    """Load the saved baseline persona from data.json"""
    if not os.path.exists(BASELINE_FILE):
        return {}
    with open(BASELINE_FILE, "r") as f:
        return json.load(f)

def save_baseline(data):
    """Save the baseline persona into data.json"""
    with open(BASELINE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_baseline(key, value):
    """Update a specific field in baseline file"""
    data = load_baseline()
    data[key] = value
    save_baseline(data)

# ----------------------------------------------------
# Deviation Calculation (Main Function Needed)
# ----------------------------------------------------
def calculate_deviation(baseline, new):
    """
    Compare the baseline fingerprint with a new snapshot
    and return a deviation score (0–100).
    """
    score = 0

    # 1. Compare app usage patterns
    baseline_apps = set(baseline["apps"])
    new_apps = set(new["apps"])
    diff_apps = len(baseline_apps.symmetric_difference(new_apps)) * 20

    # 2. Compare bandwidth difference (%)
    diff_bandwidth = abs(baseline["bandwidth"] - new["bandwidth"]) / baseline["bandwidth"] * 100

    # 3. Compare number of connections
    diff_connections = abs(baseline["connections"] - new["connections"]) * 10

    score = diff_apps + diff_bandwidth + diff_connections

    # Limit max score to 100
    return min(100, round(score))
