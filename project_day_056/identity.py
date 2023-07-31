# DAY 56 Project: Serving Face

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def serve_face():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
