#!/bin/python3

from collections import deque

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.
    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    s = 0
    for x,y in zip(word1, word2):
        if x != y:
            s+=1
        else:
            pass
    if s > 1:
        return False
    else:
        return True



def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    for i in range(len(ladder)-1):
        if _adjacent(ladder[i], ladder[i+1]) == False:
            return False
    return True

from collections import deque

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:
    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file
    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)
    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    with open(dictionary_file) as df:
        dictionary=df.read()
    dictionary=dictionary.split('\n')
    st = []
    st.append(start_word)
    qu = deque()
    qu.append(st)
    while len(qu)!=0:
        d_st = qu.popleft()
        if _adjacent(d_st[-1],end_word): 
            d_st.append(end_word)
            return d_st

        for word in dictionary:
            if _adjacent(word, d_st[-1]):
                qu.append(d_st+[word])
                dictionary.remove(word)
    return 'None'
