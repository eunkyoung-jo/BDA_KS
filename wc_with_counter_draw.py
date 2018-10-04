#2018/10

from tokenise_ko_with_nltk import *
all_tokens = tokenise_with_nltk('ko_input.txt')
#all_tokens = tokenise_with_nltk('한국학2017.09.01-2017.09.07.txt')

from collections import Counter
# it gives the sorted result by it's value
w_counts = Counter(all_tokens)

from han_fonts import *
set_Han_font()
draw_bar_chart(w_counts.most_common(7))


