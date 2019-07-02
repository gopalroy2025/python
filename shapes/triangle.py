"""
Implementation of a triangle class
"""
from shapes.shape import Shape


class Triangle(Shape):
    
    def __init__ (self,height , base, sideA, sideB):
        """
            Initialize the triangle.
        """
        self.base = base
        self.height = height
        self.sideA = sideA
        self.sideB = sideB
    def area(self):
        """
            Calculating the area of a triangle.
        """
        return (self.height * self.base)/2
    def perimeter(self):
        """
            Calculating the perimeter of a triangle.
        """
        return self.base + self.sideA + self.sideB

    def righttriangle(self):
        """
            Verify whether the triangle is a right triangle.
        """
        sides = [self.base ** 2, self.sideA ** 2, self.sideB ** 2]
        sides.sort()
        longest_side = sides.pop()
        return longest_side == sides[0] + sides[1]
            

#triangle = Triangle(2,3,4,5)
#print(triangle.area())
#print(triangle.righttriangle())
#print(triangle.perimeter())
