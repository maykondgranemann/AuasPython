class Sorteio:
    '''
    Classe para sortear o nome de um aluno a partir de um arquivo.
    Uso: Sorteio('nome_da_pasta', 'nome_do_arquivo.txt')
    '''
    
    def __init__(self, pasta, arquivo):
        '''
        Lê o arquvio com o nome dos alunos
        e armazena todos em uma lista,
        além de armazenar também a quantidade
        total de alunos.
        '''
        self.lista_alunos = []
        with open(f'{self.pasta}/{self.arquivo}','r') as alunos:
            for aluno in alunos:   
                self.lista_alunos.append(aluno.strip('\n'))
        
        self.qtd_alunos = len(self.lista_alunos)

    def apagar_sorteado(self):
        '''
        Apaga o nome do aluno sorteado do arquivo.
        '''
        with open(f'{self.pasta}/{self.arquivo}','w') as alunos:    
            for linha in self.lista_alunos[:self.qtd_alunos-2]:
                alunos.write(f'{linha}\n')
            for linha in self.lista_alunos[self.qtd_alunos-2:]:
                alunos.write(f'{linha}')
    
    def sortear(self):
        '''
        Executa o sorteio, usando a biblioteca
        'Random'. Ao final chama a função
        apagar_sorteado()
        '''
        import random
        sorteado = int( random.randint(1,self.qtd_alunos) )
        print(f'O numero sorteado foi: {sorteado}')
        for i, aluno in enumerate(self.lista_alunos):   
            if (i+1) == sorteado:
                print(f'Aluno : {aluno}')
                self.lista_alunos.pop(i)
        self.apagar_sorteado()