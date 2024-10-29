class Shape:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def perimeter(self):
        return 2 * (self._length + self._width)
    def __display_shape_type(self):
        print(f"This is a shape of type: {self._name}")
    def display_shape_type(self):
        self.__display_shape_type()

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width

# Create an instance of Rectangle
Rec1 = Rectangle(20.34, 10.20)

print("Length:", Rec1.get_length())
print("Width:", Rec1.get_width())


print(Rec1.get_name())
print("Area:", Rec1.area())
print("Perimeter:", Rec1.perimeter())
Rec1.display_shape_type()
