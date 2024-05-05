# GhostKey-Keylogger

This Python script is a keylogger tool designed to capture keystrokes on a system. It utilizes the pynput library to monitor keyboard input and saves the logged keystrokes into a text file (keylog.txt by default). The script runs in the background and records all keystrokes made by the user.

## Features:

1.Stealthy Keylogging: The script runs silently in the background without any visible indication to the user.\n
2.Customizable Log File: You can specify the name of the log file where keystrokes are saved.\n
3.Print Log: You have the option to print the contents of the keylog file.\n
4.User-Friendly Interface: Provides clear instructions and options for usage.\n

## Requirements:

 Python 3.x\n
 pynput library (automatically installed if not found)

## Installation:

Clone the Repository: To clone the repository, open your terminal and run the following command:

    git clone https://github.com/KaranParelkar/Ghostkey-Keylogger.git

Navigate to the Directory:
    
    cd Ghostkey

Install Dependencies: If you haven't installed the necessary dependencies, you can do so using pip:

    pip install pynput

Root Privileges: The script requires root privileges to run

    sudo su

Run the Script:

    python3 Ghostkey.py

This command will start the keylogger. You can use the -l or --log flag to print the contents of the keylog file:

    python3 keylogger.py -l

## Note:

Root Privileges: This script requires root privileges to run, as it interacts with system input devices.
Security and Legal Considerations: It's essential to use this script responsibly and ethically.
Keylogging without proper authorization may violate privacy laws and ethical standards.

## Disclaimer:

This script is provided for educational purposes only. The author is not responsible for any misuse or illegal activities performed with this tool. Use it at your own risk.

## Contribution:

I am thrilled to welcome contributions from the community to enhance this project! Your ideas, suggestions, and improvements are invaluable in making this keylogger even better.
