import socket
import time
import sys
import subprocess
import colorama
import threading

from colorama import Fore, Back, Style

# Get the list of required modules
required_modules = []
with open("requirements.txt") as f:
    for line in f:
        required_modules.append(line.strip())

# Install the required modules
for module in required_modules:
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# Continue with the rest of the code
sys.stdout.flush()

# Print the banner
print(Fore.BLUE + Back.RED + Style.BRIGHT + """
██╗███╗   ███╗██╗██████╗ ██╗   ██╗██╗███╗   ███╗██████╗ ██████╗ ██╗
██║████╗ ████║██║██╔══██╗██║   ██║██║████╗ ████║██╔══██╗██╔══██╗██║
██║██╔████╔██║██║██║  ██║██║   ██║██║██╔████╔██║██║  ██║██║  ██║██║
██║██║╚██╔╝██║██║██║  ██║██║   ██║██║██║╚██╔╝██║██║  ██║██║  ██║██║
██║██║ ╚═╝ ██║██║██████╔╝╚██████╔╝██║██║ ╚═╝ ██║██████╔╝╚██████╔╝██║
╚═╝╚═╝     ╚═╝╚═╝╚═════╝  ╚═════╝ ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝
X3SC4 V.1 by hive-wic aka BX-7 "THE UNDERGROUND SOLDIER"

""" + Style.RESET_ALL)

# Prompt the user for the IP address or hostname to scan
ip_address = input("Enter the IP address or hostname to scan: ")

# Print the banner
# Prompt the user for the scan speed
# Only one option for scan speed is available
scan_types = ["tcp", "udp"]
scan_speed = "fast"

# Check the scan speed
# time_delay is set to 0.25 seconds by default
time_delay = 0.25

# Start the scan
print("Scanning...")
open_ports = []
closed_ports = []

# Use a multithreaded approach to scan multiple ports at the same time
threads = []
for port in range(1, 65536):
    # Use the `with` statement to ensure that the socket is closed
    # even if an exception is raised
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        start_time = time.time()
        try:
            s.connect((ip_address, port))
            open_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            closed_ports.append(port)
        end_time = time.time()
        time_taken = end_time - start_time
        if time_taken < time_delay:
            time.sleep(time_delay - time_taken)
        # Create a new thread to scan the port
        
def scan_port(ip_address, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

for port in range(1, 1024):
    if scan_port(ip_address, port):
        open_ports.append(port)
    else:
        closed_ports.append(port)

with open("results.txt", "w") as f:
    for port in open_ports:
        f.write("Open port: {}".format(port))
    for port in closed_ports:
        f.write("Closed port: {}".format(port))