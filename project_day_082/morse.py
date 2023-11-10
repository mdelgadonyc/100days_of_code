# morse.py - Command line program that takes any string input and converts it into Morse Code.

morse_code = {
    " ": " ", 'a': '⚫ ———', 'b': '——— ⚫ ⚫ ⚫', 'c': '——— ⚫ ——— ⚫', 'd': '——— ⚫ ⚫', 'e': '⚫', 'f': '⚫ ⚫ ——— ⚫',
    'g': '——— ——— ⚫', 'h': '⚫ ⚫ ⚫ ⚫', 'i': '⚫ ⚫', 'j': '⚫ ——— ——— ———', 'k': '——— ⚫ ———', 'l': '⚫ ——— ⚫ ⚫',
    'm': '——— ———', 'n': '——— ⚫', 'o': '——— ——— ———', 'p': '⚫ ——— ——— ⚫', 'q': '——— ——— ⚫ ———', 'r': '⚫ ——— ⚫',
    's': '⚫ ⚫ ⚫', 't': '———', 'u': '⚫ ⚫ ———', 'v': '⚫ ⚫ ⚫ ———', 'w': '⚫ ——— ———', 'x': '——— ⚫ ⚫ ———',
    'y': '——— ⚫ ——— ———', 'z': '——— ——— ⚫ ⚫', '1': '⚫ ——— ——— ——— ———', '2': '⚫ ⚫ ——— ——— ———', '3': '⚫ ⚫ ⚫ ——— ———',
    '4': '⚫ ⚫ ⚫ ⚫ ———', '5': '⚫ ⚫ ⚫ ⚫ ⚫', '6': '——— ⚫ ⚫ ⚫ ⚫', '7': '——— ——— ⚫ ⚫ ⚫', '8': '——— ——— ——— ⚫ ⚫',
    '9': '——— ——— ——— ——— ⚫', '0': '——— ——— ——— ——— ———',
}

original_text = input("Please enter a phrase to convert to Morse Code: ").lower()
encoded_text = ""

for character in original_text:
    if character in morse_code:
        encoded_text += morse_code[character] + "   "
    else:
        encoded_text += character

print(f"Encoded text is: {encoded_text}")
