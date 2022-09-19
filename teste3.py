import json
import statistics

with open('dados.json', 'r') as json_file:
    dados = json.load(json_file)

media = []

for i in range(len(dados)):
    for idx, valor in dados[i].items():
        if(idx == 'valor' and valor > 0):
            media.append(valor)

dias = 0

for i in range(len(media)):
    if media[i] > statistics.mean(media):
        dias += 1

print(f'média: {statistics.mean(media):,.2f}')
print(f'Menor faturamento: {min(media):,.2f}' )
print(f'Maior faturamento: {max(media):,.2f}' )
print(f'Números de dias com o valor acima da média: {dias}')




