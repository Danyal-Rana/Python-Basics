import random

operators = ["+", "-", "*", "//"]

j = 0

for i in range (5):
    n1 = (random.randint(1, 99))
    print ("First number is:",n1)
    n2 = (random.randint(1, 99))
    print ("Second number is:",n2)
    op = random.choice(operators)
    print ("You have to perform:",op)
    ans = int(input("Enter your answer: "))
    if op=="+":
        if ans == n1+n2:
            j = j+1
            print ("Correct")
        else:
            print ("Wrong, the right answer is",n1+n2)
    elif op=="-":
        if ans == n1-n2:
            j = j+1
            print ("Correct")
        else:
            print ("Wrong, the right answer is",n1-n2)
    elif op=="*":
        if ans == n1*n2:
            j = j+1
            print ("Correct")
        else:
            print ("Wrong, the right answer is",n1*n2)
    elif op=="//":
        if ans == n1//n2:
            j = j+1
            print ("Correct")
        else:
            print ("Wrong, the right answer is",n1//n2)

print (f"You scored {j} out of 5")