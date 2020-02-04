
class EnderecoModel:
    def __init__(self, logradouro, numero, complemento, bairro, cidade, cep, id=None):
        self.id = id
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        