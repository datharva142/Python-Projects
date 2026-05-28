# DataShield

DataShield is a Python automation script that creates scheduled backups of a source folder, copies only new or updated files, creates a ZIP archive, and can send a backup report by email.

## Features

- Scheduled folder backup
- Copies only new or modified files
- Creates timestamped ZIP archives
- Sends email reports using Gmail SMTP
- Skips email reporting when no receiver email is provided

## Project Structure

```text
Datashield/
├── DataShield.py
├── sendmail.py
├── requirements.txt
├── .env.example
├── .gitignore
└── Data/
```

## Requirements

- Python 3.8 or later
- Gmail account with a Gmail App Password

Install dependencies:

```bash
pip3 install -r requirements.txt
```

## Email Setup

Set your sender email and Gmail App Password before running the script:

```bash
export DATASHIELD_MAIL_SENDER="yourgmail@gmail.com"
export DATASHIELD_MAIL_PASSWORD="your-16-character-app-password"
```

Do not use your normal Gmail password. Create an App Password from your Google Account security settings.

## Usage

Run backup every 1 minute without email reporting:

```bash
python3 DataShield.py 1 Data
```

Run backup every 1 minute and send the report to a receiver:

```bash
python3 DataShield.py 1 Data receiver@example.com
```

Show help:

```bash
python3 DataShield.py --h
```

Show usage:

```bash
python3 DataShield.py --u
```

## Notes

- Press `Ctrl + C` to stop the running scheduler.
