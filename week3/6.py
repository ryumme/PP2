class Shape:
    def __init__(self):
        pass
    def area(self):
        return self.length * self.length

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length
    
x = Square(4)
print(x.area())