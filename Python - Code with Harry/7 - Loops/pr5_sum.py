# Write a program to find the sum of first n natural numbers using a while loop.

n = int(input("Enter the number: "))

sum = 0

i = 0
while i<n+1:
    sum = sum + i
    i += 1

# for i in range (0, n+1):
#     sum = sum + i

print ("The sum is:",sum)