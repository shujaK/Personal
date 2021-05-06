from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import requests

webhook = "LINK TO DISCORD WEBHOOK"
print('Attempting to connect webdriver')
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)
print('Webdriver connected\n\n---')

UTORID = ''
PASSWORD = ''

xPath = {"ECE159H1": "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/history-academic/div/div[2]/div/div[4]/table/tbody/tr/td/table/tbody/tr[2]/td[5]",
         "ESC102H1": "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/history-academic/div/div[2]/div/div[4]/table/tbody/tr/td/table/tbody/tr[3]/td[5]",
         "ESC190H1": "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/history-academic/div/div[2]/div/div[4]/table/tbody/tr/td/table/tbody/tr[4]/td[5]",
         "ESC195H1": "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/history-academic/div/div[2]/div/div[4]/table/tbody/tr/td/table/tbody/tr[5]/td[5]",
         "MAT185H1": "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/history-academic/div/div[2]/div/div[4]/table/tbody/tr/td/table/tbody/tr[6]/td[5]",
         "MSE160H1": "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/history-academic/div/div[2]/div/div[4]/table/tbody/tr/td/table/tbody/tr[7]/td[5]"}

def gotoPage():
    browser.get("https://acorn.utoronto.ca/sws/#/history/academic")
    time.sleep(3)

def enterCreds():
    user = browser.find_element_by_name('j_username')
    user.send_keys(UTORID)
    passw = browser.find_element_by_name('j_password')
    passw.send_keys(PASSWORD)
    passw.send_keys(Keys.RETURN)
    #print('SLEEPING FOR 5 SECS')
    time.sleep(5)
    #print('NAVIGATING TO ACADEMIC HISTORY PAGE')
    gotoPage()
 
def checkPage():
    if browser.title == 'Academic History':
        return True
    
    return False

def refresh():
    browser.refresh()
    time.sleep(3)

def checkMark(xpath):
    grade = browser.find_element_by_xpath(xpath)
    if grade.text != 'IPR':
        return True
    
    return False

def sendReq(webhook, course):
    requests.post(webhook, data={"content": f"@everyone {course} marks out"})



c = 0
run = True

while run:
    SLEEP_TIME = 300  # time to sleep in seconds
    if checkPage():
        c += 1
    
        print(f'\nCheck #{c}, as of {datetime.now().strftime("%H:%M:%S")}')
        for key in xPath.keys():
            try:
                check = checkMark(xPath[key])

            except:
                print('    ERROR, SKIPPING')
                check = False

            if check:
                sendReq(webhook, key)
                xPath.pop(key)
        
            else:
                print(f"    {key} marks NOT out")
                time.sleep(2)
        
        refresh()
        print(f"    #Sleeping for {SLEEP_TIME} seconds#")
        time.sleep(SLEEP_TIME)

    else:
        gotoPage()
        enterCreds()
