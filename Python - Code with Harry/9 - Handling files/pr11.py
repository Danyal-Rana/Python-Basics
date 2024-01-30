# Write a python program to rename a file to “renamed_by_python.txt.”

import os

with open("pr11.txt", "r") as f:
    content = f.read()

with open("pr11_renamed.txt", "w") as f:
    f.write(content)

os.remove("pr11.txt")