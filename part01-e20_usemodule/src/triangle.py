# Enter you module contents here
"Calculates area and hypothenuse of a right triangle"

__author__="Davide Butera"
__version__= "1.0"

import math 

def hypothenuse(a, b):
    "Given sides a and b calculates hypothenuse"
    return math.sqrt(a**2+b**2)

def area(a, b):
    "Given sides a and b calculates area"
    return a*b/2