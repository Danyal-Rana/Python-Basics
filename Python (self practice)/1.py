n = int(input("Enter the number: "))

for i in range (1, (n*3)+1):
    if i<=n:
        print ("*"*i)
    elif i<=2*n:
        print (" "*n, end="")
        print ("*"*i)
    elif i<=3*n:
        print (" "*(3*n), end="")
        print ("*"*i)