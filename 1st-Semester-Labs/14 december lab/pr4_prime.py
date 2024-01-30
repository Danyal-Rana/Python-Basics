n = int (input("Enter a number: "))

prime = True

if n==0:
    print("Zero is neither a prime number nor a composite number")

elif n==1:
    print("1 is not a prime number.")

elif n>0:
    for i in range (2, n):
        if (n%i==0):
            prime = False
            break

if prime:
    print ("The entered number is a Prime number.")
else:
    print ("The entered number is NOT a Prime number.")