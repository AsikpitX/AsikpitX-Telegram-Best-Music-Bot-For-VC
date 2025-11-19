import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

def search_spotify_track(track_name):
    results = sp.search(q=track_name, limit=1, type='track')
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return f"{track['name']} {track['artists'][0]['name']}"
    return None
