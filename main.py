import flet
from flet import Column, ElevatedButton, Text, TextField
import logic
import webbrowser

def main(page):

    module = TextField(label="unit module codehs assignment")
    greetings = Column()
    t = Text(value="type unit module codehs assignment. example: unit-3 3.3 battleships-move.java: ",size=30,weight="bold")
    # t2 = Text(value="type esc to start typing")

    def btn_click(e):
        webbrowser.open(logic.getUrl(module.value))
    
    def btn_click2(e):
        code = logic.getCode(module.value)
        logic.type(code)

    page.add(
        t,
        module,
        ElevatedButton("get code", on_click=btn_click),
        ElevatedButton("type code", on_click=btn_click2),
        greetings,
    )

flet.app(target=main)