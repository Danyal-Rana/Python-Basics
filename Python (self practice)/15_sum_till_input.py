n = int(input("Enter the number till which you want the sum: "))
sum = 0

for i in range (1, n+1):
    num = ("1" * i)
    num = int(num)
    sum = sum + num

print (sum)