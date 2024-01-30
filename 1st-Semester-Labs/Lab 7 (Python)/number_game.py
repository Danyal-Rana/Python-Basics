num = 14

x = int(input("Enter any number: "))

if (x == num):
    print("You guessed the correct number, Congrats")

elif (x > num):
    print("The entered number is greater, Try a smaller one.")

elif (x < num):
    print("The entered number is smaller, Try a greater one.")

    x = int(input("Enter any number (second attempt): "))

    if (x == num):
        print("You guessed the correct number, Congrats")

    elif (x > num):
        print("The entered number is greater, Try a smaller one.")

    elif (x < num):
        print("The entered number is smaller, Try a greater one.")

        x = int(input("Enter any number (third attempt): "))

        if (x == num):
            print("You guessed the correct number, Congrats")

        elif (x > num):
            print("The entered number is greater, Try a smaller one.")

        elif (x < num):
            print("The entered number is smaller, Try a greater one.")
