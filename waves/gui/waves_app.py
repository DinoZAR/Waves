from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Interface(BoxLayout):
    pass


class WavesApp(App):
    def build(self):
        return Interface()
