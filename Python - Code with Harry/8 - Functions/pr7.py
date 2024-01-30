string = "      Pakistan is our Country. The capital of Pakistan is Islamabad.     "
word = input("Enter the word you want to remove: ")

def rem_strip (string, word):
    string = string.replace(word, "")
    string = string.strip()
    print (string)

rem_strip (string, word)