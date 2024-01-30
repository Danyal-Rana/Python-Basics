import random
n1 = int(random.randrange(1, 99))
n2 = int(random.randrange(1, 99))

print(n1)
print(n2)

o = input("What do you want to do? \nEnter '+' to perform addition or \nEnter '-' to perform substraction or \nEnter '*' to perform multiplication or \nEnter '/' to perform division: ")

ans = int(input("Now, enter your answer, so that it can be Verified: "))

if o == "+":
    if ans == n1+n2:
        print("Congrats, Your answer is correct")
    else:
        print("You entered the wrong answer, the correct answer is: ", n1+n2)
elif o == "-":
    if ans == n1-n2:
        print("Congrats, Your answer is correct")
    else:
        print("You entered the wrong answer, the correct answer is: ", n1-n2)
elif o == "*":
    if ans == n1*n2:
        print("Congrats, Your answer is correct")
    else:
        print("You entered the wrong answer, the correct answer is: ", n1*n2)
elif o == "/":
    if ans == n1/n2:
        print("Congrats, Your answer is correct")
    else:
        print("You entered the wrong answer, the correct answer is: ", n1/n2)
else:
    print("You entered the wrong command :)")
