from dao. autor_dao import AutorDao
from model.autor import Autor

dao = AutorDao()

teste = dao.get_by_id(11)

print(teste)