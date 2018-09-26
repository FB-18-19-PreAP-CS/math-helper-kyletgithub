from math import *

def main():
    answers = ('1','2','3','4','5','6')
    while True:
        print()
        print("     MATH HELPER     ")
        print("Choose a formula: ")
        print("1) Distance")
        print("2) Pythagorean Theorem")
        print("3) Quadratic Formula")
        print("4) Slope")
        print("5) Circumference")
        print("6) Quit Program")
        print()
        ans = (input('> '))
        if ans not in answers:
            print("Not Valid Input")
        else:
            if ans == '1':
                print("====DISTANCE FORMULA====")
                print("ENTER: 'x1'")
                num1 = float(input('> '))
                print("ENTER: 'y1'")
                num2 = float(input('> '))
                print("ENTER: 'x2'")
                num3 = float(input('> '))
                print("ENTER: 'y2'")
                num4 = float(input('> '))                
                print(distance(num1,num2,num3,num4))
            
            if ans == '2':
                print("====PYTHAGOREAN THEOREM====")
                print("ENTER: SIDE 1")
                num1 = float(input('> '))
                print("ENTER: SIDE 2")
                num2 = float(input('> '))
                print(pythag(num1,num2))
                
            if ans == '3':
                print("====QUADRATIC FORMULA====")
                print("ENTER: A")
                num1 = float(input('> '))
                print("ENTER: B")
                num2 = float(input('> '))
                print("ENTER: C")
                num3 = float(input('> '))
                print(quadratic_form(num1,num2,num3))
                
            if ans == '4':
                print("====SLOPE====")
                print("ENTER: x1")
                num1 = float(input('> '))
                print("ENTER: y1")
                num2 = float(input('> '))
                print("ENTER: x2")
                num3 = float(input('> '))
                print("ENTER: y2")
                num4 = float(input('> '))
                print(slope(num1,num2,num3,num4))
                
            if ans == '5':
                print("====CIRCUMFERENCE====")
                print("ENTER: RADIUS")
                num = float(input('> '))
                print(circum(num))
                
            if ans == '6':
                break  

def distance(x1,y1,x2,y2):
    ''' returns the distance between points
        (x1, y1) and (x2, y2)
        
        >>> distance(0,0,0,0)
        0.0
        
        >>> distance(5,5,10,10)
        7.07
        
        >>> distance(6,8,9,12)
        5.0
        
        >>> distance(10000,5000,15000,20000)
        15811.39
        
        >>> distance(1,2,3,4)
        2.83
        
    '''
    y = y2 - y1
    x = x2 - x1
    d = sqrt(y**2 + x**2)
    d = round(d, 2)
    print('')
    print('')
    return 'Distance: ' + str(d)

def pythag(a, b):
    ''' returns the length of the hypotenuse
        in a right triangle

        >>> pythag(0,0)
        0.0
        
        >>> pythag(3,4)
        5.0
        
        >>> pythag(-5,10)
        11.18
        
        >>> pythag(20,30)
        36.06
        
        >>> pythag(-5,-9)
        10.3
        
    '''
    if a == 0 or b == 0:
        return 'Not a triangle'
    c = sqrt(a**2 + b**2)
    c = round(c, 2)
    print('')
    print('')
    return "Side C: " + str(c)

def quadratic_form(a, b, c):
    ''' applies the quadratic formula to a, b and c
        and returns the zeros
        
        >>> quadratic_form(1, 5, 6)
        ((-2.0, 0), (-3.0, 0))
               
        >>> quadratic_form(1, 5, 10)
        "function doesn't cross x-axis"
        
        >>> quadratic_form(2, 4, -6)
        ((1.0, 0), (-3.0, 0))
        
        >>> quadratic_form(1, -4, 3)
        ((3.0, 0), (1.0, 0))
        
        >>> quadratic_form(3, 7, 4)
        ((-1.0, 0), (-1.3, 0))

        
    '''
    d = b**2 - (4 * a * c)
    if d < 0:
        return "function doesn't cross x-axis"
    zero1 = (-b + sqrt(d))
    zero2 = (-b - sqrt(d))
    zero1 = zero1/(2*a)
    zero2 = zero2/(2*a)
    zero1 = round(zero1, 1)
    zero2 = round(zero2, 1)
    print('')
    print('')
    return (zero1, 0), (zero2, 0)

def slope(x1, y1, x2, y2):
    ''' returns slope between points (x1,y1)
        and (x2,y2)
        >>> slope(1,2,3,4)
        1.0
        
        >>> slope(-5,6,-8,12)
        -2.0
        
        >>> slope(1,4,1,6)
        Traceback (most recent call last):
            ...
        ValueError: denominator cannot equal zero
        
        >>> slope(7,2,4,1)
        0.3
        
        >>> slope(1,2,1,2)
        Traceback (most recent call last):
            ...
        ValueError: denominator cannot equal zero
        
    '''
    y = y2 - y1
    x = x2 - x1
    if x1 == x2 and y1 != y2:
        return('undefined slope: vertical line')
    if (x1, y1) == (x2, y2):
        return('not a line')
    ans = round(y/x, 1)
    print('')
    print('')
    return 'Slope: ' + str(ans)

def circum(r):
    ''' returns he cirumference of a circle when given
        the radius, rounded to 2 deciaml places
        
        >>> circum(5)
        31.42
        
        >>> circum(0)
        0.0
        
        >>> circum(10)
        62.83
        
        >>> circum(20000)
        125663.71
        
        >>> circum(-3)
        -18.85
        
    '''
    c = round(pi * 2 * r ,2)
    print('')
    print('')
    return 'Circumference: ' + str(c)

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    main()
    






