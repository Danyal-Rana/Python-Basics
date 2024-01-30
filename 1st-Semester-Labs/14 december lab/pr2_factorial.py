n = int(input("Enter a number: "))


if n == 0:
    print("The factorial of Zero is: 1.")
elif n<0:
    print("The factorial of negative number is not posible.")
else:
    f = 1
    i = 1
    for i in range(1, n+1):
        f = f*i
    print ("The factorial of entered number",n, "is:", f)