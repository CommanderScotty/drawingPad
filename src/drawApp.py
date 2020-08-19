from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.actionbar import ActionBar, ActionGroup, ActionButton, ActionLabel, ActionView
from kivy.factory import Factory as F

class DrawPad(BoxLayout):
    def __init__(self):
        super().__init__(orientation = 'vertical')
        # Set up action bar
        ribbon = F.ActionBar()
        ribbonView = F.ActionView()
        ap = F.ActionPrevious(title='hi', with_previous=False)
        ap.app_icon = ''
        
        ## Set up action bar buttons
        pencil = ActionButton(text='Pen')
        eraser = ActionButton(text='Eraser')
        
        ## Add components to GUI
        ribbonView.add_widget(ap)
        ribbonView.add_widget(pencil)
        ribbonView.add_widget(eraser)
        
        ribbon.add_widget(ribbonView)

        self.add_widget(ribbon)

        # Set up drawing canvas
        self.add_widget(Label(text="hi"))
