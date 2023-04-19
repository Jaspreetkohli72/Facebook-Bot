import json
import os
from datetime import datetime
import pyautogui
import time as t
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

winFlag = 0
if(os.name == 'nt'):
    print("Windows")
    filename = 'Config/configWin.json'
    winFlag = 1
elif(os.name == 'posix'):
    print("linux")
    filename = 'Config/configLin.json'


def writeToJSONFile(path, filename, data):
    filePathNameWExt = './'+path+'/'+filename
    with open(filePathNameWExt, 'w')as fp:
        json.dump(data, fp)


configRead = json.load(
    open(filename, 'r+'))
dataRead = json.load(
    open('assets/data.json', 'r+'))


iLoad = configRead['initialRun']
if(iLoad):
    chPath = input("Enter the path to chrome\n")
    if(chPath == "" or chPath == " "):
        exit('no data entered')
    else:
        if(os.path.exists(chPath)):
            print('Chrom path Saved')
        else:
            exit('File not found')
    uname = input("Enter the username\n")
    if(uname == "" or uname == " "):
        exit('no data entered')
    else:
        print('Username Saved')
    pwd = input("Enter the password\n")
    if(pwd == "" or pwd == " "):
        exit('no data entered')
    else:
        print('Password Saved')
    data = {}
    data['initialRun'] = False
    data['chromePath'] = chPath
    data['uname'] = uname
    data['passwd'] = pwd
    writeToJSONFile('./', filename, data)
    exit('Data saved please rerun the program to load the data')

else:
    print("False")
    chPath = configRead['chromePath']
    if(os.path.exists(chPath)):
        print('Chrome Found')
    else:
        exit('File not found not found')
    uname = configRead['uname']
    passwd = configRead['passwd']
    price = '45'


botOptions = Options()
botOptions.add_argument('--use-fake-ui-for-media-stream')
botOptions.add_argument('--disable-infobars')
botOptions.add_argument('--disable-notifications')
botOptions.binary_location = chPath


def multiTab(num):
    i = 0
    while i <= num:
        pyautogui.press('tab')
        i += 1


class dateTimeCls:

    def dateFn(self):
        now = datetime.now()
        current_date = now.strftime("%b%d%Y%H_%M_%S_%f")
        return current_date


class facebook:

    def __init__(self):
        self.bot = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=botOptions)

    def login(self):
        bot = self.bot
        bot.get('https://www.facebook.com')

        # find username
        bot.find_element(By.XPATH, '//*[@id="email"]')
        pyautogui.typewrite(uname, interval=0.2)
        pyautogui.press('tab')

        # find password
        bot.find_element(By.XPATH, '//*[@id="pass"]')
        pyautogui.typewrite(passwd, interval=0.2)
        pyautogui.press('enter')

        # goto marketplace
        bot.implicitly_wait(20)
        bot.get('https://www.facebook.com/marketplace/create/item')

        # add photo
        bot.implicitly_wait(20)
        multiTab(10)
        pyautogui.press('enter')
        t.sleep(2)
        pyautogui.typewrite(
            dataRead['image'], interval=0.2)
        pyautogui.press('enter')

        # add title
        multiTab(3)
        t.sleep(5)
        for title in dataRead['title']:
            print(title)
            pyautogui.typewrite(title, interval=0.2)

        # add price
        pyautogui.press('tab')
        pyautogui.typewrite(price, interval=0.2)

        # add category
        pyautogui.press('tab')
        pyautogui.press('enter')
        multiTab(14)
        pyautogui.press('enter')

        # add condition
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('enter')

        # add Brand
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite('Internet', interval=0.2)

        # add description
        pyautogui.press('tab')
        for desc in dataRead['description']:
            # Traverse through all the items in the tags array
            print(desc)
            pyautogui.typewrite(desc, interval=0.2)
        pyautogui.press('tab')
        pyautogui.press('tab')

        # add tags
        # Traverse through all the items in the tags array
        for tag in dataRead['tags']:
            print(tag)
            pyautogui.typewrite(tag, interval=0.2)
            pyautogui.press('enter')
        pyautogui.press('tab')

        # add location
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('tab')

        # add delivery method
        multiTab(5)
        pyautogui.press('enter')
        pyautogui.press('tab')

        # press next btn
        multiTab(3)
        pyautogui.press('enter')


fb = facebook()
fb.login()


t.sleep(20000)
