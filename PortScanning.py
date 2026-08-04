import socket
import threading
from datetime import datetime

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = get_service_name(port)
            print(f"✅ Port {port} is open  ({service})")
            return port, service
        sock.close()
    except:
        pass
    return None

def get_service_name(port):
    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP-Alt"
    }
    return services.get(port, "Unknown")

def scan_ports(ip, start_port, end_port):
    print(f"\n🔍  Port Scanning {ip} From {start_port} than {end_port}")
    print("-" * 50)
    open_ports = []

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=lambda p=port: open_ports.append(scan_port(ip, p)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return [p for p in open_ports if p is not None]

if __name__ == "__main__":
    ip = input("🌐  Target IP (example 192.168.1.1): ")
    start = int(input("🔢 Starting Port "))
    end = int(input("🔢 End Port : "))

    open_ports = scan_ports(ip, start, end)

    if open_ports:
        print("\n✅  Open Ports:")
        for port, service in open_ports:
            print(f"   {port} → {service}")
    else:
        print("\n❌ No game ports found.")
