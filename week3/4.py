class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Naruto", "Uzumaki")
x.printname()

class child(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, self.gradyear)

y = child("Boruto", "Uzumaki", 2023)
y.welcome()
