# DAY 62 Project: Cafe Wifi

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
csv_file_path = 'cafe-data.csv'
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    coffee_choices = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
    wifi_choices = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
    power_choices = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 9:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee_choices)
    wifi_rating = SelectField('Wifi Strength Rating', choices=wifi_choices)
    power_rating = SelectField('Power Socket Availability', choices=power_choices)
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST':
        # Make the form write a new row into cafe-data.csv
        # if form.validate_on_submit()
        if form.validate_on_submit():
            cafe = form['cafe'].data
            location = form['location'].data
            open_time = form['open_time'].data
            close_time = form['close_time'].data
            coffee_rating = form['coffee_rating'].data
            wifi_rating = form['wifi_rating'].data
            power_rating = form['power_rating'].data
            new_cafe = [cafe, location, open_time, close_time, coffee_rating, wifi_rating, power_rating]

            with open(csv_file_path, mode='a', encoding='utf-8', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                csv_writer.writerow(new_cafe)
            return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
