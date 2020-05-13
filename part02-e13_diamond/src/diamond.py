#!/usr/bin/env python3

import numpy as np

def diamond(n):
    a = np.eye(n,dtype=int)
    b = np.flip(a,1)[1:]
    c = np.concatenate((a,b))
    d = np.flip(c)[:,:-1]
    return np.concatenate((d,c),1)

def main():
    print(diamond(6))

if __name__ == "__main__":
    main()
