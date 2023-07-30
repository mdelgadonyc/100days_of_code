# DAY 55 Project: Higher, Lower Game [Web Version]

from flask import Flask
import random

app = Flask(__name__)
secret = 0
TOO_HIGH_MESSAGE = ('<h1 style="color: purple">Too high, try again!</h1><img '
                'src="https://media.giphy.com/media/2fOkK1z4lmh5vRFFcb/giphy.gif">')
TOO_LOW_MESSAGE = ('<h1 style="color: red">Too low, try again!</h1><img '
                'src="https://media.giphy.com/media/dKpEvFHdGsZBRuszpv/giphy.gif">')
FOUND_ME_MESSAGE = ('<h1 style="color: green">You found me!</h1><img '
                'src="https://media.giphy.com/media/3orieUe6ejxSFxYCXe/giphy.gif">')

# Create a new Flask application where the home route displays an <h1> that says "Guess a number between 0 and
#  9" and display a gif of your choice from giphy.com.
@app.route('/')
def welcome_screen():

    # Generate a random number between 0 and 9.
    global secret
    secret = random.randint(0, 9)
    html_message = ('<h1>Guess a number between 0 and 9</h1><img '
                    'src="https://media.giphy.com/media/e9kmj7qsaMKcxcavR5/giphy-downsized.gif">')
    return html_message

# Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number
#  against the generated random number. If the number is too low, tell the user it's too low, same with too high or
#  if they found the correct number. try to make the <h1> text a different colour for each page.  e.g. If the random
#  number was 5: if 3: "Too low, try again!" or 8: "Too high, try again!" or 5: "You found me!"
@app.route('/<int:number>')
def num_guess(number):
    if 0 <= number <= 9:
        if number < secret:
            message = TOO_LOW_MESSAGE
        elif number == secret:
            message = FOUND_ME_MESSAGE
        else:
            message = TOO_HIGH_MESSAGE
        # message = f"You guessed {number}🔮 The secret number is {secret}"
    else:
        message = f"Please guess a number between 0 and 9"
    return message


if __name__ == "__main__":
    app.run(debug=True)


