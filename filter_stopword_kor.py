#from: https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
#2018/12

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('korean'))
example_sent = "우리는 오늘 불용어 처리를 배운다. 그리고 이것은 예문이다"
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(word_tokens)
print(filtered_sentence)
