
def word_score(x):
    '''scores words based on letters and returns highest scoring word'''
    letters = [chr(i) for i in range(97,123)]
    scores = [i for i in range(1,27)]
    score_table = dict(zip(letters, scores))
    word_lst = x.split()
    word_score = 0
    place = 0

    for word in word_lst:
        score = 0
        for letter in word:
            score += score_table[letter]
        if score > word_score:
            word_score = score
            place = word_lst.index(word)
    return word_lst[place]

print(word_score('oh my goodness what a xylophone'))

def char_count(string):
    '''return number of characters as a dictionary'''
    return {i: string.count(i) for i in string}

print(char_count('hello'))
