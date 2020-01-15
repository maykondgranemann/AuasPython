import sys
sys.path.append('/Users/mdgranemann/Documents/Github/AlunosPython/TrabalhosPython/33-Aula33/Aula33-4')

from model.pessoa import Pessoa
from dao.pessoa_db import PessoaDb

p = Pessoa()
p_db = PessoaDb()

lpc = p_db.listar_todos()
p.exportar_txt(lpc)