#Gets lyrics for currently playing song from Genius, prints it according to timestamp of playing song
#Lines are printed one character at a time with a loop
#gets song time variable, song, artist from main program

from lyricsgenius import Genius
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import time
import arcade

#Genius Keys
geniusToken = 'pM7WjImnWP7CNs2Yar2_UQ7msm2ROVuaNZD-7E9pTbWv8s5IgyqBRZnjUkH9XiqT'
genius = Genius(geniusToken)

#Spotipy Keys
clientID='1257d28231e947ef8e13189d2f0dea34'
clientSecret='2ec39e604aa0488d8b3cfd324cb46c4e'
RDU='http://example.com'

def lyricsCrawler(dt, artist, title):
    artist = genius.search_artist(artist, max_songs=0, sort="title")
    song = artist.song(title)
    lyrics = song.lyrics
    Lyrics = lyrics.splitlines()

    for i in Lyrics:
        #return(i)
        #time.sleep(1)
        arcade.draw_text(i, 100, i*50, arcade.color.GREEN, 10)
