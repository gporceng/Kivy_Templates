from kivy.app import App




class simple4(App):
    def build(self):
        self.title = "Title with buttons and text area - By Gregory Porceng"
    pass


if __name__ == '__main__':
    simple4().run()