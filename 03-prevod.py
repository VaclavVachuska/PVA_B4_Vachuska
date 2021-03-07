import kivy
kivy.require('1.10.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.logger import Logger
from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')

class Box(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Box, self).__init__(*args, **kwargs)

    def buttonpress(self):
        hodnota = self.vstup.text
        euronaczk = str(round(float(self.vstup.text) * 26.17, 2))
        czknaeuro = str(round(float(self.vstup.text) / 26.17, 2))
        usdnaczk = str(round(float(self.vstup.text) * 21.68, 2))
        czknausd = str(round(float(self.vstup.text) / 21.68, 2))

        self.ids.euro1.text = f'{hodnota} euro je: {euronaczk} czk'
        self.ids.euro2.text = f'{hodnota} czk je: {czknaeuro} euro'
        self.ids.usd1.text = f'{hodnota} usd je: {usdnaczk} czk'
        self.ids.usd2.text = f'{hodnota} czk je: {czknausd} usd'

    def quit(self,*arvs):
        App.get_running_app().stop()

class PrevodApp(App):
    def on_stop(self):
        Logger.critical("good bye")
    def build(self):
        return Box()

if __name__ == '__main__':
        PrevodApp().run()
