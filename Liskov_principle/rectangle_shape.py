from shape import Shape


class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height
    
