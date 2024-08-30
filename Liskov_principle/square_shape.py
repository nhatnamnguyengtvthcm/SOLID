


from shape import Shape
from rectangle import Rectangle


class Square(Shape):

    def __init__(self, side):
       self.side = side


    def set_side(self, side):
        self.side = side

    def get_side(self):
        return self.side

    def get_area(self):
        return self.side * self.side
    