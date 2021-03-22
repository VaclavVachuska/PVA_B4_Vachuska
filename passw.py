from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import random

Window.size = (400, 500)

Builder.load_file('passw.kv')

class MyLayout(Widget):

    def GeneratePassw(self):
        keyword = self.ids.passw_input.text
        array_pass = list(keyword)
        random.shuffle(array_pass)
        password = ''.join(array_pass)
        self.ids.passw_output.text = f'{password}'

    def SavePassw(self):
        f = open("heslo.txt", "w")
        f.write(f'{self.ids.passw_output.text}')
        f.close()

class passw(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    passw().run()