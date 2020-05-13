#!/usr/bin/env python3

import os
import pandas as pd

def average_temperature():
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kumpula-weather-2017.csv'))
    df = pd.read_csv(file)
    df = df[df["m"]==7]
    
    return  df['Air temperature (degC)'].mean()

def main():
    print(f"Average temperature in July: {average_temperature()}")
    return

if __name__ == "__main__":
    main()
