import kivy
from kivy.app import App
from kivy.uix.button import Button

class tlacitka(App):

    def build(self):
        tlacitko = Button(text="Zmáčkni mě!")
        return tlacitko

tlacitko1 = tlacitka()
tlacitko1.run()
