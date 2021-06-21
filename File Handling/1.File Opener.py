file_path = '../file/File Opener/text.txt'

try:
    open(file_path, "r")
    print('File found')

except:
    print('File not found')
