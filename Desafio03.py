print('-=-'*10)
print('''\033[7m          DESAFIO 03          \033[m''')
print('-=-'*10)
print('Executando soma')
n1 = float(input('Valor de uma casa: R$'))
n2 = float(input('Valor da outra casa: R$'))
s = n1+n2
print('O valor da casa 1 R${:.2f} somado a casa 2 R${:.2f} e equivalente a R${:.2f}'.format(n1, n2, s))
