import requests as req
from bs4 import BeautifulSoup

# url do site
url = "https://www.youtube.com/feed/trending"

# baixando o conteúdo do site
page = req.get(url)

# pegando o conteúdo do site e transferindo para o analizador
soup = BeautifulSoup(page.text, 'html.parser')

#pegando todos os conteúdos das div's com a seguinte classe
for titles in soup.find_all(class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link'):
    print("")
    print(titles.text)
    
