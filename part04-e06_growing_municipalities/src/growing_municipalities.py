#!/usr/bin/env python3

import pandas as pd
import os

def municipalities_of_finland():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'municipal.tsv'))
    df = pd.read_csv(file, sep="\t")
    df = df.set_index("Region 2018")
    df = df["Akaa":"Äänekoski"]

    return df

def growing_municipalities(df):
    growing = "Population change from the previous year, %"
    g = len(df[df[growing]>0.0])
    
    return g/len(df)

def main():
    df = municipalities_of_finland()
    g = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {g*100:.1f}%")
    
    return

if __name__ == "__main__":
    main()
