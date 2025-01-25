import requests
from colorama import Fore

def get_geolocation(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        
        if response.status_code == 200:
            data = response.json()
            print(f"{Fore.GREEN}Geolocation for {ip}:")
            print(f"{Fore.CYAN}City: {data.get('city')}")
            print(f"{Fore.CYAN}Region: {data.get('region')}")
            print(f"{Fore.CYAN}Country: {data.get('country')}")
            print(f"{Fore.CYAN}Coordinates: {data.get('loc')}")
            print(f"{Fore.CYAN}Organization: {data.get('org')}")
            print(f"{Fore.CYAN}Hostname: {data.get('hostname')}")
            print(f"{Fore.CYAN}IP Type: {data.get('ip')}")
            print(f"{Fore.CYAN}ASN: {data.get('asn')}")
            print(f"{Fore.CYAN}Country Code: {data.get('country')}")
            print(f"{Fore.CYAN}IP Version: {data.get('version')}")
            print(f"{Fore.CYAN}Region Code: {data.get('region_code')}")
            print(f"{Fore.CYAN}City Coordinates: {data.get('loc')}")
        else:
            print(f"{Fore.RED}Error: Failed to retrieve geolocation data. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"{Fore.RED}Error fetching geolocation: {e}")