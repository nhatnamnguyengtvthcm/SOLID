


from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    
    def set_width(self, width):
        return self.set_side(width)

    
    def set_height(self, height):
        return self.set_side(height)

    