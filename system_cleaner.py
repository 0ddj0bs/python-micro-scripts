import os
import shutil

TEMP_DIR = os.environ.get("TEMP")


def calculate_dir_size(target_path):
    """Recursively walks a folder and calculates total size in bytes."""
    total_bytes = 0
    for root, dirs, files in os.walk(target_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            try:
                total_bytes += os.path.getsize(full_path)
            except (PermissionError, FileNotFoundError):
                continue
    return total_bytes


def clean_dir(target_path):
    """Deletes unlocked files and subdirectories inside target_path."""
    deleted_count = 0
    skipped_count = 0

    for item in os.listdir(target_path):
        item_path = os.path.join(target_path, item)
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                deleted_count += 1
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                deleted_count += 1
        except (PermissionError, FileNotFoundError):
            skipped_count += 1

    return deleted_count, skipped_count


if __name__ == "__main__":
    print(f"Target Directory: {TEMP_DIR}\n")

    initial_bytes = calculate_dir_size(TEMP_DIR)
    initial_mb = initial_bytes / (1024 * 1024)
    print(f"Initial Temp Size: {initial_mb:.2f} MB")

    print("Starting cleanup...")
    deleted, skipped = clean_dir(TEMP_DIR)
    print(f"Cleanup finished: {deleted} removed | {skipped} skipped (locked by Windows)")

    final_bytes = calculate_dir_size(TEMP_DIR)
    final_mb = final_bytes / (1024 * 1024)
    freed_mb = initial_mb - final_mb

    print(f"Remaining Temp Size: {final_mb:.2f} MB")
    print(f"Total Space Freed: {freed_mb:.2f} MB")