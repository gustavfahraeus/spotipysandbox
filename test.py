import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = '8e0ef5ab14b54e40ac3431781bdd6d6f'
SPOTIFY_CLIENT_SECRET = '5c91cc6ba00d4c42813022b41f3f5330'

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,client_secret=SPOTIFY_CLIENT_SECRET,scope=scope,redirect_uri='http://localhost:8888/callback'))

results = sp.current_user_saved_albums(limit=50, offset=0)
for item in results['items']:
    print(item['album']['name'])
    anotherResult = sp.album_tracks(item['album']['id'])['items']
    for result in anotherResult:
        pprint.pprint('* ' + result['name'])
    print()
   