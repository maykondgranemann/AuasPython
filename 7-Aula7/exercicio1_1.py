#--- Exercício 1 - Dicionario
#--- Escreva um programa que leia os dados de cerveja
#--- Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume
#--- Crie um dicionario para armazenar os dados
#--- Imprima os dados do dicionário (não dicionário completo)

# Resolvido por: Gabriel Rodrigo Parasky <3

marca = input('Informe a marca\n')
tipo = input('Informe o tipo\n')
ibu = input('Informe o IBU\n')
abv = input('Informe o ABV\n')
ebc = input('Informe o EBC\n')
volume = input('Informe o volume\n')

inf_cerveja = {'Marca':marca , 'Tipo':tipo , 'IBU':ibu , 'ABV':abv , 'EBC':ebc , 'Volume':volume}
print(f"{inf_cerveja['Marca']} | {inf_cerveja['Tipo']} | {inf_cerveja['IBU']} | {inf_cerveja['ABV']} | {inf_cerveja['EBC']} | {inf_cerveja['Volume']}")