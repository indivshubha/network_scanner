#trying to make a network port scanner to see which port are open on a given host

import socket


def input_host():
    host = input("Enter the host to scan (IP address or hostname): ")
    if not host:
        print("No host provided. Exiting.")
        exit(1)
    else:
        return host

def scan_host(host):
    print("Scanning...")
    open_ports = []
    for ports in range (1, 65536):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, ports))
            if result == 0:
                open_ports.append(ports)
                print(f"Port {ports} is open")
    if not open_ports:
                print("No open ports found.")
    print("Scan complete.")

def main():
    scan_host(input_host())


if __name__ == "__main__":
    main()

