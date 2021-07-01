print('-=-'*10)
print('''\033[7m          DESAFIO 34          \033[m''')
print('='*30)
print('')
print('''\033[1mEscreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.\033[m''')
print('')
sa = float(input('Digite seu salário para saber seu aumento: R$'))
if sa >= 1250:
    print('Seu salario é R${:.2f} com aumento de 10% ficará em R${:.2f}'.format(sa, (sa*1.1)))
else:
    print('Seu salário é menor que R${:.2f} com aumento de 15% ficará em R${:.2f}'.format(sa, (sa+(sa*15/100))))