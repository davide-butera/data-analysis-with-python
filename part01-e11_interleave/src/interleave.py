#!/usr/bin/env python3

def interleave(*lists):
    l = []
    z = zip(*lists)
    for i in z:
        l.extend(i)
    return l

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()