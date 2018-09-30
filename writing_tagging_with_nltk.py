#2018/09/17
import nltk

my_file = open('transcript.txt')
rst_file = open('out.txt', 'w')
for l in my_file:
    tokens = nltk.word_tokenize(l)
    #print(tokens)
    rst_file.write(' '.join(tokens) +'\n')
    tagged_tokens = nltk.pos_tag(tokens)
    #print(tagged_tokens)
    tagged = ''
    for (w, t) in tagged_tokens:
        tagged += w +'/' + t +'+'
    tagged = tagged[:-1]
    rst_file.write(tagged+'\n')

my_file.close()
rst_file.close()


