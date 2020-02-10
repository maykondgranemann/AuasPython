from Aula55.model.autor import Autor
from Aula55.model.editora import Editora
from Aula55.model.genero import Genero

class Livro:
    id = 0
    titulo = ''
    sinopse = ''
    data_primeira_publicacao = ''
    autor = Autor()
    editora = Editora()
    genero = Genero()