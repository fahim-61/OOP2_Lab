class Shape:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def perimeter(self):
        return 2 * (self.length + self.width)

class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self,"Rectangle")
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width


Rec1 = Rectangle(20.34, 10.20)

print(Rec1.area())
print(Rec1.perimeter())
print(Rec1.get_name())