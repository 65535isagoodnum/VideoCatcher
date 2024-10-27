import re
from collections import defaultdict

from util import *


class BilibiliCatcher:
    regax = r"window.__playinfo__=(.*?)</script>"

    def __init__(self, video_url):
        self.response = defaultdict(Response)
        self.url = video_url

    def catch(self, proxies=None):
        self.response["web"] = connect(self.url, headers=get_header())

        html_data = self.response["web"].text

        play_info = re.findall(BilibiliCatcher.regax, html_data)[0]
        data = json.loads(play_info)

        video_url = data['data']['dash']['video'][0]['baseUrl']
        audio_url = data['data']['dash']['audio'][0]['baseUrl']

        self.response["video"] = connect(video_url, headers=get_header())
        self.response["audio"] = connect(audio_url, headers=get_header())
        return self

    def save(self, name):
        save(name, self.response["video"].content, self.response["audio"].content)

    def getstatu(self):
        print(self.response)


if __name__ == '__main__':
    url = "https://www.bilibili.com/video/BV1hAy5YVEFK/"
    catcher = BilibiliCatcher(url)
    catcher.catch().getstatu()
    catcher.save("first_video")
