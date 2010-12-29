# -*- coding: utf-8 -*-

#Top level views for benzene

from flask import render_template

from benzene import app
from benzene import top_level_forms as forms

@app.route('/')
def home():
    return render_template('visitor_home.html')

@app.route('/register')
def register():
    return 'This will be registration page'

@app.route('/login')
def login():
    return 'This will be login page'