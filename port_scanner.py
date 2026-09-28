import socket

TARGET = "127.0.0.1"   
PORTS_TO_SCAN = [21, 22, 80, 135, 443, 445, 3389]


def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
         
        try:
            service_name = socket.getservbyport(port, "tcp")
        except OSError:
            service_name = "Unknown Service"

        print(f"[OPEN]   Port {port:<5} | Service: {service_name}")
    else:
        print(f"[CLOSED] Port {port:<5}")

    s.close()


if __name__ == "__main__":
    print(f"--- Starting Port Scan on {TARGET} ---")
    for port in PORTS_TO_SCAN:
        scan_port(TARGET, port)
    print("--- Scan Complete ---")