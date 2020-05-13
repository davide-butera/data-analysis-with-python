#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    x1 = np.array([2,4,6,7]) 
    y1 = np.array([4,3,5,1]) 
    plt.plot(x1,y1)
    x2 = np.array([1,2,3,4])   
    y2 = np.array([4,2,3,1]) 
    plt.plot(x2,y2)
    plt.title("Figure 1")  # Add a title to the figure
    plt.xlabel("x-axis")       # Give a label to the x-axis
    plt.ylabel("y-axis")       # Give a label to the y-axis
    plt.show()                    # Tell matplotlib to output the figure.

if __name__ == "__main__":
    main()