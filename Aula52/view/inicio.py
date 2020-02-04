from flask import Flask
from flask_restful import Api

from Aula52.controller.pessoa_controller import PessoaController
from Aula52.controller.endereco_controller import EnderecoController

app = Flask(__name__)
api = Api(app)

#--- Rotas de pessoa
api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')

#--- Rotas de endereco
api.add_resource(EnderecoController, '/api/endereco', endpoint='enderecos')
api.add_resource(EnderecoController, '/api/endereco/<int:id>', endpoint='endereco')

app.run(debug=True)
