n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

for i in range (n1+1, n2):
    d = i
    global s
    s = 0
    while d > 0:
        r = d%10
        s += r**3
        d //= 10
    if s == i:
        print(f"{i} is an Armstrong number.")
    else:
        pass
