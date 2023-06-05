# Day 24 Project: Mail Merge Challenge

def write_letter(template_text, name):
    formatted_name = name.strip()

    with open(f"Output/ReadyToSend/letter_for_{formatted_name}.txt", "w") as file:
        file.write(template_text.replace("[name]", formatted_name))


with open("Input/Letters/starting_letter.txt") as letter_file:
    template_text = letter_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    write_letter(template_text, name)
