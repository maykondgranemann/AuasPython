nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')
idade = int(input('Digite sua idade:'))

print(f'Nome:{nome} Sobrenome:{sobrenome} Idade: {idade}')

if idade < 18:
    print('Não pode usar mercado Tech, para o que presta')
else:
    print('Pode usar mercado Tech e chapar o coco')
    