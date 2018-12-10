#2018/10
# Topic modeling with gensim LDA
# reference:
# https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/

from gensim import corpora
import gensim
import string
import pprint

ddir='lda_data'

# input
f = open(ddir+'/input.txt.out', 'r', encoding='utf-8')
lines = f.readlines()

# compile documents
doc_list = []
for doc in lines:
    doc_list.append(doc)

doc_term = [doc.split() for doc in doc_list]
print(len(doc_term))

''' Document-Term Matrix '''
# Creating the term dictionary of our courpus, where every unique term is assigned an index.
# Turn our tokenized docs into a id-term dictionary.
dictionary = corpora.Dictionary(doc_term)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_term]

''' Running LDA Model '''
# Set parameters.
n_topics = 5
n_words = 15
chunksize = 10      # chunksize is the number of documents to be used in each training chunk. (how many documents to load into memory)
passes = 1          # default is 1. passes is the total number of training passes through the corpus.
iterations = 1000    #default is 50. (Number of sampling iterations)
update_every = 1    # by default, update_every=1,  the model update is done once every after each batch of `chunksize` documents
#eval_every = 1
random_state = 2004  # random_state is the seed for one.

# Create an object for LDA model and Do
# Running and Trainign LDA model on the document term matrix.
# alpha and eta are hyperparameters that affect sparsity of the document-topic (theta) and topic-word (lambda) distributions.
# Both default to a symmetric 1.0/num_topics prior.
lda_model = gensim.models.ldamodel.LdaModel(doc_term_matrix,
                                            id2word=dictionary,
                                            num_topics=n_topics,
                                            iterations=iterations,
                                            update_every=update_every,
                                            #eval_every=eval_every,
                                            chunksize=chunksize,
                                            passes=passes,
                                            alpha='auto',
                                            eta='auto',
                                            random_state=random_state,
                                            per_word_topics=True)

''' Result '''
print('*** results ***')
#pprint.pprint(lda_model.print_topics())
pprint.pprint(lda_model.print_topics(num_topics=n_topics, num_words=n_words)) #if num_topics=-1, all topics will be in result
#pprint.pprint(lda_model.show_topics(num_topics=n_topics, num_words=10, log=False, formatted=True))
pprint.pprint(lda_model.get_topics())

# output
topic_file = open(ddir+'/lda_topics.txt', 'w', encoding='utf-8')
doc_file = open(ddir+'/doc_topic.txt', 'w', encoding='utf-8')
term_file = open(ddir+'/term_topic.txt', 'w', encoding='utf-8')

# the result of topics
for i_topic in range(n_topics):
    topic_file.write('%s\t%s\n' % (i_topic, str(lda_model.print_topic(i_topic, topn=n_words)).replace('*',' ').replace('"','')))

# doc by topic distribution (for the given document bow)
i = 1
for dtm in doc_term_matrix:
    print('d%s %s' % (i, lda_model.get_document_topics(dtm)))
    doc_file.write('d%s\t%s\n' % (i, lda_model.get_document_topics(dtm)))
    i = i+1

# word by topic distribution
for tid in range(len(dictionary)):
    #print('t%s %s' % (tid, lda_model.get_term_topics(dictionary[tid])))
    #print('%s %s' % (dictionary[tid], lda_model.get_term_topics(dictionary[tid])))
    term_file.write('%s\t%s\n' % (dictionary[tid], lda_model.get_term_topics(dictionary[tid])))


# Save model, corpus, and dictionary
print('*** save lda model, corpus, and dictionary ***')
dictionary.save(ddir+'/dictionary.dict')
corpora.MmCorpus.serialize(ddir+'/corpus.mm',doc_term_matrix)
lda_model.save(ddir+'/model.lda')


f.close()
doc_file.close()
term_file.close()
topic_file.close()
