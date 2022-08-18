import requests
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Item:
    def __init__(self, num, name, bid):
         self.num = num
         self.name = name
         self.bid = bid
    
    def info(self):
        return (f"{self.num} | {self.name}: ${self.bid}")
    
    def compare(self, item):
        if self.bid != item.bid:
            return False
        
        return True
    
    def update(self, bid):
        self.bid = bid
        print(self.info())
        print("\r****")


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(300, 768)

if True:
	u = ""
	p = ""


driver.get("https://ontario.hibid.com/")
try:
    login_button = driver.find_element(By.XPATH, "/html/body/app-root/div/header/nav/app-header/div[1]/app-middle-header/div[1]/div/div[3]")

except:
    login_button = driver.find_element(
    	By.XPATH, "/html/body/app-root/div/header/nav/app-header/div[1]/app-top-header/div/div/div[1]/ul/app-user-menu/li/app-login-link/div")

login_button.click()
time.sleep(1)
u_form = driver.find_element(By.XPATH, "/html/body/modal-container/div/div/app-login-container/div/app-login/div[2]/div/div/div[1]/form/div[1]/div/input")
p_form = driver.find_element(By.XPATH, "/html/body/modal-container/div/div/app-login-container/div/app-login/div[2]/div/div/div[1]/form/div[2]/div[1]/input")

u_form.send_keys(u)
p_form.send_keys(p, Keys.ENTER)
time.sleep(1)

driver.get("https://ontario.hibid.com/account/watchlist")
time.sleep(2)

iDict = {}
def check():
    refresh = driver.find_element(
        By.XPATH, "/html/body/app-root/div/main/div/div[1]/app-watch-list-page/div/div[1]/app-watched-search/div[1]/button")
    refresh.click()
    time.sleep(2)
    lot_list = driver.find_element(By.XPATH, "/html/body/app-root/div/main/div/div[1]/app-watch-list-page/div/div[2]/div")

    t_lot_list = lot_list.text
    # print(t_lot_list + "\n\n")
    t_lot_list = t_lot_list.split("\n")
    iList = []
    print("\n-----")

    for n in range(len(t_lot_list)):
        i = t_lot_list[n]
        if "Lot" in i:
            numName = i.split("|")
            num = numName[0]
            name = numName[-1]
        
        elif "Bidding" in i:
            high_bid = i
            iList.append(Item(num.ljust(13, " "), name, high_bid))
            #print(f"#{num}|  {name}: {high_bid}")

        elif "BID" in i:
            high_bid = i.split(" ")[-1]
            iList.append(Item(num.ljust(13, " "), name, high_bid))
            #print(f"#{num}|  {name}: ${high_bid}")


    for item in iList:
        if item.num not in iDict:
            iDict[item.num] = item
            print(iDict[item.num].info())
        
        else:
            existingItem = iDict[item.num]
            if item.bid != existingItem.bid:
                if item.bid == "Bidding Closed" and "FINAL" not in item.bid:
                    try:
                        existingItem.update(f"FINAL: {existingItem.bid}")
                    
                    except:
                        existingItem.update(item.bid)
                
                else:
                    existingItem.update(item.bid)

# for i in iDict:
#     print(iDict[i].info())

while True:
    check()
    for i in range(60, 0, -1):
        print(f"Sleeping ({i})", end="\r")
        time.sleep(1)
