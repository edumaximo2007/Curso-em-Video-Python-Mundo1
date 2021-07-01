print('-=-'*10)
print('''\033[7m          DESAFIO 33          \033[m''')
print('='*30)
print('')
print('\033[1mFaça um programa que leia três números e mostre qual é o maior qual e o menor.\033[m')
print('')
print('-=-'*20)
n = int(input('Digite um número: '))
print('-=-'*20)
n1 = int(input('Digite um número: '))
print('-=-'*20)
n2 = int(input('Digite um número:'))
print('-=-'*20)
#Verificando quem é menor.
p = n
if n1 < n and n1 < n2:
    p = n2
if n2 < n and n2 < n1:
    p = n2
#Verificando quem é maior.
m = n
if n1 > n and n1 > n2:
    m = n1
if n2 > n and n2 > n1:
    m = n2
print('O menor número e o {}'.format(p))
print('O maior número e o {}'.format(m))