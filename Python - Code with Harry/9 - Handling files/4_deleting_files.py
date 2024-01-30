import os

if os.path.exists("file_to_del.txt"):
    os.remove("file_to_del.txt")
else:
    print ("The targeted file does not exist")

# os.rmdir("myfolder")