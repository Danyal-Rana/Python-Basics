n1 = int(input("Enter the first integar: "))
n2 = int(input("Enter the second integar: "))

def hcf(n1, n2):
    if n1>n2:
        smaller = n2
    else:
        smaller = n1
    for i in range (1, smaller+1):
        if (n1%i==0) and (n2%i==0):
            global HCF
            HCF = i
    return HCF

hcf (n1, n2)

print (f"The HCF of {n1} and {n2} is {HCF}.")