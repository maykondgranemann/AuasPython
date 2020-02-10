import random
numero_alunos = 40
tamanho_grupo = 2
numero_de_grupos = numero_alunos/tamanho_grupo

def ler_alunos():
    with open('00-Sorteios/lista_alunos.txt','r') as arquivo:
        for a in arquivo:
            lista_alunos.append(a.strip())

def busca_nome_aluno(index):
    return lista_alunos[index]            

lista_alunos = []            
lista_sorteados = []
ler_alunos()

for i in range(0, numero_alunos):
    sorteado =  random.randint(1,numero_alunos-1)
    while(lista_sorteados.count(sorteado) > 0):
        sorteado =  random.randint(0,numero_alunos-1)
    lista_sorteados.append(sorteado)


print('='*50)
print('\n'*3)

lista_alunos_sorteados=[]
for i in range(0,numero_alunos, tamanho_grupo):
    s1 = lista_sorteados[i]
    s2 = lista_sorteados[i+1]
    n1 = busca_nome_aluno(s1)
    n2 = busca_nome_aluno(s2)
    grupo = (n1, n2)
    lista_alunos_sorteados.append(grupo)

    
for i in range(len(lista_alunos_sorteados)):
    print(f' Grupo: {i+1} ')
    print('{} {} - {}'.format(' '*4 , lista_alunos_sorteados[i][0] , lista_alunos_sorteados[i][1]) )

print('\n'*3)
print('='*50)