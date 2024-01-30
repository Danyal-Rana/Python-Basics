from time import time
from text_samples import *
import random

highest_wpm = 50

test_start = True

while test_start != str(0):

    def speed_and_time(text, user_input, start_time, end_time):
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

    def mistakes(text, user_input, default_characters):
        global errors
        errors = 0
        for i in range(default_characters):
            try:
                if user_input[i] != text[i]:
                    errors = errors + 1
            except:
                errors = errors + 1
        return errors

    def checking_accuracy(errors, default_characters):
        global accuracy
        errors_percentage = round((errors/default_characters)*100)
        accuracy = 100 - errors_percentage
        return accuracy

    print("\n ***Typing Speed Test*** \n")

    t = input("Enter the category of sentence you want to type. \nPress 1 to get easy sentences (only lowercase alphabets) or \nPress 2 to get Medium sentences (Lowercase and Uppercase sentences with basic Punctuation) or\nPress 3 to get Hard sentences (including Numbers and Punctuation marks along with Alphabets) or\nPress 4 to enter your own custom text : ")

    if t == '1':
        text = random.choice(easy)
    elif t == '2':
        text = random.choice(medium)
    elif t == '3':
        text = random.choice(hard)
    elif t =='4':
        text = input("\nEnter your own text: ")
    else:
        print(
            "\nYou entered the wrong command, therefore you have to Type Hard sentences :)")
        text = random.choice(hard)
    default_characters = sum(len(characters) for characters in text)

    print(" \nType the given sentence and Press Enter when you're done \n ")

    print(f"Sentence is = {text} \n")

    start_time = time()
    user_input = input("Start Typing: ")
    end_time = time()

    speed_and_time(text, user_input, start_time, end_time)
    mistakes(text, user_input, default_characters)
    checking_accuracy(errors, default_characters)

    print(f"\nYour typing speed is {wpmSpeed} WPM.\n")
    print(f"Your typing speed is {cpmSpeed} CPM.\n")
    print(
        f"You made {errors} errors while typing {input_characters} characters out of {default_characters} characters.\n")
    print(f"Your Typing accuracy is {accuracy}%.\n")

    if highest_wpm < wpmSpeed and accuracy>90:
        print(f"Congrats, You set new highest speed of {wpmSpeed} WPM.\n")
        highest_wpm = wpmSpeed
    else:
        pass

    def typist(wpmSpeed):
        if wpmSpeed < 40:
            print("Your typing speed is below average. You should learn proper typing techniques and practice more to improve your speed :) \n")
        elif wpmSpeed >= 40 and wpmSpeed < 50 and accuracy >=90:
            print(
                "You are an average typist, you still have significant room to improve :) \n")
        elif 50 <= wpmSpeed <= 70 and accuracy >=92 :
            print("Your typing speed is above average. Keep Practicing :) \n")
        elif 70 < wpmSpeed < 100 and accuracy >=95:
            print(
                "Great! You are typing at productive speed. This is the speed required for most jobs :) \n")
        elif wpmSpeed >= 100 and accuracy >=98 :
            print("Awesome! You're typing at the competitive speed :) \n")
        else:
            print ("You have to focus on Accuracy.\n")

    typist(wpmSpeed)

    test_start = input("Are you ready to start new test? (Enter any key to start or 0 to exit ---> ")

print ("\nThank You for Being Here.\n")