import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "01_MDG_PESSOA"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    sobrenome = db.Column(db.String(length=100))
    idade = db.Column(db.Integer)

    def __str__(self):
        return f"{self.id},{self.nome},{self.sobrenome},{self.idade}"
