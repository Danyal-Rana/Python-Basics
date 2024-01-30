import random

comp = random.randint(1, 3)
if comp == 1:
    comp = 'snake'
elif comp == 2:
    comp = 'water'
elif comp == 3:
    comp = 'gun'
else:
    print ("You entered the wrongs command :) ")

user = input ("Enter snake or water or gun:  " )

def swg(comp, gun):
    if comp == user:
        print (f"Game is Tie, as both entered same command.")
    elif comp == 'snake':
        if user == 'water':
            print ("You loss, Computer wins.")
        elif user == 'gun':
            print ("Congrats, You Win.")
    elif comp == 'water':
        if user == 'snake':
            print ("Congrats, You Win.")
        elif user == 'gun':
            print ("Draw")
    elif comp == 'gun':
        if user == 'water':
            print ("Draw")
        elif user == 'snake':
            print ("You loss, Computer wins.")

print (f"Computer entered: {comp}")
print (f"You entered: {user}.")
swg (comp, user)