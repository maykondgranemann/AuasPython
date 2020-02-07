import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = "Produto"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))
    def __str__(self):
        return f"{self.id},{self.nome},{self.descricao}"