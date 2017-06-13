from app import db, models


u = models.User.query.get(1)
print(u)

posts = u.posts.all()
print(posts)

e = models.User.query.get(2)
print(e.posts.all())
