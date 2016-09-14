# jtwitter-simulator
Simulate a twitter user with your Raspberry Pi    

First install tweepy on your pi with the following command `sudo pip install tweepy`

Create an e-mail account with Gmail or any mail service you like. Use that email to register a new account with Twitter. When creating a Twitter account **be sure to enter a phone number** or else you will not ba able to add a Twitter app.

Having done this, log in as your bot and go to https://apps.twitter.com/app/new. Fill out the form, (Callback URL is not necessary). Once complete click on the *Keys and Access Tokens* tab. Generate the access tokens by clicking on the button near the bottom. Copy the Access Token, Access Token Secret, Consumer Key (API Key), and Consumer Secret (API Secret) and paste them into the code in the following lines
```
access_token = "TWITTER_APP_ACCESS_TOKEN"
access_token_secret = "TWITTER_APP_ACCESS_TOKEN_SECRET"
consumer_key = "TWITTER_APP_CONSUMER_KEY"
consumer_secret = "TWITTER_APP_CONSUMER_SECRET"
```

Add your script to a cronjob with the command `/usr/bin/python /path/to-bot/sim.py` and follow your new bot. Add `>> /path/to-log/sim.log` to the command to log the tweets to that file.
