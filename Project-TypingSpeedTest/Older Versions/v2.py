from time import time
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


sample_texts = ["a quick brown fox jumps over the lazy dog.", "the five boxing wizards jump quickly.", "pack my box with five dozen liquor jugs."]

text = random.choice(sample_texts)
default_characters = sum(len(characters) for characters in text)

print ("\n ***Typing Speed Test*** \n")

print (text)

print (" \nType the given sentence and Press Enter when you're done \n ")


start_time = time()
user_input = input("Start Typing: ")
end_time = time()

speed_and_time (text, user_input, start_time, end_time)
mistakes (text, user_input, default_characters)
checking_accuracy (errors, default_characters)

print (f"Your typing speed is {wpmSpeed} (wpm).")
print (f"Your typing speed is {cpmSpeed} (cpm).")
print (f"You made {errors} errors while typing {input_characters} characters out of {default_characters} characters.")
print (f"Your Typing accuracy is {accuracy}%.")

if highest_wpm <= wpmSpeed:
    print (f"Congrats, You set new highest speed of {wpmSpeed} wpm.")
    highest_wpm = wpmSpeed
else:
    pass