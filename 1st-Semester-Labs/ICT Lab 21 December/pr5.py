n = int(input("Enter a number: "))

n1 = str(n)

n2 = len(n1)

sum = 0

for i in range (1, n2+1):
    r = n%10
    sum = sum + r
    n = n//10
print (sum)