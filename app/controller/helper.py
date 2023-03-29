import base64
import hashlib
import os
import re
import requests
from requests_oauthlib import OAuth2Session
from flask import current_app
from app import db
from app.models.user import User, Timeline
# Create a code verifier
code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

# Create a code challenge
code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
code_challenge = code_challenge.replace("=", "")


def make_token():
    return OAuth2Session(
            current_app.config.get('CLIENT_ID'), 
            redirect_uri=current_app.config.get('REDIRECT_URI'), 
            scope=current_app.config.get('SCOPES'))

def create_user(access_token):
    url = current_app.config.get('PROFILE_URL')  
    headers = {
        "Authorization": f'Bearer {access_token}',
    }
    response = requests.get(url, headers=headers)
    user_info=response.json().get('data')
    if not user_info:
        return False
    return insert_user(user_info)

def insert_user(user_info):
    user =  User.query.filter_by(t_user_id=user_info.get('id')).first()
    if user:
        return user
    else:
        uinfo = {
            't_user_id': user_info['id'] ,
            'name': user_info['name'] ,
            't_user_name': user_info['username'] ,
            }
        user = User(**uinfo)
        db.session.add(user)
        db.session.commit()
        return user
    

def fetch_timeline(user_id,access_token):
    url = current_app.config.get('TIMELINE_URL').format(user_id)
    headers = {
        "Authorization": f'Bearer {access_token}',
        "User-Agent": "ReverseChronSampleCode",
    }
    response = requests.request("GET", url, headers=headers)
    insert_timelines(response.json().get('data'),user_id)
    

def insert_timelines(data, user_id):
    # TODO bulk insert
    for each in data:
        insert_timeline_db(each, user_id)

def insert_timeline_db(data, user_id):
    tweet =  Timeline.query.filter_by(tweet_id=data.get('id')).first() 
    if tweet:
        return tweet
    else:
        tw = {
            'tweet_text': data.get('text'),
            'tweet_id': data.get('id'),
            'user_id': user_id,
        }
        tweet = Timeline(**tw)
        db.session.add(tweet)
        db.session.commit()
        return tweet

def get_timeline_from_db(user_id):
    return Timeline.query.filter_by(user_id=user_id)