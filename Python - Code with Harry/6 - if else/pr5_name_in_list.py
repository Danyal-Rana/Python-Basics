namelist = ["ali", "ahmad", "akbar", "aslam", "asghar"]

name = input("Enter a name: ")

if (name in namelist):
    print ("The entered name is present in the list.")

else:
    print ("The entered name is not present in the list.")