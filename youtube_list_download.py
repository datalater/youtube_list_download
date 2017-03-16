import requests
import re
from bs4 import BeautifulSoup

def parsing_list(list_url):
    resp = requests.get(list_url).text
    soup = BeautifulSoup(resp, 'lxml')

    youtube_url = "https://www.youtube.com/"
    for link in soup.select('.yt-uix-sessionlink'):
        if "watch" in link.get('href'):
            if link.get('title') is not None:
                print(link.get('title'),"\n","- "+youtube_url + link.get('href'))
    

# list_url = "https://www.youtube.com/user/goodboy1384/videos"
list_url = str(input("youtube_url을 입력하세요." +"ex) https://www.youtube.com/user/goodboy1384/videos"+"\n"+":"))
parsing_list(list_url)
