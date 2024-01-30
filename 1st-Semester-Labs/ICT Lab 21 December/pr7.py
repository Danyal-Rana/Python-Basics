n = int (input("Enter a number: "))

n1 = str(n)

n2 = len(n1)

i = 0

while i < n2:
    r = n%10
    print (r, end="")
    n = n//10
    i += 1