# f = open("files.txt", "a")
# f.write("\nNow, I am appending the file.")
f = open("files.txt", "w")
f.write("Woops! I have deleted the content.")
f.close()

f = open("files.txt", "r")
print (f.read())