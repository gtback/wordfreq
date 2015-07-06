#!/usr/bin/env python
"""
wordfreq.py - Count the frequency of words in text.
"""
import argparse
import collections
import ConfigParser
import operator
import os
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

def output_results(word_freqs, outstream, count=10):
    """Output 10 most frequent words."""
    for x in word_freqs[:count]:
        outstream.write(str(x) + '\n')

def parse_args():
    """Parse arguments from the command line."""
    parser = argparse.ArgumentParser("Count the frequency of words in text.")
    parser.add_argument('-c', '--count', type=int,
                        help="Number of words to report. Default: 10")
    parser.add_argument('infile', nargs="?", help="Source text. Default: STDIN")
    parser.add_argument('outfile', nargs="?", help="Result destination. Default: STDOUT")

    return parser.parse_args()

def parse_envvars():
    """Get options from environment variables."""
    return {
        'count': os.environ.get('WF_COUNT'),
        'infile': os.environ.get('WF_INFILE'),
        'outfile': os.environ.get('WF_OUTFILE'),
    }

def parse_config(conffile):
    """Get options from a config file."""
    config = ConfigParser.ConfigParser()
    config.read(conffile)
    options = {}
    if config.has_option('wordfreq', 'count'):
        options['count'] = config.getint('wordfreq', 'count')
    if config.has_option('wordfreq', 'infile'):
        options['infile'] = config.get('wordfreq', 'infile')
    if config.has_option('wordfreq', 'outfile'):
        options['outfile'] = config.get('wordfreq', 'outfile')
    return options


def wordfreq(count=10, infile=None, outfile=None):
    if not infile:
        data = sys.stdin.read()
    else:
        data = read_text(infile=infile)
    words = count_words(data)
    word_freqs = sort_words(words)
    if not outfile:
        output_results(word_freqs, outstream=sys.stdout, count=count)
    else:
        with open(outfile, 'w') as outfile:
            output_results(word_freqs, outstream=outfile, count=count)

def main():
    """Main wordfreq function."""
    args = parse_args()
    env = parse_envvars()
    conf = parse_config('wordfreq.conf')

    count = int(args.count or env['count'] or conf.get('count')) or 10
    infile = args.infile or env['infile'] or conf.get('infile') or None
    outfile = args.outfile or env['outfile'] or conf.get('outfile') or None

    wordfreq(count, infile, outfile)

if __name__ == '__main__':
    main()
