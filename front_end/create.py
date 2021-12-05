from application import db
from application.models import Creatures

db.drop_all()
db.create_all()