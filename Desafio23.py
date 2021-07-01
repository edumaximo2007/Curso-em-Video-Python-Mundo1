print('-=-'*10)
print('''\033[7m          DESAFIO 23        \033[m''')
print('-=-'*10)
print('')
print('''\033[1mFaça um programa que leia um número de 0 a 9999 e mostre na tela cada um digitos separados.
EX:
Digite um número: 1834

Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1\033[m''')
print('')
p1 = str(input('Podemos começar?  '))
if p1 =='Sim':
    print('Responda abaixo')
else:
    print('Você não tem escolha inseto maldito')    
print('')
n1 = int(input('Digite um número: '))
print('Analisando o número: {}'.format(n1))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 //1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('')
print('\033[1mParabéns você concluiu esta tarefa com exito!\033[m')