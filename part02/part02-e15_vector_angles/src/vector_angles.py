#!/usr/bin/env python3

import numpy as np
import scipy.linalg
import numpy.linalg as la

"""
def vector_lengths(a):
    return np.sqrt(np.sum(np.square(a), axis=1))

def vector_angles(X, Y):
    denominator=vector_lengths(X)*vector_lengths(Y)
    dotprod=np.sum(X*Y, axis=1)
    div=dotprod/denominator
    return np.degrees(np.arccos(np.clip(div,-1.0,1.0)))
"""
#mettere np.degrees dentro questa funzione per passare l'esercizio su TMC 
def vector_angles(X, Y):
    ip = np.sum(X*Y, axis=1) #inner product
    Xlen = scipy.linalg.norm(X, 2, axis=1)
    Ylen = scipy.linalg.norm(Y, 2, axis=1)
    cosine = ip/(Xlen*Ylen)
    cosine = np.clip(cosine, -1.0, 1.0) #force cosine between -1 and 1 
    radians = np.arccos(cosine) 
    return radians


def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    b=np.random.randint(0,10, (4,4))
    print(a)
    print(b)
    print(np.round(np.degrees(vector_angles(a,b)), 2))

if __name__ == "__main__":
    main()
