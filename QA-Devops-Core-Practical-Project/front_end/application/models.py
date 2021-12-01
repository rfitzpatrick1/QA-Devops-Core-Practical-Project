from application import db

class Creatures(db.Model):
    name=db.Column(db.String(50), primary_key=True)
    type=db.Column(db.String(50))
    continent=db.Column(db.String(50))
