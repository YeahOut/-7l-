from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

client_id = "0a3419c6f1934f9c85e6f0381335c2b0"
client_secret = "effc3df0867845fe8434dcb9a263c2bf"

# BTS
lz_uri = 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.artist_top_tracks(lz_uri)

# get top 5 tracks
for track in results['tracks'][:5]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print(sp.audio_features(track['id']))
