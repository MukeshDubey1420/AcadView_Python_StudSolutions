#
# import tweepy
#
#
# #Authentication consumer info
# consumer_key='consumer_key'
# consumer_secret='consumer_secret'
#
# #Authentication Acess Tokens
# access_token='access_token'
# access_token_secret='access_token_secret'
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
#
# tweets=api.search('#NotWithoutMyDog', lang="en", count=10, tweet_mode="extended")
# # print(tweets)
# for tweet in tweets:
#     print("--------------------")
#     print(tweet.full_text)
#     print("--------------------\n")
#
#
#
# status = "Tweet tweet"
# api.update_status(status=status)

#Create from https://developer.spotify.com
#pip install spotipy

# import spotipy
#
# from spotipy.oauth2 import SpotifyClientCredentials
#
# client_credentials_manager = SpotifyClientCredentials(client_id='Insert your client id', client_secret='Insert your client secret')
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# playlists = sp.user_playlists('2slphad0xy3sag1v3hzhb8iqb')
#
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
