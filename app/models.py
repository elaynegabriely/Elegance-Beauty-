from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define o modelo de exemplo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullbale=False)
    create_data = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<User {self.name}>'

class Post(db.Model):
    __tablename__ = 'posts'

id =  db.Column(db.)