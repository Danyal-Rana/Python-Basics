n = input("Enter a four digit number: ")

if n.isdigit and len(n) == 4:

    reversed_n = n[::-1]
    print ("The reversed number is: ", reversed_n)

else:
    print ("Invalid input, Kindly enter a four digit integar:)")