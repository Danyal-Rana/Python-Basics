class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mymethod(self):
        print (f"Hello, my name is {self.name} and I'm {self.age} years old.")

p = Person("Danyal", 20)
p.mymethod()