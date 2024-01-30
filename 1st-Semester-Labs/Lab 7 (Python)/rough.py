num = 15

x = int(input("Enter any number: "))

if (x == num):
    print ("You guessed the correct number, Congrats! ")

elif (x > num):
        print ("You entered a greater number, try with a smaller one. ")

elif (x < num):
    print ("You entered a smaller number, try with a greater one. ")

    y = int (input("Enter the number second time: "))

    if (y == num):
        print("You guessed the correct number, Congrats! ")

    elif (y > num):
        print ("You entered a greater number, try with samller one. ")

    elif (y < num):
        print ("You entered a smaller number, try with a greater one. ")

        z = int (input("Enter the number last time: "))

        if  (z == num):
            print ("You gussed the right number, Congrats! ")

        elif (z > num):
            print ("You entered a greater number")

        elif (z < num):
            print("You entered the smaller number.")