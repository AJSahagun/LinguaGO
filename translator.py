# Before running: Install "deep-translator" and "langdetect" library
from time import time
from deep_translator import GoogleTranslator
from langdetect import detect
from io import BytesIO
from gtts import gTTS
import pygame
import time
# Dictionary for Language ISO code (also used in Language Menu)
language_dict = {
    "af": "Afrikaans", "ar": "Arabic", "bg": "Bulgarian", "bn": "Bengali", "ca": "Catalan", "cs": "Czech",
    "cy": "Welsh", "da": "Danish", "de": "German", "el": "Greek", "en": "English", "es": "Spanish",
    "et": "Estonian", "fa": "Persian", "fi": "Finnish", "fr": "French", "gu": "Gujarati", "he": "Hebrew",
    "hi": "Hindi", "hr": "Croatian", "hu": "Hungarian", "id": "Indonesian", "it": "Italian", "ja": "Japanese",
    "kn": "Kannada", "ko": "Korean", "lt": "Lithuanian", "lv": "Latvian", "mk": "Macedonian", "ml": "Malayalam",
    "mr": "Marathi", "ne": "Nepali", "nl": "Dutch", "no": "Norwegian", "pa": "Punjabi", "pl": "Polish",
    "pt": "Portuguese", "ro": "Romanian", "ru": "Russian", "sk": "Slovak", "sl": "Slovenian", "so": "Somalia",
    "sq": "Albanian", "sv": "Swedish", "sw": "Swahili", "ta": "Tamil", "te": "Telugu", "th": "Thai",
    "tl": "Tagalog", "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu", "vi": "Vietnamese",
    "zh-cn": "Classical Chinese", "zh-tw": "Traditional Chinese"
}
# Converted the keys and values of 'language_dict' for the Language Menu
keys = list(language_dict.keys())
values = list(language_dict.values())

iterator = 0  # Variable for iterating the keys and values list continuously
# Loop for printing the Language Menu
for row in range(11):
    for col in range(5):
        #  F-string Alignment syntax:
        #  {:<(width)} - left
        #  {:^(width)} - center
        #  {:>(width)} - right
        print(f"[{keys[iterator] : ^5}] {values[iterator] : <17}", end=' ')
        iterator += 1
    print()
#create the audio
def speak(text, language):
    mp3_fo = BytesIO()
    tts = gTTS(text=text, lang=language,slow=False)
    tts.write_to_fp(mp3_fo)
    return mp3_fo

target_language = input("\nTranslate to (language): ")
text_to_translate = input("Translate (text): ")
detected = detect(text_to_translate)
tts = gTTS(text_to_translate)
#play the audio
pygame.init()
pygame.mixer.init()
sound = speak(text_to_translate,detected)
pygame.mixer.music.load(sound, 'mp3')
pygame.mixer.music.play()
#wait for audio to be played
time.sleep(2)
#  Translation is done inside the print function using f-string
print(f"""
Language detected: {language_dict[detected]}
Translated: {GoogleTranslator(target=target_language).translate(text_to_translate)}""")
