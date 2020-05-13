#!/usr/bin/env python3

import sys

def file_count(filename):  
    linecount, wordcount, charactercount = 0, 0, 0
    with open(filename) as f:
        lines = f.readlines()
        linecount = len(lines)
        for line in lines:
            line = line.split()
            for word in line:
                wordcount+=1
        f.seek(0)
        charactercount = sum(len(word) for word in f.read())
    return (linecount, wordcount, charactercount)

def main():
    for filename in sys.argv[1:]:
        linecount, wordcount, charactercount = file_count(filename)
        print(f"{linecount}\t{wordcount}\t{charactercount}\t{filename}")

if __name__ == "__main__":
    main()
