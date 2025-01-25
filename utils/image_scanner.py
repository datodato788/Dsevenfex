import os
from PIL import Image
from PIL.ExifTags import TAGS
from colorama import Fore, Style
from utils.helpers import clear_console
from utils.ascii_art import print_separator, print_navbar


def image_scanner():
    while True:
        clear_console()
        print_navbar("Main menu / Image Scanning")
        print(f"{Fore.BLUE}[1] {Fore.GREEN}Default file (imageScannerFile){Style.RESET_ALL}")
        print(f"{Fore.BLUE}[2] {Fore.GREEN}Choose file location (CustomFilePath){Style.RESET_ALL}")
        print(f"{Fore.BLUE}[0] {Fore.RED}Go Back to Main Menu{Style.RESET_ALL}")
        print_separator()
        choice = input(f"{Fore.YELLOW}Choose an option: {Style.RESET_ALL}")

        if choice == "1":
            folder_path = "imageScannerFile"
        elif choice == "2":
            folder_path = input(f"{Fore.YELLOW}Enter folder path to scan: {Style.RESET_ALL}")
            if not os.path.isdir(folder_path):
                print(f"{Fore.RED}Folder not found: {folder_path}{Style.RESET_ALL}")
                input(f"{Fore.YELLOW}Press Enter to return to the scanning menu...{Style.RESET_ALL}")
                continue
        elif choice == "0":
            print(f"{Fore.GREEN}Returning to Main Menu...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Try again...{Style.RESET_ALL}")
            continue

        def extract_exif(image_path):
            """
            Extracts EXIF data from a single image.
            """
            try:
                image = Image.open(image_path)
                exif_data = image._getexif()

                if not exif_data:
                    return f"{Fore.RED}EXIF data not found for {image_path}.{Style.RESET_ALL}"

                extracted_data = {}
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    extracted_data[tag_name] = value

                return extracted_data
            except Exception as e:
                return f"{Fore.RED}Error processing {image_path}: {str(e)}{Style.RESET_ALL}"

        def display_exif_data(exif_info):
            """
            Displays the extracted EXIF data in a clean format.
            """
            clear_console()
            print_separator()
            print(f"{Fore.CYAN}Image EXIF Data{Style.RESET_ALL}")
            print_separator()
            for key, value in exif_info.items():
                print(f"{Fore.GREEN}{key}{Style.RESET_ALL}: {Fore.YELLOW}{value}{Style.RESET_ALL}")
            print_separator()
            input(f"{Fore.YELLOW}Press ENTER to return to the menu... {Fore.RESET}")

            clear_console()

        def list_and_select_file(folder_path):
            """
            Lists files in the folder and allows the user to select one by name.
            """
            try:
                files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
                if not files:
                    print(f"{Fore.RED}No files found in the folder.{Style.RESET_ALL}")
                    input(f"{Fore.YELLOW}Press Enter to return to the scanning menu...{Style.RESET_ALL}")
                    return None

                while True:
                    clear_console()
                    print_navbar("Main menu / Image Scanning / File")
                    print(f"{Fore.CYAN}Files in folder:{Style.RESET_ALL}")
                    for idx, file in enumerate(files, start=1):
                        print(f"{Fore.BLUE}[{idx}] {Fore.GREEN}{file}{Style.RESET_ALL}")
                    print(f"{Fore.BLUE}[0] {Fore.RED}Go Back{Style.RESET_ALL}")

                    print_separator()
 
                    choice = input(f"{Fore.YELLOW}Choose an option: {Style.RESET_ALL}")
                    if choice == "0":
                        return "go_back"
                    try:
                        idx = int(choice) - 1
                        if 0 <= idx < len(files):
                            return os.path.join(folder_path, files[idx])
                    except ValueError:
                        pass
                    print(f"{Fore.RED}Invalid choice. Try again.{Style.RESET_ALL}")

            except Exception as e:
                print(f"{Fore.RED}Error listing files: {str(e)}{Style.RESET_ALL}")
                input(f"{Fore.YELLOW}Press Enter to return to the scanning menu...{Style.RESET_ALL}")
                return None

        def process_single_file(file_path):
            """
            Processes a single file.
            """
            if file_path and os.path.isfile(file_path):
                exif_info = extract_exif(file_path)
                if isinstance(exif_info, dict):
                    display_exif_data(exif_info)
                else:
                    print(exif_info)
                    input(f"{Fore.YELLOW}Press ENTER to return to the menu... {Fore.RESET}")
                    clear_console()
            else:
                print(f"{Fore.RED}File not found: {file_path}{Style.RESET_ALL}")

        while True:
            selected_file = list_and_select_file(folder_path)
            if selected_file == "go_back":
                break
            elif selected_file:
                process_single_file(selected_file)
