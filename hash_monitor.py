import hashlib
import time

TARGET_FILE = "secret.txt"


def calculate_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        content = f.read()
        hasher.update(content)
    return hasher.hexdigest()  


baseline_hash = calculate_hash(TARGET_FILE)
print(f"--- Baseline Established ---")
print(f"File: {TARGET_FILE}")
print(f"SHA-256: {baseline_hash}\n")
print("Monitoring active... (Press Ctrl+C to stop)")

while True:
    time.sleep(5)
    current_hash = calculate_hash(TARGET_FILE)

    if current_hash == baseline_hash:
        print("[OK] File intact.")
    else:
        print("\n[ALERT] File modified or tampered with!")
        print(f"New Hash: {current_hash}")
        break