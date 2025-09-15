
from pytube import Playlist

u = Playlist("YOUR_PLAYLIST_URL_Here") # in this middle section of double quote there is youtube playlist list which you want to download 

for video in u.videos:
    stream = video.streams.get_highest_resolution()
    stream.download()
