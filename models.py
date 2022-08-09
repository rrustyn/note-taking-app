from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User (db.Model):
    """User"""

    __tablename__ = "users"

    username = db.Column(
        db.String(20),
        primary_key=True,)
    password = db.Column(
        db.String(100),
        nullable=False,)
    email = db.Column(
        db.String(50),
        nullable=False,
        unique=True)
    first_name = db.Column(
        db.String(30),
        nullable=False,)
    last_name = db.Column(
        db.String(30),
        nullable=False,)

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """Register user with hashed password and return user"""

        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(username=username,
                   password=hashed,
                   email=email,
                   first_name=first_name,
                   last_name=last_name)
