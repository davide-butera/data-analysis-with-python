#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    s = re.findall(r'\[[^\w\-\+]*(\+?\-?\d+)? *]', s)
    #s = re.findall(r'\[\s*([+-]?\d+)\s*\]', s)
    result = []
    for i in s:
        if(i.startswith("+-")):
            continue
        else: result.append(int(i))
    return result     

def main():
    print(integers_in_brackets(" afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()