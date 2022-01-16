import spotipy
import sys
from spotipy.oauth2 import SpotifyOAuth

scope = "user-modify-playback-state"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'varese'

total = spotify.search(q='track:' + name, type='track')['tracks']['total']
if (total > 1000):
    total = int(total / 10)

if (total > 0):
    results = spotify.search(q='track:' + name, type='track', limit=1, offset=total-1)
    track_uri = results['tracks']['items'][0]['uri']
    album_uri = results['tracks']['items'][0]['artists'][0]['uri']

    # MacBook
    device_id = '83e760a679b4a01af5c48b6dc7a9dfb4d7c08ee4'
    # PhoneyBologna
    #device_id = '0b0c9d95bbeb8fcb45d96561a7080e70b4cf164d'
    spotify.start_playback(device_id=device_id, uris=[track_uri])