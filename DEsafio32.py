from datetime import date
print('-=-'*10)
print('''\033[7m          DESAFIO 32          \033[m''')
print('-=-'*10)
print('')
print('\033[1mFaça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.\033[m')
print('')
n = int(input('Digite o ano para analisar, ou coloque 0 para analisar o ano atual:  '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano de {} é \033[1mBISSEXTO.\033[m'.format(n))
else:
    print('O ano de {} não é \033[1mBISSEXTO.\033[m'.format(n))
