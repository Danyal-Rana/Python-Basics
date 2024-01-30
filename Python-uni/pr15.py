a = int(input("Ener the number to which you want to get the table: "))

b = int(2)

print("i   b     i**b")

for i in range(1, a+1):
    print(f"{i}   {b}     {i**b}")
    b = int(b+1)