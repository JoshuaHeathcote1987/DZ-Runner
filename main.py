
# Title: Dayz Auto Runner
# Description: This script allows the user to auto run on dayz as long as the window is selected.
# Author: Josh
# Date: 2025-02-27
# Version: 1.0


import pyautogui as g
import time as t
import win32gui
import win32process
import psutil
import os

def get_active_window_exe():
    hwnd = win32gui.GetForegroundWindow()  # Get active window handle
    _, pid = win32process.GetWindowThreadProcessId(hwnd)  # Get process ID
    
    for process in psutil.process_iter(attrs=['pid', 'name', 'exe']):
        if process.info['pid'] == pid:
            return process.info['name']  # Return the executable name
    
    return None

def main():
    current_exe = ''
    desired_exe = ''

    while True:
        exe_name = get_active_window_exe()
        if current_exe == desired_exe:
            g.press('w', interval=1)

if __name__ == "__main__":
    os.system('cls')
    t.sleep(3)
    main()