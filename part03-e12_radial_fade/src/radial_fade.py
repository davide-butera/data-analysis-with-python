#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt

def center(a):
    height, width = a.shape[:2]
    print(height,width)
    return ((height-1)/2.0,(width-1)/2.0) # note the order: (center_y, center_x)

def radial_distance(a):
    h, w = np.indices(a.shape[:2]) 
    ind  = np.dstack((h,w)) # array populated with indices [0,0],[0,1],...
    c = center(a)
    dist = np.linalg.norm(ind - c, axis=2)

    return dist

def scale(a, tmin=0.0, tmax=1.0):
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))


def radial_mask(a):
    dists = radial_distance(a)
    return scale(-dists)

def radial_fade(a):
    mask = radial_mask(a)
    return a * mask[:,:,np.newaxis]

def main():
    _, ax = plt.subplots(3)
    painting = plt.imread(os.path.abspath(os.path.join(os.path.dirname(__file__), 'painting.png')))
    ax[0].imshow(painting)
    ax[1].imshow(radial_mask(painting))
    ax[2].imshow(radial_fade(painting))
    plt.show()

if __name__ == "__main__":
    main()
