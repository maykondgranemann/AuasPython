
from Aula52.dao.base_dao import BaseDao
from Aula52.model.produto_model import ProdutoModel

class ProdutoDao(BaseDao):
    def __init__(self):
        super().__init__("Produto")

    def listar_todos(self):
        tuplas = super().listar_todos()
        lista = []
        for p in tuplas:
            model = ProdutoModel(p[1], p[2], p[0])
            lista.append(model.__dict__)
        return lista

    def buscar_por_id(self, id):
        p = super().buscar_por_id(id)
        model = ProdutoModel(p[1], p[2], p[0])
        return model.__dict__

    def inserir(self, model:ProdutoModel):
        comando_sql = """INSERT INTO {}  
                            (
                                NOME,
                                DESCRICAO
                            )VALUES
                            (
                                '{}',
                                '{}'
                            )
                            """.format(self.tabela, model.nome, model.descricao)

        model.id = super().inserir(comando_sql)
        return model.__dict__

    def alterar(self, model:ProdutoModel):
        comando_sql =""" UPDATE {}
                            SET 
                                NOME = '{}',
                                DESCRICAO = '{}'
                            WHERE ID = {}
                            """.format(self.tabela, model.nome, model.descricao, model.id)
        super().alterar(comando_sql)
        return model.__dict__

    def deletar(self, id):
        return super().deletar(id)
