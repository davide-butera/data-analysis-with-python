#!/usr/bin/env python3

def word_frequencies(filename="src/alice.txt"):
    with open(filename, 'r') as content_file:
        dictionary = {}
        for line in content_file:
            content = line.split()
            for word in content:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    return dictionary

def main():
    word_frequencies()

if __name__ == "__main__":
    main()
