from tkinter import *
from tkinter import ttk, messagebox
import speech_recognition
from ttkwidgets.autocomplete import AutocompleteCombobox
from linguago import LinguaGo

root = Tk()
root.title('LinguaGO')
root.configure(background='#1e1e24')
icon = PhotoImage(file=r"L.png")
# a raw string of the file path to be recognized as icon
root.iconphoto(False, icon)
root.geometry("824x350")
lg = LinguaGo()


# FUNCTIONS FOR BUTTONS AND FUNCTIONALITY
def translate():
    output_box.delete(1.0, END)
    trans_lang = combo_trans.get()
    source_lang = combo_1.get()
    text_to_translate = input_box.get(1.0, END)
    translation = lg.translate(text_to_translate, source_lang, trans_lang)
    output_box.insert(1.0, translation)
    detect()
    if trans_lang in lg.character:
        label2.set(f"Romanization: {lg.romanize(translation, trans_lang)}")


def detect(show=True):
    if combo_1.get() == 'Auto':
        detected = lg.detect(input_box.get(1.0, 'end-1c'))
        if show:
            label1.set(f"Detected Language: {detected}")
        return 'English' if detected is None else detected
    else:
        return combo_1.get()


def text_to_speech_input():
    if input_box.get(1.0, END) == '\n':
        messagebox.showerror('Error', "No Text Found.")
    else:
        lg.speak(input_box.get(1.0, 'end-1c'), combo_1.get())


def text_to_speech_output():
    if output_box.get(1.0, END) == '\n':
        messagebox.showerror('Error', "No Text Found.")
    else:
        lg.speak(output_box.get(1.0, END), combo_trans.get())


def spellcheck_input():
    lang = detect()
    text = input_box.get(1.0, 'end-1c')
    if lang in lg.spell_support:
        label1.set(f"Spell Checked: {lg.correct(text, lg.lang_to_iso[lang])}")
    else:
        messagebox.showinfo('Notice', f"Spellchecking {lang} is not supported.\n\n"
                                      f"Supported languages:\n"
                                      f" {', '.join(lg.spell_support)}")


def speech_to_text():
    try:
        text = lg.recognize()
    except speech_recognition.UnknownValueError:
        messagebox.showerror('Error', "Couldn't recognize the voice properly.")
    except speech_recognition.RequestError:
        messagebox.showerror('Error', "Couldn't request result from Google.")
    else:
        input_box.insert(1.0, text)


def clear():
    input_box.delete(1.0, END)
    output_box.delete(1.0, END)
    label1.set('')
    label2.set('')


def switcher():
    temp_text_box = input_box.get(1.0, 'end-1c')
    temp_combo = detect(show=False)
    input_box.delete(1.0, END)
    label1.set('')
    input_box.insert(1.0, output_box.get(1.0, 'end-1c'))
    combo_1.set(combo_trans.get())
    output_box.delete(1.0, END)
    label2.set('')
    output_box.insert(1.0, temp_text_box)
    combo_trans.set(temp_combo)


# GUI
st = ttk.Style()
st.theme_use('xpnative')
# TEXT BOXES
# INPUT TEXT BOX
input_box = Text(root,
                 height=10,
                 width=40,
                 font='Arial')
input_box.grid(row=1, columnspan=2, padx=10, pady=10)
translate_photo = PhotoImage(file="icon-trans.png").subsample(2, 2)

# OUTPUT TEXT BOX
output_box = Text(root,
                  height=10,
                  width=40,
                  font='Arial')
output_box.grid(row=1, column=4, padx=10, pady=10)
# DISABLE INPUT IN OUTPUT BOX
output_box.bind("<Button-1>", lambda e: 'break')
output_box.bind("<Key>", lambda e: 'break')

# LABELS
label1 = StringVar()
label2 = StringVar()

# LABEL 1
Label(root,
      textvariable=label1,
      wraplength=300,
      fg='white',
      font='lato',
      bg='#1e1e24', ).grid(row=2, columnspan=2)

# LABEL 2
Label(root,
      textvariable=label2,
      wraplength=300,
      fg='white',
      font='lato',
      bg='#1e1e24',).grid(row=2, column=4, columnspan=2)

# BUTTONS
# TRANSLATE BUTTON
trans_butt = Button(root,
                    image=translate_photo,
                    bg="#e0e0e0",
                    fg="#46474f",
                    command=translate)
root.bind('<Return>', lambda e: translate())
trans_butt.grid(row=1, column=3, padx=10, pady=10)

# TTS BUTTON 1
tts_photo = PhotoImage(file="icon-tts.png").subsample(2, 2)
button_tts1 = Button(root,
                     image=tts_photo,
                     bg="#e0e0e0",
                     fg="#46474f",
                     command=text_to_speech_input)
button_tts1.grid(row=4, columnspan=1, padx=5, pady=5)

# SPELL CHECK BUTTON
spllchck_photo = PhotoImage(file="icon-spellcheck.png").subsample(2, 2)
button_spellcheck = Button(root,
                           image=spllchck_photo,
                           bg="#e0e0e0",
                           fg="#46474f",
                           command=spellcheck_input)
button_spellcheck.grid(row=4, columnspan=2, padx=5, pady=5)

# STT BUTTON
stt_photo = PhotoImage(file="icon-stt.png").subsample(2, 2)
button_stt = Button(root,
                    image=stt_photo,
                    bg="#e0e0e0",
                    fg="#46474f",
                    command=speech_to_text)
button_stt.grid(row=4, column=1, padx=5, pady=5)

# CLEAR BUTTON
clearbutt = Button(root,
                   text="Clear",
                   bg="#46474f",
                   fg="#e0e0e0",
                   command=clear)
clearbutt.grid(row=2, column=3, padx=10, pady=10)

# TTS BUTTON 2
button_tts2 = Button(root,
                     image=tts_photo,
                     bg="#e0e0e0",
                     fg="#46474f",
                     command=text_to_speech_output)
button_tts2.grid(row=4, column=4, padx=5, pady=5)

# SWITCH BUTTON
switch_photo = PhotoImage(file="icon-swap.png").subsample(2, 2)
switch_butt = Button(root,
                     image=switch_photo,
                     bg="#e0e0e0",
                     fg="#46474f",
                     command=switcher)
switch_butt.grid(row=3, column=3, pady=5, padx=5)


# COMBO BOXES
# SOURCE COMBO BOX
combo_1 = AutocompleteCombobox(root, width=30, completevalues=lg.lang)  # shows the languages in dropdown
combo_1.current(3)
combo_1.grid(row=3, columnspan=3, pady=10, padx=10)

# TRANSLATION COMBO BOX
combo_trans = AutocompleteCombobox(root, width=30, completevalues=lg.raw_lang)
combo_trans.current(0)
combo_trans.grid(row=3, column=4, padx=10, pady=10)

root.mainloop()
