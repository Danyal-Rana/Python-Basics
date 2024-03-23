# while loop

i = 0

while i < 10:
    print(f"The value of i is: {i}")
    i += 1
    if i == 5:
        print ("Here the value of i is 5")
        continue
else:
    print ("i is no longer less than 10")