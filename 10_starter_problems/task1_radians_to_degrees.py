# Convert radians into degrees

def radians_to_degrees(radians):
    # import math library to access value of pi
    from math import pi
    # 1° = π/180°
    degrees = 180 / pi * radians
    return degrees
