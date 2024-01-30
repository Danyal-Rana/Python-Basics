from time import time
import random

def speed_and_time (text, user_input, start_time, end_time):
    time_consumed = end_time - start_time
    minutes = time_consumed / 60
    global chars
    chars = sum(len(item) for item in text)
    words = chars / 5
    global wpmSpeed
    wpmSpeed = round(words / minutes)
    global cpmSpeed
    cpmSpeed = round(chars / minutes)
    return wpmSpeed and cpmSpeed and chars

def mistakes (text, user_input):
    for i in range(sum(len(item) for item in text)):
        global errors
        errors = 0
        if text[i] != user_input[i]:
            errors = errors + 1
        else:
            errors = 0
    return errors

def checking_accuracy (errors, chars):
    global accuracy
    errors_percentage = round((errors/chars)*100)
    accuracy = 100 - errors_percentage
    return accuracy


sample_texts = ["a quick brown fox jumps over the lazy dog.", "the five boxing wizards jump quickly.", "pack my box with five dozen liquor jugs."]

text = random.choice(sample_texts)

print ("\n ***Typing Speed Test*** \n")

print (text)

print (" \nType the given sentence and Press Enter when you're done \n ")


start_time = time()
user_input = input("Start Typing: ")
end_time = time()

speed_and_time (text, user_input, start_time, end_time)
mistakes (text, user_input)
checking_accuracy (errors, chars)

print (f"Your typing speed is {wpmSpeed} (wpm).")
print (f"Your typing speed is {cpmSpeed} (cpm).")
print (f"You made {errors} errors.")
print (f"Your Typing accuracy is {accuracy}%.")