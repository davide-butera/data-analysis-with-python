#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    iris = load()
    return scipy.stats.pearsonr(iris[:,0],iris[:,2])[0]

def correlations():
    return np.corrcoef(load(),rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
