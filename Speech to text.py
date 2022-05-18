# Before running: Install "deep-translator" and "langdetect" library
from deep_translator import GoogleTranslator
from langdetect import detect
import speech_recognition as sr
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
# Converted the keys and values of 'language_dict' as a list for the Language Menu
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

class Speech_to_Text:
    r = sr.Recognizer()

    target_language = input("\nTranslate to (language): ")
    #where speech to text happens
    with sr.Microphone() as source:
        print ("Speak: ")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print (speech_text)

        except sr.UnknownValueError:
            ("couldn't recognize the voice properly")
        except sr.RequestError:
            ("Couldn't reqeust result form Google")

    detected = detect (speech_text)
    print(f"""
Language detected: {language_dict[detected]}
Translated: {GoogleTranslator(target=target_language).translate(speech_text)}""")
