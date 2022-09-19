dados = {
		'sp': 67836.43,
		'rs': 36678.66,
        'mg': 29229.88,
        'es': 27165.48,
        'outros': 19849.53
}

total = sum(dados.values())

print('Procentagem de valores mensais em cada estado:')
for idx, valor in dados.items():
    print(f'{idx} - {valor*100/total:.2f}%')

