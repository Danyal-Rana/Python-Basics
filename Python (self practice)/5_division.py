n = int(input("Enter the number: "))

count = 0
for i in range (1, n+1):
    if n%i==0:
        print (i, end=", ")
        count += 1

print (f"\nThe entered number {n} is divisble by {count} numbers.")