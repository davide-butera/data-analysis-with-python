#!/usr/bin/env python3

def main():
    for i in range(5):
        for j in range(5):
            if (i+j+2)==5:
                print(f"({i+1},{j+1})")

if __name__ == "__main__":
    main()
