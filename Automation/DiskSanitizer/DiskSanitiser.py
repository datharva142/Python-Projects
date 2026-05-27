import hashlib
import os

def CalculateChecksum(FileName):
    with open(FileName, "rb") as fobj:
        hobj = hashlib.md5()

        Buffer = fobj.read(1000)

        while len(Buffer) > 0:
            hobj.update(Buffer)
            Buffer = fobj.read(1000)

    return hobj.hexdigest()


def CheckDuplicateList(value):
    if len(value) > 1:
        return True
    else:
        return False


def FindDuplicate(DirectoryName="Demo_Data"):
    if not os.path.isdir(DirectoryName):
        print("There is no such directory")
        return {}

    Duplicate = {}

    for FolderName, SubFolderName, Filename in os.walk(DirectoryName):
        for fname in Filename:
            fname = os.path.join(FolderName, fname)

            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate


def DeleteDuplicate(Path="Demo_Data"):
    MyDict = FindDuplicate(Path)

    Result = list(filter(CheckDuplicateList, MyDict.values()))

    total_duplicate_files = 0
    deleted_count = 0

    original_files = []
    removed_files = []

    for value in Result:
        original_file = value[0]
        original_files.append(original_file)

        duplicate_files = value[1:]
        total_duplicate_files = total_duplicate_files + len(duplicate_files)

        print("\nOriginal File Kept : ", original_file)

        for duplicate_file in duplicate_files:
            print("Copied Duplicate File Found : ", duplicate_file)

            choice = input("Do you want to delete this copied file? (y/n): ")

            if choice.lower() == "y":
                os.remove(duplicate_file)
                removed_files.append(duplicate_file)
                deleted_count = deleted_count + 1
                print("Deleted : ", duplicate_file)
            else:
                print("Not Deleted : ", duplicate_file)

    print("\n---------- Summary ----------")
    print("Total Same Copy Files Detected : ", total_duplicate_files)
    print("Total Files Deleted           : ", deleted_count)

    print("\nOriginal Files Kept:")
    for file in original_files:
        print(file)

    print("\nRemoved Files:")
    if len(removed_files) == 0:
        print("No files removed")
    else:
        for file in removed_files:
            print(file)


def main():
    DeleteDuplicate()


if __name__ == "__main__":
    main()