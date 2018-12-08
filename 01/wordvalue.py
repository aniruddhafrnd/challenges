from data import DICTIONARY, LETTER_SCORES

word_list = []
word_value = {}
#max_value = ''


def load_words():
    """Load dictionary into a list and return list"""
    #pass
    with open(DICTIONARY, "r") as f:
        for line in f:
            word_list.append(line.strip("\n"))

    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    mywrdlist = list(word)
    i,mysum = 0,0
    #print(word)
    while i < len(mywrdlist) :
        #print (type(mywrdlist[i].upper()))
        if (mywrdlist[i].isalpha()):
            mysum += LETTER_SCORES[mywrdlist[i].upper()]
        i += 1
    return mysum




def max_word_value(argwordlist=word_list):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    for word in argwordlist:
        mywrdlist = list(word)
        i,mysum = 0,0
        #print(word)
        while i < len(mywrdlist) :
            #print (type(mywrdlist[i].upper()))
            if (mywrdlist[i].isalpha()):
                mysum += LETTER_SCORES[mywrdlist[i].upper()]
            i += 1
            #print("i is:-", i)
            word_value[word] = mysum


    max_value = max(word_value, key = lambda key: word_value[key])

    return max_value
    pass

if __name__ == "__main__":
    #load_words()
    #calc_word_value()
    #max_word_value()
    #print(word_list[:10])
    #print(word_value)

    pass # run unittests to validate
