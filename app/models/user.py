from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    t_user_id = db.Column(db.String(50))
    t_user_name = db.Column(db.String(50))

class Timeline(db.Model):
    __tablename__ = 'timeline'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    tweet_id = db.Column(db.String(50))
    tweet_text = db.Column(db.String(1024))


