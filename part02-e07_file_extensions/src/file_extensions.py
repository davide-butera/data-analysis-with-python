#!/usr/bin/env python3
import re

def file_extensions(filename):
    noext = []
    dictionary = {}
    with open(filename, "r") as f:  
        for l in f:
            if(l[0]=="." or ("." not in l)):
                noext.append(l.strip())
            else:
                ext = re.findall(r"\.(.{0,3})$", l)[0]
                if(ext not in dictionary):
                    dictionary[ext] = []
                    dictionary[ext].append(l.strip())
                else:
                    dictionary[ext].append(l.strip())
    return (noext, dictionary)

def main():
    l, d = file_extensions("src/filenames.txt")
    print(f"{len(l)} files with no extension")
    for k, v in d:
        print(k,len(v))

if __name__ == "__main__":
    main()
