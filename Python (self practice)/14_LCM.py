n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

def checking_lcm (n1, n2):
    if n1>n2:
        greater = n1
    else:
        greater = n2

    while(True):
        if (greater % n1 == 0 ) and (greater % n2 == 0):
            lcm = greater
            break
        greater += 1
    return lcm

print (f"The L.C.M of {n1} and {n2} is ",checking_lcm(n1 , n2))