#!/usr/bin/env python3
import os
import pandas as pd

def snow_depth():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kumpula-weather-2017.csv'))
    df = pd.read_csv(file)
    
    return  df['Snow depth (cm)'].max()

def main():
    print(f"Max snow depth: {snow_depth()}")
    return

if __name__ == "__main__":
    main()
