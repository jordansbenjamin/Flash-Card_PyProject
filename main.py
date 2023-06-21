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

# --------FLIP CARD--------

def flip_card(random_word):
    # english_word = new_card()
    canvas.itemconfig(canvas_card, image=card_back_img)
    canvas.itemconfig(title_text, text="English",fill="white")
    canvas.itemconfig(word_text, text=random_word["English"], fill="white")

def new_word():
    random_word = rand.choice(data_dict)
    return random_word

# --------NEW CARD----------

def new_card(random_word):
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_card, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word['French'], fill="black")
    flip_timer = window.after(3000, lambda:[flip_card(random_word)])

# --------UI SETUP--------- 

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, lambda:[flip_card(new_word())])

# Card canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Card front img
card_front_img = PhotoImage(file="./images/card_front.png")
# Card back img
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=card_front_img)
# Title text
title_text = canvas.create_text(400, 150, text="", font=TITLE_FONT)
# Word text
# word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)

canvas.grid(column=0, row=0, columnspan=2)

# Right button
right_img = PhotoImage(file="./images/right.png")
# right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, bd=0, command=new_card)
right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, bd=0, command=lambda:[new_card(new_word())])
right_btn.grid(column=1, row=1)

# Wrong button
wrong_img = PhotoImage(file="./images/wrong.png")
# wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=new_card)
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=lambda:[new_card(new_word())])
wrong_btn.grid(column=0, row=1)

new_card(new_word())

window.mainloop()