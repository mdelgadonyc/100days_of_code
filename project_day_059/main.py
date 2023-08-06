from flask import Flask, render_template
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


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
