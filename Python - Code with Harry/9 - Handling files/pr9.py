with open("pr8.txt", 'r') as f:
    content1 = f.read()

with open("pr8_copy.txt", 'r') as f:
    content2 = f.read()

if content1==content2:
    print ("Files are identical.")
else:
    print ("Files are NOT identical.")