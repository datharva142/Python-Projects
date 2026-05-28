import time
import sys
import os
import schedule
import shutil
import hashlib
import zipfile
from sendmail import send_report


def make_zip(folder):
    """Create a timestamped zip archive of the backup folder."""
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "-" + timestamp + ".zip"

    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    # Store files with paths relative to the backup folder.
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative  = os.path.relpath(full_path, folder)
            zobj.write(full_path, relative)

    zobj.close()

    return zip_name


def calculate_hash(path):
    """Calculate the MD5 hash of a file to detect content changes."""
    hobj = hashlib.md5()
    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()


def BackupFiles(Source, Destination):
    """Copy only new or updated files from Source to Destination."""
    copied_files = []

    print("Creating the Backup Folder for Backup Process")

    os.makedirs(Destination, exist_ok=True)

    # Walk through every folder and file inside the source directory.
    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root, file)

            # Preserve the same folder structure inside the backup directory.
            relative  = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy the file if it's new or changed
            if (not os.path.exists(dest_path)) or \
               (calculate_hash(src_path) != calculate_hash(dest_path)):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files


def StartBackUpProcess(Source="Data", Receiver=None):
    """Run one backup cycle and optionally send an email report."""
    BackupName = "Backup"
    Border     = "-" * 50

    print(Border)
    print("Backup Process Started Successfully at : ", time.ctime())
    print(Border)

    start_time = time.time()                          

    # Backup files first, then archive the completed backup folder.
    files    = BackupFiles(Source, BackupName)
    zip_file = make_zip(BackupName)

    print("Backup Completed Successfully")
    print("Files Copied : ", len(files))
    print("Zip file Created : ", zip_file)

    print(Border)
    if Receiver:
        # Send the report only when a receiver email is provided.
        print("Sending backup report via email ...")
        send_report(
            source       = Source,
            backup_name  = BackupName,
            zip_file     = zip_file,
            copied_files = files,
            start_time   = start_time,
            receiver     = Receiver,
        )
    else:
        # Backup still succeeds even when email reporting is skipped.
        print("Backup completed, but report was not sent to anyone.")
        print("To send a report, run: python3 DataShield.py TimeInterval SourceDirectory ReceiverEmail")


def main():

    Border = "-" * 50
    print(Border)
    print("--------- Data Shield System------------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] in ("--h", "--H"):
            print("This script is used to :")
            print("1 : Takes Autobackup at Given Time")
            print("2 : Backup Only New and Updated Files")
            print("3 : Create an Archive of the Backup Periodically")
            print("4 : Send an Email Report after every backup run")

        elif sys.argv[1] in ("--u", "--U"):
            print("Use The Automation script as:")
            print("  ScriptName.py  TimeInterval  SourceDirectory  ReceiverEmail")
            print("")
            print("  TimeInterval    : Time in minutes for periodic scheduling")
            print("  SourceDirectory : Name of directory to be backed up")
            print("  ReceiverEmail   : Email address that receives backup reports")
            print("")
            print("Set DATASHIELD_MAIL_SENDER and DATASHIELD_MAIL_PASSWORD before running.")

        else:
            print("Unable to Proceed as there is no such option")
            print("Use --h or --u to get more details")

    # Expected format: python DataShield.py 5 Data receiver@example.com
    elif len(sys.argv) in (3, 4):
        receiver = None
        if len(sys.argv) == 4:
            receiver = sys.argv[3]

        print("Time Interval is : ", sys.argv[1])
        print("Directory Name is : ", sys.argv[2])
        if receiver:
            print("Receiver Email is : ", receiver)

        # Schedule the backup process at the given minute interval.
        schedule.every(int(sys.argv[1])).minutes.do(StartBackUpProcess, sys.argv[2], receiver)

        print(Border)
        print("Data Shield System gets Started Successfully")
        print("Time Interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the Execution")
        print(Border)

        try:
            # Keep the script running so scheduled backups can execute.
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nBackup scheduler stopped by user")

    else:
        print("Invalid number of command line arguments")
        print("Unable to Proceed as there is no such option")
        print("Use --h or --u to get more details")

    print(Border)
    print("---------Thank You for Using Our Script-----------")
    print(Border)


if __name__ == "__main__":
    main()
