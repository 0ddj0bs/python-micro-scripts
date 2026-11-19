# Python Security & System Automation Suite (`python-micro-scripts`)

A modular collection of standalone Python CLI utilities built to automate endpoint security checks, file integrity verification, network diagnostics, log parsing, and system maintenance.

---

## 🛠️ Scripts Overview

### 🔐 Security & Cryptography
| Script | Description | Core Concepts & Libraries |
| :--- | :--- | :--- |
| `keylogger_detector.py` | Scans active system processes for suspicious keylogging behavior and generates an automated diagnostic report. | Process Inspection, OS/System Monitoring, Automated Reporting |
| `integrity_scanner.py` | Performs chunked SHA-256 baseline hashing to verify file integrity and detect unauthorized modifications. | `hashlib` (SHA-256), Chunked File I/O, Baseline Verification |
| `hash_monitor.py` | Monitors target files for hash mismatches and logs security state changes. | Cryptographic Hashing, File State Tracking |
| `secret_generator.py` | Generates cryptographically secure passwords/tokens with entropy evaluation. | `secrets`, Entropy Analysis, Secure Token Generation |

### 🌐 Network & Uptime Monitoring
| Script | Description | Core Concepts & Libraries |
| :--- | :--- | :--- |
| `port_scanner.py` | Scans target host ports and resolves active network service names. | `socket`, TCP/IP Networking, Service Resolution |
| `Website_Uptime_Response_Monitor.py` | Tracks website availability and measures HTTP response latency. | HTTP Requests, Latency Benchmarking |
| `uptime_monitor.py` | Logs continuous uptime checks to structured CSV records (`uptime_log.csv`). | `csv`, Time-Series Logging, Availability Tracking |
| `crypto_tracker.py` | Fetches and displays real-time cryptocurrency market prices via public APIs. | REST API Integration, JSON Parsing |

### ⚙️ Log Analysis & System Automation
| Script | Description | Core Concepts & Libraries |
| :--- | :--- | :--- |
| `log_analyzer.py` | Parses application logs (`sample_app.log`), counts critical keyword occurrences, and outputs `alert_report.txt`. | Regex/Pattern Matching, Frequency Analysis, Report Generation |
| `log_parser.py` | Filters raw server logs (`server.log`) to isolate error entries into `errors_only.log`. | Stream Filtering, Log Triage, File I/O |
| `system_cleaner.py` | Modular system cleanup utility that removes temporary clutter and calculates freed disk space. | `os` / `shutil`, Modular Functions, Disk Usage Metrics |
| `file_organizer.py` | Automatically categorizes and sorts directory files by file type/extension. | File System Automation, Directory Management |

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/0ddj0bs/python-micro-scripts.git](https://github.com/0ddj0bs/python-micro-scripts.git)
   cd python-micro-scripts
