from flask import render_template, request, redirect, session, current_app

def index():
    print(current_app.config)
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="Hello world")