import requests
import re
from bs4 import BeautifulSoup

def parsing_list(list_url):
    list_url = "https://www.youtube.com/playlist?list=PLXJ3W1lEGK8VD5JJlAqoe5ieJ2XbCzQbo"

    resp = requests.get(list_url).text
    soup = BeautifulSoup(resp, 'lxml')

    for tr in soup.select('.yt-uix-tile'):
        data_title = tr.get('data-title')
        print(data_title)


# list_url = "https://www.youtube.com/user/goodboy1384/videos"
