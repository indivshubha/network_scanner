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
    top_ports = [
        1, 3, 7, 9, 13, 17, 19, 20, 21, 22, 23, 25, 26, 37, 53, 79, 80, 81, 82, 83,
        84, 85, 88, 89, 90, 99, 100, 106, 109, 110, 111, 113, 119, 125, 135, 139, 143,
        144, 146, 161, 163, 179, 199, 211, 212, 222, 254, 255, 256, 259, 264, 280,
        311, 318, 383, 389, 399, 427, 443, 444, 445, 458, 464, 481, 497, 500, 512,
        513, 514, 515, 520, 521, 540, 554, 587, 593, 631, 636, 646, 648, 666, 667,
        668, 683, 687, 691, 700, 705, 711, 714, 720, 722, 726, 749, 765, 777, 783,
        787, 800, 801, 808, 843, 873, 880, 888, 898, 900, 901, 902, 903, 911, 912,
        981, 987, 990, 992, 993, 995, 999, 1000, 1001, 1002, 1007, 1009, 1010, 1021,
        1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033,
    ]

    print("Scanning...")
    open_ports = []
    threads = []

    for port in top_ports:
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

