n = int(input("Enter a number:"))

for i in range(n):
    space = (" " * (n-i-1))
    star = ("*" * (2*i+1))
    print (space, end="")
    print (star, end="")
    print (space)