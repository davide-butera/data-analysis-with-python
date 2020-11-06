#!/usr/bin/env python3

def sum_equation(L):
    if(L == []):
        return "0 = 0"
    s = ' + '.join(map(str, L)) 
    s += f" = {sum(L)}"
    return s

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
