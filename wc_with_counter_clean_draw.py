#2018/10

from tokenise_ko_with_nltk import *
#all_tokens = tokenise_with_nltk('ko_input.txt')
all_tokens = tokenise_with_nltk('한국학.txt')

from collections import Counter
# it gives the sorted result by it's value

from han_fonts import *
set_Han_font()

def clean_tokens(all_t):
    '''
    ignore = ['"', '\'', ',', '.', ' ', '“', '”', '‘', '’', '?', '!', '@', '#', '$', '%', '&', '(', ')']
    c_tokens = [w for w in all_t if w not in ignore]
    return c_tokens
    '''
    ignore = list('''!()-=+[]{};:'"\,<>./?@#$%^&*_~“”‘’''')
    c_tokens = [w for w in all_t if w not in ignore]
    print(c_tokens)
    print(ignore)
    return c_tokens

wc_tokens = clean_tokens(all_tokens)

w_freq = Counter(wc_tokens)
draw_bar_chart(w_freq.most_common(7))

