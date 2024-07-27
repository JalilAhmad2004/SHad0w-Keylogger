# SHad0w Keylogger
Welcome to the SHad0w Keylogger project! This tool is designed to log keystrokes and upload the logs to a server. The project consists of a Python script for logging, a shell script for setting up dependencies, and PHP files for managing file uploads on the server.

## Features
Keylogging: Captures keystrokes and writes them to a log file.
Log Uploading: Uploads the log file to a server when the ESC key is pressed.
Server Management: Includes PHP scripts for file uploads and listing uploaded files.
Prerequisites
Before running the keylogger, ensure that you have the following set up:

## Apache2 Server: 
You need to have an Apache2 server running. If it's not installed, you can install it using the following commands:

    sudo apt update
    sudo apt install apache2
Directory Setup: The PHP scripts will interact with the uploads directory. Make sure you set it up on your server.

## Setup Instructions
Clone the Repository

    git clone https://github.com/yourusername/shad0w-keylogger.git

## Configure PHP Files

Copy the provided PHP files to your Apache2 server's root directory and create the necessary directories:

    sudo mousepad /var/www/html/upload_form.php
    sudo mousepad /var/www/html/upload.php
    sudo mousepad /var/www/html/list_files.php
Paste the contents of upload_form.html into upload_form.php, the contents of upload.php into upload.php, and the contents of list_files.php into list_files.php.

## Install Required Python Packages and Run the keylogger

Run the following command to install the necessary Python packages, it will automatically install necessary libraries:

    bash install_requirements.sh

For first time it is compulsory to use bash script, other then that you can simple run the script directly using command:
  
    sudo python3 key.py

The script will check for required libraries and install them if necessary. Once running, it will capture keystrokes and upload the log file to the server when the ESC key is pressed.

Contributions
Contributions are welcome! If you have ideas for improvements or new features, please feel free to fork the repository and submit a pull request. We're also working on creating a proper online exploit, so any contributions in that area are especially appreciated.

## Open for Contributions

## Disclaimer
Use this tool responsibly. Unauthorized use of keyloggers or other monitoring software can be illegal and unethical. Ensure you have permission from the relevant parties before using this software. I'm not responsible for any illegal usage as I've created it for legal and educational purpose.
