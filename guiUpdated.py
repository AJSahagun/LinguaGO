####NOTE!!####
# to run, install 'tkinter', 'deep_translator', 'ttkwidgets' libraries
from tkinter import *
from tkinter import ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
from deep_translator import GoogleTranslator
from agca_tts import textToSpeech
# window of the app

root = Tk()
root.title('TRANSLATOR PROTOTYPE')
root.configure(background='#1e1e24')
img = PhotoImage(file=r"C:\Users\user\Desktop\Programming\Python\PYCHARM\icon.png")
root.iconphoto(False,img)
# logo thing
root.geometry("882x300")

# Function for lang switch
def switcher ():
    # switch dropdown boxes current value
    temp = combo_1.get()
    combo_1.set(combo_trans.get())
    combo_trans.set(temp)

# function for clear button
def clear():
    txt_box.delete(1.0, END)
    trans_box.delete(1.0, END)

# function for translate button
def translated ():
    # The functionality will be removed here but instead going to be called through an import
    trans_box.delete(1.0, END)

    try:
        # Gets from language keys
        for key, value in lang.items():
            if value == combo_1.get():
                from_language_key = key
        # Gets to language keys
        for key, value in lang.items():
            if value == combo_trans.get():
                to_from_language_key = key

        # translation
        words = GoogleTranslator(source=from_language_key, target=to_from_language_key).translate(txt_box.get(1.0, END))

        # output translated text to screen
        trans_box.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)
    # until here :D  TY

# TEXT TO SPEECH FUNCTION!!
def tts ():
    textToSpeech.speak(txt_box, lang)
    pass




# callout languages
# will be removed and called out from an import instead
lang = language_dict = {
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


# converted to list
lang_list1 = list(lang.values())
lang_list2 = list(lang.values())


# lang_det_list = list(lang_det.values())


# Text box input
txt_box = Text(root, height=10, width=40)
txt_box.grid(row=0, column=0, pady=20, padx=10)


# Translate Button
trans_button = Button(root,
                      text="Translate!",
                      bg="#46474f",
                      fg="#e0e0e0",
                      font=("Helvetica", 24),
                      command=translated)
trans_button.grid(row=0, column=1, padx=10)


# Translated Box output

trans_box = Text(root, height=10, width=40)
trans_box.grid(row=0, column=2, pady=20, padx=10)

# disables inputs to translated box
trans_box.bind("<Button-1>", lambda e: "break")
trans_box.bind("<Key>", lambda e: "break")

# BUTTONS!! KASAMA DITO TEXT TO SPEECH
button_tts1 = Button(root,
                     text="Text to speech",
                     bg="#46474f",
                     fg="#e0e0e0",
                     font=("Helvetica", 15),
                     command=tts)
button_tts1.grid(row=2, column=0, pady=10, padx=5)


button_tts2 = Button(root,
                     text="Text to speech",
                     bg="#46474f",
                     fg="#e0e0e0",
                     font=("Helvetica", 15),
                     command=tts)
button_tts2.grid(row=2, column=2, pady=10, padx=5)

# dito papasok ang language detection para automatic na magshow ang language na tinype mo!
'''
How I envision it to work... 
----------------------|                         |-------------------------|
WORDS to be trans     |                         |                         |
                      |         TRANSLATE       |                         |
                      |                         |                         |
                      |                         |                         |
----------------------|                         |-------------------------|
SPELL CHECKER PROMPT  e.g. Do you mean "spellchecked word "
------------------------------|
COMBO_BOX1/suggested          |      <= Gonna be replaced with suggested note combo box with a note above 
------------------------------|          'Are these the languages you are trying to translate your entry to?'
'''

# CODE OF CUSTOM COMBO BOX THEME BELOW

combo_style = ttk.Style()

#combo_style.theme_create('customStyle', parent='aqua') clam, default, alt, classic, winnative, xpnative, vista

combo_style.theme_use('xpnative')

# COMBO BOXES AKA drop down boxes
# for input
combo_1 = AutocompleteCombobox(root, width=50, completevalues=lang_list1) # shows the languages in dropdown
combo_1.current(10)
combo_1.grid(row=1, column=0)

# for translated output
combo_trans = AutocompleteCombobox(root, width=50, completevalues=lang_list2)
combo_trans.current(10)
combo_trans.grid(row=1, column=2)

# CLEAR BUTTON
clearbutt = Button(root,
                   text="Clear",
                   bg="#46474f",
                   fg="#e0e0e0",
                   command=clear)
clearbutt.grid(row=2, column=1)

# Switch Button
switch_butt = Button(root,
                     text="Switch Language",
                     bg="#46474f",
                     fg="#e0e0e0",
                     command=switcher)
switch_butt.grid(row=1, column=1)





# vital function!! a gui runs in a loop
root.mainloop()