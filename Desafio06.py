print('-=-'*10)
print('''\033[7m         DESAFIO 06           \033[m''')
print('-=-'*10)
print('Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada')
pergunta = str(input('Podemos começar? '))
if pergunta == 'Sim':
    print('Responda abaixo')
else:
    print('Você não tem escolha!!')
print('')
p1 = int(input('Digite um valor: '))
p2 = p1*2
p3 = p1*3
p4 = p1**(1/2)
print('O dobro de {} e {} '.format(p1, p2))
print('O triplo de {} e {} '.format(p1, p3))
print('A raiz quadra de {} e {:.2} '.format(p1, p4))
print('Esses valores correspodem ao seu calculo')
print('Bons esstudos!')



