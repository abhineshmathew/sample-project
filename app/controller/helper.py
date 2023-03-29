import base64
import hashlib
import os
import re
from requests_oauthlib import OAuth2Session
from flask import current_app

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