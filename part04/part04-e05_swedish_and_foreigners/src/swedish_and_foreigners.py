#!/usr/bin/env python3
import os 
import pandas as pd

def municipalities_of_finland():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'municipal.tsv'))
    df = pd.read_csv(file, sep="\t")
    df = df.set_index("Region 2018")
    df = df["Akaa":"Äänekoski"]
    return df

def swedish_and_foreigners():
    df = municipalities_of_finland()
    s = "Share of Swedish-speakers of the population, %"
    f = "Share of foreign citizens of the population, %"
    df = df[(df[s] > 5.0) & (df[f] > 5.0)]
    df = df[['Population', s, f]]

    return df
    

def main():
    print(swedish_and_foreigners())
    print(swedish_and_foreigners().corr())
    return

if __name__ == "__main__":
    main()
