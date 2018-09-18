#2018/09/17
import nltk
from nltk.corpus import brown
CONTENT = 'news'
brown_tagged_sents = brown.tagged_sents(categories=CONTENT)
brown_sents = brown.sents(categories=CONTENT) #untagged

#Bigram
train_size = int(len(brown_tagged_sents)*0.95)
print(train_size, 'from', len(brown_tagged_sents))
train_sents = brown_tagged_sents[:train_size]
test_sents = brown_tagged_sents[train_size:]

#default for backoff
def_tagger = nltk.DefaultTagger('NN')
unigram_tagger = nltk.UnigramTagger(train_sents, backoff=def_tagger)
bigram_tagger = nltk.BigramTagger(train_sents, backoff=unigram_tagger)

print(bigram_tagger.evaluate(test_sents))
print(bigram_tagger.tag(brown_sents[0]))

