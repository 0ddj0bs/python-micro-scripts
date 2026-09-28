import os
import shutil

TEMP = os.environ.get("TEMP")
print(f"path: {TEMP}")

total_bytes = 0

for root, dirs, files in os.walk(TEMP):
    for filename in files:
        full_path = os.path.join(root, filename)

        try:
            total_bytes += os.path.getsize(full_path)
        except (PermissionError, FileNotFoundError):
            continue

print(f"Total Bytes: {total_bytes}")
total_mb = total_bytes / (1024 * 1024)
print(f"Total Size: {total_mb:.2f} MB")

 
deleted_count = 0
skipped_count = 0

for item in os.listdir(TEMP):
    item_path = os.path.join(TEMP, item)

    try:
        if os.path.isfile(item_path):
            os.remove(item_path)
            deleted_count += 1
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            deleted_count += 1
    except (PermissionError, FileNotFoundError):
        skipped_count += 1

print(f"Cleanup complete: {deleted_count} items removed | {skipped_count} items skipped")