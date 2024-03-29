from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        user_dict = self.__dict__
        if "_sa_instance_state" in user_dict:
            del user_dict["_sa_instance_state"]
        return user_dict
