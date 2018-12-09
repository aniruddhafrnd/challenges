#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
import string, sys, time

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7
IPWRDSZ = 0


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    myletters = random.choices(POUCH,k=NUM_LETTERS)

    print (myletters)

    return myletters

def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        word = input("please enter your word from above letters drawn:-")
        if (_validation(word, draw) == True):
            break
        else:
           decision = input("Your entered word is Not in dictionary, do you want to play again(Y/N):-")
           if decision.upper() == 'N':
               sys.exit()

    return word



def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    print (list(word))
    print((all(letter in list(map(str.lower, draw)) for letter in list(word))))
    print(word in DICTIONARY)

    return ((all(letter in list(map(str.lower, draw)) for letter in list(word)) and (word in DICTIONARY)))

    #return ((all(letter in list( draw) for letter in list(word)) and (word in DICTIONARY)))
    pass


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    #pass
    allwords = _get_permutations_draw(draw)

    #print('all words are :- {}'.format(allwords))
    #print(type(DICTIONARY))

    return list(set(allwords).intersection(DICTIONARY))



def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""



    draw = list(map(str.lower,draw))
    print(draw)

    # a1 = list(map("".join,itertools.permutations(draw,1)))
    # a2 = list(map("".join,itertools.permutations(draw,2)))
    # a3 = list(map("".join,itertools.permutations(draw,3)))
    # a4 = list(map("".join,itertools.permutations(draw,4)))

    # print (a1,a2,a3,a4)
    allperms = []
    i = 0
    while i <= len(draw):

        if i != 0:
            #print('value of i:{}'.format(i))
            var2 = list(map("".join, itertools.permutations(draw, i)))
            #print("words here are ", var2)
            allperms.extend(var2)
            #allperms.
        i = i + 1

    #print("All permutations are :- ", allperms)
    #return list(map("".join,itertools.permutations(draw,IPWRDSZ)))
    return allperms




# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))
    print(type(draw))

    word = input_word(draw)
    global IPWRDSZ
    IPWRDSZ= len(word)
    print("word size is :-",IPWRDSZ)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    print(possible_words)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
