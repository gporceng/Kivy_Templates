from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

#Window.clearcolor = (.0059,63,255,255)
class JobSearch(App):
    def build(self):
        #returns a window object with all it's widgets

        self.title = 'Job Search Visualizer - By Gregory Porceng'
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.95, 0.85)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.50}
        self.window.padding = [0,-45]
        return self.window

# run
if __name__ == "__main__":
    JobSearch().run()