import os
import smtplib
from email.message import EmailMessage


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

SENDER_EMAIL = ""
APP_PASSWORD = ""


def send_email_with_attachment(sender, app_password, receiver, subject, body, attachment_path):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with open(attachment_path, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(attachment_path)

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name
    )

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)


def send_surveillance_report(log_file, receiver=None):
    sender = SENDER_EMAIL or os.getenv("SYSTEM_SURVEILLANCE_MAIL_SENDER")
    app_password = APP_PASSWORD or os.getenv("SYSTEM_SURVEILLANCE_MAIL_PASSWORD")

    missing = []

    if not sender:
        missing.append("sender email")

    if not app_password:
        missing.append("Gmail app password")

    if not receiver:
        missing.append("receiver email")

    if missing:
        print("Email report skipped. Missing details:")
        print(", ".join(missing))
        return False

    subject = "System Surveillance Log Report"

    body = """System Surveillance log file has been generated successfully.

Please find the log file attached with this email.

Regards,
System Surveillance
"""

    try:
        send_email_with_attachment(
            sender,
            app_password,
            receiver,
            subject,
            body,
            log_file
        )

        print("Email report sent successfully!")
        return True

    except Exception as error:
        print("Unable to send email report.")
        print("Error:", error)
        return False


def main():
    receiver = input("Enter receiver email: ").strip()
    log_file = input("Enter log file path: ").strip()

    send_surveillance_report(log_file, receiver)


if __name__ == "__main__":
    main()