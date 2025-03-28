# schedulartask
A Python script to schedule and automate tasks.
1. Open Task Scheduler
Press Win + S, type Task Scheduler, and open it.

2. Start the Wizard
In the right panel, click Create Basic Task.

Name: Type a name (e.g., Run Python Script).
Description (optional): Add a note like "Update database daily".
Click Next.

3. Choose Trigger
Select when to run the task:

Daily/Weekly/When I log in/At startup, etc.

Example: Daily → Click Next.

Set the Start time (e.g., 3:00 AM) and frequency (e.g., every 1 day).

Click Next.

4. Choose Action
Select Start a Program → Click Next.

5. Configure the Script
Program/script:
Browse to python.exe (usually in C:\Python3XX\python.exe).
Replace 3XX with your Python version (e.g., Python311).

Add arguments:
Type the full path to your script in quotes, e.g.:
"C:\Automation\task2.py"

Start in:
Type the folder where your script lives, e.g.:
C:\Automation

Click Next → Finish.

6. Test the Task
Right-click your task in Task Scheduler → Run.

Check if sample_data.csv and example.db are updated in your script’s folder.
