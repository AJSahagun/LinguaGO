# Before running: Install "deep-translator", "langdetect","io","gtts",and "pygame" library
from time import time
from deep_translator import GoogleTranslator
from langdetect import detect
from io import BytesIO
from gtts import gTTS
import pygame
import time

#create the audio
class textToSpeech:

    def speak(self, language):
        mp3_fo = BytesIO()
        tts = gTTS(text='self', lang=language, slow=False)
        tts.write_to_fp(mp3_fo)
        # tts = gTTS(self)
        #play the audio
        pygame.init()
        pygame.mixer.init()
        sound = speak(self, detect(self))
        pygame.mixer.music.load(sound, 'mp3')
        pygame.mixer.music.play()
        #wait for audio to be played
        time.sleep(2)
        return mp3_fo
    #  Translation is done inside the print function using f-string
    '''print(f"""
    Translated: {GoogleTranslator(target=target_language).translate(text_to_translate)}""")'''