from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.graphics import Rectangle


from kivy.app import App


class simple2(App):
    def build(self):
        self.title = "Label and 3 buttons - By Gregory Porceng"

    pass


if __name__ == '__main__':
    simple2().run()