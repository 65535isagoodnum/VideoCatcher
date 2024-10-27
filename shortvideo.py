import json
import random
import requests

with open("source.json", "r") as f:
    json_data = json.load(f)

headers = {"User-Agent": random.choice(json_data["headers"])}


class ShortVideoCatcher:
    def __init__(self, video_url):
        self.url = video_url
        self.response = None

    def catch(self):
        self.response = requests.get(url=self.url, headers=headers)
        print(self.response)
        return self

    def save(self, name: str):
        video_data = self.response.content
        with open("out/" + name + ".mp4", "wb") as f:
            f.write(video_data)


if __name__ == '__main__':
    url = input()
    ShortVideoCatcher(url).catch().save("video1")
