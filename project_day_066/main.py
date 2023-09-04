from flask import Flask, jsonify, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # returns the dictionary produced by the dictionary comprehension
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


## HTTP GET - Read Record
@app.route("/search")
def cafe_search():
    location = request.args.get('loc')
    test_location = "Peckham"
    search_results = db.session.query(Cafe).filter(Cafe.location == location).all()
    if len(search_results) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    else:
        return jsonify(cafes=[cafe.to_dict() for cafe in search_results])


@app.route("/random")
def random_cafe():
    all_cafes = db.session.query(Cafe).all()
    cafe = random.choice(all_cafes)

    return jsonify(cafe=cafe.to_dict())


@app.route("/all")
def all_cafes():
    all_cafes = db.session.query(Cafe).all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/cafes/<cafe_id>")
def get_single_cafe(cafe_id):
    cafe = db.session.get(Cafe,cafe_id)

    return jsonify(cafe.to_dict())


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    message = {"success": "Successfully added the new cafe."}
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    # add new cafe to the open database session
    db.session.add(new_cafe)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        message = {"error": "Encountered error processing request."}

    finally:
        db.session.close()

    return jsonify(response=message)

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    print(new_price)

    # add new cafe to the open database session
    try:
        cafe = db.session.get(Cafe, cafe_id)
        cafe.coffee_price = new_price
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        message = {"error": e }

    finally:
        db.session.close()



    return new_price


## HTTP DELETE - Delete Record


@app.route("/")
def home():
    return render_template("index.html")









if __name__ == '__main__':
    app.run(debug=True)
