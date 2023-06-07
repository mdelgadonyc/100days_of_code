# Day 26 Project: Papa-Yankee-Tango-Hotel-Oscar-November!

import pandas as pd

# Create a dictionary in this format:
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_code_dict = {row[1].letter: row[1].code for row in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

phonetic_list = [nato_code_dict[letter] for letter in user_word]
print(phonetic_list)
