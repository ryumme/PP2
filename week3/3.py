class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def func(self):
        print("Hello " + self.name)

p2 = Person("John", 36)
p2.func()
print(p2.name)
print(p2.age)

del p2.age
del p2