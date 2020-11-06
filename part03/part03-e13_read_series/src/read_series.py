#!/usr/bin/env python3
import pandas as pd
import numpy as np

def read_series():
    data = []
    indices = []
    while True:             
        line = input("")  
        if not line:     # inp == "": 
            break          
        i, v = line.split()
        indices.append(i)
        data.append(v)
    return pd.Series(data,indices)

def main():
    pass

if __name__ == "__main__":
    main()