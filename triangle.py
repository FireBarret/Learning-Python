import math
def area(base, height):
    '''(number, number)-> number
    Return the area of a triangle given base and height.

    >>> area(2,4)
    4.0
    >>> area(3.4, 7.5)
    12.75
    '''

    return base * height / 2

def perimeter(side1, side2, side3):
    '''(number, number, number) -> number
    Return the perimeter of a triangle given the length of all 3 sides.

    >>> perimeter(1,2,3)
    6

    >>> perimeter(5,9,10)
    24
    '''
    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    ''' (number, number, number) -> float
    Return the semiperimeter of a triangle given the length of all 3 sides.

    >>>semiperimeter(4,5,9)
    9.0

    >>>semiperimeter(7,9,10)
    13.0
    '''
    return (side1 + side2 + side3) / 2

def area_hero(side1, side2, side3):
    ''' (number, number, number) -> float

    Return the area of a triangle given the length of all 3 sides.
    
    >>>area_hero(3,4,5)
    6.0
    '''
    semi= semiperimeter(side1, side2, side3)
    ss1 = semi - side1
    ss2 = semi - side2
    ss3 = semi - side3
    under_root = semi * ss1 * ss2 * ss3
    return math.sqrt(under_root)

    
