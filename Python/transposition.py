#! /usr/bin/env python3
# coding: utf-8
# pylint: disable=C0301, R0201


"""All imports"""


from math import ceil
from useful import useful


"""
Part II : Transposition
"""


class Transposition:
    """Class made to bring together the functions needed to encrypt and decrypt with Transposition method"""

    def __init__(self):

        self.choice = useful.choice(
            to_print=useful.color(text="\nWhat do you want to do with the Transposition cipher ?", style="bright"),
            choices_values={
                1: "Encrypt",
                2: "Decrypt",
                3: "Show documentation"})
        if self.choice == 1:
            self.encrypt_transposition()
        elif self.choice == 2:
            self.decrypt_transposition()
        else:
            print("https://en.wikipedia.org/wiki/Transposition_cipher")

    def encrypt_transposition(self):
        """This function encrypt a text by the transposition method"""

        #  If the user have to fill some informations
        text = input(useful.color(text="Enter the text to encrypt :\n", style="bright", is_input=True))
        while True:
            try:
                key = int(input(useful.color(text="Enter the key :\n", style="bright", is_input=True)))
                if key <= len(text):
                    break
                print("The length of this key isn't valid")
            except ValueError:
                print("The type of the key isn't valid")

        # Creating the board according to the key
        len_text = len(text)
        encrypted_text = ""
        text += " " * (key - len_text % key)

        # Filling the board with the text
        for f_iter in range(0, key):
            for s_iter in range(0, len_text):
                if s_iter % key == f_iter:
                    encrypted_text += text[s_iter]
        print("Encrypted text :", useful.color(text=encrypted_text, color="red"))

    def decrypt_transposition(self):
        """This function decrypt a text encrypted by the transposition method"""

        possibilities = []
        encrypted_text = input(useful.color(text="Enter the encrypted text :\n", style="bright", is_input=True))
        languages_choosed = useful.choice(
            to_print=useful.color(text="In which language has it been encrypted ?", style="bright"),
            choices_values=useful.language_choices)
        if languages_choosed == 3:
            languages_choosed = [1, 2]
        else:
            languages_choosed = [languages_choosed]

        # Creating all the possible boards
        for key in range(1, len(encrypted_text)):
            columns = int(ceil(len(encrypted_text) / float(key)))
            rows = key
            unfilled = (columns * rows) - len(encrypted_text)
            decrypted = [""] * columns
            column = 0
            row = 0

            # Filling each possible boards with the encrypted text character
            for char in encrypted_text:
                decrypted[column] += char
                column += 1
                if (column == columns) or (column == columns - 1 and row >= rows - unfilled):
                    column = 0
                    row += 1

            decrypted = "".join(decrypted)
            possibilities.append((decrypted, key))

        final_pos = []
        for language_chosen in languages_choosed:
            [final_pos.append(possibility) for possibility in
             useful.see_if_language(
                 encrypted_sentences=possibilities, language=useful.language_choices[language_chosen])]

        if final_pos:
            print("\n" + useful.color(text="Possibilities :", style="bright"))
            for final_p in final_pos:
                print(useful.color(text=final_p[0], color="red"), "with key",
                      useful.color(text=final_p[1], color="red"))
        else:
            print("\n" + useful.color(text="Nothing found : Brute-Force :", style="bright"))
            for possibility in possibilities:
                print(useful.color(text=possibility[0], color="red"),
                      "with key", useful.color(text=possibility[1], color="red"))
