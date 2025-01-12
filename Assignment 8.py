class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

class Rectangle(Quadrilateral):
    def __init__(self, length, breadth):
        super().__init__(length, breadth, length, breadth)

    def area(self):
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.a * self.a


length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
rect = Rectangle(length, breadth)
print("Rectangle perimeter:", rect.perimeter())
print("Rectangle area:", rect.area())


side = float(input("\nEnter the side of the square: "))
sq = Square(side)
print("Square perimeter:", sq.perimeter())
print("Square area:", sq.area())
