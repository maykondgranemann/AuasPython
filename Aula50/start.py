from flask import Flask
from flask_restful import Api

from Aula50.controllers.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa')


app.run(debug=True)