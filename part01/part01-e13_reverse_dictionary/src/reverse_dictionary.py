#!/usr/bin/env python3
    
def reverse_dictionary(d):
    out = {}
    for v in d.values():  
        for value in v:
            if value not in out:
                out[value] = []
    for i in d:
        for j in out:
            if j in map (lambda x : x,d[i]):
                out[j].append(i)
                out[j].sort()
    return out

def main():
    d ={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
