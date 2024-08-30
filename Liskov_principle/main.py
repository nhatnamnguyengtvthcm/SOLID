


from rectangle import Rectangle
from square import Square


def main():
    rectangle = Rectangle(10, 20)
    print("Area of rectangle:", rectangle.get_area())
    square = Square(10)
    print("Area of square:", square.get_area())
    # use_rectangle(rectangle)
    use_rectangle(square)

    

def use_rectangle(rectangle):
    rectangle.set_height(20)
    rectangle.set_width(30)
   
    assert rectangle.get_height() == 20, "Height is not equal 20"

    # assert rectangle.get_width() == 30, "Width is not equal 30"
  
if __name__ == "__main__":
    main()