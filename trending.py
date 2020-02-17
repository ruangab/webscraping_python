import requests as req
from bs4 import BeautifulSoup

url = "https://www.youtube.com/feed/trending"
page = req.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

for titles in soup.find_all(class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link'):
    print("")
    print(titles.text)
    
