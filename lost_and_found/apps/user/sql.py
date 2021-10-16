from datetime import datetime
from lost_and_found.apps.peizi import db
db=db
class user(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    pwd=db.Column(db.Integer,nullable=False)
    phone=db.Column(db.Integer,nullable=False)
    date=db.Column(db.String)
    bool=db.Column(db.String)

#     添加一个参数，后面用于管理员进行封号

class text_1(db.Model):
    __tablename__='text_3'
    id=db.Column(db.String(20),primary_key=True)
    title=db.Column(db.String(30),nullable=False)
    user_id=db.Column(db.String(20),nullable=False)
    phone=db.Column(db.String(11),nullable=False)
    place=db.Column(db.String(300),nullable=False)
    text=db.Column(db.String(500),nullable=False)
    times=db.Column(db.DateTime)
class text_2(db.Model):
    __tablename__='text_2'
    id=db.Column(db.String(20),primary_key=True)
    user_id=db.Column(db.String(20))
    phone = db.Column(db.String(11), nullable=False)
    bool=db.Column(db.String(10))


class News(db.Model):
    __tablename__='news'
    id = db.Column(db.String(20), primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    phone=db.Column(db.String(20),nullable=False)