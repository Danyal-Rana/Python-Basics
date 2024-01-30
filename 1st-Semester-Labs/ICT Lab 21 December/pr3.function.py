def header():
    print ("\n This is the header \n")

def com(n1, n2):
    if n1==n2:
        print (f"Both numbers are equal.")
    elif n1>n2:
        print (f"First number {n1} is greater than second number {n2}.")
    elif n2>n1:
        print (f"Second number {n2} is greater than first number {n1}.")

def footer():
    print ("\n This is the footer \n")

header()

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

com (n1, n2)

footer()