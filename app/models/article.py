from . import db
import datetime


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    read_times = db.Column(db.BigInteger, nullable=False, default='0')
    good = db.Column(db.BigInteger, nullable=False, default='0')
    bad = db.Column(db.BigInteger, nullable=False, default='0')
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    is_delete = db.Column(db.SMALLINT)

    def __init__(self, username, title, content, read_times=1, good=0, bad=0, create_time=datetime.datetime.now(),
                 update_time=datetime.datetime.now(), is_delete=0):
        self.username = username
        self.title = title
        self.content = content
        self.read_times = read_times
        self.good = good
        self.bad = bad
        self.create_time = create_time
        self.update_time = update_time
        self.is_delete = is_delete

    def __repr__(self):
        return '<Article %r>' % self.title

    def to_dict(self):
        article_dict = self.__dict__
        if "_sa_instance_state" in article_dict:
            del article_dict["_sa_instance_state"]
        return article_dict
