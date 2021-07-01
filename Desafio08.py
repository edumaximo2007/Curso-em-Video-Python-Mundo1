print('-=-'*10)
print('''\033[7m         DESAFIO 08          \033[m''')
print('='*10)
print('Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.')
Pergunta = str(input('Podemos começar? ')).strip()
if pergunta == 'Sim':
    print('Responda abaixo')
else:
    print('Você não tem escolha!! hahahaha')
print('')
n = float(input('Digite sua altura: '))
print('Eu tenho {}m '.format(n))
n1 = n*100
print('Quantos Cm tem {}m ?'.format(n))
print('{}m tem {}Cm'.format(n, n1))
print('Quantos milimetros tem em {}m ?'.format(n))
n2 = n*1000
print('{}m tem {}mm '.format(n,n2))
