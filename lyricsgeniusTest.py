
##NOT PART OF MAIN
#Input artist and song and get lyrics printed back

from lyricsgenius import Genius
import time
token = 'pM7WjImnWP7CNs2Yar2_UQ7msm2ROVuaNZD-7E9pTbWv8s5IgyqBRZnjUkH9XiqT'
genius = Genius(token)

artist = "Tally Hall"
songTitle = "&"

artist = genius.search_artist(artist, max_songs=0, sort="title")
#print(artist.songs)


song = artist.song(songTitle)
print(song.lyrics)
Lyrics = song.lyrics
x = Lyrics.splitlines() #Returns as list so each line can be called individually
print(x)

print(x[4])

for i in x:
    print(i)
    time.sleep(1)