import os

file_path = '../File Handling/deleted.py'

try:

    os.remove(file_path)

except FileNotFoundError:
    print("File already deleted!")
