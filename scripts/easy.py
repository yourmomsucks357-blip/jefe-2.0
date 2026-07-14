import socket
import threading
from queue import Queue

def scan_port(target_ip, port, timeout=0.5):
    """Scan a single port on a target IP."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                return f"Port {port} is OPEN"
    except:
        pass
    return None

def scan_subnet(target_ip, start_port=1, end_port=1024, threads=10):
    """Multi-threaded port scanner for a subnet."""
    open_ports = []
    q = Queue()
    for port in range(start_port, end_port + 1):
        q.put(port)

    def worker():
        while not q.empty():
            port = q.get()
            result = scan_port(target_ip, port)
            if result:
                open_ports.append(result)
            q.task_done()

    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.start()
        t.join()

    return open_ports

def network_scan(subnet="192.168.1.0/24"):
    """Scan a local subnet for active devices (ARP-based)."""
    import subprocess
    try:
        # Linux/macOS: Use `nmap` or `arp-scan`
        result = subprocess.run(
            ["nmap", "-sn", subnet],
            capture_output=True, text=True
        )
        return result.stdout
    except:
        return "Error: Install `nmap` or run as root."

if __name__ == "__main__":
    print("=== Port Scanner ===")
    target = input("Enter target IP (e.g., 192.168.1.1): ")
    print("\n".join(scan_subnet(target)))

    print("\n=== Network Scanner ===")
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    print(network_scan(subnet))
