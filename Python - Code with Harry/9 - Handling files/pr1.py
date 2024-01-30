# checking a word in file

f = open("creating_file.txt")
d = f.read()
if 'danyal' in d:
    print ("The word 'danyal' is present in file.")
else:
    print ("The word 'danyal' is NOT present in file.")

f.close()