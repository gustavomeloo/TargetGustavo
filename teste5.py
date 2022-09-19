text = input('Digite uma palavra: ')

for i in range(len(text)-1, -1, -1):
    print(text[i], end='')