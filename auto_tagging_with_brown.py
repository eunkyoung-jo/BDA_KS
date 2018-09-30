#2018/09/17
import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')

#train set & test set are divided
train_size = int(len(brown_tagged_sents)*0.9)
print(train_size, 'from', len(brown_tagged_sents))
train_sents = brown_tagged_sents[:train_size]
test_sents = brown_tagged_sents[train_size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
print(unigram_tagger.evaluate(test_sents))

brown_sents = brown.sents(categories='news')
print(unigram_tagger.tag(brown_sents[0]))

#train & test, not divided. fully trained.
unigram_tagger_full = nltk.UnigramTagger(brown_tagged_sents)
print(unigram_tagger_full.evaluate(brown_tagged_sents))
brown_sents = brown.sents(categories='news')
print(unigram_tagger_full.tag(brown_sents[0]))

