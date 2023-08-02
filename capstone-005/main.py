# DAY 57 Project: [Capstone] Blogging

from flask import Flask, render_template
import post

app = Flask(__name__)
blogs = post.Post()


@app.route('/post/<num>')
def show_post(num):
    return render_template("post.html", number=num, blog=blogs.get_post(num))


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs.get_all_posts())


if __name__ == "__main__":
    app.run(debug=True)
