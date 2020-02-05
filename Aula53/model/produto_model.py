from Aula53.model.base_model import BaseModel

class ProdutoModel(BaseModel):

    def __init__(self):
        self.nome = self.db.Column(self.db.String(length=100))
        self.descricao = self.db.Column(self.db.String(length=200))
        self.id = self.db.Column(self.db.Integer, primary_key=True)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.nome,self.descricao)