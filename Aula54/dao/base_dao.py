#--- Importacao do pacote e nomeando para db
import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker


class BaseDao:
    def __init__(self, model_type):
        self.model_type = model_type
        #criando engine com o banco e passando a string de conexao =
        #formato da string (SGBD+conector://user:pwd@url:port/database)
        conexao = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
        criador_de_sessao = db.orm.sessionmaker()
        criador_de_sessao.configure(bind=conexao)
        self.sessao = criador_de_sessao()

    def listar_todos(self) -> list:
        return self.sessao.query(self.model_type).all()

    def buscar_por_id(self, id):
        return self.sessao.query(self.model_type).filter_by(id=id).one()

    def deletar(self, id) -> str:
        model = self.sessao.query(self.model_type).filter_by(id=id).one()
        self.sessao.delete(model)
        self.sessao.commit()
        return f"Deletado obj de id {id}"

    def inserir(self, model) -> str:
        self.sessao.add(model)
        self.sessao.commit()
        return f"Obj de id: {model.id} criada"

    def alterar(self, model) -> str:
        self.sessao.merge(model)
        self.sessao.commit()
        return f"Obj {model.nome} alterado com sucesso!"