# Write a program to find out the line number where python is present from question 6.

content = True

i = 1

with open("pr6_log.txt") as f:
    while content:
        content = f.readline().lower()
        if 'python' in content:
            print (content)
            print (f"Python word is present at line number {i}")
        i += 1
    else:
        print ("Python is not present.")