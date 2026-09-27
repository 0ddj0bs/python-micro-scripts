import csv
import os
import time
from datetime import datetime
import requests

 
SITES_TO_CHECK = [
    "https://www.google.com",
    "https://www.github.com",
    "https://httpbin.org/status/404",
    "https://invalid-url-that-doesnt-exist.org",
]
LOG_FILE = "uptime_log.csv"


def init_csv():
    """Create the CSV log file with headers if it doesn't exist yet."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "URL", "Status", "Latency (s)"])


def log_result(timestamp, url, status, latency):
    """Append a single site check result to the CSV file."""
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, url, status, latency])


def check_site(url):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        latency = round(time.time() - start_time, 2)
        status_code = response.status_code

        if 200 <= status_code < 300:
            status_str = f"ONLINE ({status_code})"
            print(f"[{timestamp}] [ONLINE]  {url} | {latency}s")
        else:
            status_str = f"WARNING ({status_code})"
            print(f"[{timestamp}] [WARNING] {url} | {latency}s")

        log_result(timestamp, url, status_str, latency)

    except requests.exceptions.RequestException:
        status_str = "OFFLINE"
        print(f"[{timestamp}] [OFFLINE] {url} | Unable to connect!")
        log_result(timestamp, url, status_str, "N/A")


if __name__ == "__main__":
    init_csv()
    print(f"--- Running Website Uptime Check (Logging to {LOG_FILE}) ---")
    for site in SITES_TO_CHECK:
        check_site(site)