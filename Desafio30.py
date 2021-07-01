print('-=-'*10)
print('''\033[7m          DESAFIO 30          \033[m''')
print('-=-'*10)
print('''\033[1mCrie um programa que leia um número inteiro e 
mostre na tela se ela é PAR ou ímpar.\033[m''')
print('-=-'*20)
print('')
n = int(input('Digite um número: '))
n1 = n % 2
if n1 == 0:
    print('O número {} e par!!'.format(n))
else:
    print('O número {} e impar!!'.format(n))