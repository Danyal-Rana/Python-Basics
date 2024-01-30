# Write a program to print the multiplication table of a given number using while loop.

n = int(input("Enter a number: "))

i = 1

while (i>11):
    print (str(n)+ " * " +str(i)+ " = " +str(n*i))
    i = i+1