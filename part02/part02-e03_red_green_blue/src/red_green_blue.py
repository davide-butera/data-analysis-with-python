#!/usr/bin/env python3

import re
import os

def red_green_blue(filename="src/rgb.txt"):
    colours = []
    with open(filename, "r") as fp:  
        for cnt, line in enumerate(fp, start = 2):
            s = re.findall(r"^\s*(\d{0,3})\s*(\d{0,3})\s*(\d{0,3})\s*(.*)", line)[0]
            t = "\t".join(s)
            colours.append(t)
    colours = colours[1:]        
    return colours


def main():
    red_green_blue()

if __name__ == "__main__":
    main()
