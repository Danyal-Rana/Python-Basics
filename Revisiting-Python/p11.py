# functions 

def myFunction (fName):
    print (f"My name is {fName}")


def myFunction2 (fName):
    print (f"My name is {fName}")


myFunction ("Danyal")
myFunction2 (fName= "Danyal Rana", lName="Dani")

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")