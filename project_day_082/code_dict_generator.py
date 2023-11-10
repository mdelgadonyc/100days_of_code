# helper script I created to partially generate the character to Morse Code dictionary.

text = ""

for num in range(26):
    letter = chr(ord('a') + num)
    text += f"'{letter}': '', "

for num in range(10):
    text += f"'{num}': '', "

print(text)
