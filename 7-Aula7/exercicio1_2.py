#--- Exercício 1 - Dicionario
#--- Escreva um programa que leia os dados de cerveja
#--- Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume
#--- Crie um dicionario para armazenar os dados
#--- Imprima os dados do dicionário (não dicionário completo)


#--- Resolvido por Gustavo Antunes Voltolini
cerveja = {}
cerveja ['Marca'] = (input('Digite a marca: '))
cerveja ['Tipo'] = (input('Digite o tipo: '))
cerveja ['IBU'] = int(input('Digite o IBU(inteiros): '))
cerveja ['ABV'] = float(input('Digite o ABV(inteiros): '))
cerveja ['EBC'] = float(input('Digite o EBC: '))
cerveja ['volume'] = float(input('Digite o volume: '))

print (f"Marca{cerveja['Marca']} - Tipo: {cerveja['Tipo']} - IBU: {cerveja['IBU']} - ABV: {cerveja['ABV']} - EBC: {cerveja['EBC']} - Volume: {cerveja['volume']}")
