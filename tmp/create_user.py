from app import db, models


def add_com(u):
    db.session.add(u)
    db.session.commit()


u = models.User(nickname='john', email='john@email.com')
add_com(u)
w = models.User(nickname='susan', email='susan@email.com')
add_com(w)
