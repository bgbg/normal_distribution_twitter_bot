#!/usr/local/bin/python2

import tweepy

from configobj import ConfigObj
import os


class TwitterAPI:
    def __init__(self, config):
        consumer_key = config['consumer_key']
        consumer_secret = config['consumer_secret']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = config['access_token']
        access_token_secret = config['access_token_secret']
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    import numpy as np
    import time
    file_dir = '/Users/boris/workspace/normal_distribution_twitter_bot/src'
    fn_config = os.path.join(file_dir, 'normal_distribution_twitter_bot.ini')
    config = ConfigObj(fn_config)
    if np.random.rand() < 0.7:
        twitted = str(np.random.randn())
        sleep_seconds = np.random.randint(1, 6)
        time.sleep(sleep_seconds)
        twitter = TwitterAPI(config)
        twitter.tweet(twitted)
    else:
        twitted = '_____________'
    open(os.path.join(file_dir, "./bot.log"), 'a').write("%s: %s\n" % (time.asctime(), twitted))
    print('done')
