#!/usr/bin/env python3

import os
import pandas as pd

def cyclists():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Helsingin_pyorailijamaarat.csv'))
    df = pd.read_csv(file,sep=";")
    df = df.dropna(axis=0, how='all')
    df = df.dropna(axis=1, how='all')

    return df


def main():
    print(cyclists())
    return
    
if __name__ == "__main__":
    main()
