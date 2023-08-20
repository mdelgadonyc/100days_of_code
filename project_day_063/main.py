from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///virtual-library.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()

    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get('title')
        author = request.form.get('author')
        rating = float(request.form.get('rating'))

        book = Book(title=title, author=author, rating=rating)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/<int:id_num>", methods=["GET"])
def edit(id_num):
    print(f"User requested editing of the rating for book with ID {id_num}")
    return "UNDER CONSTRUCTION"


if __name__ == "__main__":
    app.run(debug=True)

