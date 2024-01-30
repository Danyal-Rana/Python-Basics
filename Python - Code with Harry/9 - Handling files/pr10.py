# Write a program to wipe out the contents of a file using python

import os

with open("pr10.txt", 'w') as f:
    f.write("")


# this method is used to delete the file
# os.remove("pr10.txt")