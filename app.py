from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/city')
def city():
    return render_template('city.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/user')
def user():
    return render_template('user.html')