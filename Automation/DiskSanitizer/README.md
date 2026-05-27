# Duplicate File Finder and Remover

This Python script finds duplicate files inside a folder by comparing their MD5 checksums. It keeps the first file found as the original file and asks for permission before deleting each copied duplicate file.

## Features

- Finds duplicate files inside the `Demo_Data` folder.
- Keeps the original file safely.
- Asks before deleting each copied duplicate file.
- Shows the total number of same copy files detected.
- Shows the total number of files deleted.
- Displays the original files kept.
- Displays the names of removed files.

## Demo Folder Structure

Prepare a folder named `Demo_Data` in the same location as the Python script.

Example:

```text
Demo_Data/
├── duplicate1.txt
├── duplicate2.txt
├── duplicate3.txt
├── file1.txt
├── file2.txt
└── uniquefile.txt
```

Some of these files should contain the same data so the script can detect them as duplicates.

## Requirements

- Python 3.x

No external Python packages are required. The script uses only built-in Python modules:

- `hashlib`
- `os`

## How to Run

Save the Python code in a file, for example:

```text
DuplicateFileRemover.py
```

Then run:

```bash
python DuplicateFileRemover.py
```

On some systems, use:

```bash
python3 DuplicateFileRemover.py
```

## How It Works

1. The script walks through all files inside the `Demo_Data` folder.
2. It calculates the checksum of every file.
3. Files with the same checksum are treated as duplicates.
4. The first file in each duplicate group is kept as the original file.
5. The script asks whether to delete each copied duplicate file.
6. At the end, it prints a summary.

## Example Output

```text
Original File Kept :  Demo_Data/duplicate1.txt
Copied Duplicate File Found :  Demo_Data/duplicate2.txt
Do you want to delete this copied file? (y/n): y
Deleted :  Demo_Data/duplicate2.txt

---------- Summary ----------
Total Same Copy Files Detected :  1
Total Files Deleted           :  1

Original Files Kept:
Demo_Data/duplicate1.txt

Removed Files:
Demo_Data/duplicate2.txt
```

## Note

The original file is not moved or copied anywhere. It remains stored in its original location. Only copied duplicate files are deleted when you give permission.