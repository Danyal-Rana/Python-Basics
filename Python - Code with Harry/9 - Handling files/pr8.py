# Write a program to make a copy of a text file “this.txt.”

with open("pr8.txt", 'r') as f:
    content = f.read()

with open("pr8_copy.txt", 'w') as f:
    f.write(content)