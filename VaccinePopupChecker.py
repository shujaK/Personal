import praw
import time
import requests

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    username= '',
    password= "",
    user_agent="")
sub = reddit.subreddit("toronto")
id = "md2mm4"
code = 'l6r'
age = 18
webhook = "https://discord.com/api/webhooks/830933284925472771/1CCVnfhaPGgDIh3qiHJ7gmWd2hAWmiinvRtFptpGeSRnv0lUdhiyZYEcCSPzD2EfwBX4"
sleepTime = 3600

def getContent(id):
    content = reddit.submission(id).selftext
    
    return content.split('\n')

def cutContent(list, code, age):
    cutList = []
    for i in list:
        if code.lower() in i.lower():
            if str(age) in i:
                cutList.append(i)
    
    return cutList

def lToStr(list):
    str = ''
    for i in list:
        str += i
        str += '\n---\n'
    
    return str

def webhookTrigger(webhook, content):
    requests.post(webhook, data={"name": "vax update", "content": f"@everyone , new vax update: \n{content}\n\n@  https://old.reddit.com/r/toronto/comments/md2mm4/toronto_vaccination_registration_information_and/"})

listCache = cutContent(getContent(id), code, age)

while True:
    print('Checking...')
    currentList = cutContent(getContent(id), code, age)
    if currentList != listCache:
        print('Change detected, triggering webhook')
        webhookTrigger(webhook, lToStr(currentList))
        listCache = currentList[:]
    
    else:
        print(f'No change, resting for {sleepTime} seconds...')
    time.sleep(sleepTime)
