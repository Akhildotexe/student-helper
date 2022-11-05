import flet
from flet import Column, ElevatedButton, Text, TextField
import webbrowser
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
    time.sleep(1)
    for i in code.split(" "):
        if i != "" and i != " ":
            print(i)
            keyboard.write(i)
            keyboard.press_and_release('space')
            time.sleep(.5)

def main(page):

    page.title = "student helper - by kausthbuh"
    module = TextField(label="number name")
    greetings = Column()
    t = Text(value="type unit mod assignment  example: unit-3 3.2 discounts.java",size=30,weight="bold")
    # t2 = Text(value="type esc to start typing")

    def btn_click(e):
        webbrowser.open(getUrl(module.value))
        
    def btn_click2(e):
        code = getCode(module.value)
        type(code)

    page.add(
        t,
        module,
        ElevatedButton("get code", on_click=btn_click),
        ElevatedButton("type code", on_click=btn_click2),
        greetings,
    )

flet.app(target=main)

