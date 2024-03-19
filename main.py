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
import random

winFlag = 0
if (os.name == 'nt'):
    print("Windows")
    filename = 'Config/configWin.json'
    winFlag = 1
elif (os.name == 'posix'):
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
if (iLoad):
    chPath = input("Enter the path to chrome\n")
    if (chPath == "" or chPath == " "):
        exit('no data entered')
    else:
        if (os.path.exists(chPath)):
            print('Chrom path Saved')
        else:
            exit('File not found')
    imgPath = input("Enter the path to image folder\n")
    if (imgPath == "" or imgPath == " "):
        exit('no data entered')
    else:
        if (os.path.exists(imgPath)):
            print('Image path Saved')
        else:
            exit('File not found')
    uname = input("Enter the username\n")
    if (uname == "" or uname == " "):
        exit('no data entered')
    else:
        print('Username Saved')
    pwd = input("Enter the password\n")
    if (pwd == "" or pwd == " "):
        exit('no data entered')
    else:
        print('Password Saved')
    data = {}
    data['initialRun'] = False
    data['chromePath'] = chPath
    data['uname'] = uname
    data['passwd'] = pwd
    data['image'] = imgPath
    writeToJSONFile('./', filename, data)
    exit('Data saved please rerun the program to load the data')

else:
    print("False")
    chPath = configRead['chromePath']
    if (os.path.exists(chPath)):
        print('Chrome Found')
    else:
        exit('File not found not found')
    imgPath = configRead['image']
    if (os.path.exists(imgPath)):
        print('Image Found')
    else:
        exit('Image not found not found')
    uname = configRead['uname']
    passwd = configRead['passwd']
    price = '45'


botOptions = Options()
botOptions.add_argument('--use-fake-ui-for-media-stream')
botOptions.add_argument('--disable-infobars')
botOptions.add_argument('--disable-notifications')
botOptions.add_argument('--disable-blink-features=AutomationControlled')
botOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
botOptions.binary_location = chPath
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
botOptions.add_experimental_option("prefs", prefs)


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

        files = os.listdir(configRead['image'])
        images = [f for f in files if f.endswith(".jpg") or f.endswith(".png")]
        random_img = random.choice(images)
        print(random_img)
        image = configRead["image"]+'\\'+random_img
        pyautogui.typewrite(image, interval=0.2)
        pyautogui.press('enter')

        # add title
        multiTab(5)
        t.sleep(5)
        random_title = random.choice(dataRead['title'])
        print(random_title)
        pyautogui.typewrite(random_title, interval=0.2)

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

        # add description
        pyautogui.press('tab')
        random_desc = random.choice(dataRead['description'])
        print(random_desc)
        pyautogui.typewrite(random_desc, interval=0.2)
        pyautogui.press('tab')

        # add Brand
        pyautogui.press('tab')
        pyautogui.typewrite('Internet', interval=0.2)

        # add tags
        # Traverse through all the items in the tags array
        multiTab(2)
        pyautogui.hotkey('shift', 'tab')
        for tag in dataRead['tags']:
            print(tag)
            pyautogui.typewrite(tag, interval=0.2)
            pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')

        # add location
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('tab')

        # # add delivery method
        # multiTab(5)
        # pyautogui.press('enter')
        # pyautogui.press('tab')

        # press next btn
        multiTab(22)
        pyautogui.press('enter')

        # # publish
        # multiTab(17)
        # pyautogui.press('enter')


fb = facebook()
timesRun = input('Enter the amount of posts you want to create\n')

for i in range(0, timesRun+1):
    fb.login()


t.sleep(20000)
