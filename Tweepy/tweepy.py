import tweepy
# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
api.update_status('Hello Python Central!')



# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))