from tkinter import *
import pandas
import csv
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# pandas part ........---_____------___----_____------______--------------->
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def french_lol():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(normal_text, text="French", fill="black")
    canvas.itemconfig(translated_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_back, image=old_image)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(normal_text, text="English", fill="white")
    canvas.itemconfig(card_back, image=new_image)
    canvas.itemconfig(translated_text, text=current_card["English"], fill="White")

def right_click():

    to_learn.remove(current_card)
    data_t = pandas.DataFrame(to_learn)
    data_t.to_csv("data/words_to_learn.csv", index=False)

    french_lol()


# tkinter part.......................-____-----___-----_____----___-->

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
old_image = PhotoImage(file="card_front.png")
new_image = PhotoImage(file="card_back.png")
wrong = PhotoImage(file="wrong.png")
right = PhotoImage(file="right.png")

card_back = canvas.create_image(400, 265, image=old_image)
normal_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
translated_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_button = Button(image=right, highlightthickness=0, command=right_click)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong, highlightthickness=0, command=french_lol)
wrong_button.grid(column=0, row=1)

french_lol()
window.mainloop()
