#!/usr/bin/env python3

import sys

def summary(filename="hy/hy-data-analysis-with-python-spring-2020/part02-e05_summary/src/example.txt"):
    with open(filename, 'r') as content_file:
        numbers = []
        for line in content_file:
            try: 
                x = float(line)
                numbers.append(x)
            except ValueError: 
                print("Error")
        n = len(numbers)
        s = sum(numbers)
        mean = s/n
        variance = sum([((x - mean) ** 2) for x in numbers]) / (n-1)
        stddev = variance ** 0.5
    print("prova")
    
    return (s,mean,stddev)

def main():
    l = sys.argv[1:]

    for i in l:
        triple = summary(i)
        print(f"File: {i} Sum: {triple[0]:.6f} Average: {triple[1]:.6f} Stddev: {triple[2]:.6f}")
 

if __name__ == "__main__":
    main()
