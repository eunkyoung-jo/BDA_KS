#2018/09/17
#how to avoid dict errors.
#how to count something using dict

from collections import defaultdict
counts = defaultdict(int)
from nltk.corpus import brown

for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
    #print(word, tag)
    counts[tag] += 1

print(counts['NOUN'])
print(sorted(counts))

print('\n[sorted by key]')
for k in sorted(counts):
    print(k, counts[k])

print('\n[sorted by value]')
for k in sorted(counts, key=counts.get, reverse=True):
    print(k, counts[k])
