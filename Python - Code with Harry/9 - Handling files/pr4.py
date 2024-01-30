# A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file

with open("pr4.txt") as f:
    content = f.read()
    if 'donkey' in content:
        content = content.replace('donkey', 'dude')
        with open("pr4.txt", "w")as f:
            f.write(content)
    else:
        pass
