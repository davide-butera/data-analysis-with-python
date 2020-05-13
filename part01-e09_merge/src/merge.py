#!/usr/bin/env python3

def merge(L1, L2):
    n1 = len(L1)
    n2 = len(L2)
    L3 = [None] * (n1 + n2) 
    i, j, k = 0, 0, 0

    while i < n1 and j < n2: 

        if L1[i] < L2[j]: 
            L3[k] = L1[i] 
            k = k + 1
            i = i + 1
        else: 
            L3[k] = L2[j] 
            k = k + 1
            j = j + 1
      
    while i < n1: 
        L3[k] = L1[i]
        k = k + 1
        i = i + 1

    while j < n2: 
        L3[k] = L2[j]
        k = k + 1
        j = j + 1
    return L3


def main():
    L1 =[1, 2, 3, 5, 7, 8, 9]
    L2 =[0, 4, 5]
    L3 = merge(L1,L2)
    print(L3)

if __name__ == "__main__":
    main()
