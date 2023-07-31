from flask import Flask, render_template
from random import randint
import requests

app = Flask(__name__)


@app.route('/')
def home():
    first_name = "Moises"
    number = randint(1, 100)
    return render_template("index.html", num=number, name=first_name)


@app.route('/guess/<name>')
def guess(name):
    gender = get_gender(name)
    age = get_age(name)
    name = name.title()

    return render_template("guess.html", name=name, gender=gender, age=age)


def get_gender(name):
    url = f"https://api.genderize.io?name={name}"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response.raise_for_status()
    data = response.json()
    return data["gender"]


def get_age(name):
    url = f"https://api.agify.io?name={name}"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    return data["age"]


if __name__ == "__main__":
    app.run(debug=True)
