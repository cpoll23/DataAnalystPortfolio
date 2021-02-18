#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Here is the script written in order to scrape Spotify's Web API for information on specific songs to create my database.



#Importing the necessary packages, including Spotipy specifically for their API. Time imported for the sake of their servers.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time



#Authenticating and connecting to the API using my credentials.
client_id = '92c01bec5f754cc29339516b0c49e9d7'
client_secret = '3f0ef64df7d144c59b08a164db1ed3c5'

client_credentials_manager = SpotifyClientCredentials('92c01bec5f754cc29339516b0c49e9d7',
                                                      '3f0ef64df7d144c59b08a164db1ed3c5')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



#Here we start the scraping by getting Track IDs, making sure our results aren't paginated, as is the default.
def getTrackIDs(user, playlist_id):
    ids = []
    results = sp.user_playlist_tracks(user, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    for item in tracks:
        track = item['track']
        ids.append(track['id'])
    return ids



#The tracks come from a playlist I created in Spotify, scraped with my username and the ID of the playlist.
ids = getTrackIDs('cpoll23', '2dxJRwhQfFLQb3mEiwMeza')



#Now its time to get the specific items we want from our tracks using the IDs we just pulled. We want general info like
#name and release date, but also song features like danceability and loudness, all condensed into a list.
def getTrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']

    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    valence = features[0]['valence']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, acousticness, danceability, energy, liveness, loudness, speechiness, valence, tempo, time_signature]

    return track



#Finally, we loop over the tracks using the function created earlier, and save this all to a csv.
tracks = []
for i in range(len(ids)):
    time.sleep(.1)
    track = getTrackFeatures(ids[i])
    tracks.append(track)

df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'acousticness',
                                   'danceability', 'energy', 'liveness', 'loudness', 'speechiness', 'valence',
                                   'tempo', 'time_signature'])
df.to_csv("daftpunkproject.csv", sep=',', index=False)

