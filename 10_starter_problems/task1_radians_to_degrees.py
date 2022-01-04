# Convert radians into degrees

def radians_to_degrees(radians):
    # import math library to access value of pi
    from math import pi
    # 1deg = pi/180deg
    degrees = 180 / pi * radians
    return degrees
