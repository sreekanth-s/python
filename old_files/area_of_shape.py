import math
pi = math.pi


def menu():

    print(""" Select the appropriate number against which shape you want to calculate the area.""")
    print("""
    1. Circle
    2. Rectangle
    3. Triangle
    4. Square
    """)


def area_of_shape(shape):
    """Returns the area of respective shape you pass"""

    menu()

    shape=int(input("Enter the number: "))

    if shape < 1 or shape > 4:
        print("Enter a valid number.")
        area_of_shape(shape)

    elif shape == 1:
        radius = int(input("Enter the radius of the circle: "))
        print(f" The area of the circle with radius {radius} is ", circle_area(radius) )

    elif shape == 2:
        length = int(input("Enter the length of the rectangle: "))
        breadth = int(input("Enter the breadth of the rectangle: "))
        print(f" The area of the rectangle of length {length} and breadth {breadth} is", rectangle_area(length, breadth) )

    elif shape == 3:
        base = int(input("Enter the base of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        print(f"The area of the triangle of base {base} and height {height} is", triangle_area(base, height) )

    elif shape == 4:
        side = int(input("Enter the side of the square: "))
        print(f"The area of the square with side {side} is", square_area(side) )


def circle_area(radius):
    """Returns the area of the circle when radius is passed"""

    return pi * (radius ** 2)


def rectangle_area(length, breadth):
    """Returns the area of the rectangle when its length and breadth are passed"""

    return length * breadth


def triangle_area(base, height):
    """Returns the area of the triangle when its base and height are passed"""

    return 0.5 * base * height

def square_area(side):
    """ Returns the area of the square if a side is passed """

    return side ** 2


area_of_shape(0)
