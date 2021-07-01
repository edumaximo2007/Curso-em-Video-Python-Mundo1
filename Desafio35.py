import emoji
print('-=-'*10)
print('''\033[7m          DESAFIO 35          \033[m''')
print('='*30)
print('')
print(emoji.emojize(''':bulb: \033[1mDesenvolva um programa que leia o comprimento de três retas e diga 
ao usuário se elas podem ou não forma um triângulo.\033[m''', use_aliases=True))
print('')
print('Digite para saber se e possível forma um triângulo')
n1 = float(input('Digite um número A: '))
n2 = float(input('Digite um número B: '))
n3 = float(input('Digite um número C: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os números acima podem forma um triângulo!!')
else:
    print('Os números acima não podem forma um triãngulo!!')