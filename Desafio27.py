print('-=-'*10)
print('''\033[7m          DESAFIO 27          \033[m''')
print('='*30)
print('')
print('''\033[1mFaça um programa que leia o nome completo de uma pessoa, mostrando 
em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza.
Primeiro: Ana
Último: Souza\033[m''')
print('')
n = str(input('Digite um nome: ')).strip()
n1 = n.split()
n2 = n1[0]
print('Seu primeiro nome e {}'.format(n2))
n3 = (n1[len(n1)-1])
print('Seu último nome e {}'.format(n3))
#print('Seu último nome e {}'.format(n1[len(n1)-1]))


