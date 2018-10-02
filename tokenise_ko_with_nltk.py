#2018/10
import nltk

def tokenise_with_nltk(infn):
    my_file = open(infn, encoding='utf-8')
    all_tokens = [] # for a list of all tokens from all lines
    for l in my_file:
        tokens = nltk.word_tokenize(l)
        all_tokens.extend(tokens)

    my_file.close()
    return all_tokens

def write_tokenised(all_t, outfn):
    rst_file = open(outfn, 'w', encoding='utf-8')
    '''you should add a line to write all_t to rst_file
    hint is 'use join() function'
    Have a look at 'ko_out.txt' '''
    rst_file.close()

if __name__ == "__main__":
    all_tokens=tokenise_with_nltk('ko_input.txt')
    write_tokenised(all_tokens, 'ko_out.txt')
    print(all_tokens)

