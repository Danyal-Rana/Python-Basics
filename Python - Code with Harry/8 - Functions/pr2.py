c = float(input("Enter the temperature in Celsius: "))

def temp(d):
    farenheit = (c*1.8)+32
    farenheit = float(farenheit)
    print("The entered temperature is %.2f" % farenheit ,"in Farenheit.")

temp(c)