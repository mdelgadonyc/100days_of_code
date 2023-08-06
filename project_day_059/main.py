# DAY 59+60 Project: Weird Musings [Improved version of the Day 57 "Blogging" Capstone]

from flask import Flask, render_template, request
import requests

NPOINT_ENDPOINT = "https://api.npoint.io/d8332566712a9f862efc"

app = Flask(__name__)

response = requests.request("GET", NPOINT_ENDPOINT)
response.raise_for_status()
data = response.json()


@app.route("/")
def home():
    return render_template("index.html", blogs_data=data)


@app.route("/post/<num>")
def post(num):
    index = int(num) - 1
    return render_template("post.html", blog_data=data[index])


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        message = ("Successfully sent your message")
        return render_template("contact.html", contact_message=message)

    elif request.method == 'GET':
        message = "Contact Me"
        return render_template("contact.html", contact_message=message)


if __name__ == "__main__":
    app.run(debug=True)
