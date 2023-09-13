import pandas
import random
from tkinter import *
from card import Card

selected_word_dict = {}
# row_display = None
# import openpyxl

BACKGROUND_COLOR = "#B1DDC6"
ITALIC_FONT = ("Arial", 40, "italic")
BOLD_FONT = ("Arial", 60, "bold")


# -----------------------New Card Action--------------------------------#
def new_card_gen():
    canvas.itemconfig(card_display, image=card_image_front)
    canvas.itemconfig(eng_meaning, text="")
    front_card.new_card()
    canvas.itemconfig(top_lang_text, text="Chinese", fill="black")
    canvas.itemconfig(chinese_word, text=f"{front_card.chinese_word}")
    canvas.itemconfig(pinyin_word, text="")


# -----------------------Check Action--------------------------------#
def check_press():
    # new_row = rand_row(hsk_data, word_keys)
    # canvas.itemconfig(chinese_word, text=new_row.Chinese)

    # canvas_word_show()
    # new_card = Card(hsk_data)
    # canvas.itemconfig(chinese_word, text=f"{new_card.chinese_word}")
    # canvas.itemconfig(pinyin_word, text="")
    words_to_learn = front_card.hsk_dict
    words_to_learn = words_to_learn.remove(front_card.selected_word_dict)

    try:
        with open("./data/words_to_learn.xlsx", mode="rb") as to_learn_file:
            to_learn_data = pandas.read_excel(to_learn_file)
    except FileNotFoundError:
        # with open("words_to_learn.xlsx", mode="w") as to_learn_file:
        #     pandas.to_excel()
        to_learn_split = hsk_data.to_dict(orient="split")
        to_learn_list = to_learn_split["data"]
        to_learn_df = pandas.DataFrame(to_learn_list, columns=['Chinese', 'Pinyin', 'English'])
        to_learn_df.to_excel("./data/words_to_learn.xlsx", index=False)
    else:
        to_learn_split = to_learn_data.to_dict(orient="split")
        to_learn_list = to_learn_split["data"]
        to_learn_list.remove(front_card.selected_word_list)
        to_learn_df = pandas.DataFrame(to_learn_list, columns=['Chinese', 'Pinyin', 'English'])
        to_learn_df.to_excel("./data/words_to_learn.xlsx", index=False)

    new_card_gen()


# -----------------------Cross Action--------------------------------#
def cross_press():
    # canvas_word_show()
    # rand_record_pick()
    # new_card = Card(hsk_data)
    # canvas.itemconfig(chinese_word, text=f"{new_card.chinese_word}")
    # canvas.itemconfig(pinyin_word, text="")
    new_card_gen()


# ------------------------Hint Action--------------------------------#
def hint_press():
    canvas.itemconfig(pinyin_word, text=f"{front_card.pinyin_hint}")
    window.after(3000, card_flip)


# ----------------------Card Flip Action------------------------------#
def card_flip():
    canvas.itemconfig(card_display, image=card_image_back)
    canvas.itemconfig(top_lang_text, text="English", fill="white")
    canvas.itemconfig(pinyin_word, text="")
    canvas.itemconfig(chinese_word, text="")
    canvas.itemconfig(eng_meaning, text=f"{front_card.english_meaning}")


# ---------------------File Open and Key Gen-------------------------#

try:
    with open("./data/words_to_learn.xlsx", mode="rb") as relearn_file:
        relearn_data = pandas.read_excel(relearn_file)
except FileNotFoundError:
    with open("./data/HSK1_WL.xlsx", mode="rb") as hsk_file:
        hsk_data = pandas.read_excel(hsk_file)
    # hsk_dict = hsk_data.to_dict(orient="records")
    # print(hsk_dict)
    # print(hsk_data.iloc[7].Pinyin)
    front_card = Card(hsk_data)
else:
    front_card = Card(relearn_data)

# def rand_record_pick():
#     global selected_word_dict
#     selected_word_dict = random.choice(hsk_dict)
#
#     canvas.itemconfig(chinese_word, text=selected_word_dict["Chinese"])


# word_keys = list(hsk_dict["Chinese"].keys())


# chinese_list = list(hsk_dict["Chinese"].values())
# pinyin_list = list(hsk_dict["Pinyin"].values())
# english_list = list(hsk_dict["English"].values())
# print(f"key\n{word_keys}")
# print(f"Cn\n{chinese_list}")
# print(f"Pin\n{pinyin_list}")
# print(f"En\n{english_list}")

# def rand_row(hsk_dataframe, word_keys_list):
#     random_word_key = random.choice(word_keys_list)
#     row_data_display = hsk_dataframe.iloc[random_word_key]
#     return row_data_display


# def canvas_word_show():
#     global row_display
#     row_display = rand_row(hsk_data, word_keys)
#     canvas.itemconfig(chinese_word, text=f"{row_display.Chinese}")

# return [f"{row_display.Chinese}", f"{row_display.Pinyin}"]


# ---------------------------UI Stuff-----------------------------------#
window = Tk()
window.config(padx=15, pady=5, bg=BACKGROUND_COLOR)
window.title("Flashy")

# card canvas
canvas = Canvas()
card_image_front = PhotoImage(file="./images/card_front.png")
card_image_back = PhotoImage(file="./images/card_back.png")
canvas.config(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_display = canvas.create_image(400, 263, image=card_image_front)
canvas.grid(row=0, column=0, columnspan=3)

# top lang text
top_lang_text = canvas.create_text(400, 150, text="Chinese", font=ITALIC_FONT)

# chinese word
chinese_word = canvas.create_text(400, 263, text=f"{front_card.chinese_word}", font=BOLD_FONT)

# pinyin equivalent
pinyin_word = canvas.create_text(400, 400, text="", font=ITALIC_FONT)

# english meaning
eng_meaning = canvas.create_text(400, 263, text="", fill="white", font=BOLD_FONT)

# rand_record_pick()
# canvas_word_show()

# check mark button
check_img = PhotoImage(file="./images/check.png")
check_button = Button(image=check_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=check_press)
check_button.grid(row=1, column=0)

# hint button
hint_img = PhotoImage(file="./images/hint.png")
hint_button = Button(image=hint_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=hint_press)
hint_button.grid(row=1, column=1)

# cross mark button
cross_img = PhotoImage(file="./images/cross.png")
cross_button = Button(image=cross_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=cross_press)
cross_button.grid(row=1, column=2)

window.mainloop()
