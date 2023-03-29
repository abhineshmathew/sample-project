from flask import render_template, request, redirect, session, current_app
from app.models.user import *
from .helper import fetch_timeline, get_timeline_from_db

def index():
    if session.get('logged_in_token') and session.get('logged_in_id'):
        fetch_timeline(session.get('logged_in_id'), session.get('logged_in_token'))
        data =  get_timeline_from_db(session.get('logged_in_id'))
        return render_template('home.html', data=data)
    else:
        return render_template('index.html')