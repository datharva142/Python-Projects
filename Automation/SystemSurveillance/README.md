# System Surveillance

System Surveillance is a Python automation script that creates system monitoring log files at a scheduled time interval and sends the generated log file by email.

## Features

- Creates automatic timestamped log files.
- Runs periodically based on a user-defined time interval.
- Stores CPU usage information.
- Stores RAM usage information.
- Stores disk usage information.
- Stores network sent and received data.
- Stores running process details.
- Sends the generated log file to a receiver email address.
- Creates the log folder automatically if it does not already exist.

## Requirements

- Python 3.x
- `psutil`
- `schedule`

Install required packages:

```bash
pip install -r requirements.txt
On some systems, use:

pip3 install -r requirements.txt
Project Files
SystemSurveillance/
├── SystemSurveillance.py
├── sendmail.py
├── requirements.txt
└── README.md
Email Setup
This project uses Gmail SMTP to send the generated log file by email.

In sendmail.py, keep credentials empty for GitHub:

SENDER_EMAIL = ""
APP_PASSWORD = ""
Before running the script, set your email credentials as environment variables.

For macOS/Linux:

export SYSTEM_SURVEILLANCE_MAIL_SENDER="yourmail@gmail.com"
export SYSTEM_SURVEILLANCE_MAIL_PASSWORD="your-gmail-app-password"
For Windows Command Prompt:

set SYSTEM_SURVEILLANCE_MAIL_SENDER=yourmail@gmail.com
set SYSTEM_SURVEILLANCE_MAIL_PASSWORD=your-gmail-app-password
Use a Gmail App Password instead of your normal Gmail password.

How to Run
Run the script with three command line arguments:

python SystemSurveillance.py TimeInterval DirectoryName ReceiverEmail
Example:

python SystemSurveillance.py 5 Logs receiver@example.com
This command creates a log file inside the Logs folder every 5 minutes and sends that log file to receiver@example.com.

On some systems, use:

python3 SystemSurveillance.py 5 Logs receiver@example.com
Stop the script with:

Ctrl + C
Help Commands
To display script information:

python SystemSurveillance.py --h
To display usage instructions:

python SystemSurveillance.py --u
Log File Name
The script creates log files with names like:

SystemSurveillance_2026-05-28_20-30-15.log
Log File Contains
Each generated log file contains:

CPU usage
RAM usage
Disk usage
Network sent data
Network received data
Running process information
Process Information
For each running process, the script stores:

PID
Process name
Username
Status
Start time
CPU usage percentage
Memory usage percentage
Note
Some process or disk details may be skipped if the operating system does not allow access.

Do not upload your real email password or Gmail App Password to GitHub.
```