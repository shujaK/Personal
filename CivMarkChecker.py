from selenium import webdriver
import tkinter as tk
from tkinter import ttk
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from datetime import datetime

print('Attempting to connect webdriver')
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)
print('Webdriver connected\n\n---')

UTORID = ''
PASSWORD = ''

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

def checkMark():
    #print('SLEEPING FOR 3 SECS')
    browser.refresh()
    time.sleep(3)
    grade = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/history-academic/div/div[2]/div/div[3]/table/tbody/tr/td/table/tbody/tr[2]/td[5]")
    if grade.text != 'IPR':
        return True
    
    print('    Not yet...')
    return False

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x",padx=100,  pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


c = 0
run = True

while run:
    SLEEP_TIME = 300  # time to sleep in seconds
    if checkPage():
        c += 1
        print(f'\nCheck #{c}, as of {datetime.now().strftime("%H:%M:%S")}')
        try:
            check = checkMark()
        
        except:
            print('    ERROR, SKIPPING')
            SLEEP_TIME = 1 # time to sleep in seconds
            check = False
			
        if check:
            browser.quit()
            print('CIV MARK OUT!!!')
            popupmsg('CIV MARK OUT!!!')
            run = False

        else:
            print(f'    Trying again in {SLEEP_TIME}s')
            time.sleep(SLEEP_TIME)

    else:
        gotoPage()
        enterCreds()
