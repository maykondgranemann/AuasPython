# pip3 install flask_mysqldb
# referencia ao Mysql

import MySQLdb

def listar_todos(c):
    c.execute('SELECT * FROM 01_MDG_PESSOA')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM 01_MDG_PESSOA WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM 01_MDG_PESSOA WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)


conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019' )
cursor= conexao.cursor()

#listar_todos(cursor)
# buscar_por_id(cursor, 3)
buscar_por_sobrenome(cursor,'Gru')
