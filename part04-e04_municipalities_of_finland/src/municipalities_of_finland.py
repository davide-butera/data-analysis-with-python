#!/usr/bin/env python3

import os
import pandas as pd


def municipalities_of_finland():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'municipal.tsv'))
    df = pd.read_csv(file, sep="\t")
    df = df.set_index("Region 2018")
    df = df["Akaa":"Äänekoski"]

    return df

def main():
    df = municipalities_of_finland()
    print(df.sort_values(by=['Proportion of the unemployed among the labour force, %']))
    return
    
if __name__ == "__main__":
    main()
