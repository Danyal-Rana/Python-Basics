# Write a program to find whether a given number is prime or not.

n = int(input("Enter a number: "))

prime = True

for i in range (2, n):
    if (n%i==0):
        prime = False
        break

if prime:
    print ("The entered number is a Prime number.")
else:
    print ("The entered number is not a Prime number.")