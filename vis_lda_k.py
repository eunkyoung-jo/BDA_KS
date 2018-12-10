#2018/12
#coding:utf-8

from gensim import corpora
import gensim
import pyLDAvis.gensim
import bs4

#pyLDAvis.enable_notebook()

ddir='lda_data'
# load saved model, corpus, and dictionary
dictionary = gensim.corpora.Dictionary.load(ddir+'/dictionary.dict')
corpus = gensim.corpora.MmCorpus(ddir+'/corpus.mm')
lda = gensim.models.LdaModel.load(ddir+'/model.lda')

#visualise topic model
vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
#save vis
pyLDAvis.save_html(vis,ddir+'/vis_lda.html')

