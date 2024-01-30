m1 = int(input("Enter the marks of subject 1 (Out of 100): "))
m2 = int(input("Enter the marks of subject 2 (Out of 100): "))
m3 = int(input("Enter the marks of subject 3 (Out of 100): "))

if (m1<33 or m2<33 or m3<33):
    print("You are fail because of low marks in subjects.")

elif (m1+m2+m3)/3 < 40:
    print ("You are fail becuase of less total.")

else:
    ("Congrats! You are Pass.")