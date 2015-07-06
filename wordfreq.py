#!/usr/bin/env python
"""
wordfreq.py - Count the frequency of words in text.
"""
import collections
import operator

def main():
    # Read text
    with open('gettysburg.txt') as f:
        data = f.read()

    # Collect occurences of each word
    words = collections.defaultdict(int)
    for word in data.split():
        word = word.strip('-,.').lower()
        words[word] += 1

    # Sort the word data from most frequent to least frequent.
    word_freqs = sorted(words.items(), key=operator.itemgetter(1), reverse=True)

    # Output 10 most frequent words.
    with open('results.txt', 'w') as f:
        for x in word_freqs[:10]:
            f.write(str(x) + '\n')
            print(x)

if __name__ == '__main__':
    main()
