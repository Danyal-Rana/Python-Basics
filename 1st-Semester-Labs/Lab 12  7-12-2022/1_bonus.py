s = int(input("Enter your salary: "))
b = (s/100)*5
pay = s + b
y = int(input("Enter your years of service: "))
if (y>5):
    pay = str(pay)
    print ("Your net bonus amount is: " + pay)
else:
    print ("You are not eligible for bonus")