import psutil
import time
from utils import save_baseline

def collect_baseline(duration=60):
    """
    Collects baseline network behavior for a given duration (default 60 seconds)
    and stores average usage per process.
    """

    print("[+] Collecting baseline network behavior...")
    process_data = {}

    start_time = time.time()

    while time.time() - start_time < duration:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                io = proc.io_counters()
                net = proc.connections()

                sent = io.write_bytes if io else 0
                received = io.read_bytes if io else 0
                conn_count = len(net)

                if proc.info['name'] not in process_data:
                    process_data[proc.info['name']] = {
                        'sent': [],
                        'received': [],
                        'connections': []
                    }

                process_data[proc.info['name']]['sent'].append(sent)
                process_data[proc.info['name']]['received'].append(received)
                process_data[proc.info['name']]['connections'].append(conn_count)

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        time.sleep(1)

    # Calculate averages
    final_profile = {}
    for process, values in process_data.items():
        final_profile[process] = {
            'avg_sent': sum(values['sent']) / len(values['sent']) if len(values['sent']) > 0 else 0,
            'avg_received': sum(values['received']) / len(values['received']) if len(values['received']) > 0 else 0,
            'avg_connections': sum(values['connections']) / len(values['connections']) if len(values['connections']) > 0 else 0
        }

    save_baseline(final_profile)
    print("[+] Baseline collection completed and saved to data.json!")


if __name__ == "__main__":
    collect_baseline(60)  # Collect for 60 seconds
