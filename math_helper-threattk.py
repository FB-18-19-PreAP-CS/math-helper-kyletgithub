from math import *


def distance(x1,y1,x2,y2):
    ''' returns the distance between points
        (x1, y1) and (x2, y2)
    '''
    y = y2 - y1
    x = x2 - x1
    d = sqrt(y**2 + x**2)
    d = round(d, 2)
    return d







