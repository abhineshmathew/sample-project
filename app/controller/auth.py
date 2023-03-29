import base64
import requests

from flask import redirect, session, request, url_for, current_app
from .helper import code_verifier, code_challenge, make_token


def login():
    global twitter
    twitter = make_token()
    authorization_url, state = twitter.authorization_url(
        current_app.config.get('AUTH_URL'), code_challenge=code_challenge, code_challenge_method="S256"
    )
    session["oauth_state"] = state
    return redirect(authorization_url)

def callback():
    code = request.args.get("code")

    headers = {
        "Content-Type" : "application/x-www-form-urlencoded",
        "Authorization" : 'Basic {}'.format(base64.b64encode('{}:{}'.format(
                                current_app.config.get('CLIENT_ID'), 
                                current_app.config.get('CLIENT_SECRET')
                            ).encode()).decode())
        }

    data = {
        "code": code,
        "grant_type": "authorization_code",
        "code_verifier": code_verifier,
        "redirect_uri": current_app.config.get('REDIRECT_URI')
    }

    response = requests.post(current_app.config.get('TOKEN_URL'), headers=headers, data=data)
    print(response.json())
    session["logged_in"] = True
    return redirect(url_for('main.index'))

def logout():
    session['logged_in'] = False
    return redirect(url_for('main.index'))