#!/usr/bin/env python3
import math 
def transform(s1, s2):
    l = []
    t1 = map(int, s1.split())
    t2 = map(int, s2.split())
    z = list(zip(t1,t2))
    for i in z:
        l.append(i[0]*i[1])
    return l

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
