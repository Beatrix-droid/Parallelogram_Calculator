"""this program class will return the area, perimeter and main diagonal length
of any parallelogram inputted by the user, as well as how many times the
area of another shape will fit into the parallelogram."""

import textwrap
import math


class Parallelogram:
    """the Parallelogram class will return the area, perimeter and main diagonal length
    of any parallelogram inputted by the user. It works on rectangles, rhombuses and
    parallelograms in general"""

    @classmethod
    def from_str(cls, str_height, str_width, str_angle):
        height = int(str_height.lstrip("height ="))
        width = int(str_width.lstrip("width ="))
        angle = int(str_angle.lstrip("angle ="))
        return cls(width, height, angle)

    def __init__(self, width, height, angle):
        self.width = width
        self.height = height
        self.angle = angle

    def set_width(self, width):
        """use set_width to set the width of your rectangle"""
        self.width = width

    def set_height(self, height):
        """use set_height  to set the height of your rectangle"""
        self.height = height

    def set_angle(self, angle):
        """use set_angle to set the interior angles of your parallelogram.
        Opposite angles are congruent and a parallelogram's
        interior angles add up to 360 degrees, so only one angle parameter
        is needed for this function)"""
        self.angle = angle

    def get_area(self):
        """use get_area to compute the area of the your quadrilateral"""
        area = self.width * self.height * (round(abs(math.sin(math.radians(self.angle))), 2))
        return area

    def get_perimeter(self):
        """use get_perimeter to compute the perimeter of your quadrilateral"""
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        """use get_diagonal to find the length of the main diagonal of your quadrilateral"""
        if self.angle == 90:
            diagonal = round(((self.width ** 2 + self.height ** 2) ** .5), 5)
            return diagonal
        diagonal_1 = round(((self.width ** 2 + self.height ** 2) - (2 * self.width * self.height  \
        * math.cos(math.radians(self.angle)))) ** .5, 5)
        diagonal_2 = round(((self.width ** 2 + self.height ** 2) + (2 * self.width * self.height  \
        * math.cos(math.radians(self.angle))))  ** .5, 5)
        return "diagonal no. 1 = {}, diagonal no.2 = {}".format(diagonal_1, diagonal_2)

    def __repr__(self):
        """use __repr__ to return information about the values you inputted for your
        quadrilateral"""
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def get_picture(self):
        """use get_picture to get a picture of your parallelogram (only if its sides
        are less than 50 units long"""
        if isinstance(self.width, str):
            return self.repr()
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        elif self.angle != 90:
            return "Parallelograms that are not Rectangles or Squares cannot have pictures"
        else:
            area = (self.width * self.height * "*")
            return textwrap.fill(area, self.width) + "\n"

    def get_amount_inside(self, shape_2):
        """"use get_amount_inside to figure out how many times the area of another shape fits
        inside your quadrilateral"""
        self.shape2 = shape_2
        ratio = self.get_area() // shape_2.get_area()
        if ratio > 0:
            return ratio
        return 0


class Square(Parallelogram):

    """This class is a sublcass of the Parallelogram class. This class is used to perform the
    Parallelogram class's calculations on squares"""

    @classmethod
    def from_str(cls, str_side):
        side = int(str_side.lstrip("side ="))
        return cls(side)

    def __init__(self, side):
        super().__init__(side, side, 90)

    def set_side(self, side):
        """ use set_width to set the side of the square"""
        self.width = side
        self.height = side

    def __repr__(self):
        return "Square(side={})".format(self.width)

    def get_picture(self):
        if isinstance(self.width, str):
            return self.repr()
        if self.width > 50:
            return "Too big for picture."
        area = (self.width ** 2 * "*")
        return textwrap.fill(area, self.width) + "\n"
