# if-elif ladder

a = int (input("Enter first number: "))
b = int (input("Enter second number: "))

if (a>b):
    print ("a is greater than b")
elif (b>a):
    print ("b is greater than a")
else:
    print ("Both a and b are equal")

print ("a is greater than b") if a>b else print("b is greater than a") if b>a else print("Both are equal")

if a>b or b>a:
    pass