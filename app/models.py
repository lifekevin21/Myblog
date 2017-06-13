from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='users', lazy='dynamic')

    def is_authenticated(self):     # is_authenticated 允许用户验证，只返回True
        return True

    def is_active(self):            # is_active 有效账户都返回True，除非禁止账户
        return True

    def is_anonymous(self):         # is_anonymous 伪造用户之外都是True
        return True

    def get_id(self):               # get_id 返回用户唯一标识符，以str格式
        try:
            return str(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
