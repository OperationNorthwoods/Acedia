import os
from flask import Flask, render_template, redirect
from config import API_KEY
from markupsafe import escape
import requests
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


class SteamSearch(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SteamSearch()
    if form.validate_on_submit():
        return redirect('/results.html')
    return render_template('index.html', form=form)

@app.route('/results')
def results():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)