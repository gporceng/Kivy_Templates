from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.graphics import Rectangle

#Window.clearcolor = (.0059,63,255,255)
class JobSearch(App):
    def build(self):
        #returns a window object with all it's widgets

        self.title = 'Simple Label and Button - By Gregory Porceng'
        self.window = FloatLayout(size=(500,500))
        title = Label(text = 'Hello World',
                        size_hint=(.5,.5),
                        pos_hint = {"center_x": 0.5, "center_y":0.80}
                        )
        button_one = Button(text = 'Run',
                        size_hint=(.5,.1),
                        pos_hint = {"center_x": 0.5, "center_y":0.5}
                        )
        

    
        self.window.add_widget(title)
        self.window.add_widget(button_one)
        return self.window

# run
if __name__ == "__main__":
    JobSearch().run()