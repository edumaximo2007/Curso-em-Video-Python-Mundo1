print('-=-'*10)
print('''\033[7m         DESAFIO 07           \033[m''')
print('-=-'*10)
print('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média. ')
print('')
pergunta = input('Podemos começar? ')
if pergunta == 'Sim':
    print('Responda')
else:
    print('Você não tem escolha!!')
print('')
nome = str(input('Qual e o seu nome? ')).strip()
print('{} tirou 4 no primeiro teste de matematica e 5 no segundo teste, sabendo que a média e 5, qual foi a média de {}? '.format(nome, nome))
n1 = float(input('Coloque a nota do primeiro teste: '))
n2 = float(input('Coloque a nota do segundo teste: '))
s1 = n1+n2
s2 = s1/2
print('Dessa forma a média de {} e {} '.format(nome, s2))
print('\033[1mParabéns!!\033[m')

