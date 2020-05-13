#!/usr/bin/env python3
import os
import pandas as pd

def subsetting_by_positions():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'UK-top40-1964-1-2.tsv'))
    df = pd.read_csv(file, sep="\t")
    df = df.iloc[1:11,2:4]  

    return df

def main():
    print(subsetting_by_positions())
    return

if __name__ == "__main__":
    main()
