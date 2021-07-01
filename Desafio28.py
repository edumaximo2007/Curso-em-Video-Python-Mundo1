from random import randint
print('-=-'*10)
print('''\033[7m         DESAFIO 28         \033[m''')
print('-=-'*10)
print('')
print('''\033[1mEscreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.\033[m''')

p1 = str(input('Podemos começar? ')).strip()
if p1 == 'Sim':
    print('Obrigado!')
else:
    print('Você não tem escolha inseto maldito.')
print('')
print('-=-'*20)
print('Tente advinhar o número que eu estou pensando entre 0 e 5...')
print('-=-'*20)
p2 = int(input('Digite um número entre 0 e 5: '))
print('-=-'*20)
pc = randint(0, 5)
if p2 == pc:
    print('O miseravel é um genio!')
else:
    print('\033[1mErrou feio inseto maldito, você digitou o número {} e eu pensei no número {}\033[mnão'.format(p2, pc))