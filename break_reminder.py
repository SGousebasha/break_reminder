#!/usr/bin/env python3
import time
import subprocess

def send_notification():
    subprocess.run(['notify-send', 'Break Reminder', 'Time to take a 20-second break!'])

def applicationStartedNotification():
    subprocess.run(['notify-send', 'Break Remider', 'Remider started'])

def main():
    while True:
        applicationStartedNotification()
        time.sleep(20)  # Wait for 20 seconds
        send_notification()  # Optionally notify again after the break
        time.sleep(1200 - 20)  # Wait for 20 minutes minus the 20 seconds break tim

if __name__ == "__main__":
    main()