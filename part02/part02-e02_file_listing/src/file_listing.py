#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    tuples = []
    with open(filename, "r") as f:  
        for l in f:
            size = int(re.findall(r'[a-z] *([\d]*) [A-Z]', l)[0])
            month = re.findall(r'([A-Z][a-z][a-z])', l)[0]
            day = int(re.findall(r'(\d{1,2}) \d', l)[0])
            hourmin = re.findall(r'(\d\d):(\d\d)', l)[0]
            savedfilename = re.findall(r' (\S*)$', l)[0]
            hour, minute = hourmin
            hour = int(hour)
            minute = int(minute)
            t = (size, month, day, hour, minute, savedfilename)
            tuples.append(t)
    return tuples

def main():
    file_listing()

if __name__ == "__main__":
    main()
