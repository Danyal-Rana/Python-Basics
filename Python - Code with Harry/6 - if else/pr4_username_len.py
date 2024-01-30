# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter the username: ")

x = username.__len__()

if (x<10):
    print ("The entered username contains character less than 10.")
elif (x==10):
    print ("The entered username contains character less than 10.")
else:
    print ("The entered username contains character more than 10.")