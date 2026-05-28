import time
import psutil
import sys
import os
import schedule
from sendmail import send_surveillance_report


def PrintHeader(title):
    Border = "-" * 60
    print(Border)
    print(title.center(60))
    print(Border)


def WriteHeader(fobj, title):
    Border = "-" * 60
    fobj.write(Border + "\n")
    fobj.write(title.center(60) + "\n")
    fobj.write(Border + "\n")


def CreateLog(FolderName):
    Border = "-" * 60

    if os.path.exists(FolderName):
        if os.path.isdir(FolderName) == False:
            print("Unable to Create Folder")
            return None
    else:
        os.mkdir(FolderName)
        print("Directory For Logs gets Created Successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    Filename = os.path.join(FolderName, "SystemSurveillance_%s.log" % timestamp)
    print("Log File gets Created with name : ", "\n", Filename)

    with open(Filename, "w") as fobj:
        WriteHeader(fobj, "Platform Surveillance System")

        fobj.write("Log created at : " + time.ctime() + "\n")
        fobj.write(Border + "\n\n")

        fobj.write("----------------System Report----------------------\n")

        fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())

        mem = psutil.virtual_memory()
        fobj.write("RAM Usage : %s %%\n" % mem.percent)
        fobj.write(Border + "\n")

        fobj.write("\n------------Disk Usage Report--------------------\n")

        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                fobj.write("%s -> %s %% Used\n" % (part.mountpoint, usage.percent))
            except:
                pass

        fobj.write(Border + "\n")

        net = psutil.net_io_counters()
        fobj.write("\n------------Network Usage Report-------------------\n")
        fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
        fobj.write("Received : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
        fobj.write(Border + "\n")

        Data = ProcessScan()

        fobj.write("\n------------Process Report-------------------\n")

        for info in Data:
            fobj.write("PID : %s\n" % info.get("pid"))
            fobj.write("Name : %s\n" % info.get("name"))
            fobj.write("Username : %s\n" % info.get("username"))
            fobj.write("Status : %s\n" % info.get("status"))
            fobj.write("Start Time : %s\n" % info.get("create_time"))
            fobj.write("CPU %% : %.2f\n" % info.get("cpu_percent"))
            fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
            fobj.write(Border + "\n")

        fobj.write(Border + "\n")
        fobj.write("----------------End of Log File------------------- \n")
        fobj.write(Border + "\n")

    return Filename


def ProcessScan():
    listprocess = []

    # Warm up for CPU percent
    try:
        process_list = list(psutil.process_iter())
    except:
        return listprocess

    for proc in process_list:
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    try:
        process_list = list(psutil.process_iter())
    except:
        return listprocess

    for proc in process_list:
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time"])

            try:
                info["create_time"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.localtime(info["create_time"])
                )
            except:
                info["create_time"] = "N/A"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent("rss")

            listprocess.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess


def CreateLogAndSendMail(FolderName, ReceiverEmail):
    LogFile = CreateLog(FolderName)

    if LogFile != None:
        send_surveillance_report(LogFile, ReceiverEmail)


def main():
    Border = "-" * 60

    PrintHeader("Platform Surveillance System")

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to : ")
            print("1. Create automatic logs")
            print("2. Execute periodically")
            print("3. Send log file by email")
            print("4. Store information about processes")
            print("5. Store information about CPU")
            print("6. Store information about RAM usage")
            print("7. Store information about Secondary storage")
            print("8. Store information about network usage")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use The Automation script as")
            print("ScriptName.py TimeInterval DirectoryName ReceiverEmail")
            print("TimeInterval: Time in minutes for periodic scheduling")
            print("DirectoryName: Name of the directory to create auto log")
            print("ReceiverEmail: Email address to send generated log file")

        else:
            print("Unable to Proceed as there is no such option")
            print("Use --h or --u to get more details")

    elif len(sys.argv) == 4:
        try:
            TimeInterval = int(sys.argv[1])
        except:
            print("Invalid time interval. Please enter time in minutes.")
            return

        DirectoryName = sys.argv[2]
        ReceiverEmail = sys.argv[3]

        print("Time Interval is : ", TimeInterval)
        print("Directory Name is : ", DirectoryName)
        print("Receiver Email is : ", ReceiverEmail)

        schedule.every(TimeInterval).minutes.do(
            CreateLogAndSendMail,
            DirectoryName,
            ReceiverEmail
        )

        print("Platform Surveillance System gets Started Successfully")
        print("Directory Created with Name : ", DirectoryName)
        print("Time Interval in minutes : ", TimeInterval)
        print("press Ctrl + C to stop the Execution")

        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nExecution stopped by user")

    else:
        print("Invalid number of command line arguments")
        print("Unable to Proceed as there is no such option")
        print("Use --h or --u to get more details")

    print(Border)
    print("Thank You for Using Our Script".center(60))
    print(Border)


if __name__ == "__main__":
    main()