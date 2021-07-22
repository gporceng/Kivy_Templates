from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from functools import partial

import random
import time

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):

    def __init__(self,**kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        self.displayScreenThenLeave()

    def displayScreenThenLeave(self):
        # 'time.sleep(3)' is a stand-in for "execute some code here"
        time.sleep(3)
        self.changeScreen()

    # I want this function to send the user back to ScreenOne.
    def changeScreen(self):
        pass

class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)

class ScreensApp(App):

    def build(self):
        m = Manager(transition=NoTransition())
        return m

if __name__ == "__main__":
    ScreensApp().run()