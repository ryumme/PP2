import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx**2 + dy**2)
        return str("Distance: ({})".format(distance))

point1 = Point(3, 4)
point2 = Point(5, 7)

point1.show()
point1.move(2, 1)
point1.show()

distance = point1.dist(point2)

print(distance)