import gtts
from playsound import playsound
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class VraagApp(App):
    def build(self):
        self.vragen = self.lees_vragen_uit_bestand("vragen_antwoorden.txt")
        self.index = 0

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.vraag_label = Label(text=self.vragen[self.index], font_size=20)
        self.volgende_knop = Button(text="Volgende", size_hint=(1, 0.2))
        self.volgende_knop.bind(on_press=self.volgende_vraag)

        self.layout.add_widget(self.vraag_label)
        self.layout.add_widget(self.volgende_knop)

        self.voorlees_vraag(self.vragen[self.index], self.index)

        return self.layout

    def lees_vragen_uit_bestand(self, bestandsnaam):
        with open(bestandsnaam, 'r', encoding='utf-8') as file:
            vragen = file.readlines()
        return [vraag.strip() for vraag in vragen if vraag.strip() != ""]

    def voorlees_vraag(self, vraag, index):
        bestand_naam = f"vraag_{index}.mp3"
        tts = gtts.gTTS(vraag, lang='nl')
        tts.save(bestand_naam)
        playsound(bestand_naam)
        os.remove(bestand_naam)

    def volgende_vraag(self, instance):
        self.index += 1
        if self.index < len(self.vragen):
            self.vraag_label.text = self.vragen[self.index]
            self.voorlees_vraag(self.vragen[self.index], self.index)
        else:
            self.vraag_label.text = "Einde van de vragenlijst!"
            self.volgende_knop.disabled = True

if __name__ == '__main__':
    VraagApp().run()
