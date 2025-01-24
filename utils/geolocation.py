import requests
from colorama import Fore

def get_geolocation(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        print(f"{Fore.GREEN}Geolocation for {ip}:")
        print(f"{Fore.CYAN}City: {data.get('city')}")
        print(f"{Fore.CYAN}Region: {data.get('region')}")
        print(f"{Fore.CYAN}Country: {data.get('country_name')}")
        print(f"{Fore.CYAN}Coordinates: {data.get('latitude')}, {data.get('longitude')}")
    except Exception as e:
        print(f"{Fore.RED}Error fetching geolocation: {e}")
