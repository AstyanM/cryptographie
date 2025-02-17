#! /usr/bin/env python3
# coding: utf-8
# pylint: disable=C0301, R0201


"""All imports"""


from useful import useful


"""
Part I : Ceasar
"""


class Ceasar:
    """Class made to bring together the functions needed to encrypt and decrypt with Ceasar method"""

    def __init__(self):

        self.choice = useful.choice(
            to_print=useful.color(text="\nWhat do you want to do with the Ceasar cipher ?", style="bright"),
            choices_values={
                1: "Encrypt",
                2: "Decrypt",
                3: "Show documentation"})
        if self.choice == 1:
            print("Encrypted text :", useful.color(text=self.encrypt_ceasar(), color="red"))
        elif self.choice == 2:
            self.decrypt_ceasar()
        else:
            print("https://en.wikipedia.org/wiki/Caesar%27s_cipher")

    def encrypt_ceasar(self, key=None, sentence=None):
        """This function encrypt a text using the ceasar method"""

        encrypted_sentence = ""

        #  If the user have to fill some informations
        if not sentence:
            sentence = input(useful.color(text="Enter a sentence to encrypt :\n", style="bright", is_input=True))
        if not key:
            while True:
                try:
                    key = int(input(useful.color(text="Enter the key :\n", style="bright", is_input=True)))
                    break
                except ValueError:
                    print("The type of the key isn't valid")

        for letter in sentence.lower():
            alpha_letter = useful.become_alpha(letter=letter)
            if alpha_letter:

                # We add the key position to the letter position
                new_letter_place = useful.alpha.index(alpha_letter) + key % 26
                if new_letter_place >= 26:
                    new_letter_place -= 26
                encrypted_sentence += useful.alpha[new_letter_place]
            elif letter == " ":
                encrypted_sentence += letter
            else:
                continue

        return encrypted_sentence

    def decrypt_ceasar(self):
        """This function decrypt a text encrypted by the ceasar method"""

        encrypted_text = input(useful.color(text="Enter the encrypted text :\n", style="bright", is_input=True))
        other_key = useful.choice(to_print=useful.color(text="Do you know the key ?", style="bright"),
                                  choices_values={
                                      1: "Yes",
                                      2: "No"})

        if other_key == 1:
            print(useful.color(text=self.encrypt_ceasar(
                key=26 - (useful.choice(to_print=useful.color(text="What is the key ? ", style="bright")) % 26),
                sentence=encrypted_text), color="red"))

        else:
            languages_choosed = useful.choice(
                to_print=useful.color(text="In which language has it been encrypted ?", style="bright"),
                choices_values=useful.language_choices)
            if languages_choosed == 3:
                languages_choosed = [1, 2]
            else:
                languages_choosed = [languages_choosed]

            # Creating a list with all the possible sentences
            list_options = []
            for language_chosen in languages_choosed:
                [list_options.append(possibility) for possibility in
                 useful.see_if_language(
                     encrypted_sentences=[(self.encrypt_ceasar(key=shift, sentence=encrypted_text), shift) for shift
                                          in range(1, 26)], language=useful.language_choices[language_chosen])]

            # If we found some possible sentences
            if list_options:
                print("\n" + useful.color(text="Possibilities :", style="bright"))
                for option in list_options:
                    print(useful.color(text=option[0], color="red"), "with key",
                          useful.color(text=option[1], color="red"))

            # If there's no possibilities
            else:
                print("\n" + useful.color(text="No language found : Brute-Force :", style="bright"))
                for other_key in range(1, 26):
                    print(
                        useful.color(text=self.encrypt_ceasar(key=other_key, sentence=encrypted_text), color="red"),
                        "with key", useful.color(text=str(26 - other_key), color="red"))
