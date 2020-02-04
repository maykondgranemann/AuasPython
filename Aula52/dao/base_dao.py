import MySQLdb

class BaseDao:
    def __init__(self, nome_tabela):
        host = "mysql.topskills.dev"
        database = "topskills01"
        user = database
        passwd = "ts2019"
        self.tabela = nome_tabela
        self.conexao = MySQLdb.connect(host=host, database=database, user=user, passwd=passwd)
        self.cursor = self.conexao.cursor()

    def listar_todos(self):
        self.cursor.execute("SELECT * FROM {}".format(self.tabela))
        tuplas = self.cursor.fetchall()
        return tuplas

    def buscar_por_id(self, id):
        self.cursor.execute("SELECT * FROM {} WHERE ID = {}".format(self.tabela, id))
        tupla = self.cursor.fetchone()
        return tupla

    def inserir(self, comando_sql):
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id = self.cursor.lastrowid
        return id

    def alterar(self, comando_sql):
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self, id):
        self.cursor.execute(""" DELETE FROM {}
                                        WHERE ID = {}
                                    """.format(self.tabela, id))
        self.conexao.commit()
        return  "Registro de id {} deletado com sucesso".format(id)