import os

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import os


class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        return "Form submitted"

    form = LoginForm()
    return render_template('login.html', form=form)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
