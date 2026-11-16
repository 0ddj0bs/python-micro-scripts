import psutil
import os
from datetime import datetime
import psutil

SUSPICIOUS_KEYWORDS = [
    "keylog",
    "hook",
    "pynput",
    "keyboard",
    "logger",
    "capture"
]

def scan_processes():
    flagged = []
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            info = proc.info
            name = (info.get('name') or '').lower()
            cmdline = " ".join(info.get('cmdline') or []).lower()
            exe_path = (info.get('exe') or '').lower()

            # Check if any suspicious keyword appears in the process name or command line
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in name or keyword in cmdline:
                    flagged.append({
                        "pid": info['pid'],
                        "name": info['name'],
                        "exe": info['exe'],
                        "cmdline": cmdline,
                        "matched": keyword
                    })
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return flagged

def save_report(results, output_dir="scan_reports"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(output_dir, f"keylogger_scan_{timestamp}.txt")

    with open(report_path, "w", encoding="utf-8") as report:
        report.write(f"Keylogger Process Scan Report\n")
        report.write(f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write("=" * 50 + "\n\n")

        if not results:
            report.write("[OK] No suspicious processes detected.\n")
        else:
            report.write(f"[ALERT] {len(results)} suspicious process(es) flagged:\n\n")
            for item in results:
                report.write(f"PID     : {item['pid']}\n")
                report.write(f"Name    : {item['name']}\n")
                report.write(f"Path    : {item['exe']}\n")
                report.write(f"Cmdline : {item['cmdline']}\n")
                report.write(f"Matched : '{item['matched']}'\n")
                report.write("-" * 50 + "\n")

    return report_path

if __name__ == "__main__":
    print("Scanning active processes for suspicious activity...\n")
    results = scan_processes()

    if not results:
        print("[OK] No suspicious processes detected.")
    else:
        print(f"[ALERT] Found {len(results)} suspicious process(es):\n")
        for item in results:
            print(f"PID     : {item['pid']}")
            print(f"Name    : {item['name']}")
            print(f"Path    : {item['exe']}")
            print(f"Matched : '{item['matched']}'")
            print("-" * 40)

    saved_file = save_report(results)
    print(f"\nReport saved to: {saved_file}")