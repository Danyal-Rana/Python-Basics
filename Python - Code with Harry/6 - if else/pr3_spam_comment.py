# A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.


c = input("Enter comment: ")

if ("make a lot of money" in c):
    print("This is a spam comment")
elif ("buy now" in c):
    print("This is a spam comment")
elif ("subscribe this" in c):
    print("This is a spam comment")
elif ("click this" in c):
    print("This is a spam comment")
else:
    print("This is not a span comment")