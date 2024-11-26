from flask_sqlalchemy import SQLAlchemy

# Inicializa a extensão do SQLAlchemy
db = SQLAlchemy()

# Define o modelo de exemplo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
