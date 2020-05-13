#!/usr/bin/env python3
import os 
import pandas as pd
import numpy as np

def special_missing_values():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'UK-top40-1964-1-2.tsv'))
    df = pd.read_csv(file, sep="\t")
    df = df[(df.LW != "New")  & (df.LW != "Re") ]
    df["LW"] = pd.to_numeric(df["LW"])
    df = df[df["Pos"]>df["LW"]]

    return df
def main():

    print(special_missing_values())
    return

if __name__ == "__main__":
    main()
