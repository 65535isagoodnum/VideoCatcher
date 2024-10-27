import os
import subprocess

import requests
from requests import Response
import json
import random
import requests

with open("source.json", "r") as f:
    json_data = json.load(f)


# noinspection PyShadowingNames
def load_source() -> dict:
    return json_data


def get_header() -> dict:
    return {
        "User-Agent": random.choice(json_data["headers"]),
        "Referer": "https://space.bilibili.com/414691362/video"
    }


def get_prox() -> dict:
    return {
        "http": f"http://{random.choice(json_data["proxies"])}",
        "https": f"http://{random.choice(json_data["proxies"])}"
    }


def connect(url, headers: dict = None, proxie: dict = None) -> Response:
    return requests.get(url, headers=headers, proxies=proxie)


def save(name: str, video_data: bytes, audio_data: bytes) -> None:
    with open("out/temp/temp.mp4", mode="wb") as v:
        v.write(video_data)

    with open("out/temp/temp.mp3", mode="wb") as m:
        m.write(audio_data)

    ffmpeg = f"ffmpeg -i out\\temp\\temp.mp4 -i out\\temp\\temp.mp3 -acodec copy -vcodec copy out\\{name}.mp4"
    subprocess.run(ffmpeg)
    os.remove("out/temp/temp.mp3")
    os.remove("out/temp/temp.mp4")
