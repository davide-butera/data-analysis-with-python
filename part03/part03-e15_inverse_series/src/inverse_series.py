#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, s.array)

def main():
    print(inverse_series(pd.Series(1,['a'])))
    return

if __name__ == "__main__":
    main()
