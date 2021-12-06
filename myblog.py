# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:56:06 2021

@author: HHH
"""

from flask import Flask, render_template

app = Flask(__name__)

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