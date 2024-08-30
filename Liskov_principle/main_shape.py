


from shape import Shape
from rectangle_shape import Rectangle
from square_shape import Square


def main():
    rectangle = Rectangle(10, 20)
    print("Area of rectangle:", rectangle.get_area())
    square = Square(10)
    print("Area of square:", square.get_area())
    use_rectangle(rectangle)
    # use_rectangle(square)
    use_square(square)
    

def use_rectangle(rectangle: Rectangle):
    rectangle.set_height(20)
    rectangle.set_width(30)
   
    assert rectangle.get_height() == 20, "Height is not equal 20"

    assert rectangle.get_width() == 30, "Width is not equal 30"
  
def use_square(square: Square): 
    square.set_side(20)
    assert square.get_side() == 20, "Side is not equal 20"

if __name__ == "__main__":
    main()