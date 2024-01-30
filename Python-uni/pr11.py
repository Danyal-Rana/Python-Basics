n = int(input("Enter the number between 0-1000: "))

sum = 0

while n>0:
    r = n%10
    sum += r
    n = n//10

print ("The sum of digits of entered integar is:", sum)