def header():
    print ("\n This is the header \n")

def eo (n):
    if n%2==0:
        print ("The entered number is Even")
    else:
        print ("The entered number is Odd")

def footer():
    print ("\n This is the footer \n")

header()

n = int(input("Enter a number: "))

eo(n)

footer()