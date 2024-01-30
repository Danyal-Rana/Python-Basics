a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a>b and a>c):
    print ("First number is greater i:e (", +a, ")")

elif (b>a and b>c):
    print ("Second number is greater i:e (", +b, ")")

elif (c>a and c>b):
    print ("Third number is greater i:e (", +c, ")")

else:
    print ("Any of the two entered numbers are equal.")