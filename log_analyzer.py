error_count = 0
warning_count = 0
critical_count = 0
alert_logs = []

with open("sample_app.log", "r") as f:
    for line in f:
        clean_line = line.strip()
        
        if "ERROR" in clean_line:
            error_count += 1
            alert_logs.append(clean_line)
        elif "WARNING" in clean_line:
            warning_count += 1
        elif "CRITICAL" in clean_line:
            critical_count += 1
            alert_logs.append(clean_line)

print("--- LOG ANALYSIS SUMMARY ---")
print(f"Errors found: {error_count}")
print(f"Warnings found: {warning_count}")
print(f"Critical issues found: {critical_count}")

with open("alert_report.txt", "w") as report:
    report.write("=== INCIDENT ALERT REPORT ===\n")
    report.write(f"Errors Found: {error_count}\n")
    report.write(f"Warnings Found: {warning_count}\n")
    report.write(f"Critical Issues Found: {critical_count}\n\n")
    
    report.write("--- DETAILED INCIDENT LOGS ---\n")
    for log in alert_logs:
        report.write(f"{log}\n")

print("\nAlert report updated with detailed incident logs: alert_report.txt")