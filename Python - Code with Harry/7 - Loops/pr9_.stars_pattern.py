n = int(input("Enter a number: "))
n2 = int((n+1)/2)

for i in range(n):
    star1 = ("*" * n)
    star2 = ("* " * n2)
    if (i%2==0):
        print (star1)
    elif (i%2!=0):
        print (star2)