import jtweeter

access_token = "TWITTER_APP_ACCESS_TOKEN"
access_token_secret = "TWITTER_APP_ACCESS_TOKEN_SECRET"
consumer_key = "TWITTER_APP_CONSUMER_KEY"
consumer_secret = "TWITTER_APP_CONSUMER_SECRET"
user_id = 000000000 #user id of twitter user to simulate.

def main():
    jtweeter.tweet(access_token, access_token_secret, consumer_key, consumer_secret, user_id)
    
if __name__ == '__main__':
    main()