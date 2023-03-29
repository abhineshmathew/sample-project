import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(50))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'database.db')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTH_URL = "https://twitter.com/i/oauth2/authorize"
    TOKEN_URL = "https://api.twitter.com/2/oauth2/token"
    REDIRECT_URI = 'http://127.0.0.1:5000/oauth/callback'
    SCOPES = ["tweet.read", "users.read", "tweet.write", "offline.access"]
    PROFILE_URL = "https://api.twitter.com/2/users/me"
    TIMELINE_URL = "https://api.twitter.com/2/users/{}/timelines/reverse_chronological"
    