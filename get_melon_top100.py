from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

client_id = "0a3419c6f1934f9c85e6f0381335c2b0"
client_secret = "effc3df0867845fe8434dcb9a263c2bf"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#kor
URI = "spotify:playlist:6kbzPEHj3uMPRFsR3v6xzE"

playlist = sp.playlist_items(URI)
cnt = 1
for cur_song in playlist['items']:
    id = cur_song['track']['id']
    track = sp.track(id)
    artist = track['artists'][0]['name']
    name = track['album']['name']
    key = sp.audio_features(id)[0]['key']
    print(cnt," ################################")
    print("artist :", artist)
    print("name :", name)
    print("key :", key,"\n")
    cnt += 1
