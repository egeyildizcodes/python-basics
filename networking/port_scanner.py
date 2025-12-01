import socket
import threading

open_ports = []

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        open_ports.append(port)
        s.close()
    except:
        pass

def scan(ip):
    threads = []
    print(f"Scanning {ip}...")
    
    for port in range(1, 65536):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Open ports:")
    print(open_ports)

if __name__ == "__main__":
    target = input("Target IP: ")
    scan(target)

