from kivy.app import App
from kivy.uix.button import Button

class WavesApp(App):
    def build(self):
        return Button(text='Hello World')

WavesApp().run()
