n = int(input("How many number do you want to get in order? "))

list1 = []

for i in range(n):
    num = int(input("Enter the number: "))
    thislist = [num]
    list1.extend (thislist)

list1.sort()
print ("The ascending order of the entered numbers, is: " ,list1)

list1.sort (reverse = True)
print ("The descending order of the entered numbers, is: " ,list1)