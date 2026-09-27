LOG_FILE = "server.log"
OUTPUT_FILE = "errors_only.log"

def extract_errors(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            if "ERROR" in line or "CRITICAL" in line:
                outfile.write(line)

if __name__ == "__main__":
    extract_errors(LOG_FILE, OUTPUT_FILE)
    print("Done! Check errors_only.log")