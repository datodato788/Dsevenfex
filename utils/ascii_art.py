from colorama import Fore

def create_ascii_art(text):
    ascii_art = f"""
    ____                            __
   |  _ \ ___  _____   _____ _ __  / _| _____  __
   | | | / __|/ _ \ \ / / _ \ '_ \| |_ / _ \ \/ /
   | |_| \__ \  __/\ V /  __/ | | |  _|  __/>  < 
   |____/|___/\___| \_/ \___|_| |_|_|  \___/_/\_\\
   {text}
    """
    return f"{Fore.GREEN}{ascii_art}"

def print_separator():
    print(f"{Fore.RED}==================={Fore.GREEN}D7FEX{Fore.YELLOW}===================")
