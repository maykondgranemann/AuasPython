from Aula54.model.produto_model import Produto
from Aula54.dao.base_dao import BaseDao

class ProdutoDao(BaseDao):
   def __init__(self):
       super().__init__(Produto)