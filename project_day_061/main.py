# DAY 61 Project: WTForm Signin!

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5
import os


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = os.environ["ENV_SECRET_KEY"]
env_email = os.environ["ENV_EMAIL"]
env_password = os.environ["ENV_PASSWORD"]


def authenticate(email, password):
    print("Inside the authenticate method")
    print(f"email is: {email} and password is: {password}")

    return email == env_email and password == env_password


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            if authenticate(email=form.email.data, password=form.password.data):
                return render_template('success.html')
            else:
                return render_template('denied.html')

    # form.validate_on_submit()
    return render_template('login.html', form=form)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
