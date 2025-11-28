import time
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def load_logs():
    try:
        with open("monitor_log.json", "r") as f:
            return json.load(f)
    except:
        return []

def dashboard():
    console.clear()
    console.rule("[bold cyan]GhostNet Mirror — Live Dashboard[/bold cyan]")

    while True:
        logs = load_logs()

        if not logs:
            console.print("[yellow]Waiting for data...[/yellow]")
            time.sleep(2)
            continue

        last = logs[-1]

        # Table for live snapshot
        table = Table(title="Current Snapshot", show_header=True, header_style="bold magenta")
        table.add_column("Field")
        table.add_column("Value")

        table.add_row("Timestamp", last["timestamp"])
        table.add_row("Apps", ", ".join(last["apps"]))
        table.add_row("Bandwidth", str(last["bandwidth"]) + " KB/s")
        table.add_row("Connections", str(last["connections"]))
        table.add_row("Deviation", str(last["deviation"]) + "%")
        table.add_row("Alert", last["alert"] if last["alert"] else "None")

        console.clear()
        console.print(table)

        # Panel for Alerts
        if last["alert"]:
            console.print(Panel(last["alert"], style="bold red"))
        else:
            console.print(Panel("No alerts detected", style="green"))

        time.sleep(2)


if __name__ == "__main__":
    dashboard()
