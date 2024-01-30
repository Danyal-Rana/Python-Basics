class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of the entered number ({num}) is: {num**2}")

    def cube(self):
        print(f"The cube of the entered number ({num}) is: {num**3}")

    def squareRoot(self):
        print(f"The squareRoot of the entered number ({num}) is: {num**0.5}")


op = int(input("Press 1 for square or Press 2 for cube or press 3 for square root: "))

if 1 <= op <= 3:
    pass
else:
    print("You entered the wrong command :)")

num = int(input("Enter a number: "))

a = Calculator(num)

if op == 1:
    a.square()
elif op == 2:
    a.cube()
elif op == 3:
    a.squareRoot()
