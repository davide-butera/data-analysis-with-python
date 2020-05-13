#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    mask = a[:,1] > a[:,-2]
    return a[mask]
    
def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print(a)
    print(column_comparison(a))

if __name__ == "__main__":
    main()
