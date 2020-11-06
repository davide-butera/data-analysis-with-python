#!/usr/bin/env python3

import pandas as pd

def cities():
    cities = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    populations = [643272, 279044, 231853, 223027, 201810]
    areas = [715.48, 528.03, 689.59, 240.35, 3817.52]
    data = {'Population': populations, 'Total area': areas} 
    return pd.DataFrame(data, index=cities)
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
