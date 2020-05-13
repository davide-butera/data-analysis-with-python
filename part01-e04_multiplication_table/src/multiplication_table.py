#!/usr/bin/env python3


def main():
    for i in range(10):
        if i!=0: print()
        for j in range(10):
            print(f"{((i+1)*(j+1)):4d}", end=" ")

if __name__ == "__main__":
    main()
