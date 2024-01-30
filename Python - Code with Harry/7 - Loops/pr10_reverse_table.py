# Write a program to print the multiplication table of n using for loop in reversed order.

n = int (input ("Enter a number: "))

for i in range (11, 1, -1):
    i = i-1
    t = n*i
    print(n, "X",i, "=" ,t)