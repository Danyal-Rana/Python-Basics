total_balls = int(10)

y = int(input("Enter the size of red ball: "))

red = 0
blue = 0
green = 0
others = 0

for i in range(1, total_balls+1):
    size = int(input(f"Enter the size of {i} ball: "))
    if size == y:
        red += 1
    elif size == 2*y:
        blue += 1
    elif size == 3*y:
        green += 1
    else:
        others += 1

print (f"You have total {red} red balls, {blue} blue balls ,{green} green balls and {others} other colored balls.")