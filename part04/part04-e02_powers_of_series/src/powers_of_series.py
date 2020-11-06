#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    rows = s.values.reshape((-1, 1))
    columns = np.arange(1, k+1)
        
    return pd.DataFrame(rows**columns, s.index, columns)

def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
