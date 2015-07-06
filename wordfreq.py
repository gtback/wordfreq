#!/usr/bin/env python
"""
wordfreq.py - Count the frequency of words in text.
"""
import argparse
import collections
import operator
import sys

def read_text(infile):
    """Read text"""
    with open(infile) as f:
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

def output_results(word_freqs, outstream):
    """Output 10 most frequent words."""
    for x in word_freqs[:10]:
        outstream.write(str(x) + '\n')

def parse_args():
    """Parse arguments from the command line."""
    parser = argparse.ArgumentParser("Count the frequency of words in text.")
    parser.add_argument('infile', nargs="?", help="Source text. Default: STDIN")
    parser.add_argument('outfile', nargs="?", help="Result destination. Default: STDOUT")

    return parser.parse_args()

def main():
    """Main wordfreq function."""
    args = parse_args()
    if not args.infile:
        data = sys.stdin.read()
    else:
        data = read_text(infile=args.infile)
    words = count_words(data)
    word_freqs = sort_words(words)
    if not args.outfile:
        output_results(word_freqs, outstream=sys.stdout)
    else:
        with open(args.outfile, 'w') as outfile:
            output_results(word_freqs, outstream=outfile)

if __name__ == '__main__':
    main()
