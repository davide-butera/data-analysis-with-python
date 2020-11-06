#!/usr/bin/env python3

import math

def main():
    while(True):
        i = input("Choose a shape (triangle, rectangle, circle): ")

        if(i=="triangle"):
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            print(f"The area is {base*height/2}")
        
        elif(i=="rectangle"):
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            print(f"The area is {width*height}")

        elif(i=="circle"):
            radius = int(input("Give radius of the circle: "))
            print(f"The area is {radius*radius*math.pi}")
        
        elif(i==""):
            break
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
