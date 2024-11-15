#!/usr/bin/env python

import subprocess
import time

sus_processes = ("smb", "ssh", "vnc", "ftp", "rdp", "telnet")

while True:
    time.sleep(1)
    command = subprocess.run(["ps", "-e"], capture_output=True, text=True)
    
    for process in sus_processes:
        if process in command.stdout:
            subprocess.run(["zenity", "--warning", "--text=A suspect process has been detected running, please do a security check", "--icon=warning.jpg"], capture_output=True)
