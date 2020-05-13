#!/usr/bin/env python3

def extract_numbers(s):
    s = s.split()
    res = []
    for i in s:
        try:
            res.append(int(i))
        except ValueError:
            try:
                res.append(float(i))
            except ValueError:
                print("not an int nor a float")
    return res

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
