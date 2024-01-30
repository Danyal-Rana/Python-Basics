x = int(input("Enter the quantity you want to purchase: "))
p = x*100
p1 = str (p)
d = 0.1
dx = p*d
c = p-dx
c1 = str(c)
if (x>1000):
    print("The total cost is: " + c1)
else:
    print ("You are not eligible for discount. \n The total cost is: " +p1)