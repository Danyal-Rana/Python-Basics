n = int(input("Enter the number of studensts: "))

highest_score = 0
second_highest_score = 0
third_highest_score = 0

for i in range (n):
    m = int(input(f"Enter the marks of Student {i+1}: "))
    if m > highest_score:
        third_highest_score = second_highest_score
        second_highest_score = highest_score
        highest_score = m

print (f"The third highest grades are {third_highest_score}")
print (f"The second highest grades are {second_highest_score}")
print (f"The Highest grades are {highest_score}")