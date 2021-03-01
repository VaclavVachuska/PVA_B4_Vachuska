import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,700)

Builder.load_file('kalkulacka.kv')

class MujLayout(Widget):
    def clear(self):
        self.ids.kalkulacka_input.text = '0'

    def button_press(self, button):
        hodnota = self.ids.kalkulacka_input.text

        if "error" in hodnota:
            hodnota = ''

        if hodnota == "0":
            self.ids.kalkulacka_input.text = ''
            self.ids.kalkulacka_input.text = f'{button}'
        else:
            self.ids.kalkulacka_input.text = f'{hodnota}{button}'

    def znamenko(self, sign):
        hodnota = self.ids.kalkulacka_input.text
        self.ids.kalkulacka_input.text = f'{hodnota}{sign}'

    def rovnase(self):
        hodnota = self.ids.kalkulacka_input.text
        try:
            odpoved = eval(hodnota)
            self.ids.kalkulacka_input.text = str(odpoved)
        except:
            self.ids.kalkulacka_input.text = "error"

class Kalkulacka(App):
    def build(self):
        return MujLayout()

if __name__ == '__main__':
    Kalkulacka().run()
