n1 = int(input("Enter the first number of interval: "))
n2 = int(input("Enter the second number of interval: "))

for i in range (n1+1, n2):
    for j in range (2, i):
            if i%j==0:
                break
    else:
        print (i)