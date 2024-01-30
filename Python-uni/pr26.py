# Write a program that displays, ten numbers per line, all the numbers from 100 to 200 that are 
# divisible by 5 or 6, but not both. The numbers are separated by exactly one space.

number_per_line = 0
j = 1

for i in range (100, 201):
    if (i%5==0 or i%6==0) and not (i%5==0 and i%6==0):
        print(i , end=" ")
        number_per_line += 1
        if number_per_line == j*10:
            print ()
            j += 1