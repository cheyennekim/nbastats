from sqlalchemy import sql, orm
from app import db


class Player(db.Model):
    __tablename__ = 'players'
    name = db.Column('name', db.String(20), primary_key=True)
