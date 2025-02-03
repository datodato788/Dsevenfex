import scapy.all as sc
import socket
import os
import subprocess
import time
import json
import requests
from colorama import Fore, Style, init
from utils.helpers import install_dependencies, clear_console
from utils.ascii_art import print_separator ,print_navbar


init(autoreset=True)

class NetworkScanner:
    DEBUG = True  
    LOG_FILE = "network_scan_log.json"  

    def __init__(self):
        self.local_ip = self.get_local_ip()
        self.network_range = self.get_network_range()

    @staticmethod
    def get_local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception as e:
            print(f"{Fore.RED}Error retrieving local IP: {e}{Style.RESET_ALL}")
            return None

    def get_network_range(self):
        if self.local_ip:
            return ".".join(self.local_ip.split("." )[:-1]) + ".1/24"
        return None

    @staticmethod
    def ping_device(ip):
        try:
            start_time = time.time()
            result = subprocess.run(["ping", "-n", "1", "-w", "100", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            latency = round((time.time() - start_time) * 1000, 2)
            return result.returncode == 0, latency
        except Exception as e:
            print(f"{Fore.RED}Ping error ({ip}): {e}{Style.RESET_ALL}")
            return False, None

    def scan_network(self, port_count=40):
        if not self.network_range:
            print(f"{Fore.RED}Failed to determine network range.{Style.RESET_ALL}")
            return {}

        print(f"{Fore.CYAN}Scanning network: {self.network_range} (Pinging {port_count} IPs){Style.RESET_ALL}")

        devices = {}

        try:
            arp_request = sc.ARP(pdst=self.network_range)
            broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered_list = sc.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

            for answer in answered_list:
                devices[answer[1].psrc] = {"mac": answer[1].hwsrc, "latency": None}
                print(f"{Fore.GREEN}[+] Found device: {answer[1].psrc} - {answer[1].hwsrc}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}ARP scan error: {e}{Style.RESET_ALL}")

        base_ip = ".".join(self.network_range.split(".")[:-1])
        for i in range(1, port_count + 1):
            ip = f"{base_ip}.{i}"
            if ip not in devices:
                reachable, latency = self.ping_device(ip)
                if reachable:
                    devices[ip] = {"mac": "UNKNOWN", "latency": latency}
                    print(f"{Fore.YELLOW}[+] Device reachable: {ip} - Latency: {latency} ms{Style.RESET_ALL}")
        
        return devices

    @staticmethod
    def get_mac_vendor(mac):
        try:
            response = requests.get(f"https://api.macvendors.com/{mac}")
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"{Fore.RED}MAC Vendor API error: {e}{Style.RESET_ALL}")
        return "Unknown"

    def save_results(self, devices):
        with open(self.LOG_FILE, "w", encoding="utf-8") as file:
            json.dump(devices, file, indent=4, ensure_ascii=False)
        print(f"{Fore.GREEN}Results saved to: {self.LOG_FILE}{Style.RESET_ALL}")

    def print_results(self, devices):
        print( "-" * 60 + Style.RESET_ALL)
        print(f"{Fore.YELLOW}{'IP Address':<15}{'MAC Address':<20}{'Vendor':<20}{'Latency (ms)'}{Style.RESET_ALL}")
        print( "-" * 60 + Style.RESET_ALL)

        for ip, info in devices.items():
            vendor = self.get_mac_vendor(info["mac"]) if info["mac"] != "UNKNOWN" else "UNKNOWN"
            print(f"{Fore.GREEN}{ip:<15}{info['mac']:<20}{vendor:<20}{info['latency'] if info['latency'] else 'N/A'}{Style.RESET_ALL}")
            print( "-" * 60 + Style.RESET_ALL)


    def scan_network_and_display(self, port_count=50):
        devices = self.scan_network(port_count=port_count)
        clear_console()
        print_navbar(f"Main menu / Network Scanner / {Fore.RED}{port_count} ")
        self.save_results(devices)
        self.print_results(devices)

