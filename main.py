from tkinter import *
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
FRENCH_WORDS_FILE = "./data/french_words.csv"

# --------DATA---------

data = pd.read_csv(FRENCH_WORDS_FILE)

data_dict = data.to_dict(orient='records')

random_word = rand.choice(data_dict)


# --------UI SETUP--------- 

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Card front img
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
# Title text
title_text = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
# Word text
# word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
word_text = canvas.create_text(400, 263, text=random_word['French'], font=WORD_FONT)

canvas.grid(column=0, row=0, columnspan=2)

# --------NEW WORD----------

def new_word():
    random_word = rand.choice(data_dict)
    
    canvas.itemconfig(word_text, text=random_word['French'])

# --------UI SETUP CONT--------- 

# Right button
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, bd=0, command=new_word)
right_btn.grid(column=1, row=1)

# Wrong button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=new_word)
wrong_btn.grid(column=0, row=1)

window.mainloop()