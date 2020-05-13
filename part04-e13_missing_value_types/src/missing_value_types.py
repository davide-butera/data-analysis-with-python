#!/usr/bin/env python3


import pandas as pd
import numpy as np

def missing_value_types():
    columns = ["Year of independence", "President"]
    state = ["United Kingdom", "Finland", "USA","Sweden","Germany", "Russia"]
    year = [np.nan, 1917,1776,1523,np.nan,1992]
    president = [np.nan,"Niinistö","Trump",np.nan,"Steinmeier","Putin"]

    data = {columns[0]: year, columns[1]: president}
    
    return pd.DataFrame(data,index=state)
               
def main():
    print(missing_value_types())
    return

if __name__ == "__main__":
    main()
