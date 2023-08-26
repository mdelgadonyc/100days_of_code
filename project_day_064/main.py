from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('ENV_SECRET_KEY')
Bootstrap5(app)

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-list.db'
db = SQLAlchemy()
db.init_app(app)


class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


# Create Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


def search_titles(movie_title):
    url = "https://api.themoviedb.org/3/search/movie"
    api_key = os.environ.get('ENV_API_KEY')

    params = {
        "query": f"{movie_title}",
        "include_adult": "false",
        "language": "en-US",
        "page": "1",
    }

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response


@app.route("/choose")
def choose():
    movie_id = request.args.get('id')
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_key = os.environ.get('ENV_API_KEY')

    params = {
        "language": "en-US"
    }

    headers = {
        "accept": "application/json",
        "Authorization": f"{api_key}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    new_movie = Movie()
    new_movie.title = data['title']
    new_movie.img_url = f'https://image.tmdb.org/t/p/original/{data["poster_path"]}'
    new_movie.year = data['release_date'].split('-')[0]
    new_movie.description = data['overview']

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', id=new_movie.id))


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_movie_form = AddMovieForm()

    if add_movie_form.validate_on_submit():
        movie_title = add_movie_form.title.data
        
        response = search_titles(movie_title)
        data = response.json()
        movies_list = data['results']
        return render_template('select.html', movies=movies_list)

    return render_template('add.html', form=add_movie_form)


@app.route("/delete", methods=['GET'])
def delete():
    movie_id = request.args.get('id')
    movie = db.session.execute(db.select(Movie).filter_by(id=movie_id)).scalar()

    if movie:
        db.session.delete(movie)
        db.session.commit()

    return redirect(url_for('home'))


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    movie_id = request.args.get('id')
    rate_form = RateMovieForm()

    # movie = Movie.query.get(movie_id)
    movie = db.session.execute(db.select(Movie).filter_by(id=movie_id)).scalar()

    if request.method == 'POST':
        if rate_form.validate_on_submit():
            movie.rating = rate_form.rating.data
            movie.review = rate_form.review.data
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('edit.html', form=rate_form, movie_title=movie.title, id=movie_id)


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(db.desc(Movie.ranking)))
    movies = result.scalars()
    return render_template("index.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
