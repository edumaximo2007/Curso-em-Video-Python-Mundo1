print('-=-'*10)
print('''\033[7m          DESAFIO 31           \033[m''')
print('-=-'*10)
print('')
print('''\033[1mDesenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrado R$0,50 por Km para viagens 
de até 200Km e R$0,45 para viagens mais longas\033[m''')
print('')
p1 = float(input('Digite a Km percorrida: '))
p2 = p1 * 0.50
p3 = p1 * 0.45
if p1 <= 200:
    print('Sua corrida deu {}Km o valor a pagar e de R${:.2f}'.format(p1, p2))
else:
    print('Sua corrida deu {}Km o valor a pagar e de R${:.2f}'.format(p1, p3))
