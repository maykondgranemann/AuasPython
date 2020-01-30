from flask_restful import Resource

class PessoaController(Resource):
    def get(self):
        return 'Acessando metodo GET'

    def post(self):
        return 'Acessando metodo POST'

    def put(self):
        return 'Acessando metodo PUT'

    def delete(self):
        return 'Acessando metodo DELETE'