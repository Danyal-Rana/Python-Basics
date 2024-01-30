# Write a dummy authentication system program in which you accept user inputs for email and password. 
# Let's say the correct email and password are abc@gmail.com and abc respectively.
# If the email and password entered are correct it should display "user is logged in"
# if the email is incorrect then prompt the user that the password is not correct.
# If the password is correct then prompt the user to enter the 
# correct email. If both are incorrect then display the corresponding message

email = input ("Enter the email: ")

password = input("Enter the password: ")

if email=="abc@gmail.com" and password == "abc":
    print ("User is logged in.")
elif email=="abc@gmail.com" and password != "abc":
    print ("Password is incorrect")
elif email!="abc@gmail.com" and password == "abc":
    print ("Email is incorrect")
else:
    print ("Both are incorrect")