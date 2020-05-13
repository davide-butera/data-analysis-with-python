#!/usr/bin/env python3
import os
import pandas as pd

def below_zero():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kumpula-weather-2017.csv'))
    df = pd.read_csv(file)
    df = df[df["Air temperature (degC)"]<0]
    
    return len(df)

def main():
    print(f"Number of days below zero: {below_zero()}")
    return
    
if __name__ == "__main__":
    main()
