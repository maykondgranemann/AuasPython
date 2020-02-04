from flask_restful import Resource
from flask import request

from Aula52.model.pessoa_model import PessoaModel
from Aula52.dao.pessoa_dao import PessoaDao

class PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao()

    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar_todos()

    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade)
        return self.dao.inserir(pessoa)

    def put(self, id):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade, id)
        return self.dao.alterar(pessoa)

    def delete(self, id):
        return self.dao.deletar(id)