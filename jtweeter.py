import random
import tweepy

def tweet(access_token, access_token_secret, consumer_key, consumer_secret, user_id):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    tweets = api.user_timeline(user_id = user_id, count = 100)
    text = ''
    for status in tweets:
        text += status.text + '\n'
    
    l = 4
    table = generate_markov_table(text, l)
    tweet = generate_markov_text(table, l).split(' ',1)[1].rsplit(' ',1)[0].replace('&amp;','&')
    
    print tweet
    api.update_status(tweet)
    
def generate_markov_table(text, l):
    table = dict()
    
    for i, c in enumerate(text):
        char = text[i:i+l]
        table[char] = dict()
            
    for i, c in enumerate(text):
        o = l
        char_index = text[i:i+l]
        char_count = text[i+o:i+l*2]
       
        if len(char_count) == l: 
            if char_count in table[char_index]:
                table[char_index][char_count] = table[char_index][char_count] + 1
            else:
                table[char_index][char_count] = 1
        
    return table

def generate_markov_text(table, l): 
    char = random.choice(slicedict(table))
    o = char.lstrip()
    for i in range(1, 144/l):
        new_char = return_weighted_char(table[char])
        
        if new_char:
            char = new_char
            o = o + new_char
        else:
            char = random.choice(table.keys())
    
    return o
            
def return_weighted_char(array):
    total = sum(array.values())
    if total == 0:
        return ""
        
    rand = random.randint(1, total)
    for item in array:
        if rand <= array[item]:
            return item
        rand = rand - array[item]
      
def slicedict(d):
    return [key for key, value in d.items() if key.startswith('\n')]