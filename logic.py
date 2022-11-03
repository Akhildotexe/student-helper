import keyboard
import time
import requests 
from bs4 import BeautifulSoup

def getCode(module):
    url_input = module.split(" ")
    URL = f"https://raw.githubusercontent.com/kausthubh-coder/apcs-codehs/master/{url_input[0]}/{url_input[1]}/{url_input[2]}"
    page = requests.get(URL)

    return page.text

def getUrl(module):
    url_input = module.split(" ")
    URL = f"https://raw.githubusercontent.com/kausthubh-coder/apcs-codehs/master/{url_input[0]}/{url_input[1]}/{url_input[2]}"
    return URL
    
def type(code):
    for i in code.split(" "):
        keyboard.write(i)
        time.sleep(.5)
        keyboard.press_and_release('space')
