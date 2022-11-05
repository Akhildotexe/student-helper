import flet
from flet import Column, ElevatedButton, Text, TextField
import logic.codehs_logic as codehs_logic
import webbrowser

def main(page):

    module = TextField(label="number name")
    greetings = Column()
    t = Text(value="type unit mod assignment  example: unit-3 3.2 discounts.java",size=30,weight="bold")
    # t2 = Text(value="type esc to start typing")

    def btn_click(e):
        webbrowser.open(codehs_logic.getUrl(module.value))
        
    def btn_click2(e):
        code = codehs_logic.getCode(module.value)
        codehs_logic.type(code)

    page.add(
        t,
        module,
        ElevatedButton("get code", on_click=btn_click),
        ElevatedButton("type code", on_click=btn_click2),
        greetings,
    )

flet.app(target=main)