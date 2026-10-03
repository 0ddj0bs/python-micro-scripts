import os
import json
import hashlib

def calculate_file_hash(filepath, chunk_size=4096):
    """Calculate SHA-256 hash of a file using chunk-based binary reading."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (PermissionError, FileNotFoundError) as e:
        print(f"[!] Error reading {filepath}: {e}")
        return None

def generate_baseline(directory, baseline_file="baseline.json"):
    """Scan directory and save initial SHA-256 hashes to a JSON file."""
    baseline = {}
    print(f"[*] Generating baseline for directory: {directory}")
    
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.abspath(os.path.join(root, file))
            file_hash = calculate_file_hash(full_path)
            if file_hash:
                baseline[full_path] = file_hash

    with open(baseline_file, "w") as f:
        json.dump(baseline, f, indent=4)
        
    print(f"[+] Baseline successfully saved with {len(baseline)} tracked files.")

def verify_integrity(baseline_file="baseline.json"):
    """Compare current directory state against the stored baseline."""
    if not os.path.exists(baseline_file):
        print("[!] Baseline file not found. Run baseline generation first.")
        return

    with open(baseline_file, "r") as f:
        baseline = json.load(f)

    print("[*] Starting file integrity scan...")
    modified_files = []
    missing_files = []

    for filepath, original_hash in baseline.items():
        if not os.path.exists(filepath):
            missing_files.append(filepath)
        else:
            current_hash = calculate_file_hash(filepath)
            if current_hash != original_hash:
                modified_files.append(filepath)

    print("\n--- Integrity Report ---")
    if not modified_files and not missing_files:
        print("[+] All files intact. No changes detected.")
    else:
        if modified_files:
            print("[!] MODIFIED FILES:")
            for f in modified_files:
                print(f"  - {f}")
        if missing_files:
            print("[!] MISSING/DELETED FILES:")
            for f in missing_files:
                print(f"  - {f}")

if __name__ == "__main__":
    target_dir = "./test_folder"
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        with open(f"{target_dir}/sample.txt", "w") as f:
            f.write("Integrity test content.")

    generate_baseline(target_dir)

    verify_integrity()