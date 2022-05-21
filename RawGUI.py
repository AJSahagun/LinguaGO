from tkinter import *
from tkinter import ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox

root = Tk()
root.title('LinguaGO')
root.configure(background='#1e1e24')
icon = PhotoImage(file=r"C:\Users\user\Desktop\Programming\Python\PYCHARM\L.png")
# a raw string of the file path to be recognized as icon
root.iconphoto(False, icon)
root.geometry("824x350")

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
input_box.grid(row=1, columnspan=2, padx=10, pady=10)

translate_photo = PhotoImage(file="icon-trans.png").subsample(2, 2)
# TRANSLATE BUTTON
trans_butt = Button(root,
                image=translate_photo,
                bg="#e0e0e0",
                fg="#46474f",
                command=translate)
trans_butt.grid(row=1, column=3, padx=10, pady=10)


# OUTPUT TEXT BOX
output_box = Text(root,
                  height=10,
                  width=40,
                  font='Arial')
output_box.grid(row=1, column=4, padx=10, pady=10)

# DISABLE INPUT IN OUTPUT BOX

output_box.bind("<Button-1>", lambda e: 'break')
output_box.bind("<Key>", lambda e: "break")

spllchck_photo = PhotoImage(file="icon-spellcheck.png").subsample(2, 2)
button_spellcheck = Button(root,
                           image=spllchck_photo,
                           bg="#e0e0e0",
                           fg="#46474f",
                           command=spellcheck_input)
button_spellcheck.grid(row=2, columnspan=2, padx=5, pady=5)

tts_photo = PhotoImage(file="icon-tts.png").subsample(2, 2)
button_tts1 = Button(root,
                     image=tts_photo,
                     bg="#e0e0e0",
                     fg="#46474f",
                     command=text_to_speech_input)
button_tts1.grid(row=2, columnspan=1, padx=5, pady=5)


button_tts2 = Button(root,
                     image=tts_photo,
                     bg="#e0e0e0",
                     fg="#46474f",
                     command=text_to_speech_output)
button_tts2.grid(row=2, column=4, padx=5, pady=5)


stt_photo = PhotoImage(file="icon-stt.png").subsample(2, 2)
button_stt = Button(root,
                     image=stt_photo,
                     bg="#e0e0e0",
                     fg="#46474f",
                     command=speech_to_text)
button_stt.grid(row=2, column=1, padx=5, pady=5)



lang_list = ['']

# COMBO BOXES

combo_style = ttk.Style()
combo_style.theme_use('xpnative')

combo_1 = AutocompleteCombobox(root, width=30, completevalues=lang_list) # shows the languages in dropdown
combo_1.current(0)
combo_1.grid(row=3, columnspan=3, pady=10, padx=10)


combo_trans = AutocompleteCombobox(root, width=30, completevalues=lang_list)
combo_trans.current(0)
combo_trans.grid(row=3, column=4, padx=10, pady=10)


# CLEAR BUTTON

clearbutt = Button(root,
                   text="Clear",
                   bg="#46474f",
                   fg="#e0e0e0",
                   command=clear)
clearbutt.grid(row=2, column=3, padx=10, pady=10)


# SWITCH BUTTON

switch_photo = PhotoImage(file="icon-swap.png").subsample(2, 2)
switch_butt = Button(root,
                     image=switch_photo,
                     bg="#e0e0e0",
                     fg="#46474f",
                     command=switcher)
switch_butt.grid(row=3, column=3, pady=5, padx=5)


root.mainloop()
