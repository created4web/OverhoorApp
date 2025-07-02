from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import gtts
import os
from kivy.core.audio import SoundLoader

class VraagLezer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.vragen = self.lees_vragen('vragen_antwoorden.txt')
        self.index = 0

        self.vraag_label = Label(text="Druk op 'Volgende' om te starten", font_size='20sp')
        self.add_widget(self.vraag_label)

        self.button = Button(text="Volgende vraag", size_hint=(1, 0.3), font_size='20sp')
        self.button.bind(on_press=self.volgende_vraag)
        self.add_widget(self.button)

    def lees_vragen(self, bestandsnaam):
        with open(bestandsnaam, 'r', encoding='utf-8') as file:
            return [regel.strip() for regel in file.readlines() if regel.strip()]

    def volgende_vraag(self, instance):
        if self.index < len(self.vragen):
            vraag = self.vragen[self.index]
            self.vraag_label.text = vraag
            self.speel_vraag_af(vraag)
            self.index += 1
        else:
            self.vraag_label.text = "Alle vragen zijn gesteld."
            self.button.disabled = True

    def speel_vraag_af(self, tekst):
        filename = "vraag.mp3"
        tts = gtts.gTTS(tekst, lang='nl')
        tts.save(filename)
        sound = SoundLoader.load(filename)
        if sound:
            sound.play()

class VraagApp(App):
    def build(self):
        return VraagLezer()

if __name__ == '__main__':
    VraagApp().run()
