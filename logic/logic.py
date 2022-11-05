import keyboard
import time
import requests 
from bs4 import BeautifulSoup

def getCode(module):
    url_input = module.split(" ")
    URL = f"https://raw.githubusercontent.com/kausthubh-coder/apcs-codehs/master/{url_input[0]}/{url_input[1]}/{url_input[2]}"
    page = requests.get(URL)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # return soup.get_text()
    page = requests.get(URL)
    return page.text

def getUrl(module):
    url_input = module.split(" ")
    URL = f"https://raw.githubusercontent.com/kausthubh-coder/apcs-codehs/master/{url_input[0]}/{url_input[1]}/{url_input[2]}"
    return URL

def type(code):
    time.sleep(1)
    for i in code.split(" "):
        if i != "" and i != " ":
            print(i)
            keyboard.write(i)
            keyboard.press_and_release('space')
            time.sleep(.5)
    # time.sleep(1)
    # keyboard.write(code)
