from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox

root = Tk()
root.title('TRANSLATOR PROTOTYPE')
root.configure(background='#1e1e24')
root.geometry("958x400")

# FUNCTIONS FOR BUTTONS AND FUNCTIONALITY

def translate():
    pass

def text_to_speech_input():
    pass

def text_to_speech_output():
    pass

def spellcheck_input():
    pass

def speech_to_text():
    pass

def clear():
    pass

def switcher():
    pass


# GUI

# INPUT TEXT BOX
input_box = Text(root,
                 height=10,
                 width=40,
                 font='Arial')

input_box.grid(row=0, column=0, pady=20, padx=10)

# TRANSLATE BUTTON
trans_butt = Button(root,
                text="Translate!",
                bg="#46474f",
                fg="#e0e0e0",
                font=("Helvetica", 24),
                command=translate)
trans_butt.grid(row=0, column=1, padx=10)

# OUTPUT TEXT BOX
output_box = Text(root,
                  height=10,
                  width=40,
                  font='Arial')
output_box.grid(row=0, column=2, pady=20, padx=10)

# DISABLE INPUT IN OUTPUT BOX

output_box.bind("<Button-1>", lambda e: 'break')
output_box.bind("<Key>", lambda e: "break")

spllchck_photo = PhotoImage(file="icon-spellcheck.png").subsample(2, 2)
button_spellcheck = Button(root,
                           image=spllchck_photo,
                           bg="#e0e0e0",
                           fg="#e0e0e0",
                           command=spellcheck_input)
button_spellcheck.grid(row=4, column=0, pady=5, padx=5)

tts_photo = PhotoImage(file="icons-tts.png").subsample(2, 2)
button_tts1 = Button(root,
                     image=tts_photo,
                     bg="#e0e0e0",
                     fg="#e0e0e0",
                     command=text_to_speech_input)
button_tts1.grid(row=2, column=0, pady=5, padx=5)

button_tts2 = Button(root,
                     image=tts_photo,
                     bg="#e0e0e0",
                     fg="#e0e0e0",
                     command=text_to_speech_output)
button_tts2.grid(row=2, column=2, pady=5, padx=5)

stt_photo = PhotoImage(file="icon-stt.png").subsample(2, 2)
button_stt = Button(root,
                     image=stt_photo,
                     bg="#e0e0e0",
                     fg="#e0e0e0",
                     command=speech_to_text)
button_stt.grid(row=3, column=0, pady=5, padx=5)


lang_list = ['']

# COMBO BOXES

combo_style = ttk.Style()
combo_style.theme_use('xpnative')

combo_1 = AutocompleteCombobox(root, width=20, completevalues=lang_list) # shows the languages in dropdown
combo_1.current(0)
combo_1.grid(row=1, column=0)

combo_trans = AutocompleteCombobox(root, width=20, completevalues=lang_list)
combo_trans.current(0)
combo_trans.grid(row=1, column=2)

# CLEAR BUTTON

clearbutt = Button(root,
                   text="Clear",
                   bg="#46474f",
                   fg="#e0e0e0",
                   command=clear)
clearbutt.grid(row=2, column=1)

# SWITCH BUTTON

switch_photo = PhotoImage(file="icon-swap.png").subsample(2, 2)
switch_butt = Button(root,
                     image=switch_photo,
                     bg="#e0e0e0",
                     fg="#e0e0e0",
                     command=switcher)
switch_butt.grid(row=1, column=1)

root.mainloop()
