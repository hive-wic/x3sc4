import socket
import threading

def scan_port(ip_address, port, protocol, speed):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        try:
            s.connect((ip_address, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False

def main():
    print("██╗███╗   ███╗██╗██████╗ ██╗   ██╗██╗███╗   ███╗██████╗ ██████╗ ██╗")
    print("██║████╗ ████║██║██╔══██╗██║   ██║██║████╗ ████║██╔══██╗██╔══██╗██║")
    print("██║██╔████╔██║██║██║  ██║██║   ██║██║██╔████╔██║██║  ██║██║  ██║██║")
    print("██║██║╚██╔╝██║██║██║  ██║██║   ██║██║██║╚██╔╝██║██║  ██║██║  ██║██║")
    print("██║██║ ╚═╝ ██║██║██████╔╝╚██████╔╝██║██║ ╚═╝ ██║██████╔╝╚██████╔╝██║")
    print("╚═╝╚═╝     ╚═╝╚═╝╚═════╝  ╚═════╝ ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝")
    print("X3SC4 V.1 by hive-wic aka BX-7 ")

    # Get the scanning speed
    speed = input("Enter the scanning speed (fast, medium, or slow): ")
    if speed == "fast":
        time_delay = 0.25
    elif speed == "medium":
        time_delay = 0.5
    elif speed == "slow":
        time_delay = 1
    else:
        print("Invalid speed.")
        return

    # Get the scanning protocol
    protocol = input("Enter the scanning protocol (tcp, udp, or both): ")
    if protocol == "tcp":
        protocol = "tcp"
    elif protocol == "udp":
        protocol = "udp"
    elif protocol == "both":
        protocol = "tcp,udp"
    else:
        print("Invalid protocol.")
        return

    ip_address = input("Enter the IP address or hostname to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    # Create a list of threads to scan the ports
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip_address, port, protocol, time_delay))
        threads.append(thread)

    # Start all of the threads
    for thread in threads:
        thread.start()

    # Wait for all of the threads to finish
    for thread in threads:
        thread.join()

    # Print the results
    for port in range(start_port, end_port + 1):
        if scan_port(ip_address, port, protocol, time_delay):
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))

if __name__ == "__main__":
    main()
