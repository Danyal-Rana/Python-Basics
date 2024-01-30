a1 = int(input("Enter the first angle of Triangle: "))
a2 = int(input("Enter the Second angle of Triangle: "))
a3 = int(input("Enter the third angle of Triangle: "))

sum = a1+a2+a3

if sum==180:
    if a1==a2==a3:
        print ("It is a Equilateral Triangle")
    elif a1==a2 or a1==a3 or a2==a3:
        print ("It is a Isoscels Triangle")
    elif a1==90 or a2==90 or a3==90:
        print ("It is a Right-angle Triangle")
    elif a1!=a2 and a1!=a3 and a2!=a3:
        print ("It is a Scalene Triangle")
else:
    print ("Kindly enter the valid angles :)")