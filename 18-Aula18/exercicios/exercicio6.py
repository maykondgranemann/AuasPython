# Aula 18 - 03-12-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e 
# retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: 
# codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres 
# (R$ 15,00) do que para os homens 
# (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar 
# em arquivos separados. 
# Como é uma festa de arromba, menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do
#  participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o
#  texto "Entrada Proibida!"


def ler_cadastro():
    arquivo = open('18-Aula18/exercicios/cadastro.txt','r')
    lista = []
    for pessoas in arquivo:
       pessoas = pessoas.strip().split(';')
       dicionario = {'codigo':pessoas[0], 'nome':pessoas[1], 
                     'sexo':pessoas[2], 'idade':pessoas[3]}
       lista.append(dicionario)
    arquivo.close()
    return lista
print(ler_cadastro())
# 2 - Como a entrada da festa é mais barata para mulheres 
# (R$ 15,00) do que para os homens 
# (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar 
# em arquivos separados. 
# Como é uma festa de arromba, menores de idade não podem entrar.

[{'codigo': '1', 'nome': 'fernanda de almeida', 'sexo': 'f', 'idade': '18'}
 {'codigo': '2', 'nome': 'pedro pedroca', 'sexo': 'm', 'idade': '17'},
 {'codigo': '3', 'nome': 'joana francisca', 'sexo': 'f', 'idade': '16'},
 {'codigo': '4', 'nome': 'paola silva', 'sexo': 'f', 'idade': '19'} ]

def lista_festa(lista_de_entradas):
   lista_homens = 

   for pessoa in lista_de_entradas:
      if int(pessoa['idade']) >= 18:
         if pessoa['sexo'] == 'f':
            
         else:

      else:
         print('não pode entrar')

