# Libraries to be installed:
#   - deep-translator (translator)
#   - langdetect (language detection)
#   - unidecode, unihandecode (Romanization)
#   - autocorrect (spell checker)
#   - speech_recognition, pyaudio (speech-to-text)
#           *if pyaudio installation error install using wheel file
#   - io, gtts, pygame (text-to-speech)

from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from unidecode import unidecode
from unihandecode import Unihandecoder
from autocorrect import Speller
import speech_recognition as sr
from io import BytesIO
from gtts import gTTS
import pygame
from time import sleep


# Class for all the LinguaGo variables and methods
class LinguaGo:
    # Constructor for instance variables
    def __init__(self):
        self.lang_to_iso = {'Afrikaans': 'af', 'Arabic': 'ar', 'Bulgarian': 'bg', 'Bengali': 'bn', 'Catalan': 'ca',
                            'Czech': 'cs', 'Welsh': 'cy', 'Danish': 'da', 'German': 'de', 'Greek': 'el',
                            'English': 'en', 'Spanish': 'es', 'Estonian': 'et', 'Persian': 'fa', 'Finnish': 'fi',
                            'French': 'fr', 'Gujarati': 'gu', 'Hindi': 'hi', 'Croatian': 'hr',
                            'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kannada': 'kn',
                            'Korean': 'ko', 'Lithuanian': 'lt', 'Latvian': 'lv', 'Macedonian': 'mk', 'Malayalam': 'ml',
                            'Marathi': 'mr', 'Nepali': 'ne', 'Dutch': 'nl', 'Norwegian': 'no', 'Punjabi': 'pa',
                            'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk',
                            'Slovenian': 'sl', 'Somalia': 'so', 'Albanian': 'sq', 'Swedish': 'sv', 'Swahili': 'sw',
                            'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Tagalog': 'tl', 'Turkish': 'tr',
                            'Ukrainian': 'uk', 'Urdu': 'ur', 'Vietnamese': 'vi', 'Classical Chinese': 'zh-CN',
                            'Traditional Chinese': 'zh-TW', 'Auto': 'auto'}
        self.iso_to_lang = {l: k for k, l in self.lang_to_iso.items()}
        self.lang = list(self.lang_to_iso.keys())
        self.raw_lang = list(self.lang)[0:-1]
        self.character = ['Arabic', 'Bengali', 'Bulgarian', 'Classical Chinese', 'Greek', 'Gujarati', 'Hindi',
                          'Japanese', 'Kannada', 'Korean', 'Macedonian', 'Malayalam', 'Marathi', 'Nepali', 'Persian',
                          'Punjabi', 'Russian', 'Tamil', 'Telugu', 'Thai', 'Traditional Chinese', 'Ukrainian', 'Urdu']
        self.spell_support = ['English', 'Polish', 'Turkish', 'Russian', 'Ukrainian', 'Czech',
                              'Portuguese', 'Greek', 'Italian', 'Vietnamese', 'French', 'Spanish']
        DetectorFactory.seed = 0

    def translate(self, text_to_translate, source_lang, target_lang):
        translation = GoogleTranslator(source=self.lang_to_iso[source_lang],
                                       target=self.lang_to_iso[target_lang]).translate(text_to_translate)
        return translation

    def detect(self, text, iso=False):
        if text == '':
            return None
        else:
            if iso:
                return detect(text)
            else:
                return self.iso_to_lang[detect(text)]

    def romanize(self, text_to_romanize, target_language):
        try:
            romanized = Unihandecoder(lang=self.lang_to_iso[target_language]).decode(text_to_romanize)
        except FileNotFoundError:
            return unidecode(text_to_romanize)
        else:
            return romanized

    @staticmethod
    def correct(text, lang='en', fast=False):
        correction = Speller(lang, fast=fast)
        return correction(text)

    @staticmethod
    def recognize():
        with sr.Microphone() as source:
            audio = sr.Recognizer().listen(source)
            return sr.Recognizer().recognize_google(audio)

    def speak(self, text, language='auto', wait=True):
        if language == 'Auto' or language == 'auto':
            language = self.detect(text)
        voice = BytesIO()
        tts = gTTS(text,
                   lang=self.lang_to_iso[language])
        tts.write_to_fp(voice)

        pygame.init()
        play_end = pygame.USEREVENT
        pygame.mixer.music.set_endevent(play_end)
        pygame.mixer.music.load(voice, 'mp3')
        pygame.mixer.music.play()

        if wait:
            playing = True
            while playing:
                for event in pygame.event.get():
                    if event.type != play_end:
                        sleep(1)
                    else:
                        playing = False

        pygame.quit()
