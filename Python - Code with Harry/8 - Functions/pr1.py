def greater_number(n1, n2, n3):
    if n1==n2 or n2==n3 or n1==n3:
        print ("Kindly enter the three different numbers.")
    elif n1>n2 and n1>n3:
        print (f"First number ({n1}) is the greatest among the three entered numbers.")
    elif n2>n1 and n2>n3:
        print (f"Second number ({n2}) is the greatest among the three entered numbers.")
    else:
        print (f"Third number ({n3}) is the greatest among the three entered numbers.")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

greater_number(n1, n2, n3)