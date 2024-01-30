# Repeat program 4 for a list of such words to be censored.

words = ['donkey', 'kaddu', 'motay']

with open("pr5.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%#@&")

    with open("pr5.txt", "w")as f:
        f.write(content)
