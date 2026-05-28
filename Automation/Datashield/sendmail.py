import os
import smtplib
import time
from email.message import EmailMessage


# Gmail SMTP settings used for sending backup reports.
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

# Keep these empty for GitHub. Use environment variables for real credentials.
SENDER_EMAIL = ""
APP_PASSWORD = ""


def send_email(sender, app_password, receiver, subject, body):
    """Send a plain text email using Gmail SMTP."""
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)


def send_report(source, backup_name, zip_file, copied_files, start_time, receiver=None):
    """Create and send the DataShield backup report email."""
    # Read sender credentials from constants first, then environment variables.
    sender = SENDER_EMAIL or os.getenv("DATASHIELD_MAIL_SENDER")
    app_password = APP_PASSWORD or os.getenv("DATASHIELD_MAIL_PASSWORD")

    # Stop early if any required email detail is missing.
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

    # Build a readable list of copied files for the email body.
    duration = round(time.time() - start_time, 2)
    copied_list = "\n".join(f"- {file}" for file in copied_files)
    if not copied_list:
        copied_list = "- No new or updated files were copied"

    # Prepare the backup summary that will be sent to the receiver.
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
    """Run a small email-report test from the terminal."""
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
