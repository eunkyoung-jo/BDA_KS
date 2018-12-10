#2018/06/11
import sys
from math import *

tfs = {}  #term frequency: how many times a term occurs
dfs = {}  #document frequency: how many documents a term occurs in
idfs = {} #inverse document frequency: how many docs in terms of all docs
idf_rates = {} #idf rate
tfidf_rates = {} #tf*idf rate

def get_tf_idf(docs):
    # fill out here

def write_tfidf_file(outfilename):
    outfile = open(outfilename, 'w')
    outfile.write('[word\ttf\tdf\ttf-idf]\n')
    for each in sorted(tfidf_rates, key=tfidf_rates.get, reverse=True):
        outfile.write("%s\t%d\t%d\t%f\n" %(each, tfs[each], dfs[each], tfidf_rates[each]))
    outfile.close()

def write_idfrates_file(outfilename):
    outfile = open(outfilename, 'w')
    outfile.write('[word\ttf\tdf\tidf\tidf_rate]\n')
    for each in sorted(idf_rates, key=idfs.get, reverse=True):
        outfile.write("%s\t%d\t%d\t%f\t%f\n" %(each, tfs[each], dfs[each], idfs[each], idf_rates[each]))
    outfile.close()

def write_tfs_file(outfilename):
    outfile = open(outfilename, 'w')
    outfile.write('word\ttf\tdf\n')
    for each in sorted(tfs, key=tfs.get, reverse=True):
        outfile.write("%s\t%d\t%d\n" %(each, tfs[each], dfs[each]))
    outfile.close()

def docs_tf_idf(docs, thresh_hold=3.0):
    get_tf_idf(docs)
    new_docs = []
    for doc in docs:
        new_doc = []
        for w in doc:
            if tfidf_rates.get(w, 0) > thresh_hold:
                new_doc.append(w)
        new_docs.append(new_doc)
    return new_docs

def read_docs_file(fn):
    # A doc is [word, word, word]
    # docs_file is [doc, doc, doc]
    infile = open(fn, 'r', encoding='utf-8')
    lines = infile.readlines()
    infile.close()
    docs = []
    for line in lines:
        line = line.strip()
        doc = line.split()
        docs.append(doc)
    return docs


if __name__ == "__main__":
    if len(sys.argv) > 1 :
        docs = read_docs_file(sys.argv[1])
        get_tf_idf(docs)
        write_idfrates_file(sys.argv[1] +'.idf')
        write_tfidf_file(sys.argv[1]+'.tfidf')
    else:
        doc_samples = [
    ["data", "databases", "MySQL", "MongoDB", "Python", "language", "studies"],
    ["Big", "data", "Python", "Korean", "studies", "BTS", "K-pop", "K-wave"],
    ["Korean", "studies", "data", "Korean", "language", "K-wave", "K-wave"],
    ["K-wave", "K-drama", "K-movie", "BTS", "Korean", "language", "K-wave", "Python", "data"],
    ["Big", "data", "NoSQL", "MongoDB", "Cassandra", "HBase", "Python", "language", "studies"],
    ["Python", "scikit-learn", "scipy", "numpy", "Python", "pandas", "studies", "data"],
    ["R", "Python", "C++", "statistics", "regression", "probability", "Python", "studies"],
    ["Python", "data", "machine learning", "regression", "decision trees", "libsvm", "studies"],
    ["statistics", "probability", "mathematics", "theory", "data", "studies"],
    ["machine learning", "scikit-learn", "Big", "data", "neural networks", "Python", "studies"],
    ["neural networks", "deep learning", "Big", "data", "artificial intelligence", "Python"],
    ]
        get_tf_idf(doc_samples)
        write_idfrates_file('sample.idf')
        write_tfidf_file('sample.tfidf')
