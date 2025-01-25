import requests
from colorama import Fore, Style
from utils.helpers import save_to_file, clear_console
from utils.ascii_art import create_ascii_art, print_separator ,print_navbar
from utils.nmap_scanner import nmap_quick_scan, nmap_full_scan, print_scan_results
from utils.geolocation import get_geolocation


ip_history = {}



def add_or_edit_ip(ip, note=None):
    ip_history[ip] = note or ip_history.get(ip, "")
    while True:
        clear_console()
        print_navbar("Main menu / IP Scanning / Manage IP", ip)
        print(f"{Fore.BLUE}[1] {Fore.GREEN}Full Scan")
        print(f"{Fore.BLUE}[2] {Fore.GREEN}Quick Scan")
        print(f"{Fore.BLUE}[3] {Fore.GREEN}IP Address Lookup")
        print(f"{Fore.RED}[0] {Fore.RED}Go Back")
        print_separator()
        
        choice = input(f"{Style.BRIGHT}{Fore.YELLOW}Choose an option: {Fore.RESET}")
        
        if choice == "1":
            clear_console()
            print_navbar("... / Manage IP / Full Scan ", ip)
            nmap_full_scan(ip)           
            print_separator()
            input(f"{Fore.YELLOW}Press ENTER to proceed or return... {Fore.RESET}")
        elif choice == "2":
            clear_console()
            print_navbar("... / Manage IP / Quick Scan ", ip)
            nmap_quick_scan(ip)
            print_separator()
            input(f"{Fore.YELLOW}Press ENTER to proceed or return... {Fore.RESET}")
        elif choice == "3":
            clear_console()
            print_navbar("... / Manage IP / IP Address Lookup ", ip)
            get_geolocation(ip) 
            print_separator()
            input(f"{Fore.YELLOW}Press ENTER to proceed or return... {Fore.RESET}")
        elif choice == "0":
            return
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Fore.RESET}")

def view_ip_history():
    if not ip_history:
        print_navbar("View Saved IPs")
        print(f"{Fore.RED}No saved IP addresses!{Fore.RESET}")
        input(f"{Fore.YELLOW}Press ENTER to return to the menu... {Fore.RESET}")
        return
    
    while True:
        print_navbar("View Saved IPs")
        print(f"{Fore.YELLOW}Saved IP Addresses:{Fore.RESET}")
        for index, (ip, note) in enumerate(ip_history.items(), 1):
            print(f"{Fore.BLUE}[{index}] {Fore.CYAN}{ip} - {Fore.YELLOW}{note}{Fore.RESET}")
        print_separator()

        print(f"{Fore.CYAN}Options:")
        print(f"  {Fore.GREEN}edit [index] - Edit an IP address")
        print(f"  {Fore.RED}delete [index] - Delete an IP address")
        print(f"  {Fore.RED}[0] - Go back{Fore.RESET}")
        
        choice = input(f"{Fore.YELLOW}Choose an option: {Fore.RESET}").strip().lower()
        
        if choice == "0":
            break
        elif choice.startswith("edit"):
            try:
                index = int(choice.split()[1]) - 1
                ip, _ = list(ip_history.items())[index]
                new_note = input(f"{Fore.YELLOW}Enter a new note for {ip}: {Fore.RESET}")
                add_or_edit_ip(ip, note=new_note)
            except (IndexError, ValueError):
                print(f"{Fore.RED}Invalid index!{Fore.RESET}")
        elif choice.startswith("delete"):
            try:
                index = int(choice.split()[1]) - 1
                ip, _ = list(ip_history.items())[index]
                confirm = input(f"{Fore.RED}Are you sure you want to delete {ip}? (yes/no): {Fore.RESET}")
                if confirm.lower() == "yes":
                    del ip_history[ip]
                    print(f"{Fore.GREEN}IP {ip} deleted successfully!{Fore.RESET}")
                else:
                    print(f"{Fore.YELLOW}Deletion canceled.{Fore.RESET}")
            except (IndexError, ValueError):
                print(f"{Fore.RED}Invalid index!{Fore.RESET}")
        else:
            print(f"{Fore.RED}Invalid option! Please try again.{Fore.RESET}")

