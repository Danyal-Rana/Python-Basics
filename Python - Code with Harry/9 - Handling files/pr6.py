# Write a program to mine a log file and find out whether it contains ‘python’.

with open("pr6_log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print ("Yes, Python is present.")
else:
    print ("Python is not present.")