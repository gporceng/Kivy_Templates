from kivy.app import App
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class simple5(MDApp):
    def build(self):
        self.title = ("Simple 5 Start Menu Design - By Gregory Porceng")
    pass

if __name__ == '__main__':
    simple5().run()