#!/usr/bin/env python3
import os
import pandas as pd

def main():
    df = pd.read_csv('src/municipal.tsv', sep="\t")
    print("Shape: {}, {}".format(*df.shape))  
    print("Columns:")
    print(*df.columns.values, sep='\n')

if __name__ == "__main__":
    main()
