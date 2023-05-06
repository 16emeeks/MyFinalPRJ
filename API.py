# Spotify authentification and current playing track request
# Resources
# https://developer.spotify.com/documentation/web-api/reference/get-the-users-currently-playing-track
# https://developer.spotify.com/documentation/web-api/tutorials/code-flow
# Chat GPT

import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth
from pub import run
from credentials import my_client_id, my_client_secret, redirect_uri

#credentials
CLIENT_ID = my_client_id
CLIENT_SECRET = my_client_secret
REDIRECT_URI = redirect_uri

#account authentification
def account_auth():
    # Create a SpotifyOAuth object
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope='user-read-playback-state', show_dialog=True)

    my_tokens = sp_oauth.get_cached_token()

    #Refress access token if expired
    if sp_oauth.is_token_expired(my_tokens):
        # The access token is expired, get a new one
        my_tokens = sp_oauth.refresh_access_token(my_tokens['refresh_token'])
        sp = spotipy.Spotify(auth=my_tokens)

    else :
        sp = spotipy.Spotify(auth=my_tokens)

    return my_tokens

#return current playing track
def current_track():

    my_tokens = account_auth()
    #Get request to Spotify API for JSON file of current song playing
    url = 'https://api.spotify.com/v1/me/player/currently-playing'

    access_token = my_tokens['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers) # Get request

    if response.status_code == 200:
        data = response.json()
        Song_Title = data['item']['name']
        artists = data['item']['artists'][0]['name']
        print("Downlaoding Track")
        print("Current track: " + str(Song_Title) + " by " + str(artists))

        run(str(Song_Title) + " by " + str(artists)) #MQTT publish

        return str(Song_Title) + " by " + str(artists) # Search Phrase
    else:
        print(f"Error: {response.status_code}")
        print("Probably no Song playing")
