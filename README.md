# File Organizer

## Purpose

This Python script is designed to organize files in the Downloads directory by moving them to specific folders based on their file extensions. It categorizes files into folders such as Images, Sounds, Videos, Documents, Code, Data, Installation, Zips, Torrents, and Others. Additionally, it moves folders to a designated "Folders" folder.

## File Organization

The script organizes files based on their file extensions, and each file is moved to a corresponding folder. If a file's creation date is more than 30 days old, it is moved to the appropriate folder in the "Desktop/downloadsArchive" directory. Folders are moved to the "Folders" folder.

## Usage

1. **Set Up the Script:**
   - Copy the script into a Python (.py) file.
   - Ensure that you have Python installed on your system.

2. **Configure Paths:**
   - Adjust the `who_am_i` variable to match your system's username.
   - Modify the `downloads_path` and `moving_path` variables if your Downloads and Archive folders have different paths.

3. **Run the Script:**
   - Execute the script using a Python interpreter. For example:
     ```bash
     python organize_downloads.py
     ```

4. **Check Results:**
   - The script will print messages indicating successful file and folder movements.

## Setting Up a Cron Job

[Cron](https://en.wikipedia.org/wiki/Cron) is a time-based job scheduler in Unix-like operating systems. It allows you to automate the execution of tasks at specified intervals. In this case, we want to schedule our file organizing script to run at regular intervals.

1. Open the crontab file for editing:
   
  ```bash
   crontab -e
  ```
This command opens the crontab file in the default text editor.

2. Add a new line to schedule the script to run daily, for example:
  
  ```bash
  0 0 * * * /path/to/python3 /path/to/organize_downloads.py
  ```

This example schedules the script to run every day at midnight.

3. Save and exit the editor.

Now, the script will be executed automatically according to the specified schedule.

Note: Adjust the paths and schedule according to your preferences and system configuration. Make sure to use absolute paths in the cron job.