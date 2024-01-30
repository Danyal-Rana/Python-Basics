class Programmer:
    company = "Microsoft"
    def __init__(self, name, role, product):
        self.name = name
        self.role = role
        self.product = product
    def getinfo (self):
        print (f"The name of Programmer is {self.name}, the role is {self.role} and the product on which he is working is {self.product}.")

danyal = Programmer("Danyal", 'Junior Developer', 'VS-Code')
zubair = Programmer("Zubair", 'Senior Developer', 'Outlook')
danyal.getinfo()
zubair.getinfo()