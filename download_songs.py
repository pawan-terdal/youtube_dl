from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests

import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
fhand = open()
html = requests.get("https://www.youtube.com/results?search_query=despacito")
soup = BeautifulSoup(html.text,"html.parser")
videos = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
print(videos[0]['href'])


def download():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com'+videos[0]['href']])

