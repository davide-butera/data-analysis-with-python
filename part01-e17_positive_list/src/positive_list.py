#!/usr/bin/env python3

def positive_list(L):
    def positive(n):
        if n<=0:
            return False
        else: return True
    result = list(filter(positive, L))
    return result

def main():
    print(positive_list([2,-2,0,1,-7]))

if __name__ == "__main__":
    main()
