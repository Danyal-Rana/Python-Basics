for i in range (2, 100):
    for j in range (2, i):
        if (i%j==0):
            break
    else:
        for k in range (2, i-3):
            if (i-2)%k==0:
                break
        else:
            print (f"{i-2} and {i}")