from math import *


def distance(x1,y1,x2,y2):
    ''' returns the distance between points
        (x1, y1) and (x2, y2)
        
        >>> distance(0,0,0,0)
        0.0
        
        
    '''
    y = y2 - y1
    x = x2 - x1
    d = sqrt(y**2 + x**2)
    d = round(d, 2)
    return d

def pythag(a, b):
    ''' returns the length of the hypotenuse
        in a right triangle

        >>> pythag(0,0)
        0.0
        
        
    '''
    c = sqrt(a**2 + b**2)
    c = round(c, 2)
    return c

def quadratic_form(a, b, c):
    ''' applies the quadratic formula to a, b and c
        and returns the zeros
        
        >>> quadratic_form(1, 5, 10)
        "function doesn't cross x-axis"
        
    '''
    d = b**2 - 4 * a * c
    if d < 0:
        return "function doesn't cross x-axis"
    zero1 = ((-b + sqrt(d))/2*a)
    zero2 = ((-b - sqrt(d))/2*a)
    zero1 = round(zero1, 1)
    zero2 = round(zero2, 1)
    
    return (zero1, 0), (zero2, 0)

if __name__ == "__main__":
    import doctest
    doctest.testmod()




