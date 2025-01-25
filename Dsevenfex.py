from utils.ascii_art import create_ascii_art, print_separator
from utils.ip_tools import add_or_edit_ip, view_ip_history ,print_navbar
from utils.helpers import install_dependencies, clear_console
from colorama import Fore, Style, init

init(autoreset=True)

def main_menu():
    while True:
        clear_console()
        print(create_ascii_art(f"{Fore.MAGENTA}Dsevenfex"))
        print_navbar("Main menu / ")
        print(f"  {Fore.BLUE}[1] {Fore.GREEN}IP Scanning")
        print(f"  {Fore.BLUE}[0] {Fore.RED}Exit")
        print_separator()

        choice = input(f"{Style.BRIGHT}{Fore.YELLOW}Choose an option: {Fore.RESET}")

        if choice == "1":
            while True:
                clear_console()
                print_navbar("Main menu / IP Scanning Menu ")
                print(f"  {Fore.BLUE}[1] {Fore.GREEN}Enter a New IP Address")
                print(f"  {Fore.BLUE}[2] {Fore.GREEN}View Saved IPs")
                print(f"  {Fore.BLUE}[0] {Fore.RED}Go Back to Main Menu")
                print_separator()
                
                save_ip = input(f"{Style.BRIGHT}{Fore.YELLOW}Choose an option: {Fore.RESET}")
                
                if save_ip == "1":
                    ip = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter IP Address: {Fore.RESET}")
                    note = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter Note (optional): {Fore.RESET}")
                    add_or_edit_ip(ip, note)
                    print(f"{Fore.GREEN}IP Address saved successfully!{Fore.RESET}")
                elif save_ip == "2":
                    view_ip_history()
                elif save_ip == "0":
                    break
                else:
                    print(f"{Fore.RED}Invalid choice. Please try again.{Fore.RESET}")
                    input(f"{Style.BRIGHT}{Fore.YELLOW}Press ENTER to continue...{Fore.RESET}")
        
        elif choice == "0":
            print(f"{Style.BRIGHT}{Fore.RED}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Fore.RESET}")
            input(f"{Style.BRIGHT}{Fore.YELLOW}Press ENTER to continue...{Fore.RESET}")

#my N1 python tool
if __name__ == "__main__":
    install_dependencies() 
    main_menu()
