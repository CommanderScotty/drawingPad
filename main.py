from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.config import Config

from src.drawApp import DrawPad

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class MainWindow(App):
    def build(self):
        self.icon = 'assets/feather.ico'
        return DrawPad()

MainWindow().run()
