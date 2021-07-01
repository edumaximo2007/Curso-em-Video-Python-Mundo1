print('-=-'*10)
print("""\033[7m         DESAFIO 22           \033[m""")
print('-=-'*10)
print('')
print("""\033[1mCrie um programa que leia o nome completo de uma pessoa e mostre :
O nome com todas as letras maiúsculas.
O nome com todas minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.\033[m""")
print('')
nome = str(input('Digite o nome completo: ')).strip()
max = nome.upper()
print('O nome com todas as letras maiúsculas: {}'.format(max))
min = nome.lower()
print('O nome com todas as letras minúsculas: {}'.format(min))
n = (len(nome)) - (nome.count(' '))
print('Quantas letras ao todo tem o seu nome: {}'.format(n))
#print('Quantas letras ao todo tem (sem considerar espaços):{} '.format(len(nome) - nome.count(' ')))
c1 = nome.split()
c2 = c1[0]
c3 = (len(c2))
print('Quantas letras o nome {} tem: {}'.format(c2, c3))
