from Aula54.model.pessoa_model import Pessoa
from Aula54.dao.base_dao import BaseDao

class PessoaDao(BaseDao):
   def __init__(self):
       super().__init__(Pessoa)