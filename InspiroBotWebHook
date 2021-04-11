import requests
import time

c = "webhook link"

while True:
    time.sleep(10)
    link = requests.get("https://inspirobot.me/api?generate=true").text
    requests.post(c, data={"content": link})
