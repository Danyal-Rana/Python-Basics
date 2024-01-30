# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.

def game ():
    return 684

score = game()

with open("hi_score.txt") as f:
    hi_score = f.read()


if hi_score=='':
    with open("hi_score.txt", "w") as f:
        f.write(str(score))


elif score>int(hi_score) :
    with open("hi_score.txt", "w") as f:
        f.write(str(score))