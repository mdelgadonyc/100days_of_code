import os

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            return "Form submitted"

    # form.validate_on_submit()
    return render_template('login.html', form=form)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
