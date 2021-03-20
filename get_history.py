import tweepy
from credentials import consumer_key, consumer_secret, access_token, access_token_secret



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


def get_raw(userID): 
    userID = "ArunimaKhunteta"


    tweets = api.user_timeline(screen_name=userID, 
                            count=200,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )
    return tweets


def get_needed(tweets):
    n_tweets = []
    for tweet in tweets:
        try:
            n_tweets.append(tweet.full_text)
        except:
            continue
    return n_tweets


if __name__=='__main__':
    screen_name = input("Screen name")
    tweets = get_raw(screen_name)
    n_tweets = get_needed(tweets)
    for tweet in n_tweets:
        print(tweet)

