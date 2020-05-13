#!/usr/bin/env python3

import os
import pandas as pd

def last_week():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'UK-top40-1964-1-2.tsv'))
    df = pd.read_csv(file, sep="\t")
    return pd.DataFrame()

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
