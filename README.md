GhostNet Mirror – Real-Time Network Persona Cloner

A smart cybersecurity project that builds a digital fingerprint of a user’s normal network behavior, then detects anomalies in real time.

It acts like a network guardian, warning when traffic no longer matches your usual pattern — a possible sign of hijacking, unauthorized access, or malware.

🚀 Features
✔ Baseline Persona Modeling

Learns the user’s normal:

App usage

Bandwidth consumption

Connection counts

✔ Anomaly Detection

Calculates a Deviation Score (0–100) to identify abnormal behavior.

✔ Real-Time Monitoring

Live snapshots updated every 2 seconds.

✔ Terminal Dashboard

Built using Rich for a modern UI-like terminal.

✔ Visualization Charts

Matplotlib graphs show:

Bandwidth over time

Deviation over time

App usage frequency

✔ Logging System

All snapshots stored in monitor_log.json for analysis.

🛠️ Tech Stack

Python 3

Rich (Terminal dashboard)

Matplotlib (Visualizations)

JSON for logging

VS Code (Development)

📁 Project Structure
GhostNet-Mirror/
│
├── monitor.py               # Real-time monitoring  
├── utils.py                 # Baseline + deviation logic  
├── terminal_dashboard.py    # Live UI  
├── visualize.py             # Graph visualization  
├── data.json                # Baseline persona  
├── monitor_log.json         # Generated logs  
├── README.md                # Documentation  

▶️ How to Run
1️⃣ Install dependencies
pip install rich matplotlib

2️⃣ Run the monitor
python monitor.py

3️⃣ Start the live terminal dashboard
python terminal_dashboard.py

4️⃣ Generate graphs
python visualize.py

📊 Example Outputs
✔ Live Dashboard

Shows apps, bandwidth, connections, deviation, and alerts.

✔ Graphs

Bandwidth timeline

Deviation spike chart

App frequency bar chart

⭐ Project Status

Functional & ready for demonstration.

📌 Future Enhancements

Real packet sniffing using Scapy/Wireshark API

ML-based anomaly classifier

GUI using Tkinter or Streamlit

Alert notifications

##Author##

Shivani Kawade • MScIT
