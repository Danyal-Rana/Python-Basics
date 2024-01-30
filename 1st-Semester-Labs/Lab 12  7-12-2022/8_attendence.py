c = int(input("Number of classes held: "))
a = int(input("Number of classes attended: "))
z = (a/c)*100

if (z<75):
    print ("You are not allowed to sit in exam.!")
else:
    print ("You are allowed to sit in exam.")