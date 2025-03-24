# -*- coding: utf-8 -*-
import requests

url = "https://www.pearvideo.com/video_1798786"
contId = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8350906657635253"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    "referer": "https://www.pearvideo.com/video_1798786"
}

response = requests.get(videoStatusUrl, headers=headers)
dic = response.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

with open("./video/a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
