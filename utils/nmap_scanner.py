import nmap
from colorama import Fore

def nmap_quick_scan(ip):
    nm = nmap.PortScanner()
    print(f"{Fore.YELLOW}Performing a quick scan on {Fore.CYAN}{ip}...")
    nm.scan(ip, '1-1024', '-v')
    print_scan_results(nm)

def nmap_full_scan(ip):
    nm = nmap.PortScanner()
    print(f"{Fore.YELLOW}Performing a full scan on {Fore.CYAN}{ip}...")
    nm.scan(ip, '1-65535', '-v')
    print_scan_results(nm)

def print_scan_results(nm):
    for host in nm.all_hosts():
        print(f"{Fore.GREEN}Host: {host} ({nm[host].hostname()})")
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                print(f"{Fore.CYAN}Port {port}: {state}")

