# Operações matematicas 2 - Divisao Exata, Resto da divisão, Potenciação e Raiz


#--- Divisão inteira
print(10//3)

#--- Divisão em ponto flutuante
print(10/3)

#--- Resto da divisão
print(10%7)

#--- Potenciação
print(5**5)

#--- Raiz quadrada
print(4**(1/2))

#--- Raiz cubica
print(27**(1/3))

#--- Funcao Type
print(type(10))

#--- Funcao isInstance - Valida se um objeto é de um tipo específico
print(isinstance(10.2, int))

#--- Python não possui Char, apenas Strings
#--- String com multiplas linhas com aspas tripas
print(
''' ola
        maykon'''
)
#--- String com multiplas linhas apenas com quebra de linhas
print('ola '
    'Maykon')
#--- Strings separadas por espaco, unen-se
nome = 'Maykon' " " 'Dyego' " " 'Granemann'
print(nome)
#--- Usando aspas dentro das strings
print('Calypso é "top"')

#--- Lendo tamanho da string
print(len(nome))
#--- Pegando pelo indice da string
print(nome[2])
#--- slice na string de inicio e fim
print(nome[3:7])
#--- Slice na string definindo apenas o inicio
print(nome[3:])
#--- Slice na string definindo apenas o fim
print(nome[:4])
#--- Multiplicando strings
frase = 'a mim tu não engana mais'
frase = frase *3
print(frase)
#--- validar conteudo na string
print('m' in nome)
#--- validar conteudo nao esta presenta na string
print('Maicon' not in nome)

#--- Strings são imutavies, a seguencia a seguir ocorrera erro
# nome[2] = 'a'

#--- Strings possui metodos e outras formas de manipulação, mas sempre gerando uma nova string
#--- Alterando usando o replace
print(nome.replace('Granemann', 'Rauen'))
#--- Alterando usando o slice mais concatenação
print(nome[:13]+'Rauen')

#--- Métodos de strings
qualidades = ['','Bonito','Inteligente','Carinhoso']
print(' nem '.join(qualidades))