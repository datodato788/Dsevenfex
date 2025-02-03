from utils.ascii_art import create_ascii_art, print_separator ,print_navbar
from utils.ip_tools import add_or_edit_ip, view_ip_history 
from utils.helpers import install_dependencies, clear_console
from colorama import Fore, Style, init
from utils.image_scanner import image_scanner
from utils.network_scanner import NetworkScanner


init(autoreset=True)

def main_menu():
    while True:
        clear_console()
        print(create_ascii_art(f"{Fore.MAGENTA}Dsevenfex"))
        print_navbar("Main menu / ")
        print(f"  {Fore.BLUE}[1] {Fore.GREEN}IP Scanner")
        print(f"  {Fore.BLUE}[2] {Fore.GREEN}Image Scanner")
        print(f"  {Fore.BLUE}[3] {Fore.GREEN}Network Scanner")
        print(f"  {Fore.RED}[0] Exit")
        print_separator()

        choice = input(f"{Style.BRIGHT}{Fore.YELLOW}Choose an option: {Fore.RESET}")

        if choice == "1":
            while True:
                clear_console()
                print_navbar("Main menu / IP Scanning Menu ")
                print(f"  {Fore.BLUE}[1] {Fore.GREEN}Enter a New IP Address")
                print(f"  {Fore.BLUE}[2] {Fore.GREEN}View Saved IPs")
                print(f"  {Fore.RED}[0] Go Back to Main Menu")
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
        elif choice =="2":
              image_scanner()
        elif choice =="3":
             def Network():
                       clear_console()
                       print_navbar("Main menu / Network Scanner ")
                       print(f"  {Fore.BLUE}[1] {Fore.GREEN}Choice")
                       print(f"  {Fore.BLUE}[2] {Fore.GREEN}Default (255)")
                       print(f"  {Fore.RED}[0] Go Back to Main Menu")
                       print_separator()
                       choice1 = input(f"{Style.BRIGHT}{Fore.YELLOW}Choose an option: {Fore.RESET}")
                       if choice1 =="1":
                             port_count = int(input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the number of IPs to scan: {Fore.RESET} ")) 
                             clear_console()
                             print_navbar(f"Main menu / Network Scanner / {Fore.RED}{port_count} ")
                             NetworkScanner().scan_network_and_display(port_count)
                             print_separator()
                             input(f"{Fore.YELLOW}Press ENTER to proceed or return... {Fore.RESET}")
                             Network()
          
          
                       elif choice1 =="2":
                          clear_console()
                          print_navbar(f"Main menu / Network Scanner / {Fore.RED}255")
                          NetworkScanner().scan_network_and_display(255)
                          print_separator()
                          input(f"{Fore.YELLOW}Press ENTER to proceed or return... {Fore.RESET}")
                          choice == "3"
                          input(f"{Fore.YELLOW}Press ENTER to proceed or return... {Fore.RESET}")
                          Network()

             Network()    
                 
                        

        elif choice == "0":
            print(f"{Style.BRIGHT}{Fore.RED}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Fore.RESET}")
            input(f"{Style.BRIGHT}{Fore.YELLOW}Press ENTER to continue...{Fore.RESET}")

if __name__ == "__main__":
    install_dependencies() 
    main_menu()
