#from: https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
#2018/12
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
example_sent = "This is a sample sentence, showing off the stop words filtration."
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(word_tokens)
print(filtered_sentence)
