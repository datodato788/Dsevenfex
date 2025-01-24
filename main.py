from utils.ascii_art import create_ascii_art, print_separator
from utils.ip_tools import add_or_edit_ip, view_ip_history, get_ip_info
from utils.nmap_scanner import nmap_tools_menu
from utils.helpers import clear_console, install_dependencies
from colorama import Fore, init

init(autoreset=True)

def main_menu():
    while True:
        clear_console()
        print(create_ascii_art("Dsevenfex"))
        print_separator()
        print(f"{Fore.CYAN}Main Menu:")
        print(f"{Fore.BLUE}[1] {Fore.GREEN}IP Scanning")
        print(f"{Fore.RED}[0] {Fore.RED}Exit")
        print_separator()

        choice = input(f"{Fore.YELLOW}Choose an option: {Fore.RESET}")

        if choice == "1":
            ip_selection_menu()
        elif choice == "0":
            print(f"{Fore.RED}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.YELLOW}Invalid choice. Please try again.")

if __name__ == "__main__":
    install_dependencies() 
    main_menu()
