# create parent class name as Shape
class shape:
    def draw(self):
        print('Draw a generic Shap')

# create child classes name as circle, square, rectangle
class circle(shape):
    def draw(self):
        print('Drawing a circle shape')
class square(shape):
    def draw(self):
        print('Drawing a squre shape')
class rectangle(shape):
    def draw(self):
        print("Drawing a rectangle shape")

# creating instance of classes (circle, square, rectangle)
Circle = circle()
Square = square()
Rectangle = rectangle()

# calling draw method from parent class to invoke in child class.
Circle.draw()
Square.draw()
Rectangle.draw()