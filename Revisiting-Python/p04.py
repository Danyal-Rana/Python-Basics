x = "awesome"

def myFun ():
    x = "fantastic"

    global y 
    y = "global"
    print ("Python is " + x)
    print ("Pyton is " + y , "\n")

myFun()

print ("Python is " + x)
print ("Python is " + y)