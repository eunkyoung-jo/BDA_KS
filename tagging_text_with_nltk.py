#2018/09/17
import nltk
text = nltk.word_tokenize('and now for something completely different')
print(text)
tagged_text=nltk.pos_tag(text)
print(tagged_text)

my_file = open(input('type file name:'))
for l in my_file:
    tokens = nltk.word_tokenize(l)
    print(tokens)
    tagged_tokens = nltk.pos_tag(tokens)
    print(tagged_tokens)


