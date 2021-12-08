# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:56:06 2021

@author: HHH
"""

import os
import heroku
from flask import Flask, render_template

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

@app.route('/')
def home1():
    return render_template('home2.html')

@app.route('/home')
def home():
    return render_template('home2.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/contact')
def contact():
    return render_template('contact2.html')

if __name__ == "__main__":
    app.run(debug = True)
