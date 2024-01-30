def header():
    print ("\n This is the header \n")
def footer():
    print ("\n This is the footer \n")

def greater(n1, n2):
    if n1==n2:
        print ("Both numbers are equal")
    elif n1>n2:
        x = (f"First number {n1} is greater than second number {n2}.")
        return x
    else:
        y = (f"Second number {n2} is greater than first number {n1}.")
        return y

header()

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print (greater (n1, n2))

footer()