# all prime numbers in between n1 and n2

n1 = int (input("Enter first number: "))
n2 = int (input("Enter second number: "))

for num in range (n1, n2+1):
    for i in range (2, num):
        if num%i == 0:
            break;
    else:
        print (num)