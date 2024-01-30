import math

print (f"Degree     Sin         Cos")

for i in range (0, 361, 10):
    j = round(math.sin(math.radians(i)), 4)
    k = round(math.cos(math.radians(i)), 4)

    print (f"{i}        {j}         {k}")