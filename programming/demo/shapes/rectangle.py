"""
Cs260: 2022-09-14
Convert c++ class to python

C++ source was found here:
https://raw.githubusercontent.com/bfilin/fl22data/main/demo/shapes/Rectangle.h

execute with: 
    python Rectangle.py

"""

print('Welcome cs260')
print('Convert c++ class to python', end='\n\n')


class Rectangle:

    def __init__(self, new_x = 1, new_y = 1):
        """The constructor of our class."""
        self.x = new_x
        self.y = new_y
        
    def __repr__(self):
        """Define string representation for obj

        When we use print(obj) it will print the
        out string from this method."""
        middle_dash = '---'
        plus = '+'
        pipe = '┆'
        middle_space = '   '
        row = 1
        out = 'Here is the rectangle with x=' + str(self.x) + ' y=' + str(self.y)
        
        out = out + '\n' + plus + middle_dash * self.x + plus + '\n'
        
        while row <= self.y:	
            out = out + pipe + middle_space * self.x + pipe + '\n'
            row += 1
        
        out = out + plus + middle_dash * self.x + plus + '\n'
        return out;
    
    def get_x(self):
        """Return x."""
        return self.x

    def get_y(self):
        """Return y."""
        return self.y

    def set_x(self, new_x):
        """Set a new value for instance variable x."""
        self.x = new_x

    def set_y(self, new_y):
        """Set a new value for instance variable y."""
        self.y = new_y

    def area(self):
        """Calculates and returns the area of the Rectangle."""
        return self.x * self.y

    def perimeter(self):
        """Calculates and returns the perimeter of the Rectangle."""
        return 2 * (self.x + self.y)


r = Rectangle()        # instantiate obj from our class, uses __init__() constructor, uses default arguments x=1, y=1
print(r)               # this makes use of our __repr__() definition 
print('x:', r.get_x()) # check get_x() method
print('y:', r.get_y()) # check get_y() method
r.set_x(10)            # check set_x() method
r.set_y(3)             # check set_y() method
print(r)               # this makes use of our __repr__() definition

# test area and perimeter methods
print('Area:', r.area())
print('Perimeter:', r.perimeter())

r2 = Rectangle(5,10)   # instantiate a new obj from our class, uses __init__() constructor, uses x=5, y=10
print(r2)              # this makes use of our __repr__() definition

