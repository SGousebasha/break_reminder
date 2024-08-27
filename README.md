# break_reminder
---

# Break Reminder Script

This Python script is designed to help users maintain healthy work habits by reminding them to take regular breaks. It uses the `notify-send` command, available on Linux systems, to send desktop notifications at regular intervals.

## Features

- **Automatic Notifications:** The script sends a notification every 20 minutes, reminding the user to take a short 20-second break.
- **Application Start Notification:** When the script starts, it sends a notification to indicate that the break reminder has begun, along with a console message.
- **Customizable Timing:** The script waits for 20 seconds after sending the start notification, then it sends the break reminder, and continues to run, sending reminders every 20 minutes (1200 seconds).

## How It Works

- **`send_notification()` Function:** This function sends a desktop notification reminding the user to take a 20-second break.
- **`applicationStartedNotification()` Function:** This function sends a desktop notification indicating that the break reminder script has started and prints a message to the console.
- **`main()` Function:** This is the core loop of the script. It first triggers the application start notification, waits for 20 seconds, sends the break reminder, and then waits for the remaining time in the 20-minute interval before looping again.

## How to Use

1. **Download the Script:**
   - Clone the repository or download the `break_reminder.py` script to your local machine.

2. **Make the Script Executable:**
   - Open a terminal and navigate to the directory where the script is located.
   - Run the following command to make the script executable:
     ```bash
     chmod +x break_reminder.py
     ```

3. **Run the Script:**
   - Execute the script by running:
     ```bash
     ./break_reminder.py
     ```
   - The script will start running, and you’ll see a notification that the break reminder has started. Every 20 minutes, you’ll receive a notification reminding you to take a break.

4. **Stop the Script:**
   - The script will run indefinitely, sending notifications every 20 minutes.
   - To stop the script, press `Ctrl + C` in the terminal where the script is running. This will terminate the process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
