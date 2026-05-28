import os
import smtplib
import time
from email.message import EmailMessage


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = ""
APP_PASSWORD = ""


def send_email(sender, app_password, receiver, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)


def send_report(source, backup_name, zip_file, copied_files, start_time, receiver=None):
    sender = SENDER_EMAIL or os.getenv("DATASHIELD_MAIL_SENDER")
    app_password = APP_PASSWORD or os.getenv("DATASHIELD_MAIL_PASSWORD")

    missing = []
    if not sender:
        missing.append("sender email")
    if not app_password or app_password == "paste-your-gmail-app-password-here":
        missing.append("Gmail app password")
    if not receiver:
        missing.append("receiver email")

    if missing:
        print("Email report skipped. Missing details:")
        print(", ".join(missing))
        return False

    duration = round(time.time() - start_time, 2)
    copied_list = "\n".join(f"- {file}" for file in copied_files)
    if not copied_list:
        copied_list = "- No new or updated files were copied"

    subject = f"DataShield Backup Report: {source}"
    body = f"""DataShield backup completed successfully.

Source folder : {source}
Backup folder : {backup_name}
Zip file      : {zip_file}
Files copied  : {len(copied_files)}
Duration      : {duration} seconds

Copied files:
{copied_list}

Regards,
DataShield
"""

    send_email(sender, app_password, receiver, subject, body)
    print("Email report sent successfully!")
    return True


def main():
    receiver = input("Enter receiver email: ").strip()

    send_report(
        source="Data",
        backup_name="Backup",
        zip_file="Backup-test.zip",
        copied_files=["example.txt"],
        start_time=time.time(),
        receiver=receiver,
    )


if __name__ == "__main__":
    main()
