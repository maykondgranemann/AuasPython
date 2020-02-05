from Aula53.dao.base_dao import BaseDao
from Aula53.model.produto_model import ProdutoModel

class ProdutoDao(BaseDao):
    def list_all(self):
        return self.sessao.query(ProdutoModel).all()