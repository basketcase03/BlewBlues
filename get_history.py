
def get_raw(userID): 
    tweets = api.user_timeline(screen_name=userID, 
                            count=200,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )
    return tweets
