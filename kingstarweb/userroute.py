import os,random, time

from flask import render_template, redirect, flash, session, request, url_for

from kingstarweb import app,db



@app.route('/')
def home():
    return render_template('users/index.html')

@app.route('/about')
def about():
    return render_template('users/about.html')
