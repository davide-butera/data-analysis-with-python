#!/usr/bin/env python3

import math 

class Rational(object):
    def __init__(self, n, d):
        g = math.gcd(n, d)
        self.n = n // g
        self.d = d // g
    def __repr__(self):
        return f"{self.n}/{self.d}"
    def __mul__(self, other):
        return Rational(self.n*other.n,self.d*other.d)
    def __truediv__(self, other):
        return Rational(self.n*other.d,self.d*other.n)    
    def __add__(self, other):
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        d = lcm(self.d, other.d)
        n = int(d/self.d*self.n + d/other.d*other.n)
        return Rational(n, d)
    def __sub__(self, other):
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        d = lcm(self.d, other.d)
        n = int(d/self.d*self.n - d/other.d*other.n)
        return Rational(n, d)
    def __eq__(self, other):
        return (self.n==other.n and self.d == other.d)
    def __gt__(self, other):
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        d = lcm(self.d, other.d)
        return (d/self.d*self.n > d/other.d*other.n)
    def __lt__(self, other):
        return (not self == other and not self > other)

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1+r2)
    print(r1-r2)
    print(r1*r2)
    print(r1/r2)

    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
