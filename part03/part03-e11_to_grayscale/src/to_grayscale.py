#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt
def to_grayscale(rgb):
    gray = rgb
    return np.dot(gray[...,:3], [0.2126, 0.7152, 0.0722 ])

def to_red(rgb):
    red = rgb
    red[:,:,[1,2]]=0
    return red
def to_green(rgb):
    green = rgb
    green[:,:,[0,2]]=0
    return green
def to_blue (rgb):
    blue = rgb
    blue[:,:,[0,1]]=0
    return blue

def main():
    _, ax = plt.subplots(3,1)
    painting = plt.imread(os.path.abspath(os.path.join(os.path.dirname(__file__), 'painting.png')))
    p1 = to_grayscale(painting.copy())
    p2 = to_red(painting.copy())
    p3 = to_green(painting.copy())
    p4 = to_blue(painting.copy())
    plt.show()

if __name__ == "__main__":
    main()
