#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    fh, sh = np.split(a,2,axis=1)
    b = np.sum(fh,axis=1) > np.sum(sh,axis=1)
    return a[b]

def main():
    np.random.seed(1)
    a=np.random.randint(0,10, (3,6))
    print(a)
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
