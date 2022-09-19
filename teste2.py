num = int(input('digite um número: '))
f0 = 0
f1 = 1
cond = True
print('Sequência de Fibonacci: ', end='')
print('{} -> {}' . format(f0, f1), end='')
if(num != 0 and num != 1 ):
    cond = False
    while num > f1:
        f2 = f0 + f1
        print(' -> {}' . format(f2), end='')
        f0 = f1
        f1 = f2
        if(num == f1):
            cond = True


print('\nEsse número existe na sequência Fibonacci' if cond else '\nEsse não número existe na sequência Fibonacci')

