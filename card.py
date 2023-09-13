import random
from tkinter import messagebox

class Card:

    def __init__(self, hsk_dataframe):
        self.hsk_dataframe = hsk_dataframe
        self.hsk_dict = self.hsk_dataframe.to_dict(orient="records")
        split_form = self.hsk_dataframe.to_dict(orient="split")
        self.list_of_rows = split_form["data"]

        self.chinese_word = ""
        self.pinyin_hint = ""
        self.english_meaning = ""
        self.selected_word_dict = {}
        self.selected_word_list = []
        self.new_card()

    def new_card(self):
        try:
            self.selected_word_dict = random.choice(self.hsk_dict)
        except IndexError:
            messagebox.showinfo(title="Congrats!", message="You've learnt everything!")

        else:
            self.chinese_word = self.selected_word_dict["Chinese"]
            self.pinyin_hint = self.selected_word_dict["Pinyin"]
            self.english_meaning = self.selected_word_dict["English"]

            self.selected_word_list = [self.chinese_word, self.pinyin_hint, self.english_meaning]

