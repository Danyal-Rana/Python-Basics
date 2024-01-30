# f = open("creating_file.txt", "x")

f = open("creating_file.txt", "w")
f.write("Now, I am writing in the file.")
f.close

f = open("creating_file.txt", "r")
print(f.read())
f.close()