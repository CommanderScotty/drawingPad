from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DrawPad(BoxLayout):
    def __init__(self):
        super().__init__()
        self.add_widget(Label(text="hi"))
