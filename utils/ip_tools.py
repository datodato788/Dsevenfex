import requests
from colorama import Fore
from utils.helpers import save_to_file

ip_history = {}

def add_or_edit_ip(ip, note=None):
    ip_history[ip] = note or ip_history.get(ip, "")
    print(f"{Fore.GREEN}IP Address {Fore.CYAN}{ip} {Fore.GREEN}has been added/updated!")

def view_ip_history():
    if not ip_history:
        print(f"{Fore.RED}No saved IP addresses!")
        return

    print(f"{Fore.YELLOW}Saved IP Addresses:")
    for ip, note in ip_history.items():
        print(f"{Fore.CYAN}{ip} - {Fore.YELLOW}{note}")

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        print(f"{Fore.GREEN}IP Information for {ip}:")
        print(f"{Fore.CYAN}City: {data.get('city')}")
        print(f"{Fore.CYAN}Region: {data.get('region')}")
        print(f"{Fore.CYAN}Country: {data.get('country_name')}")
        print(f"{Fore.CYAN}Latitude/Longitude: {data.get('latitude')}, {data.get('longitude')}")
    except Exception as e:
        print(f"{Fore.RED}Error fetching IP info: {e}")
