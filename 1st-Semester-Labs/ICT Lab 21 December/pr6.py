n = int(input("Enter a number: "))

n1 = str(n)

n2 = len(n1)

p = 1

for i in range (1, n2+1):
    r = n%10
    p = p * r
    n = n//10
print (p)