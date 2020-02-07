from Aula54.dao.pessoa_dao import PessoaDao
from Aula54.dao.produto_dao import ProdutoDao
from Aula54.model.pessoa_model import Pessoa

dao = PessoaDao()
dao2 = ProdutoDao()

p = Pessoa()
p.nome = "Vitao 2"
p.sobrenome = "KingOfPhilips"
p.idade = 17
p.id = 62
#print(dao.alterar(p))

print("-"*10)

#print(dao.deletar(19))
for p in dao2.listar_todos():
    print(p)


#print("-"*10)
#dao.buscar_por_id(19)
