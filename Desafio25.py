print('-=-'*10)
print('''\033[7m         DESAFIO 25           \033[m''')
print('='*30)
print('')
print('''\033[1mCrie um programa que leia o nome de 
uma pessoa e diga se ela tem SILVA no nome.\033[m''')
print('')
n1 = str(input('Digite um nome: ')).strip()
print('Seu nome tem Silva:{} '.format('silva' in n1.lower()))


