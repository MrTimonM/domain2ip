import socket
from urllib.parse import urlparse
import threading
from colorama import init, Fore

# Initialize colorama
init()

# Function to extract IP address from a given URL
def get_ip_address(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except (socket.gaierror, AttributeError):
        return None

# Function to process a website and get its IP address
def process_website(website):
    ip = get_ip_address(website.strip())
    if ip:
        print(Fore.GREEN + f"{website} IP is => {ip}")
        return ip
    else:
        print(Fore.RED + "Invalid Link")
        return None

# Prompt the user to input the path to the list.txt file
file_path = input("Enter text file name containing urls: ")

# Read the URLs from the file
website_list = []
try:
    with open(file_path, "r") as file:
        website_list = file.read().splitlines()
except FileNotFoundError:
    print("File not found.")

# Create threads for processing websites
threads = []
ip_addresses = []
for website in website_list:
    thread = threading.Thread(target=lambda: ip_addresses.append(process_website(website)))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Prompt the user for a filename to save the IP addresses
file_name = input("Enter the filename to save the IP addresses: ")

# Save IP addresses in a file
with open(file_name, "w") as file:
    for ip in ip_addresses:
        if ip:
            file.write(ip + "\n")

# Print completion message
print(Fore.RESET + "IP addresses retrieval completed.")
print(f"IP addresses saved in {file_name} file.")
