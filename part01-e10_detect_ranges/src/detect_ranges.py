#!/usr/bin/env python3

def detect_ranges(L):
    M = sorted(L)
    print(M)
    N = []
    
    currentRange=[M[0],M[0]]
    
    i=0
    while i<len(M):
        currentRange=[M[i],M[i]] 
        i+=1
        while i<len(M): 
            if M[i]-currentRange[1]==1: 
                currentRange[1]=M[i]
                i+=1    
            else: break 
        if currentRange[1]-currentRange[0]==0: 
            N.append(currentRange[0])
        else: 
            N.append((currentRange[0],currentRange[1]+1))      
    print(N)
    return N

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
