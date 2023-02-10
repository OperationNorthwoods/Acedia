import os
from flask import Flask, render_template
from config import API_KEY
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search_user():
    print('api stuffs')


if __name__ == "__main__":
    app.run(debug=True)