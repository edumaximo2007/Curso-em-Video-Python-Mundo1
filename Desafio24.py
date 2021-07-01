print('-=-'*10)
print('''\033[7m          DESAFIO 24          \033[m''')
print('-=-'*10)
print('')
print('''\033[1mCrie um programa que leia o nome de uma
cidade e diga se ela começa com o nome SANTO.\033[m''')
print('')
n1 = str(input('Digite o nome de uma cidade: ')).strip()
print(n1[:5].upper() == 'SANTO')
