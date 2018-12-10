#!/usr/bin/env python
import numpy as np
import lda
import lda.datasets

# document-term matrix of corpus
M = lda.datasets.load_reuters()
#print(M)

#print("type(corpus): {}".format(type(M)))
print("DxV shape: {}".format(M.shape))

# the vocab
N = lda.datasets.load_reuters_vocab()
print("len(vocab): {}".format(len(N)))
print("first word in vocab : {}".format(N[0]))
#for i, v in enumerate(N): print(i, v)
'''
for i, d in enumerate(M):
    print(i, len(d), d[:])
    print(M[i])
    words_per_doc = []
    for j in range(len(M[i])) :
        words_per_doc.append(N[M[i][j]])
        #print([M[i][j]])
    print(' '.join(doc_words))
'''
# a sample of the title, the word and the count in a document
titles = lda.datasets.load_reuters_titles()
print("len(doc): {}".format(len(titles)))
doc_id = 0
word_id = 0
#print("count: {}".format(M[doc_id, word_id]))
print("first 5 documents' titles")
for idx in range(5):
    print("-- doc  : {}".format(titles[doc_id+idx]))

# do lda
model = lda.LDA(n_topics=10, n_iter=100, random_state=1)
model.fit(M)
topic_word = model.topic_word_
print("type(topic_word): {}".format(type(topic_word)))
print("TxV shape: {}".format(topic_word.shape))

# the asserted dirichlet distribution of topic words.
for n in range(10):
    sum_pr = sum(topic_word[n,:])
    print("topic: {} sum: {}".format(n, sum_pr))

# topic words for each topic cluster
n = 5
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(N)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {} : {}'.format(i, ' '.join(topic_words)))

