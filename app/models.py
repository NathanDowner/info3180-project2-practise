from . import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    photo = db.Column(db.String(80))
    caption = db.Column(db.String(80))
    created_on = db.Column(db.DateTime, default=datetime.now)
    
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(256), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(80), nullable=False)
    biography = db.Column(db.String(50), nullable=False)
    profile_photo = db.Column(db.String(80), nullable=False)
    joined_on = db.Column(db.DateTime, default=datetime.now)
    
    #links
    posts = db.relationship('Post', backref='user', lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)
    followers = db.relationship('Follower', backref=)
    
    def __init__(self, username, password, fname, lname, email, loc, bio, photo):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.location = loc
        self.biography = bio
        self.photo = photo
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
        
class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    
    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id
        
    def __repr__(self):
        return '<Like by {} on post {}>.format(self.user.username, self.post_id)'
        
follows = db.Table('follows',

)
    
class Follow(db.Model):
    __tablename__ = 'follows'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id
        
    def __repr__(self):
        return '<Follow {}>'.format(self.id)

