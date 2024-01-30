n = int(input("Enter the number of lines: "))

def pattern (n):
    for i in range (n, 0, -1):
        print("*"*i)

pattern(n)