from Aula52.model.pessoa_model import PessoaModel
from Aula52.dao.base_dao import BaseDao

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__("01_MDG_PESSOA")

    def listar_todos(self):
        tuplas = super().listar_todos()
        lista = []
        for p in tuplas:
            model = PessoaModel(p[1], p[2], p[3], p[0])
            lista.append(model.__dict__)
        return lista

    def buscar_por_id(self, id):
        tupla = super().buscar_por_id(id)
        pessoa = PessoaModel(tupla[1], tupla[2], tupla[3], tupla[0])
        return pessoa.__dict__

    def inserir(self, model:PessoaModel):
        comando_sql = """INSERT INTO {}  
                            (
                                NOME,
                                SOBRENOME,
                                IDADE
                            )VALUES
                            (
                                '{}',
                                '{}',
                                {}
                            )
                            """.format(self.tabela, model.nome, model.sobrenome, model.idade )

        model.id = super().inserir(comando_sql)
        return model.__dict__

    def alterar(self, model:PessoaModel):
        comando_sql =""" UPDATE {}
                            SET 
                                NOME = '{}',
                                SOBRENOME = '{}',
                                IDADE = {}
                            WHERE ID = {}
                            """.format(self.tabela, model.nome, model.sobrenome, model.idade, model.id)
        super().alterar(comando_sql)
        return model.__dict__

    def deletar(self, id):
        return super().deletar(id)