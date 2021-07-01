print('-=-'*10)
print('''\033[7m          DESAFIO 12          \033[m''')
print('-=-'*10)
print('\033[1mFaça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\033[m')
print('')
nome = str(input('Qual é o seu nome? ')).strip()
p = str(input('Podemos começar {}? '.format(nome)))
if p == 'Sim':
    print('Responda abaixo.')
else:
    print('Você não tem escolha vadio, responda')
print('')
print('Queima de estoque tudo com 5% de desconto aproveite')
print('')
ca = float(input('Coloque aqui o valor do produto sem desconto: R$'))
n = ca*5
n1 = n/100
n2 = ca-n1
print('Produto de R${:.2f} por R${:.2f} com 5% de desconto'.format(ca, n2))
print('')
print('\033[1mParabéns {} concluiu sua tarefa!\033[m'.format(nome))


