import datetime
from app import db, models


u = models.User.query.get(1)
p = models.Post(body='My first post', timestamp=datetime.datetime.utcnow(), users=u)
db.session.add(p)
db.session.commit()
