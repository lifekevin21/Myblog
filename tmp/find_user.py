from app import db, models


users = models.User.query.all()
print(users)
for u in users:
    print(u.id, u.nickname)

e = models.User.query.get(1)
print(e)

p = models.User.query.filter_by(nickname='john').first()
print(p.id, p.email)

d = models.User.query.filter(models.User.email.endswith('email.com')).all()
print(d)
