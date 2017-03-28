import requests
import re
from bs4 import BeautifulSoup
import youtube_dl # pip install --upgrade youtube-dl


def list_download(mp4_list):
    for mp4 in mp4_list:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([mp4])


def single_download(single_url):
    try:
        list_download([single_url])
    except requests.exceptions.MissingSchema:
        print("올바른 url이 아닙니다. ex) https://www.youtube.com/watch?v=hy0rMH2yeg8")
    except KeyboardInterrupt:
        print("Keybaord에 의해 중단되었습니다.")


def parsing_list(playlist_url):
    try:
        resp = requests.get(playlist_url).text
        soup = BeautifulSoup(resp, 'lxml')

        youtube_url = "https://www.youtube.com"
        for link in soup.select('.yt-uix-sessionlink'):
            if "watch" in link.get('href'):
                if link.get('title') is not None:
                    print(link.get('title'),"\n","- "+youtube_url + link.get('href'))
                    mp4_list.append(youtube_url+link.get('href'))

        mp4_list_count = len(mp4_list)
        user_question = str(input("총 {} 개의 영상이 있습니다. 모두 다운로드 하시겠습니까? [Y/N]: ".format(mp4_list_count)))
        print(user_question)
        if user_question == "y" or user_question == "Y":
            print("중간에 멈추려면 ctrl+c를 입력하세요.")
            list_download(mp4_list)
        else:
            print("프로그램을 멈추겠습니다.")
    except requests.exceptions.MissingSchema:
        print("올바른 url이 아닙니다. ex) https://www.youtube.com/user/goodboy1384/videos")
    except KeyboardInterrupt:
        print("Keybaord에 의해 중단되었습니다.")

if __name__ == "__main__":
    # playlist_url = "https://www.youtube.com/user/goodboy1384/videos"
    # single_url = "https://www.youtube.com/watch?v=hy0rMH2yeg8"
    mp4_list = []
    user_option = input("재생목록으로 다운로드 하려면 'Y', 개별 영상 URL로 다운로드 하려면 'N'을 입력해주세요. \n: ")
    if user_option == ("y" or "Y"):
        playlist_url = str(input("="*40+"\n"+"youtube 재생목록 url을 입력하세요."+"\n"+"ex) https://www.youtube.com/user/goodboy1384/videos"+"\n"+"="*40+"\n"+":"))
        parsing_list(playlist_url)
    else:
        single_url = str(input("="*40+"\n"+"youtube 개별영상 url을 입력하세요."+"\n"+"ex) https://www.youtube.com/watch?v=hy0rMH2yeg8"+"\n"+"="*40+"\n"+":"))
        single_download(single_url)
