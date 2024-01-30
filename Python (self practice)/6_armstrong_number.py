n = int(input("Enter a 3 digit number to check whether it is an armstrong number or not: "))

s = 0
d = n

while d > 0:
    r = d%10
    s = s + r**3
    d = d//10

if n == s:
    print (f"The entered number {n} is an Armstrong number.")
else:
    print (f"The entered number {n} is NOT an armstrong number.")