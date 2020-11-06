#!/usr/bin/env python3
import os
import pandas as pd

def subsetting_with_loc():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'municipal.tsv'))
    df = pd.read_csv(file, sep="\t")
    df = df.set_index("Region 2018")
    df = df.loc["Akaa":"Äänekoski",
            ["Population",
            "Share of Swedish-speakers of the population, %",
            "Share of foreign citizens of the population, %"]
        ]
    
    return df

def main():
    return

if __name__ == "__main__":
    main()
