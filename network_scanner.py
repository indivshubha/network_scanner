#trying to make a network port scanner to see which port are open on a given host

import socket
import threading
from queue import Queue


def input_host():
    host = input("Enter the host to scan (IP address or hostname): ")
    if not host:
        print("No host provided. Exiting.")
        exit(1)
    else:
        return host

#Adding a multithreading feature to speed up the scanning process
def threaded_scan(host, port, results):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
        if s.connect_ex((host, port)) == 0:
            results.append(port)
            print(f"Port {port} is open")
    if not results:
        pass




def scan_host(host):
    print("Scanning...")
    open_ports = []
    threads = []

    for port in range(1, 65535):
        thread = threading.Thread(target=threaded_scan, args=(host, port, open_ports))
        threads.append(thread)
        thread.start()

        # Limit the number of concurrent threads
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

        for t in threads:
            t.join()
    print(f"Open ports on {host}: {open_ports}")


def main():
    scan_host(input_host())


if __name__ == "__main__":
    main()

