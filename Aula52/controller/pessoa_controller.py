from flask import request

from Aula52.model.pessoa_model import PessoaModel
from Aula52.dao.pessoa_dao import PessoaDao
from Aula52.controller.base_controller import BaseController

class PessoaController(BaseController):
    def __init__(self):
        super().__init__(PessoaDao())

    def post(self):
        self.carrega_parametros()
        model = PessoaModel(self.nome, self.sobrenome, self.idade)
        return super().post(model)

    def put(self, id):
        self.carrega_parametros()
        model = PessoaModel(self.nome, self.sobrenome, self.idade, id)
        return super().put(model)

    def carrega_parametros(self):
        self.nome = request.json['nome']
        self.sobrenome = request.json['sobrenome']
        self.idade = int(request.json['idade'])