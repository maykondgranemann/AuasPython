from flask import request

from Aula52.model.endereco_model import EnderecoModel
from Aula52.dao.endereco_dao import EnderecoDao
from Aula52.controller.base_controller import BaseController

class EnderecoController(BaseController):
    def __init__(self):
        super().__init__( EnderecoDao() )

    def post(self):
        self.carrega_parametros()
        model = EnderecoModel(self.logradouro, self.complemento, self.numero, self.bairro, self.cidade, self.cep)
        return self.dao.inserir(model)

    def put(self, id):
        self.carrega_parametros()
        model = EnderecoModel(self.logradouro, self.complemento, self.numero, self.bairro, self.cidade, self.cep, id)
        return self.dao.alterar(model)

    def carrega_parametros(self):
        self.logradouro = request.json['logradouro']
        self.numero = request.json['numero']
        self.complemento = request.json['complemento']
        self.bairro = request.json['bairro']
        self.cidade = request.json['cidade']
        self.cep = request.json['cep']