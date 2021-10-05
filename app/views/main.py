from flask import render_template, jsonify
from app import app
import random



@app.route('/')
@app.route('/index')
def index():
    # Feature flags init goes here!

    #

    # noinspection PyDictCreation
    flags = {
        "welcome_text": "welcome to my python FF tutorial!"
    }

    flags["alternate_homescreen"] = False
    return render_template(
        'index.html',
        **flags,
        title='Home'
    )


@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')