import psutil
import time

CPU_THRESHOLD = 80.0
MEM_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0
print("Strating System Recource Monitor (Press Ctrl+C to stop)...")
try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('C:\\').percent

        cpu_status = "[WARNING: HIGH CPU!]" if cpu > CPU_THRESHOLD else "[OK]"
        mem_status = "[WARNING: HIGH MEMORY!]" if mem > MEM_THRESHOLD else "[OK]"
        disk_status = "[WARNING: HIGH DISK!]" if disk > DISK_THRESHOLD else "[OK]"

        print("--- SYSTEM RESOURCE REPORT ---")
        print(f"CPU Utilization:    {cpu}% {cpu_status}")
        print(f"Memory Utilization: {mem}% {mem_status}")
        print(f"Disk Utilization:   {disk}% {disk_status}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nResource Monitoring Stopped")