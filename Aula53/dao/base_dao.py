import sqlalchemy as db

class BaseDao:
    def __init__(self):
        # ----database+conector://user:passwd@url:porta/database
        conexao = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
        criador_sessao = db.orm.sessionmaker()
        criador_sessao.configure(bind=conexao)
        self.sessao = criador_sessao()