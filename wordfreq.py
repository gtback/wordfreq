#!/usr/bin/env python
"""
wordfreq.py - Count the frequency of words in text.
"""
import collections
import operator

def read_text():
    """Read text"""
    with open('gettysburg.txt') as f:
        data = f.read()
    return data

def count_words(data):
    """Count occurences of each word"""
    words = collections.defaultdict(int)
    for word in data.split():
        word = word.strip('-,.').lower()
        words[word] += 1
    return words

def sort_words(words):
    """Sort the word data from most frequent to least frequent."""
    return sorted(words.items(), key=operator.itemgetter(1), reverse=True)

def output_results(word_freqs):
    """Output 10 most frequent words."""
    with open('results.txt', 'w') as f:
        for x in word_freqs[:10]:
            f.write(str(x) + '\n')
            print(x)

def main():
    """Main wordfreq function."""
    data = read_text()
    words = count_words(data)
    word_freqs = sort_words(words)
    output_results(word_freqs)

if __name__ == '__main__':
    main()
