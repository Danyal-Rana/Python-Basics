import random

num = random.randint(100, 999)
x = num

user_num = int(input("Enter a three digit number: "))
y = user_num

if num == user_num:
    print ("$10,000")

numDigit1 = num%10
num = num//10
numDigit2 = num%10
num = num//10
numDigit3 = num%10

user_numDigit1 = user_num%10
user_num = user_num//10
user_numDigit2 = user_num%10
user_num = user_num//10
user_numDigit3 = user_num%10

if (numDigit1 == user_numDigit1 or numDigit1 == user_numDigit2 or numDigit1 == user_numDigit3) and (numDigit2 == user_numDigit1 or numDigit2 == user_numDigit2 or numDigit2 == user_numDigit3) and (numDigit3 == user_numDigit1 or numDigit3 == user_numDigit2 or numDigit3 == user_numDigit3):
    print ("$3000")

elif (numDigit1 == user_numDigit1 or numDigit1 == user_numDigit2 or numDigit1 == user_numDigit3) or (numDigit2 == user_numDigit1 or numDigit2 == user_numDigit2 or numDigit2 == user_numDigit3) or (numDigit3 == user_numDigit1 or numDigit3 == user_numDigit2 or numDigit3 == user_numDigit3):
    print ("$1000")

print (x)
print (y)