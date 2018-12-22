from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100



Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        """Get handle and optional max_id.
        Use tweepy.OAuthHandler, set_access_token and tweepy.API
        to create api
        Use _get_tweets() helper to get a list of tweets.
        Save the tweets as data/<handle>.csv"""
        #
        #print("11111")

        self.handle = handle
        self._auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)

        #print(type(auth))
        self._auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
        self.output_file = '{}.{}'.format(os.path.join(DEST_DIR, self.handle), EXT)


        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""
        #pass
        api = tweepy.API(self._auth)



        tweets = api.user_timeline(screen_name=handle,count=NUM_TWEETS)

        tweet_list = []
        #print(tweets)

        #tweet_text = [ tweet.text for tweet in tweets]

        counter = 0


        for t in tweets:

            tweet_text = t.text
            tweet_id_str = t.id_str
            tweet_created = t.created_at

            Tweet = (tweet_id_str,tweet_created,tweet_text)

            #print(Tweet)
            # print("Tweet no --- {} -- ".format(counter))
            # print("Tweet text is -- {} \n".format(tweet_text))
            # print("Tweet id_str is -- {} \n".format(tweet_id_str))
            # print("Tweet created is -- {} \n".format(tweet_created))

            counter +=1
            #Tweet.__add__(mytuple)
            tweet_list.append(Tweet)

        #print("*****",Tweet,"****")

        return tweet_list

        # abc = (Tweet(s.id_str, s.created_at, s.text.replace('\n', ' ')) for s in tweets)
        #
        # print(abc)
        #
        # return abc



    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets.
        If you use a namedtuple get the column names with Tweet._fields.
        Otherwise define them as: id_str created_at text
        You can use writerow for the header, writerows for the rows"""
        with open(self.output_file,'w', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(Tweet._fields)
            #writer.writerow(row)

            for row in self._tweets:writer.writerow(row)
            #print(type(self._tweets))



    def __len__(self):
        """See http://pybit.es/python-data-model.html"""
        return len(self._tweets)
        #pass

    def __getitem__(self, pos):
        """See http://pybit.es/python-data-model.html"""
        return self._tweets[pos]


if __name__ == "__main__":


    for handle in ('pybites', 'bbelderbos', 'SrBachchan'):
        print('--- {} ---'.format(handle))

        user = UserTweets(handle)


        # for tw in user[:3]:
        #
        #     print(tw)
        #print()
