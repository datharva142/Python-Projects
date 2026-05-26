import hashlib
import os

def CalculateChecksum(FileName):

    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)
    
    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return

    if(Ret == False):
        print("There is no such directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, Filename in os.walk(DirectoryName):os.walk(DirectoryName)
        
    for fname in Filename:
            fname = os.path.join(FolderName, fname)

            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]
    return Duplicate

def DeleteDuplicate(Path = "Marvellous"):

    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1

            if(Count > 1):
                print("Delete File : ", subvalue)
                os.remove(subvalue)
                cnt = cnt + 1

                Count = 0
    print("Total Files Deleted : ", cnt)

def main():
    DeleteDuplicate()

if __name__ == "__main__":
    main()