with open('gettysburg.txt') as f:
    data = f.read()
import collections
words = collections.defaultdict(int)
for word in data.split():
    word = word.strip('-,.').lower()
    words[word] += 1
import operator
word_freqs = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
with open('results.txt', 'w') as f:
    for x in word_freqs[:10]:
        f.write(str(x) + '\n')
        print(x)
