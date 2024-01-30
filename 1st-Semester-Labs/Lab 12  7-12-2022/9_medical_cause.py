c = int(input("Number of classes held: "))
a = int(input("Number of classes attended: "))
z = int((a/c)*100)
z1 = str(z)
print ("Your attendence percentage is: " +z1+ " %")
if (z<75):
    e = str(input("Is there any medical cause ? (Print 'Y' for yes or 'N' for no): "))
    if (e=='Y'):
        print ("You are allowed to sit in exam.")
    else:
        print ("You are not allowed to sit in exam !")
else:
    print ("You are allowed to sit in exam.")