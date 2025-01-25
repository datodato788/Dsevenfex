import os
def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
def install_dependencies():
    """Stub for installing dependencies."""
    print("Installing dependencies (if any)...")
# utils/helpers.py
def save_to_file(data, file_name):
    try:
        with open(file_name, 'a') as file:
            file.write(data + "\n")
    except Exception as e:
        print(f"Error saving to file: {e}")
