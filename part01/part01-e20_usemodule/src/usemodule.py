#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    triangle.area(1,2)
    triangle.hypothenuse(3,4)

if __name__ == "__main__":
    main()
