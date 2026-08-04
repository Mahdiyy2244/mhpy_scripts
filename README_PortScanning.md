# 🔍 Python Port Scanner

A lightweight, multi-threaded TCP port scanner written in Python. It scans a target IP across a given port range and reports which ports are open, along with a best-guess identification of the common service running on each.

## ✨ Features

- **Multi-threaded scanning** — spins up a thread per port for fast results
- **Service identification** — maps well-known ports (FTP, SSH, HTTP, MySQL, RDP, etc.) to their common service names
- **Simple CLI interface** — just enter a target IP and a port range
- **Clear, color-coded console output** with open ports and their services

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `socket`, `threading`, `datetime` (all part of the Python standard library — no external dependencies required)

## ▶️ How to run

```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Run the scanner
python port_scanner.py
```

You'll be prompted for:
- **Target IP** — e.g. `192.168.1.1`
- **Starting port** — e.g. `1`
- **Ending port** — e.g. `1024`

### Example output

```
🔍  Port Scanning 192.168.1.1 from 1 to 1024
--------------------------------------------------
✅ Port 22 is open  (SSH)
✅ Port 80 is open  (HTTP)
✅ Port 443 is open  (HTTPS)

✅  Open Ports:
   22 → SSH
   80 → HTTP
   443 → HTTPS
```

## ⚠️ Legal & Ethical Notice

This tool is intended **strictly for educational purposes and authorized security testing**. Only scan systems and networks that you own or have **explicit written permission** to test. Unauthorized port scanning may violate the law (e.g., the Computer Fraud and Abuse Act in the US, or equivalent laws elsewhere) and the terms of service of many networks and hosting providers.

## 🚀 Possible Improvements

- Add banner grabbing to identify exact service versions
- Add support for scanning multiple IPs / CIDR ranges
- Export results to CSV or JSON
- Add a progress bar for large port ranges
- Limit thread count with a thread pool for very large scans

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you found this useful, consider giving the repo a star!
