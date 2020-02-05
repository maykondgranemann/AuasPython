from Aula52.model.endereco_model import EnderecoModel
from Aula52.dao.base_dao import BaseDao

class EnderecoDao(BaseDao):
    def __init__(self):
        super().__init__("01_MDG_ENDERECO")

    def listar_todos(self):
        tuplas = super().listar_todos()
        lista = []
        for e in tuplas:
            model = EnderecoModel(e[1], e[2], e[3], e[4], e[5], e[6], e[0])
            lista.append(model.__dict__)
        return lista

    def buscar_por_id(self, id):
        tupla = super().buscar_por_id(id)
        model = EnderecoModel(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[0])
        return model.__dict__

    def inserir(self, model: EnderecoModel):
        comando_sql = """INSERT INTO {}  
                            (
                                LOGRADOURO,
                                NUMERO,
                                COMPLEMENTO,
                                BAIRRO,
                                CIDADE,
                                CEP
                            )VALUES
                            (
                                '{}',
                                '{}',
                                '{}',
                                '{}',
                                '{}',
                                '{}'
                            )
                            """.format(self.tabela, model.logradouro, model.numero, model.complemento, model.bairro, model.cidade, model.cep )
        model.id = super().inserir(comando_sql)
        return model.__dict__

    def alterar(self, model: EnderecoModel):
        comando_sql = """ UPDATE {}
                            SET 
                                LOGRADOURO = '{}',
                                NUMERO = '{}',
                                COMPLEMENTO = '{}',
                                BAIRRO = '{}',
                                CIDADE = '{}',
                                CEP = '{}'
                            WHERE ID = {}
                            """.format(self.tabela, model.logradouro, model.numero, model.complemento, model.bairro, model.cidade, model.cep, model.id )
        super().alterar(comando_sql)
        return model.__dict__

    def deletar(self, id):
        return super().deletar(id)

