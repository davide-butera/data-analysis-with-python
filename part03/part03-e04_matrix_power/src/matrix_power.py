#!/usr/bin/env python3
import numpy as np
from functools import reduce 

def matrix_power(a, n):
    if n>=0:
        return reduce(np.matmul, (a for _ in range(n)), np.eye(a.shape[0]))
    else:
        inv = np.linalg.inv(a)
        return reduce(np.matmul, (inv for _ in range (-n)))

def main():
    a = np.array([1,2,3,4])
    a = a.reshape((2,2))
    print(a)
    print(matrix_power(a,2))


if __name__ == "__main__":
    main()



"""
def matrix_power(a, n):
    power = a
    if n<0:
        return matrix_power(np.linalg.inv(a),-n)
    if n==0:
        return np.eye(a.shape[0])
    for i in range(n-1):
        power = np.matmul(power,a)
    return power
"""