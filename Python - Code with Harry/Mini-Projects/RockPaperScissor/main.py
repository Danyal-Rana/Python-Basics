import random

comp = random.randint(1, 3)
if comp == 1:
    comp = 'rock'
elif comp == 2:
    comp = 'papar'
elif comp == 3:
    comp = 'scissor'
else:
    print ("You entered the wrongs command :) ")

user = input ("Enter rock or papar or scissor:  " )

def swg(comp, user):
    if comp == user:
        print (f"Game is Tie, as both entered same command.")
    elif comp == 'rock':
        if user == 'papar':
            print ("Congrats, You Win.")
        elif user == 'scissor':
            print ("You loss, Computer wins.")
    elif comp == 'papar':
        if user == 'rock':
            print ("You loss, Computer wins.")
        elif user == 'scissor':
            print ("Congrats, You Win.")
    elif comp == 'scissor':
        if user == 'papar':
            print ("You loss, Computer wins.")
        elif user == 'rock':
            print ("Congrats, You Win.")

print (f"Computer entered: {comp}")
print (f"You entered: {user}.")
swg (comp, user)