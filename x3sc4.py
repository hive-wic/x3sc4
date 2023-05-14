import socket
import time
import sys
import subprocess

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
scan_speed = input("Enter the scan speed (slow, medium, or fast): ")

# Check the scan speed
if scan_speed == "slow":
    time_delay = 1
elif scan_speed == "medium":
    time_delay = 0.5
else:
    time_delay = 0.25

# Start the scan
print("Scanning...")
open_ports = []
closed_ports = []
for port in range(1, 65536):
    # Use the `with` statement to ensure that the socket is closed
    # even if an exception is raised
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        start_time = time.time()
        try:
            s.connect((ip_address, port))
            open_ports.append(port)
        except socket.error:
            closed_ports.append(port)
        end_time = time.time()
        time_taken = end_time - start_time
        if time_taken < time_delay:
            time.sleep(time_delay - time_taken)

print("Scan complete")
print("Open ports: {}".format(open_ports))
print("Closed ports: {}".format(closed_ports))

# Add logging and error handling
import logging

logger = logging.getLogger(__name__)

def scan_ports(ip_address, ports):
    open_ports = []
    closed_ports = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        for port in ports:
            start_time = time.time()
            try:
                s.connect((ip_address, port))
                open_ports.append(port)
            except socket.error as e:
                closed_ports.append(port)
                logger.error("Error connecting to port {}: {}".format(port, e))
           
