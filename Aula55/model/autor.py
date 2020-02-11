import sqlalchemy as db
from sqlalchemy.orm import relationship

from Aula55.model.pessoa import Pessoa
from Aula55.model.base import Base
from Aula55.dao.pessoa_dao import PessoaDao

class Autor(Base):
    __tablename__ = "LIVRARIA_AUTOR"
    id = db.Column(db.Integer, primary_key=True)
    pseudonimo = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))
    pessoa_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_PESSOA.id'))
    pessoa = relationship(Pessoa)
