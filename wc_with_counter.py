#2018/10

from tokenise_ko_with_nltk import *
all_tokens = tokenise_with_nltk('ko_input.txt')

from collections import defaultdict
counts = defaultdict(int)
for token in all_tokens:
    counts[token] += 1
print(counts)

from collections import Counter
w_counts = Counter(all_tokens)
print('Counter() returns the sorted result by value')
w_freq=w_counts.most_common()
print(w_freq[:10]) #to see top 10

def write_counts(outfn, counts):
    '''you should add some codes here
    one of hints is
        outfile.write('%s\t%d\n' %(k, v))
    '''
write_counts('ko_freq.txt', w_freq)
