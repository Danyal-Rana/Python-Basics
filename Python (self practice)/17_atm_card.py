n = input("Enter the four digit number: ")
x = int(n)
sum = 0

for i in range (4):
    r = x%10
    sum += r
    x = (x//10)

if sum%2==0:
    new_n = n + "0"
    
elif sum%2!=0:
    new_n = n + "1"

print (f"The entered number is {n}")
print (f"The generated number is {new_n}")