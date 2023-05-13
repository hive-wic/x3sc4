import socket
import time
import sys
import subprocess

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
from pyfiglet import figlet_format

# Print the banner
ascii_banner = figlet_format("X3SCA V.1")
print(ascii_banner)

# Continue with the rest of the code
sys.stdout.flush()

# Prompt the user for the IP address or hostname to scan
ip_address = input("Enter the IP address or hostname to scan: ")

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
for port in range(1, 65536):
    start_time = time.time()
    try:
        socket.create_connection((ip_address, port))
        print("Port {} is open".format(port))
    except socket.error:
        pass
    end_time = time.time()
    time_taken = end_time - start_time
    if time_taken < time_delay:
        time.sleep(time_delay - time_taken)

print("Scan complete")
