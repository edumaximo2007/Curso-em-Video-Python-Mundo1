from math import trunc
print('-=-'*10)
print('''\033[7m          DESAFIO 16          \033[m''')
print('-=-'*10)
print('')
print('\033[1mCrie um programa que leia um número pelo teclado e mostre na tela sua porção inteira.\033[m')
print('')
p = float(input('Digite um número: '))
n = trunc(p)
print('O número digitado foi {} e sua parte inteira e {}'.format(p, n))
print('')
print('\033[1mParabéns você concluiu esta tarefa!\033[m')
