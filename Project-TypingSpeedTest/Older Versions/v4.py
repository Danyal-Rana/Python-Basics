from time import time
from text_samples import *
import random

highest_wpm = 50

def speed_and_time (text, user_input, start_time, end_time):
    time_consumed = end_time - start_time
    minutes = time_consumed / 60
    global input_characters
    input_characters = sum(len(characters) for characters in user_input)
    words = input_characters / 5
    global wpmSpeed
    wpmSpeed = round(words / minutes)
    global cpmSpeed
    cpmSpeed = round(input_characters / minutes)
    return wpmSpeed and cpmSpeed and input_characters

def mistakes (text, user_input, default_characters):
    global errors
    errors = 0
    for i in range(default_characters):
        try:
            if user_input[i] != text[i]:
                errors = errors + 1
        except:
            errors = errors + 1
    return errors

def checking_accuracy (errors, default_characters):
    global accuracy
    errors_percentage = round((errors/default_characters)*100)
    accuracy = 100 - errors_percentage
    return accuracy

print ("\n ***Typing Speed Test*** \n")

t = input("Enter the category of sentence you want to type. \nPress 1 to get easy sentences (only lowercase alphabets) or \nPress 2 to get Medium sentences (Lowercase and Uppercase sentences with basic Punctuation) or\nPress 3 to get Hard sentences (including Numbers and Punctuation marks along with Alphabets) : ")

if t=='1':
    text = random.choice(easy)
elif t=='2':
    text = random.choice(medium)
elif t=='3':
    text = random.choice(hard)
else:
    print ("\nYou entered the wrong command, therefore you have to Type Hard sentences :)")
    text = random.choice(hard)
default_characters = sum(len(characters) for characters in text)

print (" \nType the given sentence and Press Enter when you're done \n ")

print (f"Sentence is = {text} \n")


start_time = time()
user_input = input("Start Typing: ")
end_time = time()

speed_and_time (text, user_input, start_time, end_time)
mistakes (text, user_input, default_characters)
checking_accuracy (errors, default_characters)

print (f"\nYour typing speed is {wpmSpeed} (wpm).\n")
print (f"Your typing speed is {cpmSpeed} (cpm).\n")
print (f"You made {errors} errors while typing {input_characters} characters out of {default_characters} characters.\n")
print (f"Your Typing accuracy is {accuracy}%.\n")

if highest_wpm <= wpmSpeed:
    print (f"Congrats, You set new highest speed of {wpmSpeed} wpm.\n")
    highest_wpm = wpmSpeed
else:
    pass

def typist(wpmSpeed):
    if wpmSpeed < 40:
        print ("Your typing speed is below average. You should learn proper typing techniques and practice more to improve your speed :) \n")
    elif wpmSpeed < 50:
        print ("You are an average typist, you still have significant room to improve :)")
    elif wpmSpeed < 70:
        print ("Your typing speed is above average. Keep Practicing :) \n")
    elif wpmSpeed < 100:
        print ("Great! You are typing at productive speed. This is the speed required for most jobs :) \n")
    elif wpmSpeed > 100:
        print ("Awesome! You're typing at the compeitive speed :) \n")

typist(wpmSpeed)