import sys,os,string
import spacy
import nltk
from spacy.lang.en import English
from difflib import SequenceMatcher

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

NUM_TWEETS = 100
USR1_KEYWORDS = []
USR2_KEYWORDS = []

def tokenize1(mylist):
    parser = English()
    tokens = parser(mylist)

    for token in tokens:
        if token.orth_.isspace():
            continue
        # elif token.like_url:
        #     USR1_KEYWORDS.append('URL')
        # elif token.orth_.startswith('@'):
        #     USR1_KEYWORDS.append('SCREEN_NAME')
        else:
            USR1_KEYWORDS.append(token.lower_)


def tokenize2(mylist):
    parser = English()
    tokens = parser(mylist)

    for token in tokens:
        if token.orth_.isspace():
            continue
        # elif token.like_url:
        #     USR2_KEYWORDS.append('URL')
        # elif token.orth_.startswith('@'):
        #     USR2_KEYWORDS.append('SCREEN_NAME')
        else:
            USR2_KEYWORDS.append(token.lower_)


def get_lemma(word):
    #nltk.download('wordnet')
    from nltk.corpus import wordnet as wn

    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lastN_tweets(user1, user2):
    ##populate usr1 and usr2 globle list with tweets word in small case

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    api = tweepy.API(auth)

    usr1tweets = api.user_timeline(screen_name=user1,count=NUM_TWEETS)
    usr2tweets = api.user_timeline(screen_name=user2, count=NUM_TWEETS)

    usr1lst = [t.text.split(" ") for t in usr1tweets]
    usr2lst = [t.text.split(" ") for t in usr2tweets]

    makeflat = lambda abc: [ item for sublist in abc for item in sublist]

    flatlist1 = makeflat(usr1lst)
    flatlist2 = makeflat(usr2lst)

    flatstr1 = " ".join(str(x) for x in flatlist1)
    flatstr2 = " ".join(str(x) for x in flatlist2)
    tokenize1(flatstr1)
    tokenize2(flatstr2)

    #nltk.download('stopwords')
    stop_wrd = set(nltk.corpus.stopwords.words('english'))

    #print(stop_wrd)

    #print(type(USR1_KEYWORDS))

    tokens = [ token for token in USR1_KEYWORDS if len(token) > 4]
    tokens = [ token for token in tokens if token not in stop_wrd ]
    usr1_final_tokens =  "".join(str(e) for e in [get_lemma(token) for token in tokens])


    tokens = [ token for token in USR2_KEYWORDS if len(token) > 4]
    tokens = [ token for token in tokens if token not in stop_wrd ]
    usr2_final_tokens = "".join( str(e) for e in [ get_lemma(token) for token in tokens])

    #print(usr1_final_tokens)
    #print(usr2_final_tokens)

    cmp = SequenceMatcher(None,sorted(usr1_final_tokens),sorted(usr2_final_tokens)).ratio()

    print(user1,"and",user2, "matching percentage is",cmp*100)




        #usr1raw_str.append(t.text)

    pass

    #print("user1 string is:{}".format(usr1raw_str))

    #print(string.punctuation)



def similar_tweeters(user1, user2):

    ##get last N tweets of usr1 and usr2
    get_lastN_tweets(user1, user2)



    pass

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
    #     sys.exit(1)
    #
    # user1, user2 = sys.argv[1:3]

    # user1 = 'bbelderbos'
    user1 = 'pybites'
    user2 = 'importpython'


    similar_tweeters(user1, user2)
