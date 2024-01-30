n1 = int(input("Enter the marks of Physics (over100): "))
n2 = int(input("Enter the marks of Chemistry (over100): "))
n3 = int(input("Enter the marks of Biology (over100): "))
n4 = int(input("Enter the marks of Math (over100): "))
n5 = int(input("Enter the marks of Computer (over100): "))

mylist = [n1, n2, n3, n4, n5]

percentage = (sum(mylist)/500)*100

if percentage >= 90 :
    print ("Your Grade is A")
elif percentage >= 80 :
    print ("Your Grade is B")
elif percentage >= 70 :
    print ("Your Grade is C")
elif percentage >= 60 :
    print ("Your Grade is D")
elif percentage >= 40 :
    print ("Your Grade is E")
elif percentage < 40 :
    print ("Your Grade is F")
else:
    print ("Kindly enter the Valid marks :)")