n = int(input("Enter a number: "))

for i in range (n, 0, -1):
    print("*" * i)

num = str(n)
for j in range(0, n):
        print(num + num*j)